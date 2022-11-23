from rest_framework import serializers
from mailgainer_app.models import Contact


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact





