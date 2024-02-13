from mongoengine import connect, Document, StringField, ListField, ReferenceField

# Дані для підключення до MongoDB
mongo_user = 'postgres'
mongo_pass = '12345'
mongo_db_name = 'LearningDatabase'
mongo_domain = 'learningdatabase.b6ivt3u.mongodb.net'

# Підключення до MongoDB через MongoEngine
connect(host=f'mongodb+srv://{mongo_user}:{mongo_pass}@{mongo_domain}/{mongo_db_name}?retryWrites=true&w=majority')

# Визначення моделей
class Author(Document):
    fullname = StringField(required=True)
    born_date = StringField(required=True)
    born_location = StringField(required=True)
    description = StringField()

    def __str__(self):
        return f"{self.fullname}, {self.born_date}, {self.born_location}"

class Quote(Document):
    tags = ListField(StringField())
    author = ReferenceField(Author, required=True)
    quote = StringField(required=True)

    def __str__(self):
        return f"{self.quote} - {self.author.fullname}"

