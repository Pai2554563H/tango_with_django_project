from django.contrib import admin

# Register your models here.
from rango.models import Category, Page
from rango.models import UserProfile

# the layout of admin
class PageAdmin(admin.ModelAdmin):
    list_display=('title', 'category', 'url')

# Add in this class to customise the Admin Interface
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    # add slug for new category automatically and same as input name


admin.site.register(Category, CategoryAdmin)
admin.site.register(Page,PageAdmin)
admin.site.register(UserProfile)

