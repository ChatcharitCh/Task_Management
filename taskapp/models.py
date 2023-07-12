from django.db import models

# Create your models here.

# Task Model
class Task(models.Model):
    name = models.CharField(max_length=50)
    status = models.BooleanField(default=False) # ให้ค่าเริ่มต้นเป็น fault