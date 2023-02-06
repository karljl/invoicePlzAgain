from rest_framework import serializers
from .models import Invoice


class InvoiceSerializer(serializers.ModelSerializer):

    invoice_rows = serializers.PrimaryKeyRelatedField(
        read_only=True,
        many=True
    )

    class Meta:
        model = Invoice
        fields = '__all__'
