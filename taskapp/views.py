from django.shortcuts import render
from taskapp.models import Task

# Create your views here.
def index(request):
    all_task = Task.objects.all()  # ดึงข้อมูลทั้งหมดมา
    return render(request, "index.html", {"all_task": all_task}) 