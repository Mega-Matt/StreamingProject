from django.shortcuts import render
from django.views import View
# Create your views here.
from django.contrib.auth import get_user

from .models import Channel
from .forms import ChannelCreateForm
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
from django.http import FileResponse
import os
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile


media_dir = "E:/school_project/streaming_website/main/media"


def HomeView(request):
    return render(request, "main/home.html")


def makeDirnameFilename(name, chunk):
    dirname = media_dir + '/' + name
    filename = dirname + '/' + chunk + '.webm'
    return [dirname, filename]


def handle_uploaded_file(dirname, filename, f):
    path = os.path.join(media_dir, dirname)
    if os.path.exists(path):
        default_storage.save(filename, ContentFile(f.read()))
        with open(filename, "wb+") as destination:
             for chunk in f.chunks():
                 destination.write(chunk)
             destination.close()
    else:
        os.mkdir(path)
        default_storage.save(filename, ContentFile(f.read()))
        with open(filename, "wb+") as destination:
             for chunk in f.chunks():
                 destination.write(chunk)
             destination.close()


@csrf_exempt
def PostStream(request):
    name = request.POST.get('name')
    chunk = request.POST.get('chunk')
    file_obj = request.FILES.get('file', None)
    [dirname, filename] = makeDirnameFilename(name, chunk)
    handle_uploaded_file(dirname, filename, file_obj)
    return HttpResponse("OK")


@csrf_exempt
def GetStream(request, name, chunk):
    path = media_dir + '/' + name + '/' + chunk + '.webm'
    return FileResponse(open(path, 'r+b'))


'''
const fs = require('fs')
const bodyParser = require('body-parser')
const express = require('express')
const fileUpload = require('express-fileupload')

const app = express()
app.use(bodyParser.urlencoded())
app.use(bodyParser.json())
app.use(fileUpload({
    useTempFiles: true,
    tempFileDir: '/tmp/'
}))

const hostname = '0.0.0.0'
const port = 3000

    app.get('/download', (req, res) => {
    const query = req.query
    const [dirname, filename] = makeDirnameFilename(query.name, query.chunk)

    fs.promises.readFile(filename)
        .then((file) => {
            res.statusCode = 200
            res.write(file, 'binary')
            res.end()
        }).catch(() => {
        res.statusCode = 204
        res.end()
    })
})'''


# def ChannelDetails(pk, request):
#     channel = Channel.obj.get(id=pk)
#     context = {channel: "channel"}
#     return render(request, "main/channel.html", context)
#
#
# def CreateChannel(CreateView, request):
#     user = get_user(request)
#     if request.method == "POST":
#         # if the user is not logged in the function redirects them to the login page
#         if not request.user.is_authenticated:
#             return redirect(f"{settings.LOGIN_URL}?next={request.path}")
#         else:
#             form = ChannelCreateForm(request == "POST")
#             if form.is_valid():
#                 form.save()
#                 return HttpResponseRedirect("/home /")
#
#     else:
#         form = ChannelCreateForm()
#         return render(request, "main / CreateChannel.html", {"form": form})
#
#
# def Search(search_value, request):
#     channels = Channel.obj.get(name == search_value)
#     context = {channels: "channels"}
#     return render(request, "main/Search.html", context)

# def ScreenGrab(request):
#     return render(request, 'main/screen.html')
#
#
# def CameraView(request):
#     if request.method == "POST":
#         print('yippee, cute code works!')
#     return render(request, 'main/camera.html')