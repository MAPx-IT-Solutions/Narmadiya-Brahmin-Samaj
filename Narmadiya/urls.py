"""NarmadiyaBrahminSamaj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index),
    path('news',views.news),
    path('aboutsociety',views.aboutsociety),
    path('religious',views.religious),
    path('contactus',views.contactus),
    path('login',views.login),
    path('accounts/login/',views.login),
    path('register',views.register),
    path('matrimonyform',views.matrimonyform),
    path('matrimony',views.matrimony),
    path('sampark',views.sampark),
    path('pratibha',views.pratibha),
    path('sanstha',views.sanstha),
    path('samajvistar',views.samajvistar),
    path('bloodbank',views.bloodbank),
    path('donation',views.donation),
    path('add',views.add),
    path('feedback',views.feedback),
    path('reset_password',auth_views.PasswordResetView.as_view(template_name="password_reset.html"),name="reset_password"),
    path('reset_password_sent',auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"),name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"),name="password_reset_complete"),
    path('handlelogin',views.handlelogin),
    path('handlelogout',views.handlelogout),
    path('changepassword',auth_views.PasswordChangeView.as_view(template_name="changepass.html"),name="change_password"),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(template_name="passwordchanged.html"), name='password_change_done'),
    path('Profile/<int:myid>',views.profile),

    
]
