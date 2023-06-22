from django.urls import path


from .views import CartView, ShopView, ProductSingleView, CartViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'cart', CartViewSet)


app_name = 'store'

urlpatterns = [
   path('cart/', CartView.as_view(), name='cart'),
   path('', ShopView.as_view(), name='shop'),
   path('product/<int:id>/', ProductSingleView.as_view(), name='product'),
]
