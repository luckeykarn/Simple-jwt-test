from django.urls import path, include
from simple_jwt_test.models import Category, Product
from rest_framework import routers
from .viewset import CategoryListsCreate,CategoryDetailView
from rest_framework_simplejwt.views import TokenVerifyView


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
# router.register(r'category', CategoryListsCreate)
# router.register(r'category', CategoryDetailView)
# router.register(r'product', ProductViewSet)


# Wire up our API using automatic URL routing.

urlpatterns = [
    path('', include(router.urls)),

    path('categories/', CategoryListsCreate.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    #Simple-JWT 
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]