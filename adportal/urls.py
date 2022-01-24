from django.urls import path
from . import views



urlpatterns = [

    path('signin',views.signin),
    path('profile1',views.profile1),
    path('vtable',views.vendortable),
    path('utable',views.usertable),
    path('table',views.table),
    path('category', views.category),
    path('addcat', views.addcategory),
    path('signout', views.signout),
    path('delete/<int:id>',views.delete),
    path('edit/<int:id>',views.edit),
    path('subcategory',views.subcategory),
    path('addsubcat', views.addsubcat),

]