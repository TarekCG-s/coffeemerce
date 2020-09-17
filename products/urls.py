from rest_framework import routers
from .views import CoffeeMachineViewset, CoffeePodViewset

app_name = 'products'
router = routers.DefaultRouter()
router.register('machines', CoffeeMachineViewset, basename='coffee_machines')
router.register('pods', CoffeePodViewset, basename='coffee_pods')

urlpatterns = router.urls