from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(usermodel)
admin.site.register(user)

admin.site.register(product)
admin.site.register(crud)

class cadmin(admin.ModelAdmin):
    list_display=('emp_id','emp_name',)
    search_fields=('emp_id','emp_name',)
    list_filter=('emp_id',)

admin.site.register(emp,cadmin)
admin.site.site_header='hello'
admin.site.site_title='jango'

class adm(admin.ModelAdmin):
    list_display=('title','author','created_at',)
admin.site.register(admn,adm)

admin.site.register(pross)

admin.site.register(publish)

class book_model(admin.ModelAdmin):
    list_display = ('title','isbn','publication_date',)
    search_fields = ('title',)
admin.site.register(model,book_model)


admin.site.register(students)

class coursee(admin.ModelAdmin):
    list_display=('course_name',)
admin.site.register(cours,coursee)

class hoteladmin(admin.ModelAdmin):
    list_display = ('name','location','rate',)
admin.site.register(hotel,hoteladmin)

class gustadmin(admin.ModelAdmin):
    list_display = ('gust_name','check_in','hotels',)
admin.site.register(gust,gustadmin)


admin.site.register(userm)

admin.site.register(userprofile)
admin .site.register(blog)


admin.site.register(register)
admin.site.register(uss)


admin.site.register(imga)




