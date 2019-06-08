from rest_framework import serializers
from .models import Registration


class RegistrationSerialiser(serializers.ModelSerializer):

    class Meta:
        model = Registration
        fields = ('firstname', 'lastname')
        fields = '__all__'  # it will return all ur fields present in registration model


