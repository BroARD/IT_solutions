from rest_framework import viewsets
from api.serializers.car_serializer import CarSerializer, CommentSerializer
from cars.models import Car, Comment
from api.permissions import IsOwner
from rest_framework import permissions



class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsOwner]
        else:
            self.permission_classes = [permissions.IsAuthenticatedOrReadOnly]

        return super().get_permissions()


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def get_queryset(self):
        return Comment.objects.filter(car=self.kwargs['car_id'])
