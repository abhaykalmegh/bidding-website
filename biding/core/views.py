from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Painting, Bid
from .serializers import PaintingSerializer, BidSerializer


class PaintingView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        paintings = Painting.objects.all()
        serializer = PaintingSerializer(paintings, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PaintingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(painter=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BidCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, painting_id):
        painting = get_object_or_404(Painting, pk=painting_id)
        serializer = BidSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(buyer=request.user, painting=painting)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BidApprovalView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, bid_id):
        bid = get_object_or_404(Bid, pk=bid_id)
        if bid.painting.painter != request.user:
            return Response("You don't have permission to approve this bid.", status=status.HTTP_403_FORBIDDEN)
        bid.approved = True
        bid.save()
        return Response("Bid approved successfully.", status=status.HTTP_200_OK)
