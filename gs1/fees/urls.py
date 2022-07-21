from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('df/',views.django_fee),
    path('pf/',views.python_fees),
]