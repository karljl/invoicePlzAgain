from rest_framework.decorators import APIView
from rest_framework.response import Response
from .models import Invoice
from .serializers import InvoiceSerializer


class InvoiceList(APIView):

    def get(self, request):
        invoices = Invoice.objects.all()
        serializer = InvoiceSerializer(invoices, many=True)
        return Response(serializer.data)


class InvoiceDetail(APIView):

    def get(self, request, pk):
        invoice = Invoice.objects.get(id=pk)
        serializer = InvoiceSerializer(invoice, many=False)
        return Response(serializer.data)
