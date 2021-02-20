
from django.urls import path,include
from .views import addshow,delete_data,update
urlpatterns = [
    path('',addshow,name='addshow'),
    path('delete/<int:id>/',delete_data,name='deletedata'),
    path('update/<int:id>/',update,name='update')
]
