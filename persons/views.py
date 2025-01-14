from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Person
from .serializers import PersonSerializer
from django.shortcuts import get_object_or_404


class PersonListView(APIView):

    def get(self, request):
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            person = serializer.save()
            return Response(status=status.HTTP_201_CREATED, headers={
                'Location': f'/api/v1/persons/{person.id}'
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PersonDetailView(APIView):
    def get(self, request, person_id):
        person = get_object_or_404(Person, id=person_id)
        serializer = PersonSerializer(person)
        return Response(serializer.data)

    def patch(self, request, person_id):
        person = get_object_or_404(Person, id=person_id)
        serializer = PersonSerializer(person, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, person_id):
        person = get_object_or_404(Person, id=person_id)
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
