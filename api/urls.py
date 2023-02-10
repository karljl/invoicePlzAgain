from django.urls import path
from . import views

urlpatterns = [
    path('invoices/', views.InvoiceList.as_view()),
    path('invoices/<int:pk>/', views.InvoiceDetail.as_view()),
    path('invoices/<int:pk>/invoicerows/', views.InvoiceRowsByInvoice.as_view()),
    path('invoicerows/<int:pk>/', views.InvoiceRowDetail.as_view()),
    path('companies/', views.CompanyList.as_view()),
    path('companies/<int:pk>/', views.CompanyDetail.as_view()),
]
