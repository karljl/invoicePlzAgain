from django.http import Http404

from rest_framework import status
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

    def get_object(self, pk):
        try:
            return Invoice.objects.get(id=pk)
        except Invoice.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        invoice = self.get_object(pk)
        serializer = InvoiceSerializer(invoice, many=False)
        return Response(serializer.data)

    def put(self, request, pk):
        invoice = self.get_object(pk)
        serializer = InvoiceSerializer(invoice, data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
