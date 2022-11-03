from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image1 = models.FilePathField(path="/img")
    image2 = models.FilePathField(path="/img")
    image3 = models.FilePathField(path="/img")

    def __str__(self):
        return self.title