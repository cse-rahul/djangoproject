from django.urls import path
from genre import views

urlpatterns = [
    #/genres/
    path('', views.index.as_view(), name='index'),

    #genre/1 1 present id of the collection
path('register/', views.UserFormView.as_view(), name='userform'),
    path('<pk>/', views.details.as_view(), name="details"),


]
