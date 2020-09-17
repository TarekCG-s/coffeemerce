from rest_framework import serializers
from .models import CoffeePod, CoffeeMachine



class CoffeeMachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffeeMachine
        fields = '__all__'

    def to_representation(self, data):
        rep = super(CoffeeMachineSerializer, self).to_representation(data)
        return {rep['code']: rep}


class CoffeePodSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffeePod
        fields = '__all__'

    def to_representation(self, data):
        rep = super(CoffeePodSerializer, self).to_representation(data)
        return {rep['code']: rep}
