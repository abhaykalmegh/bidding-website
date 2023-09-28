from django.urls import path
from .views import PaintingView, BidCreateView, BidApprovalView

urlpatterns = [
    path('paintings/', PaintingView.as_view(), name='painting-list-create'),
    path('paintings/<int:painting_id>/bid/', BidCreateView.as_view(), name='bid-create'),
    path('bids/<int:bid_id>/approve/', BidApprovalView.as_view(), name='bid-approve'),
]
