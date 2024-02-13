from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    bio = models.TextField()

    def __str__(self):
        return self.name


class Quote(models.Model):
    text = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.CharField(max_length=200)

    def __str__(self):
        return self.text[:50]  # Показувати лише перші 50 символів цитати
