from django.db import models

# Create your models here.

class Personal_detail(models.Model):
    name = models.CharField(max_length=250, blank=True)
    description = models.CharField(max_length=500, blank=True)
    image = models.ImageField(upload_to='portfolio/image/')
    marital_status = models.CharField(max_length=10, blank=True)
    dob = models.DateField(blank=True)
    nationality = models.CharField(max_length=20, blank=True)
    hobby = models.CharField(max_length=50, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    def __str__(self):
        return self.name


class CoCurricular_activity(models.Model):
    activity_name = models.CharField(max_length=250, blank=True)
    description = models.CharField(max_length=500, blank=True)
    position = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.activity_name


class Skill(models.Model):
    title = models.CharField(max_length=250, blank=True)
    description = models.CharField(max_length=500, blank=True)
    expert_level = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=250, blank=True)
    git_link = models.URLField(max_length=500, blank=True)

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
        ('Closed', 'Closed'),
    )
    name = models.CharField(blank=True, max_length=20)
    email = models.EmailField()
    subject = models.CharField(blank=True, max_length=50)
    message = models.TextField(max_length=255)
    status = models.CharField(
        max_length=10, blank=True, choices=STATUS, default='New')
    ip = models.CharField(blank=True, max_length=20)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.email)
