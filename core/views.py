from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class AllObjectsView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        stages = Stages.objects.all()
        staff = Staff.objects.all()
        questions = Questions.objects.all()
        reviewText = ReviewText.objects.all()
        reviewVideo = ReviewVideo.objects.all()

        queryset = list(stages) + list(staff) + list(questions) + list(reviewText) + list(reviewVideo)
        return queryset

    def get(self, request):
        queryset = self.get_queryset()
        serializer = AllObjectssSerializer(queryset, many=True)
        return Response(serializer.data)
