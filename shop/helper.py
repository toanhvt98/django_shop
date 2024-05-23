from .models import ProductOrder
from django.db.models import Sum
def get_top_quantity_per_product():

    top_quantities = (
        ProductOrder.objects
        .values('product_id') 
        .annotate(total_quantity=Sum('quantity')) 
        .order_by('-total_quantity')[:10]
        .values('product_id','product_id__folder_image', 'total_quantity') 
    )

    # Top 1 each product
    top_one_quantities_per_product = {}
    for item in top_quantities[0]:
        product_id = item['product_id']
        folder_image = item['product_id__folder_image']
        total_quantity = item['total_quantity']
        if product_id not in top_one_quantities_per_product:
            top_one_quantities_per_product[product_id] = {'folder_image': folder_image, 'total_quantity': total_quantity}
    # top 10 each product
    top_ten_quantities_per_product = {}
    for item in top_quantities:
        product_id = item['product_id']
        folder_image = item['product_id__folder_image']
        total_quantity = item['total_quantity']
        if product_id not in top_ten_quantities_per_product:
            top_ten_quantities_per_product[product_id] = {'folder_image': folder_image, 'total_quantity': total_quantity}
            
    return top_one_quantities_per_product,top_ten_quantities_per_product

import os
def get_static_image_files():
    # Path to the static directory
    static_dir = "D:/django_shop/static/images"

    # Path to the image subdirectory within the static directory
    image_dir = os.path.join(static_dir, "index_images")

    # Check if the image directory exists
    if not os.path.isdir(image_dir):
        return []

    # Get a list of all files in the image directory
    image_files = [os.path.join(image_dir, file) for file in os.listdir(image_dir) if os.path.isfile(os.path.join(image_dir, file))]

    return image_files