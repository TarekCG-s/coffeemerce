from rest_framework import viewsets
from .models import CoffeePod, CoffeeMachine
from .serializers import CoffeeMachineSerializer, CoffeePodSerializer


class CoffeeMachineViewset(viewsets.ReadOnlyModelViewSet):
    model = CoffeeMachine
    serializer_class = CoffeeMachineSerializer

    def get_queryset(self):
        queryset = CoffeeMachine.objects.all()

        product_type = self.request.GET.get('type')
        if product_type:
            queryset = queryset.filter(product_type=int(product_type))

        product_class = self.request.GET.get('class')
        if product_class:
            queryset = queryset.filter(product_class=int(product_class))

        water_compatible = self.request.GET.get('water_compatible')
        if water_compatible:
            if water_compatible in ['True', 'true', 't', '1']:
                queryset = queryset.filter(water_line_compatible=True)
            elif water_compatible in ['False', 'false', 'f', '0']: 
                queryset = queryset.filter(water_line_compatible=False)

        return queryset


class CoffeePodViewset(viewsets.ReadOnlyModelViewSet):
    model = CoffeePod
    serializer_class = CoffeePodSerializer
    
    def get_queryset(self):
        queryset = CoffeePod.objects.all()

        flavor = self.request.GET.get('flavor')
        if flavor:
            queryset = queryset.filter(coffee_flavor=int(flavor))

        product_type = self.request.GET.get('type')
        if product_type:
            queryset = queryset.filter(product_type=int(product_type))

        pack_size = self.request.GET.get('size')
        if pack_size:
            queryset = queryset.filter(pack_size=int(pack_size))

        return queryset
