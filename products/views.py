from django.shortcuts import render
from django.http import HttpResponse
from .models import *
  
def index(request):
    products = list(Product.objects.all().order_by("sort_order"))
    images = Image.objects.all().order_by("sort_order")
    result = []

    for product in products:
        image = images.filter(product_id=product.id).first()

        result.append(
            {
                "content": product,
                "image": image
            }
        )

    return render(request, "index.html", context={"products": result})

def product(request, id):
    product = Product.objects.all().filter(id=id).first()
    if product:
        images = Image.objects.all().order_by("sort_order").filter(product_id=product.id)
        parameters = Parameter.objects.all().order_by("sort_order").filter(product_id=product.id)
            
        result = {
            "product": {
                "content": product,
                "images": images,
                "parameters": parameters
            }
        }

        return render(request, "product.html", context=result)
    else:
        return HttpResponse("404")