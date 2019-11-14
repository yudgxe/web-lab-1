from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from django.shortcuts import render
import os
import shutil

beginPath = os.path.join(os.path.dirname(os.path.realpath(__file__)),'source')

def parseUrl(url):
    buffer = ''
    dirPath = ''
    i = 0
    size = len(url)

    while i < size:
        if url[i] == r'/':
            dirPath = os.path.join(dirPath,buffer)
            buffer = ''
        else:
            buffer += url[i]

        if(i == size - 1 and buffer != ''):
            dirPath = os.path.join(dirPath,buffer)

        i += 1
    return os.path.join(beginPath,dirPath)

@api_view(['GET'])
def index(request):
    if not os.path.exists(beginPath):
        os.mkdir(beginPath)

    dir = parseUrl(request.path_info[1:])
    if(os.path.exists(dir)):
        return Response(os.listdir(dir))
    else:
        return Response("dir not found")

@api_view(['GET'])
def create(request):
    dirname = request.query_params.get('dirname')
    if dirname is None:
        return index(request._request)
    elif dirname == 'upload' or r'upload/':
        return Response("Change a name of dir")
    elif dirname != '':
        path = parseUrl(request.path_info[1:-7])
        pathToDir = os.path.join(path,dirname)
        if not os.path.exists(pathToDir):
            try:
                os.mkdir(pathToDir)
                return Response("Directory created")
            except FileNotFoundError:
                return Response("dir not found")
        else:
            return Response("Directory already exists")
    else:
        return Response("Dirname cannot be equal to NULL")

@api_view(["GET"])
def delete(request):
    dirname = request.query_params.get('dirname')
    if dirname is None:
        return index(request._request)
    elif dirname != '':
        path = parseUrl(request.path_info[1:-7])
        pathToDir = os.path.join(path,dirname)
        if os.path.exists(pathToDir):
            shutil.rmtree(pathToDir)
            return Response("Directory deleted")
        else:
            return Response("Directory not find")
    else:
        return Response("Dirname cannot be equal to NULL")

@api_view(["GET"])
def download(request):
    filename = request.query_params.get('filename')
    if filename is None:
        return index(request._request)
    else:
        path = parseUrl(request.path_info[1:-9])

        print(filename[len(filename) - 1])
        if filename[len(filename) - 1] == r"/":
            pathToFile = os.path.join(path,filename[0:-1])
            file = open(pathToFile,"r")
            response = HttpResponse(file,content_type='application/msword')
            response['Content-Disposition'] = 'attachment; filename=' + filename[0:-1]
        else:
            pathToFile = os.path.join(path,filename)
            file = open(pathToFile,"r")
            response = HttpResponse(file,content_type='application/msword')
            response['Content-Disposition'] = 'attachment; filename=' + filename

        return response

@api_view(['GET','POST'])
def upload(request):
    if request.method == 'POST':
        save_path = os.path.join(parseUrl(request.path_info[1:-7]),request.FILES['document'].name)
        with open(save_path, 'wb+') as destination:
            for chunk in request.FILES['document'].chunks():
                destination.write(chunk)
        return Response('File upload')

    return render(request,'upload.html')
