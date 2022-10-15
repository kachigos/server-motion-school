from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from .serializers import AdministrationSerializer, CategorySerializers, ChronologySerializers, AccreditationSerializers, FileSerializer, TeacherSerializers
from .models import Administration, File, Category, Chronology, Accreditation, Teacher


class CategoryCreateListView(generics.ListCreateAPIView):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()
    
    
class CategoryDeleteView(generics.DestroyAPIView):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()
    

class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

   
class ChronologyCreateListView(generics.ListCreateAPIView):
    serializer_class = ChronologySerializers
    queryset = Chronology.objects.all()
    
    
class ChronologyDeleteView(generics.DestroyAPIView):
    serializer_class = ChronologySerializers
    queryset = Chronology.objects.all()
    
    
class AccreditationCreateListView(generics.ListCreateAPIView):
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        
        return self.create(request, *args, **kwargs)
    serializer_class = AccreditationSerializers
    queryset = Accreditation.objects.all()
    
    
class AccreditationDeleteView(generics.DestroyAPIView):
    serializer_class = AccreditationSerializers
    queryset = Accreditation.objects.all()
    

class AccreditationDetailView(generics.RetrieveAPIView):
    serializer_class = AccreditationSerializers
    queryset = Accreditation.objects.all()
    
  
class TeacherCreateListView(generics.ListCreateAPIView):
    serializer_class = TeacherSerializers
    queryset = Teacher.objects.all()
    
    
class TeacherDeleteView(generics.DestroyAPIView):
    serializer_class = TeacherSerializers
    queryset = Teacher.objects.all()


class AdministrationAPIViewSet(ModelViewSet):
    queryset = Administration.objects.all()
    serializer_class = AdministrationSerializer

class FileAPIViewSet(ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer