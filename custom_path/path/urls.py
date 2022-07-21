from django.contrib import admin
from django.urls import path,register_converter
from . import views,converters
register_converter(converters.FourDigitConverter,'yyyy')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<yyyy:year>/',views.show_detail, name='detail')
]
