import json
import requests
from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from rest_framework import viewsets
from hubspot.crm.contacts import SimplePublicObjectInput
from hubspot.crm.contacts.exceptions import ApiException
from .models import Message, MessageSerializer, Contact, ContactSerializer
from hubspot.auth.oauth import ApiException
from hubspot import HubSpot
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework import status

API_KEY = '4f742c04-5679-4c10-9207-31a45bba1a7b'
api_client = HubSpot()
api_client = HubSpot(api_key=API_KEY)


# Serve Vue Application
index_view = never_cache(TemplateView.as_view(template_name='index.html'))


class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows messages to be viewed or edited.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class ContactViewSet(viewsets.ModelViewSet):
    
    @csrf_exempt
    @api_view(('GET',))
    @renderer_classes((TemplateHTMLRenderer, JSONRenderer))
    def getContacts(request):
        all_contacts = api_client.crm.contacts.get_all(properties=["firstname", "email", "peso__kg_", "date_of_birth", "phone"])
        serialized_contacts = []
        for contact in all_contacts:
            serialized_contacts.append(contact.to_dict())
        print(serialized_contacts)
        return Response({'data': serialized_contacts},status=status.HTTP_200_OK)
    
    @csrf_exempt
    @api_view(('POST',))
    @renderer_classes((TemplateHTMLRenderer, JSONRenderer))
    def addContact(request):
        name = request.data.get('name', '')
        email = request.data.get('email', '')
        phone = request.data.get('phone', None)
        birthdate = request.data.get('birthdate', None)
        weight = request.data.get('weight', None)

        getUrl= 'https://api.hubapi.com/contacts/v1/contact/email/'+ email +'/profile?hapikey='+ API_KEY
        response = requests.get(url=getUrl)

        if response.status_code == 200:
            responseJson = response.json()
            try:
                data=json.dumps({
                "properties": [
                    {
                    "property": "email",
                    "value": str(email)
                    },
                    {
                    "property": "firstname",
                    "value": str(name)
                    },
                    {
                    "property": "phone",
                    "value": str(phone)
                    },
                    {
                    "property": "date_of_birth",
                    "value": str(birthdate)
                    },
                    {
                    "property": "peso__kg_",
                    "value": str(weight)
                    }
                ]})

                headers = {}
                headers['Content-Type']= 'application/json'
                updateUrl ='https://api.hubapi.com/contacts/v1/contact/vid/'+ str(responseJson["vid"]) +'/profile?hapikey='+ API_KEY
                r = requests.post(data=data, url=updateUrl, headers=headers)
                return Response(status=r.status_code)

            except ApiException as e:
                print("Exception when updating contact: %s\n" % e)
        else:
            try:
                simple_public_object_input = SimplePublicObjectInput(
                properties={
                    "email": email, 
                    "firstname": name, 
                    "peso__kg_": weight, 
                    "date_of_birth": birthdate, 
                    "phone": phone
                    }
                )
                
                api_response = api_client.crm.contacts.basic_api.create(
                    simple_public_object_input=simple_public_object_input
                )

                return Response({'data': api_response.to_dict()},status=status.HTTP_200_OK)

            except ApiException as e:
                print("Exception when creating contact: %s\n" % e)
        

        