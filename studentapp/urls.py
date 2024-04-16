from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.studentapp,name='studentapp'),
    path('create-form',views.createNewPost,name='create'),
    path('update-form/<str:pid>/',views.updatePost,name='update'),
    path('delete/<str:pid>', views.delete,name='delete'),
    path('view/<str:pid>', views.view,name='view'),
]   