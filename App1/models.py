from django.db import models

# Create your models here.

class Qadi(models.Model):
    qadi_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    court_name = models.CharField(max_length=255)
    appointment_date = models.DateField()
    experience_years = models.IntegerField()

    def __str__(self):
        return self.name

class CaseResults(models.Model):
    case_id = models.AutoField(primary_key=True)
    qadi = models.ForeignKey(Qadi, on_delete=models.CASCADE)
    case_name = models.CharField(max_length=255)
    verdict = models.TextField()
    judgment_date = models.DateField()

    def __str__(self):
        return self.case_name

class ClientData(models.Model):
    full_name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    passport_no = models.CharField(max_length=20, unique=True)  # رقم جواز السفر يجب أن يكون فريدًا
    phone_number = models.CharField(max_length=20)
    lost_company = models.CharField(max_length=255)
    lose_amount = models.FloatField()
    lost_year = models.IntegerField()

    def __str__(self):
        return self.full_name