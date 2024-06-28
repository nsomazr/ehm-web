from django.urls import path, include
from users.views import UsersAPIView,MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from users import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "users"   

urlpatterns = [
    path('users/', UsersAPIView.as_view()),
    path('login_token/', MyTokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("logout/", views.logout_request, name= "logout"),
    path("login/", views.login_request, name="login"),
    path("change_password/", views.change_password, name="change-password"),
    path("update_info/", views.update_info, name="update-info"),
    path("add-staff/", views.add_staff, name="add-staff"),
    path("staffs/delete-staff/<int:id>", views.delete_staff, name="delete-staff"),
    path("staffs/deactivate-staff/<int:id>", views.deactivate_staff, name="deactivate-staff"),
    path("staffs/", views.staffs, name="staffs"),
    path("register/", views.register_request, name="register"),
    path("password_reset/", views.password_reset_request, name="password_reset"),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
