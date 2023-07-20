from django.db import models
from django.contrib.auth.models import User 

# Task Model
class Task(models.Model):
    name = models.CharField(max_length=50)
    status = models.BooleanField(default=False) # ให้ค่าเริ่มต้นเป็น fault
    manager = models.ForeignKey(User, on_delete=models.CASCADE, default=None)