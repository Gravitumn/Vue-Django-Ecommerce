import os
from django.http import JsonResponse
import json
from django.views.decorators.http import require_http_methods
from ..forms import ProductForm
from ..models import Product
from django.core.files.storage import default_storage

from django.contrib.auth import get_user_model
User = get_user_model()

@require_http_methods(['POST'])
def add_product(request):
    form = ProductForm(request.POST,request.FILES)
    if form.is_valid():
        product = form.save()
        return JsonResponse({'message': 'Product added successfully', 'product_id': product.id}, status=201)
    return JsonResponse({'errors': form.errors}, status=400)

#Get all products in database for "ADMIN", 
#if used by "USER" return all products added by that user
@require_http_methods(['GET'])
def get_all_products(request):
    if request.user.role == User.ADMIN:
        products = Product.objects.values('id','name','price','image','user')
        for product in products:
            if product['image']:
                product['image'] = request.build_absolute_uri(default_storage.url(product['image']))
        return JsonResponse(list(products),safe=False)
    else:
        products = Product.objects.filter(user=request.user).values('id', 'name', 'price', 'image')
        for product in products:
            if product['image']:
                product['image'] = request.build_absolute_uri(default_storage.url(product['image']))
        return JsonResponse(list(products), safe=False)


@require_http_methods(['PUT'])
def update_product(request, product_id):

    try:
        product = Product.objects.get(id=product_id)
        if request.body:
            try:
                data = json.loads(request.body)
                product.name = data.get('name', product.name)
                product.price = data.get('price', product.price)
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