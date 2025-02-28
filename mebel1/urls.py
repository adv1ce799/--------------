from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sale/', views.sale, name='sale'),
    path('category/<int:category_id>/', views.category_view, name='category'),
    path('kontakt/', views.kontakt, name='kontakt'),
    path('product/<slug:post_slug>/', views.product, name='product'),
    path('otziv/', views.otziv , name='otziv'),
]

