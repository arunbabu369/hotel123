from django.urls import path,include
from . import views

urlpatterns = [
    #path('base', views.base, name='base1'),
    path('signup', views.signup1, name='chanjal'),
    path('', views.login, name='login'),
    path('addrooms', views.addrooms, name='addrooms'),
    path('viewdetails',views.viewdetails,name='list'),
    path('conf_booking/<id>',views.conf_booking,name='conf_booking'),
    path('booking_page/<id>',views.booking_page,name='booking_page'),
    path('adm_logout_view',views.adm_logout_view,name='adm_logout_view'),
    path('roomtype_view',views.roomtype_view,name='roomtype_view'),
    path('booked_view',views.booked_view,name='booked_view'),
    path('adminhome',views.adminhome,name='adminhome'),
    path("logout_request", views.logout_request, name="logout_request"),
    path('payment',views.payment, name="payment"),
    path('password_reset', views.password_reset, name="password_rest"),
    path('success',views.success,name="success"),
    path('summary',views.summary,name="summary"),
    path('reset_password_page',views.reset_password_page,name="reset_password_page"),
    path('viewbookadmin', views.viewbookadmin, name="viewbookadmin"),
    path('viewroom',views.viewroom,name="viewroom"),
]


