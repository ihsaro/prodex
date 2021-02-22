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

    def validate(self, data):
        self.__validate_key(data, 'first_name')
        self.__validate_key(data, 'last_name')
        self.__validate_key(data, 'email')
        return data

    def create(self, validated_data):
        return ProdexUser.objects.create_user(**validated_data)

    def __validate_key(self, data, key):
        if key not in data:
            raise KeyError(f'{key} not present in dictionary!')
        else:
            if data[key] == '':
                raise ValidationError(f'{key} has an empty value!')
