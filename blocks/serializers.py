from rest_framework import serializers
from .models import *

class HeaderBlockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HeaderBlock
        fields = ('', )


class MainBlockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MainBlock
        fields = ('', )


class AboutBlockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AboutBlock
        fields = ('', )


class WarmingBlockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WarmingBlock
        fields = ('', )


class ServicesBlockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ServicesBlock
        fields = ('', )


class ProjectsBlockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProjectsBlock
        fields = ('', )


class StagesBlockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StagesBlock
        fields = ('', )


class TeamBlockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TeamBlock
        fields = ('', )


class QuestionsBlockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QuestionsBlock
        fields = ('', )


class ReviewsBlockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ReviewsBlock
        fields = ('', )


class ContactsBlockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ContactsBlock
        fields = ('', )


class FooterBlockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FooterBlock
        fields = ('', )


