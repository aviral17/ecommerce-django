# update it as per altest changes

from django .urls import path
from . import views
# OR from ecommerceapp import views

urlpatterns = [
    path('', views.index, name="index")
]
