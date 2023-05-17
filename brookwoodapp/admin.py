from django.contrib import admin
from .models import Log,brookuser,complaint,product,cart, category, Review,order

# Register your models here.
admin.site.register(Log),
admin.site.register(brookuser),
admin.site.register(complaint),
admin.site.register(product),
admin.site.register(cart),
admin.site.register(category),
admin.site.register(Review),
admin.site.register(order),