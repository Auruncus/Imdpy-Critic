from django.contrib import admin
from .models import Post, Profile, Movie, GenreRating


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_date')
    view_on_site = True

class ProfileAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False
    
    list_display = ('user', 'text') 
    empty_value_display = '-empty-'
    ordering = ('-text',)
    view_on_site = True
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user) 


admin.site.register(Post, PostAdmin)
admin.site.register(Profile,ProfileAdmin)
admin.site.register(Movie)

# Register your models here.
