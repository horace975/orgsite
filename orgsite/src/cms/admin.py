from django.contrib import admin

# Register your models here.
from .models import NavBlock, HomeBlock, ServicesBlock, PortfolioBlock, AboutBlock




admin.site.register(NavBlock)
admin.site.register(HomeBlock)
admin.site.register(ServicesBlock)
admin.site.register(PortfolioBlock)
admin.site.register(AboutBlock)