from django.urls import path

from accounting.views.views import AccountListCreateView, AccountDetailView, BookingDetailView, BookingListCreateView

urlpatterns = [
    path('account/', AccountListCreateView.as_view()),
    path('account/<int:id>', AccountDetailView.as_view()),
    path('booking/', BookingListCreateView.as_view()),
    path('booking/<int:id>', BookingDetailView.as_view())
]
