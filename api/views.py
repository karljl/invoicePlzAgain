from django.http import Http404

from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.response import Response

from .models import Invoice, InvoiceRow, Company
from .serializers import InvoiceSerializer, InvoiceRowSerializer, CompanySerializer


class InvoiceList(APIView):

    def get(self, request):
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


class CompanyList(APIView):

    def get_role(self, request):
        return request.query_params.get('role')

    def get(self, request):
        company_role = self.get_role(request)
        companies = Company.objects.filter(role=company_role)
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)
