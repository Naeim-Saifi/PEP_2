from django.db import models
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.PositiveIntegerField(primary_key=True)
    age = models.PositiveIntegerField()
    address = models.TextField()
    phone = models.PositiveIntegerField()
    email = models.EmailField()
    def __str__(self):
        return self.name