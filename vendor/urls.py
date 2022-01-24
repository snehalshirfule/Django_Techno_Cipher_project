

from django.urls import path
from vendor import views

urlpatterns = [

    path('signin',views.signin),
    path('signup',views.signup),
    path('vdashboard',views.vdashboard),
    path('profile',views.saveprofile),
    path('signout',views.signout),
    path('mypackage',views.mypackage),
]