from rest_framework import generics
from rest_framework.response import Response

from .models import Advert
from .serializers import AdvertSerializer


class AdvertList(generics.ListAPIView):
    queryset = Advert.objects.all()
    serializer_class = AdvertSerializer


class AdvertDetail(generics.RetrieveUpdateAPIView):
    queryset = Advert.objects.all()
    serializer_class = AdvertSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.views += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
