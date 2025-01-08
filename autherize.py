from django.shortcuts import redirect

class Autherize:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        admin_pages = {
            'admin/UserManagement':'admin'
        }

        path = request.path
        if path in admin_pages:
            allowed_roles = admin_pages[path]
            if isinstance(allowed_roles,str):
                allowed_roles= [allowed_roles]

            if request.user.is_authenticated and request.user.role not in allowed_roles:
                return redirect('access denied')
            
        return self.get_response(request)