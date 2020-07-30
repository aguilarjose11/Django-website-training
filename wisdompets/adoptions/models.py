from django.db import models

class Pet(models.Model):
    # (value stored, value displayed)
    SEX_CHOICES = [('M', 'Male'), ('F', 'Female')]
    name = models.CharField(max_length=100)
    submitter = models.CharField(max_length=100)
    species = models.CharField(max_length=30)
    breed = models.CharField(max_length=30, blank=True)
    description = models.TextField()
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, blank=True) # blank=True in case we don't know sex of a pet.
    submission_date = models.DateTimeField()
    age = models.IntegerField(null=True) # null used because blank puts a 0 in, null puts null.
    vaccinations = models.ManyToManyField('Vaccine', blank=True) # pets can have many vaccines.


class Vaccine(models.Model):
    name = models.CharField(max_length=50)

    # this is what will be displayed in the admin page.
    def __str__(self):
        return self.name # print the vaccine name
