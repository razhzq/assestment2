from django.urls import path
from . import views

urlpatterns = [
    path('purchaseorder/', views.OrderListCreate.as_view()),
    path('item/', views.ItemListCreate.as_view()),
]
