from rest_framework import serializers
from core.models import  House, Tenant, Plot

class PlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plot
        fields = '__all__'
       
class HouseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =  House
        fields = '__all__'        
        # fields = ('plot_number', 'house_number', 'electricity_number', 'water_number', 'rent_amount', 'is_vacant', 'date_joined', 'date_updated')

class TenantSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tenant
        fields = '__all__'
        # fields = ('house_number', 'date_joined', 'date_updated')