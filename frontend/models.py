from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    discs_owned = ArrayField(models.IntegerField(null=True))
    discs_wanted = ArrayField(models.IntegerField(null=True))

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class genDisc(models.model):
    name = models.CharField(max_length=256)
    desc = models.CharField(max_length=2048)
    ident_code = models.CharField(max_length=64)

    region_coding = ArrayField(models.CharField(max_length=1))
    region_release = models.CharField(max_length=3)

    disc_format = models.CharField(max_length=128)
    release_date = models.DateField(blank=True)

    date_submitted = models.DateField()
    user_submitted = models.IntegerField()

    def __str__(self):
        return self.name

class Company(models.model):
    name = models.CharField(max_length=256)
    desc = models.CharField(max_length=2048)
    founded = modes.CharField(max_length=4)
    releases = ArrayField(models.IntegerField())

    def __str__(self):
        return self.name
