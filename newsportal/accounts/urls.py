from django.urls import path
from .views import SignUp
from django.contrib.auth.views import LogoutView, TemplateView

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('logout/confirm', TemplateView.as_view(), name='logout_confirm'),
]
