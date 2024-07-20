# job_app/models.py
from django.db import models
from django.forms import ModelForm
from random import choices



class Company(models.Model):
    name = models.CharField(max_length = 200)
    Website = models.CharField(max_length = 300)
    Industry = models.CharField(max_length = 200)
    EstablishedYear = models.CharField(max_length = 200)
    Introduction = models.TextField()

class Provinces(models.Model):
    PROVINCES_CHOICES = (
        ('TEH', 'Thran') ,
        ('KHR' , 'Khorasan Razavi') ,
        ('ISF' , 'Isfahan') ,
        ('ALB', 'Alborz') ,
        ('FA', 'Fars') ,
        ('Q' , 'Qom'),
        ('EA' , 'East Azerbaijan') ,
        ('M', 'Mazandaran'), 
        ('G', 'Gilan') ,
        ('K', 'Kerman'),
        ('KH', 'Khozestan'),
        ('Y', 'Yazd'),
        ('M', 'Markazi'),
        ('QA', 'Qazvin'),
        ('HO', 'Hormozgan'),
        ('GO', 'Golestan'), 
        ('ZA', 'Zanjan'),
        ('HA', 'Hamedan') ,
        ('SE', 'Semnan'),
        ('WA', 'West Azerbaijan'),
        ('BO', 'Boushehr'),
        ('KO', 'Kordestan'),
        ('KER', 'Kermanshah'),
        ('SB', 'Sistan Balouchestan'),
        ('CHB' , 'Charmahal Bakhtiari'),
        ('A', 'Ardebil'),
        ('KB' , 'Kohkiluyeh and Boyerahmad'),
        ('I', 'Ilam'),
        ('KHJ', 'Khorasan Jonoubi'),
        ('KHS', 'Khorestan Shomali'),
        ('LO', 'Lorestan'),
        
     )
    name = models.CharField(max_length=3 , choices = PROVINCES_CHOICES)

    def __str__(self):
        return self.name

class Category(models.Model):
    CATEGORY_CHOICES = (
        ('SM' , 'Sales and Marketing') ,
        ('SP' , 'Software and Programming') , 
        ('FA' , 'Finantial and Accounting') ,
        ('O' , 'Official') ,
        ('DM' , 'DigitalMarketing') ,
        ('CP' , 'ContentProduction') ,
        ('IDS', 'It Devops Server') ,
        ('D' , 'Design') ,
        ('CS' , 'Customer Support') , 
        ('IE' , 'Industrial Enginerring') , 
        ('EE' , 'Electrical Engineering') , 
        ('CE' , 'Civil Engineering') ,
        ('HR' , 'Human Resources') , 
        ('SF' , 'Servise Force') ,
        ('E' , 'Education') , 
        ('I', 'Inventory') ,
        ('CF' , 'Cinema Feild') ,
        ('MAE' , 'Mechanical and Aerospace Engineering') ,
        ('T' , 'Technician') ,
        ('TO' , 'Tourism') , 
        ('PM' , 'Product Manager') ,
        ('M' , 'Medical') , 
        ('TR' , 'Transportation') ,
        ('HM' , 'HotelManagement') ,
        ('PR' , 'Public Relations') ,
        ('CP' , 'Chemical Petronum') ,
        ('IM' , 'Insurance Management') ,
        ('MME', 'Mine and Metalogy Engineering'),
        ('BE', 'Biomedical Engineering') ,
        ('TE' , 'Txtile Engineering') ,
        ('PH' , 'Pharmacology') , 
        ('J' , 'Journalist') ,
        ('AE' , 'Agricultural Engineering') ,
        ('MSE' , 'Musical and Sound Engineering') ,
        ('PE', 'Physical Education') 
        
    )
    name = models.CharField(max_length=3, choices = CATEGORY_CHOICES)

    def __str__(self):
        return self.name

class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ForeignKey(Provinces, on_delete=models.CASCADE)
    employer = models.ForeignKey(Company, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    min_salary = models.DecimalField(max_digits = 10, decimal_places = 2)
    max_salary = models.DecimalField(max_digits = 10, decimal_places = 2)

    def __str__(self):
        return self.title

class JobSeeker(models.Model):
    GENDER_CHOICES = (
        ('M' , 'Male') ,
        ('F' , 'Female') ,
        ('O' , 'Others')
    )
    MARITAL_CHOICES = (
        ('M' , 'Married') ,
        ('S' , 'Single')
    )
    name = models.CharField(max_length = 200)
    email_adress = models.TextField()
    phone_number = models.CharField(max_length=12)
    birthday = models.DateField()
    gender = models.CharField(max_length=1, choices = GENDER_CHOICES)
    marital_status = models.CharField(max_length=1 , choices = MARITAL_CHOICES)
    residence = models.CharField(max_length=100)
    cv = models.TextField()


