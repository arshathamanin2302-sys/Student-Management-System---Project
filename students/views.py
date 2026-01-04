from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .models import Students
from .forms import StudentForm

# Create your views here.

def list_Students(request):
    q=request.GET.get('q','').strip()
    students=Students.objects.all()
    if q:
        students=students.filter(name__icontains=q)
        students.filter(roll_no__icontains=q)
        students.filter(course__icontains=q)
    return render(request,'students/list.html',{'students':students, 'q':q})

def add_Student(request):
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student added Successfully')
            return redirect('students:list')
    else:
        form=StudentForm()
    return render(request, 'students/form.html',{'form':form, 'title':'Add Student'})

def edit_Student(request,pk):
    student=get_object_or_404(Students,pk=pk)
    
    if request.method=='POST':
        form=StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            messages.success(request,'Student updated Successfully!')
            return redirect('students:list')
    else:
        form=StudentForm(instance=student)
    return render(request,'students/form.html', {'form':form, 'title':'Edit Student'})

def delete_Student(request,pk):
    student=get_object_or_404(Students,pk=pk)
    
    if request.method=='POST':
        student.delete()
        messages.success(request,'Student deleted Successfully!')
        return redirect('students:list')
    return render(request,'students/confirm_delete.html',{'student':student})

