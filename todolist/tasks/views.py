
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Todo1
def todo_list(request):
    if request.method == "POST":
        task = request.POST.get('task')
        datetime = request.POST.get('datetime')
        status = request.POST.get('status')
        if task and datetime and status:
            Todo1.objects.create(
                task=task,
                datetime=datetime,
                status=status
            )
            messages.success(
                request,
                'Task added Successfully'
            )
        else:
            messages.error(
                request,
                'All fields are required.'
            )
        return redirect('todo_list')
    # GET request - Display all todos
    todos = Todo1.objects.all()
    return render(
        request,
        'tasks/todo_list.html',
        {'todos': todos}
    )
def edit_todo(request, id):
    todo = get_object_or_404(Todo1, id=id)
    if request.method == "POST":
        todo.task = request.POST.get('task')
        todo.datetime = request.POST.get('datetime')
        todo.status = request.POST.get('status')
        todo.save()
        messages.success(
            request,
            'Task updated successfully!'
        )
        return redirect('todo_list')
    return render(
        request,
        'tasks/edit_todo.html',
        {'todo': todo}
    )
def delete_todo(request, id):
    todo = get_object_or_404(Todo1, id=id)
    if request.method == "POST":
        todo.delete()
        messages.success(
            request,
            'Task deleted successfully!'
        )
    return redirect('todo_list')
