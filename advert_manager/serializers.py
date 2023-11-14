from rest_framework import serializers

from .models import Advert, Comments


# class CommentSerializer(serializers.ModelSerializer):
#     id = serializers.ReadOnlyField()
#
#     class Meta:
#         model = Comments
#         fields = '__all__'
#
#
# class AdvertSerializer(serializers.ModelSerializer):
#     comments = CommentSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = Advert
#         fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Comments
        fields = '__all__'


class AdvertSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    # comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Advert
        # fields = '__all__'
        fields = ['title', "pub_date", 'text', 'comments']