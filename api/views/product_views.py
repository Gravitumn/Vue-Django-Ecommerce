import os
from django.http import JsonResponse
import json
from django.views.decorators.http import require_http_methods
from ..forms import ProductForm
from ..models import Category, Product
from django.core.files.storage import default_storage

from django.contrib.auth import get_user_model
User = get_user_model()

@require_http_methods(['POST'])
@require_http_methods(['POST'])
def add_product(request):
    try:
        category_data = request.POST.get('category')
        if category_data:
            category_ids = json.loads(category_data)
        else:
            return JsonResponse({'errors': {'category': 'This field is required.'}}, status=400)
        
        print(category_ids)
        request.POST._mutable = True
        request.POST.setlist('category', category_ids)  # Set as a list of IDs
        request.POST._mutable = False
        
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False) 
            
            product.save()
            
            product.category.set(category_ids)
            
            return JsonResponse({'message': 'Product added successfully', 'product_id': product.id}, status=201)
        return JsonResponse({'errors': form.errors}, status=400)
    except json.JSONDecodeError:
        return JsonResponse({'errors': {'category': 'Invalid JSON format.'}}, status=400)

#Get all products in database for "ADMIN", 
#if used by "USER" return all products added by that user
@require_http_methods(['GET'])
def get_all_products(request):
    products = Product.objects.filter(user=request.user).values('id', 'name', 'price', 'image','category')
    for product in products:
        if product['image']:
            product['image'] = request.build_absolute_uri(default_storage.url(product['image']))
    return JsonResponse(list(products), safe=False)

#Get all products in database for "ADMIN", 
#if used by "USER" return all products added by that user
@require_http_methods(['GET'])
def show_all_products(request):
    products = Product.objects.distinct().values('id', 'name', 'price', 'image')
    for product in products:
        if product['image']:
            product['image'] = request.build_absolute_uri(default_storage.url(product['image']))
    return JsonResponse(list(products), safe=False)

@require_http_methods(['GET'])
def get_super_category_products(request,super_category_id):
    sub_category = Category.objects.filter(parent_id=super_category_id).values('id','name','parent_id')
    products = Product.objects.filter(category__in=sub_category.values_list('id', flat=True)).distinct().values('id', 'name', 'price','image')
    for product in products:
        if product['image']:
            product['image'] = request.build_absolute_uri(default_storage.url(product['image']))
    return JsonResponse(list(products),safe=False)

@require_http_methods(['GET'])
def admin_get_all_products(request):
    if request.user.role == User.ADMIN:
        products = Product.objects.values('id','name','price','image','user','category')
        for product in products:
            if product['image']:
                product['image'] = request.build_absolute_uri(default_storage.url(product['image']))
        return JsonResponse(list(products),safe=False)
    else:
        return JsonResponse({'message':'Access Denied, Admin Only'},status=403)


@require_http_methods(['PUT'])
def update_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        if request.body:
            try:
                data = json.loads(request.body)
                product.name = data.get('name', product.name)
                product.price = data.get('price', product.price)
                product.category.set(json.loads(data.get('categories')))
            except json.JSONDecodeError:
                return JsonResponse({'message': 'Invalid JSON data'}, status=400)

        else:
            return JsonResponse({'message': 'No data provided'}, status=400)

        product.save()
        return JsonResponse({'message': 'Product updated successfully'}, status=200)
    except Product.DoesNotExist:
        return JsonResponse({'message': 'Product not found'}, status=404)
    except Exception as e:
        print(str(e))
        return JsonResponse({'message': str(e)}, status=400)

@require_http_methods(['POST'])
def update_product_image(request, product_id):
    if request.content_type.startswith("multipart/form-data"):
        try:
            product = Product.objects.get(id=product_id)
            if 'image' in request.FILES:
                if product.image and os.path.isfile(product.image.path):
                    os.remove(product.image.path)
                product.image = request.FILES['image']
            else:
                print('No Image sending')
            
            product.save()
            return JsonResponse({'message': 'Product updated successfully'}, status=200)
        except Product.DoesNotExist:
            return JsonResponse({'message': 'Product not found'}, status=404)
        except Exception as e:
            print(str(e))
            return JsonResponse({'message': str(e)}, status=400)
        
@require_http_methods(['DELETE'])
def delete_product(request, product_id):

    try:
        product = Product.objects.get(id=product_id)
        if product.image and os.path.isfile(product.image.path):
            os.remove(product.image.path)
        product.delete()
        return JsonResponse({'message': 'Product deleted successfully'})
    except Product.DoesNotExist:
        return JsonResponse({'message': 'Product not found'}, status=404)
    except Exception as e:
        return JsonResponse({'message': str(e)}, status=400)