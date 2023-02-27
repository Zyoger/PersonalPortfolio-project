from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    preview = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(upload_to="static/image/project/")
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Certificate(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to="static/images/certificates/")
    file = models.FileField(upload_to="static/files/")
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title


class InformationAboutMe(models.Model):
    my_nick = models.CharField(max_length=50)
    my_photo = models.ImageField(upload_to="static/images/")
    description_main = models.TextField()
    description_second = models.TextField(blank=True)
    my_resume = models.FileField(upload_to="static/files/")
    my_phone_number = models.CharField(max_length=20)
    link_telegram = models.URLField(blank=True)
    link_instagram = models.URLField(blank=True)
    link_github = models.URLField(blank=True)
    link_vk = models.URLField(blank=True)
    link_watsapp = models.URLField(blank=True)

    def __str__(self):
        return self.my_nick
