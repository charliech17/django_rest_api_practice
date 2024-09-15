from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('get-web-event/', views.webhook_handler),
]
