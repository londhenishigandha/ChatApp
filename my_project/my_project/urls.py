from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.views.generic.base import TemplateView
from rest_framework_simplejwt import views as jwt_views
from my_app import views
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', views.SignUp.as_view(), name='signup'),  # path for signup page
    path('ChatApp/', include('django.contrib.auth.urls')),  # to implement these views in project
    path('', TemplateView.as_view(template_name='home.html'), name='home'),  # The name of a template to display for the view used to log the user in. Defaults to registration/login.html.
    url('Registration/', views.RegistrationList.as_view()),  # it will open the json data
    url('chat/', include('my_app.urls')),
]




