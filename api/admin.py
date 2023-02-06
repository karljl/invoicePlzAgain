from django.contrib import admin
from .models import Company, Invoice, InvoiceRow


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    readonly_fields = ['created']
    fields = ['document_nr', 'created', 'due_date', 'provider', 'customer']


admin.site.register(Company)
admin.site.register(InvoiceRow)
