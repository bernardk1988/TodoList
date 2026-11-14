from rest_framework import serializers
from .models import Todo1
class Todo1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Todo1
        fields = ['id','task','datetime','status']
        read_only_fields =['id']