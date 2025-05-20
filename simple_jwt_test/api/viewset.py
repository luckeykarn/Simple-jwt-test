# from simple_jwt_test.models import Category,Product
# from rest_framework import viewsets, permissions
# from .serializers import CataegorySerializer, ProductSerializer


# class CategoryViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = Category.objects.all()
#     serializer_class = CataegorySerializer
#     permission_classes = [permissions.IsAuthenticated]


# class ProductViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     permission_classes = [permissions.IsAuthenticated]


from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from simple_jwt_test.models import Category,Product
from rest_framework import viewsets, permissions
from .serializers import CategorySerializer

class CategoryListsCreate(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

class CategoryDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

