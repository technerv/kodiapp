from rest_framework import viewsets, status
from rest_framework.response import Response
from core.models import Plot, House, Tenant
from core.serializers import PlotSerializer, HouseSerializer, TenantSerializer

# ENDPOINTS
# List/Read All Plots

class PlotViewSet(viewsets.ModelViewSet):
    
    queryset = Plot.objects.all()
    serializer_class = PlotSerializer
    
    filterset_fields = ['id','plot_number']
    search_fields = ['plot_number']
    ordering_fields = ['id', 'plot_number']
    
    def get_queryset(self):
        """
        This function returns a list of all the plots for the currently authenticated user
        """   
        return Plot.objects.filter(plot_owner = self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(plot_owner=self.request.user)
    
    def perform_update(self, serializer):
        instance = self.get_object()  # instance before update
        self.request.data.get("plot_number", None)  # read data from request
        if self.request.user.is_authenticated:
            updated_instance = serializer.save(plot_owner=self.request.user)
        else:
            updated_instance = serializer.save()
              
    def destroy(self, request, pk=None, *args, **kwargs):
        instance = self.get_object()
        return super(PlotViewSet, self).destroy(request, pk, *args, **kwargs)

class HouseViewSet(viewsets.ModelViewSet):
     
    queryset = House.objects.all()
    serializer_class  = HouseSerializer

    filterset_fields = ['id', 'house_number']
    search_fields = ['house_number']
    ordering_fields = ['id', 'house_number']

    # def get_queryset(self):
    #     """
    #     This functions returns a list of all the houses for the current authenticated user         
    #     """
    #     return House.objects.filter()




        # return super().get_queryset()
    
