from django.db import models
from django.urls import reverse

class Prisoner(models.Model):

    first_name = models.CharField(verbose_name="Firstname", max_length=50)
    last_name = models.CharField(verbose_name="Lastname", max_length=50)
    id_number = models.CharField(verbose_name="Id Number", max_length=50, unique=True)
    pic = models.FileField(upload_to='profile_pics',blank=True, null=True)
    next_of_kin = models.CharField(verbose_name='Next of Kin', max_length=50)
    nxtofkin_relationship = models.CharField(verbose_name='Relationship to Nextof Kin', max_length=50)
    nxtofkin_pic = models.FileField(upload_to='profile_pics',blank=True, null=True)
    joined_on = models.DateTimeField(auto_now_add=True)
    # span = models.CharField(verbose_name='Prison Sentence', max_length=21)

    def __str__(self):
        return "{} - {} {}".format(self.id_number, self.pic, self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse('prisoners_detail', args=[str(self.id)])
