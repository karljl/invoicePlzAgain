from django.db import models
from .utils import generate_document_nr, calculate_due_date


class Company(models.Model):

    class Role(models.TextChoices):
        CUSTOMER = 'customer'
        PROVIDER = 'provider'

    role = models.CharField(choices=Role.choices, max_length=8, default=Role.CUSTOMER)

    name = models.CharField(max_length=240)
    phone = models.CharField(max_length=50)
    email = models.EmailField()

    address = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=100)

    registry_nr = models.CharField(max_length=50)
    vat_nr = models.CharField(max_length=50, blank=True)

    iban = models.CharField(max_length=50, blank=True, verbose_name='IBAN')
    bic_swift = models.CharField(max_length=50, blank=True, verbose_name='BIC/SWIFT')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'company'
        verbose_name_plural = 'companies'


class Invoice(models.Model):

    document_nr = models.CharField(max_length=20)

    created = models.DateField(auto_now_add=True)
    due_date = models.DateField()

    provider = models.ForeignKey(Company, on_delete=models.RESTRICT, related_name='provider')
    customer = models.ForeignKey(Company, on_delete=models.RESTRICT, related_name='customer')

    def __str__(self):
        return f'Invoice {self.document_nr} by {self.provider}'

    def save(self, *args, **kwargs):
        num_previous_invoices = Invoice.objects.filter(provider=self.provider).count()
        self.document_nr = generate_document_nr(num_previous_invoices)
        self.due_date = calculate_due_date()
        super().save(*args, **kwargs)


class InvoiceBody(models.Model):

    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='invoice_bodies')

    description = models.CharField(max_length=500)

    amount = models.PositiveIntegerField()
    price = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'invoice body'
        verbose_name_plural = 'invoice bodies'

    def __str__(self):
        return self.description
