from django.db import models

class Book(models.Model):
    class Meta:
        unique_together = ('title', 'author')
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publish_date = models.DateField()

    def __str__(self):
        return f"{self.title} by {self.author}"
# Create your models here.
