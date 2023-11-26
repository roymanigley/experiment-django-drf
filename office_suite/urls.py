from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(template_name='login-template.html'), name='login'),
    path('accounts/profile/', TemplateView.as_view(template_name='account-template.html'), name='profile'),
    path('api/accounting/', include('accounting.urls'))
]
