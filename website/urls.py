
from django.urls import path
from website.views import *

app_name= 'website'
urlpatterns = [
    #path('url address, 'view', name)
    path('',home_view, name='home'),
]
