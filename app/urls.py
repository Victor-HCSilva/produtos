from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_product/', views.add_product, name='add_product'),
    path('select_product/', views.select_product, name='select_product'),
    path('update_product/<int:id>/', views.update_product, name='update_product'),
    path('add_mark/', views.add_mark, name='add_mark'),
    path('delete_product/<int:id>', views.delete_product, name='delete_product'),
]