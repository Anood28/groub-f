from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm

# Create your views here.

def update_todo(request , pk):
    
    todo_id = project.objects.get(pk=pk)
    update_form = TodoForm(instance='student id')
    if request.method == 'POST' :
        update_form = TodoForm(request.POST , instance= 'student id')
    if update_form.is_valid():
        update_form.save()
        return redirect('home:std_profile')
    else:
        update_form = TodoForm(instance=student_id)

    return render(request , 'details_std.html' , {
        'Profile.html' :Profile.html,
    })

def std_profile_delete(request , pk):
    std_profile_delete = std_Profile.objects.get(pk=pk)
    std_profile_delete.delete()
    return redirect('home:std_profile')
