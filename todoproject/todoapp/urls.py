from django.urls import path
from . import views

urlpatterns = [
    path('', views.taskview, name='taskview'),
    path('delete/<int:taskid>', views.delete, name='delete'),
    path('cbvtask/',views.TasklistView.as_view(), name='cbvtask'),
    path('cbvdetail/<int:pk>/',views.Taskdetailview.as_view(), name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.Taskupdateview.as_view(), name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.Taskdeleteview.as_view(), name='cbvdelete'),

]
