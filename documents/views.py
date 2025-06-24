from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from .models import Document
from .serializers import DocumentSerializer
from .utils.xml_parser import parse_xml

class UploadDocument(APIView):
    parser_classes = [FileUploadParser]

    def post(self, request):
        file = request.FILES.get('file')
        parsed = parse_xml(file.read())
        doc = Document.objects.create(title=file.name, content=parsed)
        return Response(DocumentSerializer(doc).data)
