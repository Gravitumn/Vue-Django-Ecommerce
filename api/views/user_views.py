from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
import json
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login, logout 

from ..forms import CreateUserForm
from django.contrib.auth import get_user_model
User = get_user_model()

#----------------------------------------- Authentication ----------------------------------------------#
@ensure_csrf_cookie
@require_http_methods(['GET'])
def set_csrf_token(request):
    """
    We set the CSRF cookie on the frontend.
    """
    return JsonResponse({'message': 'CSRF cookie set'})


@require_http_methods(['POST'])
def login_view(request):
    try:
        data = json.loads(request.body.decode('utf-8'))
        email = data['email']
        password = data['password']
    except json.JSONDecodeError:
        return JsonResponse(
            {'success': False, 'message': 'Invalid JSON'}, status=400
        )

    user = authenticate(request, username=email, password=password)

    if user:
        login(request, user)
        print(f"Logged-in user's role: {request.user.role}")
        return JsonResponse({'success': True,'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'role': user.role
            }})
    return JsonResponse(
        {'success': False, 'message': 'Invalid credentials'}, status=401
    )


def logout_view(request):
    logout(request)
    return JsonResponse({'message': 'Logged out'})



@require_http_methods(['GET'])
def user(request):
    if request.user.is_authenticated:
        return JsonResponse(
            {'username': request.user.username, 'email': request.user.email, 'password':request.user.password, 'role':request.user.role, 'id':request.user.id}
        )
    return JsonResponse(
        {'message': 'Not logged in'}, status=401
    )


@require_http_methods(['POST'])
def register(request):
    data = json.loads(request.body.decode('utf-8'))
    form = CreateUserForm(data)
    if form.is_valid():
        form.save()
        return JsonResponse({'success': 'User registered successfully'}, status=201)
    else:
        errors = form.errors.as_json()
        return JsonResponse({'error': errors}, status=400)
    


#----------------------------------------- User Management ----------------------------------------------#

@require_http_methods(['GET'])
def get_all_users(request):
    if request.user.role == User.ADMIN:
        users = User.objects.values('id','username','email','role')
        return JsonResponse(list(users),safe=False)
    else:
        return JsonResponse(
            {'message':'Access denied: Admin Only'},status = 403
        )

@require_http_methods(['PUT'])
def update_user(request, user_id):
    print(request.user.role)
    if request.user.role != User.ADMIN:
        return JsonResponse({'message': 'Access denied: Admins only'}, status=403)
    
    data = json.loads(request.body)
    try:
        user = User.objects.get(id=user_id)
        user.username = data.get('username', user.username)
        user.email = data.get('email', user.email)
        user.role = data.get('role', user.role)
        if 'password' in data:
            user.set_password(data['password'])
        user.save()
        return JsonResponse({'message': 'User updated successfully'})
    except User.DoesNotExist:
        return JsonResponse({'message': 'User not found'}, status=404)
    except Exception as e:
        return JsonResponse({'message': str(e)}, status=400)
    

@require_http_methods(['DELETE'])
def delete_user(request, user_id):
    if request.user.role != User.ADMIN:
        return JsonResponse({'message': 'Access denied: Admins only'}, status=403)
    
    try:
        user = User.objects.get(id=user_id)
        user.delete()
        return JsonResponse({'message': 'User deleted successfully'})
    except User.DoesNotExist:
        return JsonResponse({'message': 'User not found'}, status=404)
    except Exception as e:
        return JsonResponse({'message': str(e)}, status=400)
    
