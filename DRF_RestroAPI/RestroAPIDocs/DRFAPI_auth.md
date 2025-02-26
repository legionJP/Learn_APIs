#
# DRF Security

# Password Auth
![alt text](image-26.png)

# Token Based Authentication
- In this if the user is authenticated the server generates the token 
- This token is combination of Long char , Hard to read , and Aplhanumerical char, symbols
- So when new API request is send the token is included in the Headers
- server side method TokenAuthentication class validate the token and match with the user 

![alt text](image-27.png)

# settings.py
- add the rest_framework.authtoken  in the installed app section 
- pipenv shell
- run migrations for the auth token app

- create the superuser
    - python manage.py createsuperuser

# Add the token for the user 
    
http://127.0.0.1:8000/admin/authtoken/tokenproxy/

# Use of the Token for secure API


- Header for the authentication
Authorization: Token adadsddadhq]ewriwrr
```py
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def secret(request):
    return Response({'message': 'This is a secret message'}, status=status.HTTP_200_OK)
```

# Generating the Token for the Users by api end point
```py
from rest_framework.authtoken.views import obtain_auth_token
path('secret/', views.secret),
    path('api-token-auth/',obtain_auth_token) # api/api-token-auth/
```