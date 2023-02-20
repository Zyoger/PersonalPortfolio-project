from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=50)
    preview = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to="portfolio/images/portfolio/")
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Certificate(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    image = models.ImageField(upload_to="portfolio/images/certificates/")
    file = models.FileField(upload_to="portfolio/files/")
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title


class PhotoAlbum(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="portfolio/images/my photo/")

    def __str__(self):
        return self.title
