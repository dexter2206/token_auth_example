from rest_framework.views import APIView


class HelloView(APIView):
    def get(self, request):
        content = {"message": "Hello World"}
