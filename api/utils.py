from django.utils import timezone


def generate_document_nr(invoice_nr: int) -> str:
    prefix = invoice_nr + 1
    month_year = timezone.now().strftime('%m-%Y')
    return f'{prefix}-{month_year}'


def calculate_due_date(days: int = 21):
    return (timezone.now() + timezone.timedelta(days=days)).date()
