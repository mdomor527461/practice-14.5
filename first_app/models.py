from django.db import models

# Create your models here.
# class Company(models.Model):
#     name = models.CharField(max_length=255,default=True)
class EmployModel(models.Model):
    # id = models.AutoField(primary_key= True)
    id = models.BigAutoField(primary_key= True)
    name = models.CharField( max_length=255)
    designation = models.CharField(max_length=255)
    salary = models.BigIntegerField(max_length=255)
    file = models.BinaryField()
    salary_date = models.DateField()
    launch_break = models.DateTimeField()
    bonus = models.DecimalField(max_digits=5, decimal_places=2,default=True)
    duration_field = models.DurationField()
    email = models.EmailField()
    choose_file = models.FileField(upload_to='files/')    
    # file_path_field = models.FilePathField(path='/')
    float_number = models.FloatField()
    # check = models.BooleanField(default=True)
    # foreign_key = models.ForeignKey(Company, on_delete=models.CASCADE)
    ip = models.GenericIPAddressField()
    