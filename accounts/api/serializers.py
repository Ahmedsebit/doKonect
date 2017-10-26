from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

from rest_framework import serializers

User = get_user_model()

class UserDisplaySerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    class Meta:
        model = User

        fields = [
            'first_name',
            'last_name',
        ]

    def get_referal_count(self, obj):
        return 0

    def get_url(self, obj):
        return reverse_lazy("profiles:detail", kwargs={"username":obj.username})
