from typing import Type

from django.db import models
from django.db.models import QuerySet
from django.http import HttpRequest
from rest_framework.serializers import Serializer

from accounting.models import Account, Booking
from accounting.services.serializers.serializers import AccountSerializer, BookingSerializer
from office_suite.abstracts.services import Service


class AccountService(Service):

    @staticmethod
    def get_serializer_class(request: HttpRequest = None) -> Type[Serializer]:
        return AccountSerializer

    @staticmethod
    def get_queryset(request: HttpRequest = None) -> QuerySet:
        return Account.objects.all()

    @staticmethod
    def get_model_class(request: HttpRequest = None) -> Type[models.Model]:
        return Account


class BookingService(Service):

    @staticmethod
    def get_serializer_class(request: HttpRequest = None) -> Type[Serializer]:
        return BookingSerializer

    @staticmethod
    def get_queryset(request: HttpRequest = None) -> QuerySet:
        return Booking.objects.all()

    @staticmethod
    def get_model_class(request: HttpRequest = None) -> Type[models.Model]:
        return Booking
