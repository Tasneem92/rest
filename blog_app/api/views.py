from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from blog_app.models import Trip, AuthUser
from . serializers import TripListSerializer, TripDetailSerializer, TripCreateSerializer

class TripListAPIView(ListAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripListSerializer

class TripDetailAPIView(RetrieveAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripDetailSerializer

    #lookup_field = 'date'
    #lookup_url_kwarg = 'abc'
class TripUpdateAPIView(UpdateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripDetailSerializer

class TripDeleteAPIView(DestroyAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripDetailSerializer

class TripCreateAPIView(CreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripCreateSerializer
    def perform_create(self, serializer):
        c_id = AuthUser.objects.get(id=self.request.user.id)
        serializer.save(bloggerid=c_id)
