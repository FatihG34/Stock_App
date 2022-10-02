from django.urls import path, include
from .views import RegisterView

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/register/', RegisterView.as_view()),

]
