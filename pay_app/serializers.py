from .models import Transaction
from rest_framework.serializers import ModelSerializer


class TransictionSerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'