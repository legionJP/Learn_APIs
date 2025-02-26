#
# Djoser library for better authentication

# Install Djoser
pipenv install Djoser

- add the app in the installed app keep it after the rest_framework
'djoser',

# Create the filed in settings.py

```PY
DJOSER = {
    "USER_ID_FIELD":"username",
    # "LOGIN_FIELD"
    # USE ANY ONE
}
# add the seesion authenticatin for the djanog admin use simulatenouly, and can be removed for the production

'DEFAULT_AUTHENTICATION_CLASSES':
    [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
```

# Enable the Djoser in the Main Urls.py file
```py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('LemonAPI.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
```
# Djosers API End Points Support 

![alt text](image-30.png)

# Note:
- Using Djoser you can set either the user ID or email address as the username.

#
# Using JWT for Auth and Registration Endpoints

- install package 
Djangorestframework-simplejwt

- Add the jwt in the installed app
- Chnage the Authentication class for JWTAuthentication in the Rest_framework field 

# Urls.py
- import the rest_framework_simplejwt.views for toeknobtainpair view and toeknrefresh view in the project level view 

```py
URL configuration for LemonRestro project.

from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('LemonAPI.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    #path('auth/', include('djoser.urls.jwt')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]
```
# Add the Access token life cycle
SIMPLE_JWT = {
    'ACESS_TOKEN_LIFETIME':timdedelta(minutes=5),

}

# Generate the Token 
http://127.0.0.1:8000/api/token/

# Refresh the JSON Token
http://127.0.0.1:8000/api/token/refresh


# JSON TOKEN 
- You can use the refresh taken to regenerate the access token , But to implement the security measure 
ypu can block the the refresh token after the some use cases for the generations of the token 

```json
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc0MDY4Njg5MSwiaWF0IjoxNzQwNjAwNDkxLCJqdGkiOiIwNDJiZTQxZTUwNDQ0YjQyYTUxNDQ2NmQ4MzMyOTkyYSIsInVzZXJfaWQiOjN9.L3S4bLxFVn4SFXEjqEFsn4l_ZrE6ryetfYCsxBCgZic",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQwNjAwNzkxLCJpYXQiOjE3NDA2MDA0OTEsImp0aSI6Ijc5MGUwM2E2Yzg3OTRkYjNhOTc2NWVmZDA0MWYzMTI1IiwidXNlcl9pZCI6M30.VDirIcpzJiidkzRjzKPectt1zaMNEj8JlfSfHn2iOEU"
}
```

# Token Blaclist for the refresh

- add the below package in the installed_apps

- 'rest_framework_simplejwt.token_blacklist',

- run the migrations

# Project level urls.py 
```python
"""
URL configuration for LemonRestro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from rest_framework_simplejwt.views import TokenBlacklistView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('LemonAPI.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    #path('auth/', include('djoser.urls.jwt')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),

]

```
- add the form  in header with refresh and refresh token to blacklist the token 
http://127.0.0.1:8000/api/token/blacklist/

