from django.contrib import admin
from .models import Invoice, InvoiceRow, Provider, Customer


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    readonly_fields = ['created']
    fields = ['document_nr', 'created', 'due_date', 'provider', 'customer']


admin.site.register(InvoiceRow)
admin.site.register(Provider)
admin.site.register(Customer)
