from django.urls import path


from .views import CartView, ShopView, ProductSingleView, CartViewSet, WishlistView, WishlistAdd, WishlistDelete
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'cart', CartViewSet)


app_name = 'store'

urlpatterns = [
   path('cart/', CartView.as_view(), name='cart'),
   path('', ShopView.as_view(), name='shop'),
   path('product/<int:id>/', ProductSingleView.as_view(), name='product'),
   path('wishlist/', WishlistView.as_view(), name='wishlist'),
   path('wishlist/add/<int:id>/', WishlistAdd.as_view(), name='add_to_wishlist'),
   path('wishlist/delete/<int:id>/', WishlistDelete.as_view(), name='delete_from_wishlist'),
]
