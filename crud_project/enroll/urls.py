from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.add, name='adddata'),
    path('delete/<int:id>/',views.delete, name='deletedata'),
    path('update/<int:id>/',views.update, name='updatedata'),
]
