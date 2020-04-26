from django.urls import path
from firstapp import views

app_name='firstapp'

urlpatterns = [
    path('user_login/',views.user_login,name='user_login'),
    path('register/',views.register,name='register'),
]

# In base.html file <!--{% url 'app_name define in urls.py file:name of the url (name='user_login') %}-->