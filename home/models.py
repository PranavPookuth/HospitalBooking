from django.db import models

# Create your models here.
class Department(models.Model):
    dep_name=models.CharField(max_length=200)
    dep_description=models.TextField()
    def __str__(self):
        return self.dep_name
class Doctors(models.Model):
    dr_name=models.CharField(max_length=200)
    dr_spec=models.CharField(max_length=200)
    dep_name=models.ForeignKey(Department,on_delete=models.CASCADE)
    dr_image=models.ImageField(upload_to='doctors')
    def __str__(self):
     return 'DR '   + self.dr_name +'-(' + self.dr_spec + ')'
class Booking(models.Model):
    p_name=models.CharField(max_length=200)
    p_phone=models.CharField(max_length=200)
    p_email=models.EmailField()
    dr_name=models.ForeignKey(Doctors,on_delete=models.CASCADE)
    booking_date=models.DateField()
    booked_on=models.DateField(auto_now=True)
   