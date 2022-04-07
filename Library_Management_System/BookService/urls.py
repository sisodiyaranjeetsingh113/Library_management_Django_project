from django.urls import path
from . import views
urlpatterns = [
    path('',views.base),
    path('accounts/profile/',views.all_book),
    path('create/',views.create_book),
    path('update/<int:id>/',views.update_book),
    path('delete/<int:id>/',views.delete_book),
]
