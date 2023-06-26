from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework import status

from .models import Cart, Product, Category
from .serializers import CartSerializer
from .views import CartViewSet


class CartViewSetTestCase(TestCase):
    fixtures = ['testdata.json']

    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        category = Category.objects.create(name="Vegetables")
        self.product = Product.objects.create(name='Test Product', description='Test Description',
                                              price=10.0, category=category)

    def test_create_cart_item(self):
        request = self.factory.post('/carts/', {'product': self.product.id})
        request.user = self.user
        view = CartViewSet.as_view({'post': 'create'})

        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], 'Product added to cart')
        self.assertEqual(Cart.objects.count(), 1)

    def test_update_cart_item(self):
        cart_item = Cart.objects.create(user=self.user, product=self.product)
        request = self.factory.put(f'/carts/{cart_item.id}/', {'quantity': 5})
        request.user = self.user
        view = CartViewSet.as_view({'put': 'update'})

        response = view(request, pk=cart_item.id)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], 'Product change to cart')
        cart_item.refresh_from_db()
        self.assertEqual(cart_item.quantity, 5)

    def test_delete_cart_item(self):
        cart_item = Cart.objects.create(user=self.user, product=self.product)
        request = self.factory.delete(f'/carts/{cart_item.id}/')
        request.user = self.user
        view = CartViewSet.as_view({'delete': 'destroy'})

        response = view(request, pk=cart_item.id)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], 'Product delete from cart')
        self.assertEqual(Cart.objects.count(), 0)


class CartSerializerTestCase(TestCase):
    fixtures = ['testdata.json']

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        category = Category.objects.create(name="Vegetables")
        self.product = Product.objects.create(name='Test Product', description='Test Description',
                                              price=10.0, category=category)
        self.cart_item = Cart.objects.create(user=self.user, product=self.product)

    def test_cart_serializer(self):
        serializer = CartSerializer(instance=self.cart_item)
        expected_data = {
            'id': self.cart_item.id,
            'user': self.user.id,
            'quantity': self.cart_item.quantity,
            'product': self.product.id,
        }
        self.assertEqual(serializer.data, expected_data)

# Create your tests here.
