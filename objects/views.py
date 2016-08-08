from django.shortcuts import render

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from objects.models import Object
from objects.serializers import ObjectSerializer

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def object_list(request):
    """
    List all code objects, or create a new object.
    """
    if request.method == 'GET':
        objects = Object.objects.all()
        serializer = ObjectSerializer(objects, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ObjectSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def object_detail(request, pk):
    """
    Retrieve, update or delete a code object.
    """
    try:
        object = Object.objects.get(pk=pk)
    except Object.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ObjectSerializer(object)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ObjectSerializer(object, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        object.delete()
        return HttpResponse(status=204)
