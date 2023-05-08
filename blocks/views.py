from rest_framework import viewsets, permissions
from rest_framework.decorators import permission_classes

from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class AllBlocksView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        header = HeaderBlock.objects.all()
        main = MainBlock.objects.all()
        about = AboutBlock.objects.all()
        production = ProductionBlock.objects.all()
        services = ServicesBlock.objects.all()
        projects = ProjectsBlock.objects.all()
        stages = StagesBlock.objects.all()
        team = TeamBlock.objects.all()
        questions = QuestionsBlock.objects.all()
        reviews = ReviewsBlock.objects.all()
        contacts = ContactsBlock.objects.all()
        footer = FooterBlock.objects.all()

        queryset = list(header) + list(main) + list(about) + list(production) + list(services) + list(projects) + list(stages) + list(team) + list(questions) + list(reviews) + list(contacts) + list(footer)
        return queryset

    def get(self, request):
        queryset = self.get_queryset()
        serializer = AllBlocksSerializer(queryset, many=True)
        return Response(serializer.data)


@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
class HeaderBlockViewSet(viewsets.ModelViewSet):
    """
    Api endpoint that returns information about Header
    """
    serializer_class = HeaderBlockSerializer
    queryset = HeaderBlock.objects.all()
#
#
# @permission_classes((permissions.IsAuthenticatedOrReadOnly,))
# class MainBlockViewSet(viewsets.ModelViewSet):
#     """
#     Api endpoint that returns information about
#     """
#     serializer_class = MainBlockSerializer
#     queryset = MainBlock.objects.all()
#
#
# @permission_classes((permissions.IsAuthenticatedOrReadOnly,))
# class AboutBlockViewSet(viewsets.ModelViewSet):
#     """
#     Api endpoint that returns information about
#     """
#     serializer_class = AboutBlockSerializer
#     queryset = AboutBlock.objects.all()
#
#
# @permission_classes((permissions.IsAuthenticatedOrReadOnly,))
# class ProductionBlockViewSet(viewsets.ModelViewSet):
#     """
#     Api endpoint that returns information about
#     """
#     serializer_class = ProductionBlockSerializer
#     queryset = ProductionBlock.objects.all()
#
#
# @permission_classes((permissions.IsAuthenticatedOrReadOnly,))
# class ServicesBlockViewSet(viewsets.ModelViewSet):
#     """
#     Api endpoint that returns information about
#     """
#     serializer_class = ServicesBlockSerializer
#     queryset = ServicesBlock.objects.all()
#
#
# @permission_classes((permissions.IsAuthenticatedOrReadOnly,))
# class ProjectsBlockViewSet(viewsets.ModelViewSet):
#     """
#     Api endpoint that returns information about
#     """
#     serializer_class = ProjectsBlockSerializer
#     queryset = ProjectsBlock.objects.all()
#
#
# @permission_classes((permissions.IsAuthenticatedOrReadOnly,))
# class StagesBlockViewSet(viewsets.ModelViewSet):
#     """
#     Api endpoint that returns information about
#     """
#     serializer_class = StagesBlockSerializer
#     queryset = StagesBlock.objects.all()
#
#
# @permission_classes((permissions.IsAuthenticatedOrReadOnly,))
# class TeamBlockViewSet(viewsets.ModelViewSet):
#     """
#     Api endpoint that returns information about
#     """
#     serializer_class = TeamBlockSerializer
#     queryset = TeamBlock.objects.all()
#
#
# @permission_classes((permissions.IsAuthenticatedOrReadOnly,))
# class QuestionsBlockViewSet(viewsets.ModelViewSet):
#     """
#     Api endpoint that returns information about
#     """
#     serializer_class = QuestionsBlockSerializer
#     queryset = QuestionsBlock.objects.all()
#
#
# @permission_classes((permissions.IsAuthenticatedOrReadOnly,))
# class ReviewsBlockViewSet(viewsets.ModelViewSet):
#     """
#     Api endpoint that returns information about
#     """
#     serializer_class = ReviewsBlockSerializer
#     queryset = ReviewsBlock.objects.all()
#
#
# @permission_classes((permissions.IsAuthenticatedOrReadOnly,))
# class ContactsBlockViewSet(viewsets.ModelViewSet):
#     """
#     Api endpoint that returns information about
#     """
#     serializer_class = ContactsBlockSerializer
#     queryset = ContactsBlock.objects.all()
#
#
# @permission_classes((permissions.IsAuthenticatedOrReadOnly,))
# class FooterBlockViewSet(viewsets.ModelViewSet):
#     """
#     Api endpoint that returns information about
#     """
#     serializer_class = FooterBlockSerializer
#     queryset = FooterBlock.objects.all()
