from rest_framework import serializers
from cars.models import Car, Comment

class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = ('id', 'make', 'model', 'year', 'description')

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['owner'] = request.user
        return super().create(validated_data)


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('content', 'created_at')

    def create(self, validated_data):
        request = self.context.get('request')
        car_id = request.parser_context['kwargs']['car_id']
        validated_data['author'] = request.user
        validated_data['car'] = Car.objects.get(id=car_id)
        return super().create(validated_data)
