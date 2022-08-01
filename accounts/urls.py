from django.urls import path
from accounts.views import signup
from board.views import func
from django.contrib.auth import views
urlpatterns = [
    path('signup/',signup,name="signup"),
    path('', func,name="index"),
    path('logout/',views.LogoutView.as_view(),name='logout'),
    path('login/', views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('changepassword/',views.PasswordChangeView.as_view(template_name='accounts/changepass.html'),name="changepass"),
    path('passwordchanged/',views.PasswordChangeDoneView.as_view(template_name='accounts/passchanged.html'), name="passchanged"),

]