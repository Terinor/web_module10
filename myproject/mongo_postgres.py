import os
import django
from datetime import datetime
from mongoengine import connect as mongo_connect, disconnect

# Налаштування Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()

from myapp.models import Author as django_Author, Quote as django_Quote  # Імпортуйте ваші моделі Django
from starter import Author as mongo_Author, Quote as mongo_Quote

# Дані для підключення до MongoDB
mongo_user = 'postgres'
mongo_pass = '12345'
mongo_db_name = 'LearningDatabase'
mongo_domain = 'learningdatabase.b6ivt3u.mongodb.net'

# Підключення до MongoDB через MongoEngine
mongo_connect(host=f'mongodb+srv://{mongo_user}:{mongo_pass}@{mongo_domain}/{mongo_db_name}?retryWrites=true&w=majority')

# Імпорт авторів
for mongo_author in mongo_Author.objects():
    author, created = django_Author.objects.get_or_create(
        name=mongo_author.fullname,
        defaults={
            'date_of_birth': datetime.strptime(mongo_author.born_date, "%B %d, %Y"),
            'bio': mongo_author.description
        }
    )

# Імпорт цитат
for mongo_quote in mongo_Quote.objects():
    # Знаходимо автора в базі PostgreSQL
    author = django_Author.objects.get(name=mongo_quote.author.fullname)

    # Створюємо нову цитату
    quote = django_Quote.objects.create(
        text=mongo_quote.quote,
        author=author,
        tags=', '.join(mongo_quote.tags)  # Перетворення списку тегів у рядок
    )

print("Дані успішно імпортовано.")

disconnect()  # Закриття підключення до MongoDB
