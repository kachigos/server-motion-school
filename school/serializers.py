from rest_framework import serializers
from .models import Administration, File, Category, Chronology, Accreditation, Teacher


class CategorySerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = '__all__'
        
        
class ChronologySerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Chronology
        fields = '__all__'
        
        
class AccreditationSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Accreditation
        fields = '__all__'
        
        
class TeacherSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Teacher
        fields = '__all__'

class AdministrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administration
        fields = '__all__'

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'
    