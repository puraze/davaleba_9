from django.db.models import Sum, Avg, Max, Min, Count, F, When, Case,CharField, ExpressionWrapper, Q
from .models import Product

avg_price = Product.objects.aggregate(Avg('price'))
avga_price = Product.objects.filter(Q(name__startwith='D')).aggregate(Avg('price'))
total_price = Product.objects.aggregate(Sum('price'))
max_price = Product.objects.aggregate(Max('price'))
min_price = Product.objects.aggregate(min('price'))
countproducts = Product.objects.annotate(product_count =Count('Product'))
avg_price_products = Product.objects.annotate(avg_price = Avg('Product'))
stock_product_value = Product.objects.annotate(stock_value = product_count*avg_price)