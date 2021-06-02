from django.contrib import admin
from .models import *
# Register your models here.
from import_export.fields import Field
from import_export import resources
from import_export.admin import ImportExportModelAdmin


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

class BookAdmin(ImportExportModelAdmin):
    resource_class = BookResource
    

admin.site.register(book, BookAdmin)   
admin.site.register(author) 
admin.site.register(publisher) 