from rest_framework.serializers import ModelSerializer, ValidationError

from .models import ProdexUser


class RegisterSerializer(ModelSerializer):
    class Meta:
        model = ProdexUser
        fields = ['first_name', 'last_name', 'email', 'username', 'password']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def create(self, validated_data):
        return ProdexUser.objects.create_user(**validated_data)
