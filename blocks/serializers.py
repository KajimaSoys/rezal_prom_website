from rest_framework import serializers
from .models import *


class AllBlocksSerializer(serializers.Serializer):
    type = serializers.SerializerMethodField()
    data = serializers.SerializerMethodField()

    def get_type(self, obj):
        return obj.__class__.__name__

    def get_data(self, obj):
        if isinstance(obj, HeaderBlock):
            serializer = HeaderBlockSerializer(obj)
        elif isinstance(obj, MainBlock):
            serializer = MainBlockSerializer(obj)
        elif isinstance(obj, AboutBlock):
            serializer = AboutBlockSerializer(obj)
        elif isinstance(obj, ProductionBlock):
            serializer = ProductionBlockSerializer(obj)
        elif isinstance(obj, ServicesBlock):
            serializer = ServicesBlockSerializer(obj)
        elif isinstance(obj, ProjectsBlock):
            serializer = ProjectsBlockSerializer(obj)
        elif isinstance(obj, StagesBlock):
            serializer = StagesBlockSerializer(obj)
        elif isinstance(obj, TeamBlock):
            serializer = TeamBlockSerializer(obj)
        elif isinstance(obj, QuestionsBlock):
            serializer = QuestionsBlockSerializer(obj)
        elif isinstance(obj, ReviewsBlock):
            serializer = ReviewsBlockSerializer(obj)
        elif isinstance(obj, ContactsBlock):
            serializer = ContactsBlockSerializer(obj)
        elif isinstance(obj, FooterBlock):
            serializer = FooterBlockSerializer(obj)
        else:
            raise ValueError('Unexpected object type')
        return serializer.data


class HeaderBlockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HeaderBlock
        fields = (
                     'logo',
                     'number',
                 )


class MainBlockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MainBlock
        fields = (
                    'title',
                    'description',
                    'image',
                 )


class AboutBlockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AboutBlock
        fields = (
                    'title',
                    'description',
                    'title_first',
                    'description_first',
                    'title_second',
                    'description_second',
                    'title_third',
                    'description_third',
                    'title_fourth',
                    'description_fourth',
                    'title_fifth',
                    'description_fifth',
                    'title_sixth',
                    'description_sixth',
                 )


class ProductionBlockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductionBlock
        fields = (
                    'title',
                    'description',
                    'video_preview',
                    'video_link',
                    'image_one',
                    'image_two',
                    'image_three',
                  )


class ServicesBlockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ServicesBlock
        fields = (
                    'title',
                    'title_first',
                    'image_first',
                    'title_second',
                    'image_second',
                    'title_third',
                    'image_third',
                  )


class ProjectsBlockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProjectsBlock
        fields = (
                    'title',
                    'title_first',
                    'image_first',
                    'video_link_first',
                    'title_second',
                    'image_second',
                    'video_link_second',
                    'title_third',
                    'image_third',
                    'video_link_third',
                  )


class StagesBlockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StagesBlock
        fields = (
                    'title',
                    'delivery_title',
                    'delivery_first',
                    'delivery_second',
                  )


class TeamBlockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TeamBlock
        fields = (
                    'title',
                    'description',
                  )


class QuestionsBlockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QuestionsBlock
        fields = (
                    'title',
                  )


class ReviewsBlockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ReviewsBlock
        fields = (
                    'title',
                  )


class ContactsBlockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ContactsBlock
        fields = (
                    'title',
                    'address',
                    'schedule',
                    'number',
                    'vk_link',
                    'inst_link',
                  )


class FooterBlockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FooterBlock
        fields = (
                    'logo',
                    'number',
                  )


