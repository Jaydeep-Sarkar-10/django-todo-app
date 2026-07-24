from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('add/', views.add_task, name='add'),
    path('delete/<int:id>',views.delete_task, name='delete'),
    path('update_task/<int:id>', views.update_task, name='update'),
    path('complete/<int:id>', views.complete_task, name='complete'),
]

