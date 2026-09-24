from django.urls import path
from . import views

app_name = 'items'

urlpatterns = [
    path('new/', views.new, name='new'),
    path('', views.browse, name='browse'),
    path('<int:pk>', views.details, name='details'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
]