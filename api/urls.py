from django.urls import path
from . import views

urlpatterns = [
    path('invoices/', views.InvoiceList.as_view()),
    path('invoices/<int:pk>/', views.InvoiceDetail.as_view()),
    path('invoices/<int:pk>/invoicerows/', views.InvoiceRowsByInvoice.as_view()),
    path('invoicerows/<int:pk>/', views.InvoiceRowDetail.as_view()),
    path('customers/', views.CustomerList.as_view()),
    path('customers/<int:pk>/', views.CustomerDetail.as_view()),
    path('providers/', views.ProviderList.as_view()),
    path('providers/<int:pk>/', views.ProviderDetail.as_view()),
]
