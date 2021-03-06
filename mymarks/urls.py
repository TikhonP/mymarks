from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('login/', views.loginp, name='loginp'),
    path('register/', views.registerp, name='registerp'),
    path('authed/', views.authed, name='authed'),
    path('logout/', views.logoutp, name='logoutp'),
    path('authed/addmark/', views.addmark, name='addmark'),
    path('authed/profile/', views.profilep, name='profilep'),
    path('authed/profile/subjects/', views.subjectsp, name='subjectsp'),
    path('authed/profile/subjects/firstset/', views.subjfirstsetp, name='subjfirstsetp'),
]
