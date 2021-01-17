from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index',views.index,name="index"),
    path('login',views.login,name="login"),
    path('dashboard',views.dashboard,name="dashboard"),
    path('adminlogin',views.adminlogin,name="adminlogin"),
    path('preg',views.preg,name="preg"),
    path('edit',views.edit,name="edit"),
    path('adminregister',views.adminregister,name="adminregister"),
    path('staffregister',views.staffregister,name="staffregister"),
    path('adminlogin',views.adminlogin,name="adminlogin"),
    path('logout',views.logout,name="logout"),
    path('pprofile',views.pprofile,name="pprofile"),
    path('pedit',views.pedit,name="pedit"),
    path('sprofile',views.sprofile,name="sprofile"),
    path('sedit',views.sedit,name="sedit"),
    path('payment',views.payment,name="payment"),
    path('attendance',views.Attend,name="attendance"),
    path('paymentadmin',views.paymentadmin,name="paymentadmin"),
    path('payfee',views.payfee,name="payfee"),
    path('payfeeadmin',views.payfeeadmin,name="payfeeadmin"),
    path('photoupload',views.photoupload,name="photoupload"),
    path('photogallery',views.photogallery,name="photogallery"),
    path('contact',views.contact,name="contact"),
               ]
