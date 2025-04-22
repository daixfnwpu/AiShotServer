from rest_framework import generics,viewsets
from ...models import Shop
from ...serializers import ShopSerializer

class ShopListView(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
