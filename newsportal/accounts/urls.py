from django.urls import path
from .views import SignUp
from django.contrib.auth.views import TemplateView, LogoutView
#from django.contrib.auth import views as auth_views
#from django.contrib.auth import views as authViews



urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('logout/confirm', TemplateView.as_view(template_name='logout_confirm.html'), name='logout_confirm'),
    #path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    #path('logout/', authViews.LogoutView.as_view(next_page='http://127.0.0.1:8000/'), name='logout'),

]
