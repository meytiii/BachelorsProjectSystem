"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from users.views import UserLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', include('users.urls')),
    path('login/', csrf_exempt(UserLoginView.as_view()), name='login'),
]



# baseurl : karshenasiproject.liara.iran.run/api

# route                          method      body                                        params

# /login                         post        {username:string,password:string}           -
# /projects                      get         -                                           type,query,capacity,status
# /projects                      post        {title:string,capacity:int,suid:string}     -
# /request-project               post        {id:string,students:array}
# /request-project/{sudd}        get         -
# /user-request                  put         {id:int,status:boolean}
# /user-request/{id}                  get         
# /supervisor-active-project/{suiid}     get    - -

# /product?brand=apple&price=10000
