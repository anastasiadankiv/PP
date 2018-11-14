from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.index),
	path('family/<int:family_id>', views.family),
	path('member/<int:member_id>', views.member),
	path('member/<int:member_id>/charge/', views.charge),
	path('member/<int:member_id>/withdraw/', views.withdraw)
]