import pdb

from django.shortcuts import render
from django.http import JsonResponse
from django.db import transaction
from django.db.models import Sum
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User
from .models import Advert, Comments
from .serializers import AdvertSerializer


class AdvertismentView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        queryset = Advert.objects.all()
        serializer = AdvertSerializer(queryset, many=True)
        print(serializer.data)
        return JsonResponse(serializer.data, safe=False)


class CommentView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            # pdb.set_trace()
            advert_id = request.data.get("advert_id")
            text = request.data.get("text")
            user = request.user
            if not advert_id or not text:
                return Response({"error": "advert_id and text are required"}, status=status.HTTP_400_BAD_REQUEST)

            try:
                my_advert = Advert.objects.get(pk=advert_id)
            except Advert.DoesNotExist:
                return Response({"error": "invalid advert_id"}, status=status.HTTP_400_BAD_REQUEST)

            my_comment = Comments(text=text, user=user, advert = my_advert)
            my_comment.save()
            return JsonResponse({"status": "Record added successfully"})

        except Exception as ex:
            return Response(ex, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        # pdb.set_trace()
        user = request.user
        comment_id = request.data.get("comment_id")

        try:
            comment = Comments.objects.get(pk=comment_id)
        except Comments.DoesNotExist:
            return Response({"error": "invalid comment_id"}, status=status.HTTP_400_BAD_REQUEST)
        if comment.user == user:
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"error": "invalid comment"}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        comment_id = request.data.get("comment_id")
        text = request.data.get("text")
        user = request.user

        try:
            comment = Comments.objects.get(pk=comment_id)
        except Comments.DoesNotExist:
            return Response({"error": "invalid comment_id"}, status=status.HTTP_400_BAD_REQUEST)

        comment.text = text

        if comment.user == user:
            comment.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"error": "invalid comment"}, status=status.HTTP_400_BAD_REQUEST)





