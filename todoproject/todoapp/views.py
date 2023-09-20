from django.http import HttpResponse
from django.shortcuts import render,redirect
from . models import Task
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.
class TasklistView(ListView):
    model = Task
    context_object_name = 'obj1'
    template_name='taskview.html'

class Taskdetailview(DetailView):
    model = Task
    template_name='detail.html'
    context_object_name='i'

class Taskupdateview(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})

class Taskdeleteview(DeleteView):
    model = Task
    template_name='delete.html'
    get_success_url= reverse_lazy('cbvtask')

def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method=="POST":
        task.delete()
        return redirect('/')
    return render(request,'delete.html',{'task':task})

def taskview(request):
    obj1=Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('name')
        priority=request.POST.get('priority')
        date=request.POST.get('date')

        obj=Task(name=name, priority=priority, date=date)
        obj.save()

    return render(request,'taskview.html',{'obj1':obj1} )

