from django.urls import path
from . import views

urlpatterns = [
    path('',views.create),
    path('1',views.display ,name="display"),
    path('2/<int:id>',views.single,name="single"),
    path('edit/<int:pk>',views.edit,name="edit"),
    path('delete/<int:jk>',views.delete, name="delete")
]