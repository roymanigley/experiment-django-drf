from accounting.services.services import AccountService, BookingService
from office_suite.abstracts.views import AbstractListCreateView, AbstractDetailView


class AccountListCreateView(AbstractListCreateView):
    service_class = AccountService


class AccountDetailView(AbstractDetailView):
    service_class = AccountService


class BookingListCreateView(AbstractListCreateView):
    service_class = BookingService


class BookingDetailView(AbstractDetailView):
    service_class = BookingService
