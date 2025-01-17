from django.urls import path
from .import views
urlpatterns = [
    path('', views.home, name='home page'),
    path('registration/', views.registration, name='registration page'),
    path('login/', views.login, name='login page'),
    path('adminlogin/',views.adminlogin,name='Admin login page'),
    path('caraddadmin/',views.CarAddAdmin,name='Car add'),
    path('showcars/',views.showcars,name='show cars'),
    path('editcar/',views.editcar,name='edit cars'),
    path('updatecar/<cars_number>',views.updatecar,name='update cars'),
    path('updatecarsinfo/<cars_number>',views.updatecarsinfo,name='update info'),
    path('delete/<str:cars_number>',views.delrec,name='delete car'),
    path('logout/', views.logout, name='logout'),
    path('rent/', views.rent, name='rent'),
    path('usercars/', views.usercarsi, name='usercars'),
    path('notapprove/<str:cars_number>',views.notapprove,name='not approve'),
    path('approved/<str:cars_number>',views.approved,name='approve'),
    path('finalapprove/<str:cars_number>',views.finalapprove,name='update info'),
    path('showcars/book/<str:cars_number>',views.book,name='book'),
    path('booking/<str:cars_number>',views.booking,name='booking'),
    path('bookusercars/',views.bookusercar,name='bookusercars'),
    path('bookusercars/book/<str:cars_number>',views.book_userar,name='bookuser'),
    path('showpayment/',views.showpayment,name='showpayment'),
    path('givereview/',views.review,name='givereview'),
    path('showadvice/',views.advices,name='showadvice'),
]