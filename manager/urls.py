from django.urls import path
from .views import main, userview, adminview, denied
from django.contrib.auth import views as AuthViews

app_name = 'manager'

urlpatterns = [
	path('', main, name = 'main'),
	path('user/', userview, name = 'user'),
	path('administration/', adminview, name = 'admin'),
	path('login/', AuthViews.LoginView.as_view(), name = 'login'),
	path('denied/', denied, name = 'denied')
]