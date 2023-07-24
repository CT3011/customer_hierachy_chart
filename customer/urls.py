from django.urls import path
from .views import view_children, logout_view

app_name="customer"

urlpatterns = [
    path('logout/', logout_view, name='logout_view')
]
