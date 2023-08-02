from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('create/', views.add_elements, name='add-elements'),
    path('all/', views.view_elements, name='view_elements'),
    path('update/<int:pk>/', views.update_elements, name='update-elements'),
    path('element/delete/<int:pk>/', views.delete_elements, name='delete-elements'),
]

