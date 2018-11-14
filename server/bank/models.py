from django.db import models

# Create your models here.


class Family(models.Model):
    surname = models.CharField(max_length = 20)
    bank = models.IntegerField()

    def set_bank(self, bank):
        self.bank = bank

    def __str__(self):
        return self.surname + " " + str(self.bank)

    def __unicode__(self):
        return self.question

class Member(models.Model):
    bank = models.IntegerField()
    family = models.ForeignKey(Family, related_name='members', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def set_bank(self, bank):
        self.bank = bank

    def __unicode__(self):
        return self.question

    def full_name(self):
        return self.family.surname+ " " + self.first_name + " " + self.last_name

    def __str__(self):
        return self.full_name() + " " + str(self.bank)