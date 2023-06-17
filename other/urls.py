from django.urls import path


from .views import CurrentDateView, HelloWorld, RandomNumber, IndexView


urlpatterns = [
   path('datetime/', CurrentDateView.as_view()),
   path('hello/', HelloWorld.as_view()),
   path('randomnum/', RandomNumber.as_view()),
   path('', IndexView.as_view())
]
