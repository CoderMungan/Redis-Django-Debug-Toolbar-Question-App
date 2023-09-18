from django.urls import path,include
from exam_test import views 
from django.contrib.auth import views as authentication_views

urlpatterns = [
    path('',views.index,name='index'),
    path('warning/',views.warning,name='warning'),
    path('login/',authentication_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',authentication_views.LogoutView.as_view(template_name='index.html'),name='logout'),
    path('register/',views.register,name='register'),
    path('question/<int:question_id>/', views.show_question, name='show_question'),
    path('completion/', views.completion_page, name='completion_page'),
    path('answers/',views.view_answers,name='answers'),
     path("__debug__/", include("debug_toolbar.urls")),



]
