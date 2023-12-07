from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
import datetime

class Voter(models.Model):
    States = [
        ('AP', 'Andhra Pradesh'),
        ('AR', 'Arunachal Pradesh'),
        ('AS','Assam'),
        ('BR', 'Bihar'),
        ('CH', 'Chandigarh'),
        ('DL', 'Delhi'),
        ('GA', 'Goa'),
        ('GJ', 'Gujarat'),
        ('HR', 'Haryana'),
        ('HP', 'Himchal Pradesh'),
        ('JH', 'Jharkhand'),
        ('KA', 'Karnataka'),
        ('KL', 'Kerala'),
        ('MP', 'Madhya Pradesh'),
        ('MH', 'Maharashtra'),
        ('MN', 'Manipur'),
        ('ML', 'Meghalaya'),
        ('MZ', 'Mizoram'),
        ('NL', 'Nagaland'),
        ('OR', 'Orissa'),
        ('PN', 'Punjab'),
        ('RJ', 'Rajasthan'),
        ('SK', 'Sikkim'),
        ('TN', 'Tamil Nadu'),
        ('TL', 'Telengana'),
        ('TR', 'Tripura'),
        ('UP', 'Uttar Pradesh'),
        ('UK', 'Uttarakhand'),
        ('WB', 'West Bengal'),
    ]
    Voter_id = models.CharField(max_length=10)
    Aadhar_no = models.CharField(max_length=12, validators=[RegexValidator(r'^\d{12,12}$')], primary_key=True, unique=True)
    Firstname = models.CharField(max_length = 100, validators=[RegexValidator("^[a-zA-Z]*$")], null=True)
    Lastname = models.CharField(max_length=100, validators=[RegexValidator("^[a-zA-Z]*$")], null=True)
    day = models.IntegerField(blank=False, null=True, validators=[MinValueValidator(1),MaxValueValidator(31)])
    month = models.IntegerField(blank=False, null=True,
                               validators=[MinValueValidator(1), MaxValueValidator(12)])
    year = models.IntegerField(blank=False, null=True,
                               validators=[MinValueValidator(1900), MaxValueValidator(2004)])
    #dob = models.IntegerField(default=datetime.date(2004,4,15), auto_now_add=False)
    pincode = models.CharField(max_length = 6, validators=[RegexValidator(r'^\d{6,6}$')])
    region = models.CharField(max_length=2,
        choices=States,
        default='GJ',)
    email = models.EmailField(max_length = 100)
    vote_done = models.BooleanField(default = False)

    def __str__(self):
        return self.Firstname

class PoliticalParty(models.Model):
    party_id = models.CharField(max_length=10, primary_key=True)
    party_name = models.CharField(max_length=100)
    party_logo = models.CharField(max_length=500)
    candidate_name = models.CharField(max_length=100, blank=True, validators=[RegexValidator("^[a-zA-Z]*$")])

    def __str__(self):
        return self.party_name



class Time_Num(models.Model):
    num = models.IntegerField(default=0)
    time = models.CharField(max_length=50)
    an = models.CharField(max_length = 20,default='',null=True,blank=True, editable=False)


class Vote(models.Model):
    Usrid = models.CharField(max_length=12)
    Vid1 = models.CharField(max_length = 100)
    Vid2 = models.CharField(max_length = 44)

class Result(models.Model):
    pn = models.CharField(max_length=20)
    vc = models.CharField(max_length=20)

    def __str__(self):
        return self.pn