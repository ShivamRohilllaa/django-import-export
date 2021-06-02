from django.contrib import admin
from .models import *
# Register your models here.
from import_export.fields import Field
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class ExportMixinAdmin(ExportMixin, admin.ModelAdmin):
    
    #Choose your format

    def get_export_formats(self):
        formats = (
            base_formats.CSV,
            base_formats.XLSX,
            base_formats.TSV,
            base_formats.ODS,
            base_formats.JSON,
            base_formats.HTML,
          )

        return [f for f in formats if f().can_export()]

    class Meta:
        abstract = True


class BookResource(resources.ModelResource):
    writer = Field()
    publisher = Field()
    
    class Meta:
        model = book
        exclude = ['qty']

    def dehydrate_writer(self, book):
        return '%s by %s' % (book.bookname, book.writer.auth.username)

    def dehydrate_publisher(self, book):
        return '%s by %s' % (book.bookname, book.publisher.auth.username)

class BookAdmin(ExportMixinAdmin):
    resource_class = BookResource
    

admin.site.register(book, BookAdmin)   
admin.site.register(author) 
admin.site.register(publisher) 