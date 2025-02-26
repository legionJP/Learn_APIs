#
# User Account Management:
# User Registration Using the Djore 

# User registration: 

http://127.0.0.1:8000/auth/users/

```json
POST /auth/users/
HTTP 201 Created
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "email": "user3@gmail.com",
    "username": "User3"
}
```
# View for super user to add user in the group
```py
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import User, Group

@api_view(['POST'])
@permission_classes([IsAdminUser])
def managers(request):
    username = request.data['username']
    if username:
        user = get_object_or_404(User,username=user)
        managers = Group.objects.get(name='Manager')
        if request.method =='POST':
            managers.user_set.add(user)
        elif request.method =='DELETE':
            managers.user_set.remove(user)

        return Response({"message":"Ok"})
    return Response({"message":'error'},status=status.HTTP_400_BAD_REQUEST)

```
- path('group/managers/users', views.managers),