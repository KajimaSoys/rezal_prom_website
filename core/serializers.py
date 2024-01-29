from rest_framework import serializers
from .models import *


class AllObjectssSerializer(serializers.Serializer):
    type = serializers.SerializerMethodField()
    data = serializers.SerializerMethodField()

    def get_type(self, obj):
        return obj.__class__.__name__

    def get_data(self, obj):
        if isinstance(obj, Stages):
            serializer = StagesSerializer(obj)
        elif isinstance(obj, Staff):
            serializer = StaffSerializer(obj)
        elif isinstance(obj, Questions):
            serializer = QuestionsSerializer(obj)
        elif isinstance(obj, ReviewText):
            serializer = ReviewTextSerializer(obj)
        elif isinstance(obj, ReviewVideo):
            serializer = ReviewVideoSerializer(obj)
        else:
            raise ValueError('Unexpected object type')
        return serializer.data


class StagesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stages
        fields = (
            'title',
            'image',
            'order',
        )


class StaffSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Staff
        fields = (
            'name',
            'post',
            'image',
            'order',
        )


class QuestionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Questions
        fields = (
            'question',
            'answer',
            'order',
        )


class ReviewTextSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ReviewText
        fields = (
            'author_name',
            'review_text',
            'author_photo',
            'review_link',
            'order',
        )


class ReviewVideoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ReviewVideo
        fields = (
            'image',
            'video_link',
            'order',
        )
