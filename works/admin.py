from django.contrib.admin import ModelAdmin,register
from .models import Company, Provinces , Category , Job , JobSeeker

@register(Company)
class CompanyAdmin(ModelAdmin):
    pass

@register(Provinces)
class ProvincesAdmin(ModelAdmin):
    pass

@register(Category)
class CategoryAdmin(ModelAdmin):
    pass

@register(Job)
class JobAdmin(ModelAdmin):
    pass

@register(JobSeeker)
class JobSeekerAdmin(ModelAdmin):
    pass

