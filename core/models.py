from django.db import models
from django.conf import settings

class Plot(models.Model):
    # check whether the plot number field can be either UUID(unique identifier id), integer field or character field 
    plot_owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Owner Name", on_delete = models.CASCADE, null=True)
    plot_number = models.CharField(max_length=10, verbose_name='Plot Number', unique=True, null=True, blank=True)
    plot_image = models.ImageField(upload_to="img", null=True, blank=True)
    date_joined = models.DateTimeField(verbose_name="Date Created", auto_now_add=True, null=True, blank=True)
    date_updated = models.DateTimeField(verbose_name="Date Updated", auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.plot_number
        
    class Meta:
        ordering = ['-date_updated']
        verbose_name_plural = "Plot Data"

class House(models.Model):
    
    plot_number = models.ForeignKey('Plot', verbose_name="Plot Number", on_delete=models.CASCADE, null=True)
    house_number = models.CharField(max_length=3, verbose_name = "House Number", blank = True)
    electricity_number = models.CharField(max_length=10, verbose_name="Electricity Account Number", blank=True)
    water_number = models.CharField(max_length=10, verbose_name="Water Meter Number", blank=True)
    rent_amount = models.IntegerField(verbose_name="Rent Amout", blank=True)
    is_vacant = models.BooleanField(default=True)
    house_image = models.ImageField(upload_to="img", blank=True, null=True)
    date_joined = models.DateTimeField(verbose_name="Date Created", auto_now_add=True, null=True, blank=True)
    date_updated = models.DateTimeField(verbose_name="Date Updated", auto_now=True, null=True, blank=True)
    
    def __str__(self):
        return self.house_number

    def get_plot_number(self):
        return self.plot_number

    class Meta:
        verbose_name_plural = "House Data"
	

class Tenant(models.Model):

    tenant_name = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name="Tenant Name", on_delete=models.CASCADE, null=True)
    house_number = models.ForeignKey(House, verbose_name="House Number", on_delete=models.CASCADE)
    date_joined = models.DateTimeField(verbose_name="Date Created", auto_now_add=True, null=True, blank=True)
    date_updated = models.DateTimeField(verbose_name="Date Updated", auto_now=True, null=True, blank=True)
    
    def get_house_no(self):
        
        """_summary_

        Returns House Number
        """
        
        return self.house_number
    
    # def get_tenant_name(self):
    #     return self.tenant_name
        
    class Meta:
        verbose_name_plural = "Tenant Data"

# class MpesaTransaction(models.Model):
#     tenant_name = models.ForeignKey(Tenant, verbose_name='Tenant Name', on_delete=models.CASCADE)
#     phone_number = models.IntegerField(verbose_name="Phone Number", unique = True, null=True, blank=True)
#     amount = models.IntegerField(verbose_name="Amount", unique = True, null=True, blank=True)
#     mpesa_transaction_id = models.CharField(max_length=10, verbose_name="Mpesa Transaction ID", unique=True, null=True, blank=True)
#     date_joined = models.DateTimeField(verbose_name="Date Created", auto_now_add=True, null=True, blank=True)
#     date_updated = models.DateTimeField(verbose_name="Date Updated", auto_now=True, null=True, blank=True)
    
#     def __str__(self):
#         return self.mpesa_transaction_id    