from django.shortcuts import render, redirect
from django.http import HttpResponse
from taskapp.models import Task
from django.contrib import messages # Messages Tags
from django.core.paginator import Paginator # Pagination
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/login")
def index(request):
    
    if request.method == "POST":
        # ดึงข้อมูลจากฟอร์ม
        name = request.POST["name"]
        # Valaidate
        if name == "":
            messages.warning(request, "Please Insert Task Name")
            return redirect("/")
        # Save
        else:
            task = Task.objects.create(name = name, manager=request.user) 
            task.save()
            messages.success(request, "Saved Successfully")
            return redirect("/")
    else :
        # all_task = Task.objects.all()  # ดึงข้อมูลทั้งหมดมา
        all_task = Task.objects.filter(manager=request.user) # ดึงข้อมูลของแต่ละ manager
        page = request.GET.get("page")
        paginator = Paginator(all_task, 5) # กำหนดรายการที่แสดงต่อ 1 หน้า
        all_task = paginator.get_page(page)
        return render(request, "index.html", {"all_task": all_task}) 

@login_required(login_url="/login")
def complete_task(request, task_id):
    task = Task.objects.get(pk = task_id)
    # User access control
    if task.manager == request.user:
        task.status = True # เปลี่ยนสถานะของงาน
        task.save()
        # messages.success(request, "Saved Successfully")
        return redirect("/")
    else:
        messages.warning(request, "You dont have permission")
        return redirect("/")

@login_required(login_url="/login")
def pending_task(request, task_id):
    task = Task.objects.get(pk = task_id)
    if task.manager == request.user:
        task.status = False # เปลี่ยนสถานะของงาน
        task.save()
        # messages.success(request, "Saved Successfully")
        return redirect("/")
    else:
        messages.warning(request, "You dont have permission")
        return redirect("/")