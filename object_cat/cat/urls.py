from django.urls import path

from . import views

app_name = 'cat'
urlpatterns = [
    path('', views.connection, name='connection'),#This is the first page
    path('signin/', views.signin, name='signin'),#This is the page where you can sign in
    path('user/<int:user_id>/<int:cat_id>/', views.detail, name='detail'),#This is the page where you can see the details of a cat
    path('user/<int:user_id>/', views.udetail, name='udetail'),#This is the page where you can see the details of a user
    path('user/<int:user_id>/add', views.add, name="add"),#This is the page where you can add a cat
    path('user/<int:user_id>/delete/<int:id>', views.delete, name='delete'),#This is the page where you can delete a cat
    path('user/<int:user_id>/edit/<int:cat_id>', views.edit, name='edit'),#This is the page where you can edit a cat
    path('user/<int:user_id>/delete',views.udelete, name = 'udelete'),#This is the page where you can delete a user
    path('user/<int:user_id>/edit', views.uedit, name='uedit'),#This is the page where you can edit a user
]