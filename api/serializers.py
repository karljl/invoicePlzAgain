from rest_framework import serializers
from .models import Invoice, InvoiceRow, Provider, Customer


class InvoiceSerializer(serializers.ModelSerializer):

    invoice_rows = serializers.PrimaryKeyRelatedField(
        read_only=True,
        many=True
    )

    class Meta:
        model = Invoice
        fields = '__all__'


class InvoiceRowSerializer(serializers.ModelSerializer):

    class Meta:
        model = InvoiceRow
        fields = '__all__'


class ProviderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Provider
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = '__all__'
