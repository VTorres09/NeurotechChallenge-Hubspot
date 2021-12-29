from django.db import models
from rest_framework import serializers


class Message(models.Model):
    subject = models.CharField(max_length=200)
    body = models.TextField()


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('url', 'subject', 'body', 'pk')


class Contact(models.Model):
    firstname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    birthday = models.DateTimeField()
    weight = models.FloatField()

class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'properties', 'created_at')
