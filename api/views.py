from django.http import Http404

from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.response import Response

from .models import Invoice, InvoiceRow, Customer, Provider
from .serializers import InvoiceSerializer, InvoiceRowSerializer, ProviderSerializer, CustomerSerializer


class InvoiceList(APIView):

    def get_provider(self, request):
        return request.query_params.get('provider')

    def get(self, request):
        provider = self.get_provider(request)

        if provider is not None:
            invoices = Invoice.objects.filter(provider=provider)
        else:
            invoices = Invoice.objects.all()

        serializer = InvoiceSerializer(invoices, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = InvoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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

    def delete(self, pk):
        invoice = self.get_object(pk)
        invoice.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class InvoiceRowsByInvoice(APIView):

    def get_invoice(self, pk):
        try:
            return Invoice.objects.get(id=pk)
        except Invoice.DoesNotExist:
            raise Http404

    def get_invoice_rows(self, invoice):
        try:
            return InvoiceRow.objects.filter(invoice=invoice)
        except InvoiceRow.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        invoice = self.get_invoice(pk)
        invoice_rows = self.get_invoice_rows(invoice)
        serializer = InvoiceRowSerializer(invoice_rows, many=True)
        return Response(serializer.data)


class InvoiceRowDetail(APIView):

    def get_object(self, pk):
        try:
            return InvoiceRow.objects.get(id=pk)
        except InvoiceRow.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        invoice_row = self.get_object(pk)
        serializer = InvoiceRowSerializer(invoice_row, many=False)
        return Response(serializer.data)

    def put(self, request, pk):
        invoice_row = self.get_object(pk)
        serializer = InvoiceRowSerializer(invoice_row, data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, pk):
        invoice_row = self.get_object(pk)
        invoice_row.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CustomerList(APIView):

    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomerDetail(APIView):

    def get_object(self, pk):
        try:
            return Customer.objects.get(id=pk)
        except Customer.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        customer = self.get_object(pk)
        serializer = CustomerSerializer(customer, many=False)
        return Response(serializer.data)

    def put(self, request, pk):
        customer = self.get_object(pk)
        serializer = CustomerSerializer(customer, data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, pk):
        customer = self.get_object(pk)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProviderList(APIView):

    def get(self, request):
        providers = Provider.objects.all()
        serializer = CustomerSerializer(providers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProviderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProviderDetail(APIView):

    def get_object(self, pk):
        try:
            return Provider.objects.get(id=pk)
        except Provider.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        provider = self.get_object(pk)
        serializer = ProviderSerializer(provider, many=False)
        return Response(serializer.data)

    def put(self, request, pk):
        provider = self.get_object(pk)
        serializer = ProviderSerializer(provider, data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, pk):
        provider = self.get_object(pk)
        provider.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
