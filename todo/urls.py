from django.urls import path
from . import views

urlpatterns = [
    path('addTask/',views.addTask,name='addTask'),
    path('mark_as_done/<int:pk>/',views.mark_as_done,name="mark_as_done"),
    path('undo/<int:pk>/',views.undo,name="undo"),
    path('editTask/<int:pk>/',views.editTask,name='editTask'),
    path('deleteTask/<int:pk>',views.deleteTask,name="deleteTask")
    
]