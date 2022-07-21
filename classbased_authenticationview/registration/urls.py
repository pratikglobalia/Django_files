from django.contrib import admin
from django.urls import path
from registration import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', views.ProfileTemplateView.as_view(), name='profile')
]
