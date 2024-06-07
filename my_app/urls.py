from django.urls import path
from .views import *

urlpatterns = [
   path('', index,name='index'), 
   path('about/', about, name='about'), 
   path('contact/', contact, name='contact'), 
   path('blog/', blog_list, name='blog'), 
   path('subscribe/', subscribe, name='subscribe'), 
]
