from django.views.decorators.http import require_http_methods
from ..models import Category 
from django.http import JsonResponse


@require_http_methods(['GET'])
def get_super_category(request):
    categories = Category.objects.filter(parent_id = None).values('id', 'name')
    return JsonResponse(list(categories), safe=False)

@require_http_methods(['GET'])
def get_sub_category(request):
    categories = Category.objects.exclude(parent_id=None).values('id','name')
    return JsonResponse(list(categories),safe=False)

@require_http_methods('GET')
def get_sub_category_by_parent(request,parent_id):
    categories = Category.objects.filter(parent_id = parent_id).values('id','name')
    return JsonResponse(list(categories),safe=False)

