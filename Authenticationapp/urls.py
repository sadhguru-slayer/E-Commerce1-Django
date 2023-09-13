from django.urls import path
from Authenticationapp import views

urlpatterns = [
    path('signup/',views.signup,name="signup"),
    path('login/',views.logins,name="logins"),
    path('logout/',views.logouth,name="logouth"),
    path('activate/<uidb64>/<token>',views.ActivateAccountView.as_view(),name='activate'),
]
