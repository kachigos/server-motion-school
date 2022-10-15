from django.contrib import admin
from .models import Category, Accreditation, Chronology, Teacher, File, Administration


class FileInlines(admin.TabularInline):
    model = File
    extra = 0


class AccreditationAdmin(admin.ModelAdmin):
    filter_horizontal = ['files',]
    


class AdministrationAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'position']

admin.site.register(Category)
admin.site.register(Accreditation, AccreditationAdmin)
admin.site.register(Chronology)
admin.site.register(Teacher)
admin.site.register(File)
admin.site.register(Administration, AdministrationAdmin)
