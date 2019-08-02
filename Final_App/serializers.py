from rest_framework import serializers
from .models import doctors


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = doctors
        fields = '__all__'

