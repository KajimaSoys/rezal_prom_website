from .serializers import *
from rest_framework import viewsets, permissions
from rest_framework.decorators import permission_classes


@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
class HeaderBlockViewSet(viewsets.ModelViewSet):
    """
    Api endpoint that returns information about
    """
    serializer_class = HeaderBlockSerializer
    queryset = HeaderBlock.objects.all()


@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
class MainBlockViewSet(viewsets.ModelViewSet):
    """
    Api endpoint that returns information about
    """
    serializer_class = MainBlockSerializer
    queryset = MainBlock.objects.all()


@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
class AboutBlockViewSet(viewsets.ModelViewSet):
    """
    Api endpoint that returns information about
    """
    serializer_class = AboutBlockSerializer
    queryset = AboutBlock.objects.all()


@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
class WarmingBlockViewSet(viewsets.ModelViewSet):
    """
    Api endpoint that returns information about
    """
    serializer_class = WarmingBlockSerializer
    queryset = WarmingBlock.objects.all()


@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
class ServicesBlockViewSet(viewsets.ModelViewSet):
    """
    Api endpoint that returns information about
    """
    serializer_class = ServicesBlockSerializer
    queryset = ServicesBlock.objects.all()


@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
class ProjectsBlockViewSet(viewsets.ModelViewSet):
    """
    Api endpoint that returns information about
    """
    serializer_class = ProjectsBlockSerializer
    queryset = ProjectsBlock.objects.all()


@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
class StagesBlockViewSet(viewsets.ModelViewSet):
    """
    Api endpoint that returns information about
    """
    serializer_class = StagesBlockSerializer
    queryset = StagesBlock.objects.all()


@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
class TeamBlockViewSet(viewsets.ModelViewSet):
    """
    Api endpoint that returns information about
    """
    serializer_class = TeamBlockSerializer
    queryset = TeamBlock.objects.all()


@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
class QuestionsBlockViewSet(viewsets.ModelViewSet):
    """
    Api endpoint that returns information about
    """
    serializer_class = QuestionsBlockSerializer
    queryset = QuestionsBlock.objects.all()


@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
class ReviewsBlockViewSet(viewsets.ModelViewSet):
    """
    Api endpoint that returns information about
    """
    serializer_class = ReviewsBlockSerializer
    queryset = ReviewsBlock.objects.all()


@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
class ContactsBlockViewSet(viewsets.ModelViewSet):
    """
    Api endpoint that returns information about
    """
    serializer_class = ContactsBlockSerializer
    queryset = ContactsBlock.objects.all()


@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
class FooterBlockViewSet(viewsets.ModelViewSet):
    """
    Api endpoint that returns information about
    """
    serializer_class = FooterBlockSerializer
    queryset = FooterBlock.objects.all()
