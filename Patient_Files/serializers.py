from rest_framework import serializers
from .models import *


class Patiant_File_NOSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patiant_File_NO
        fields = "__all__"