from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from notes.models import Note
from rest_api.serializers import NoteSerializer


class HelloView(APIView):
    def get(self, request):
        content = {"message": "Hello World"}
        return Response(content)


class NotesView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user_notes = Note.objects.filter(owner=request.user)
        return Response(NoteSerializer(user_notes, many=True).data)

    def post(self, request):
        serializer = NoteSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save(owner=request.user)

        return Response(serializer.data)


