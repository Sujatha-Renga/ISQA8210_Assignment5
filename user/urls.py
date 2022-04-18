

from django.urls import path
from .views import ChangePwView


urlpatterns = [
    path('change-password/', ChangePwView.as_view(), name='change_password'),

]