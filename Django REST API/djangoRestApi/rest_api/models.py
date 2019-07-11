from django.db import models

# Create your models here.
class Employees(models.Model):
    firstName = models.CharField(max_length=10)
    lastName = models.CharField(max_length=10)
    emp_id = models.IntegerField()
    class Meta:
        db_table = "employee"

    def __str__(self):
        return self.firstName