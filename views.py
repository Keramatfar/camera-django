from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from corona.analyzer import main
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.files import File
from django.core.files.base import ContentFile
from django.core.files.temp import NamedTemporaryFile
from urllib.request import urlopen
from django.core.files.storage import default_storage


def camera(request):
    if request.method == 'POST':
        image_path = request.POST["src"]
        image = NamedTemporaryFile()
        urlopen(image_path).read()
        image.write(urlopen(image_path).read())
        image.flush()
        image = File(image)
        name = str(image.name).split('\\')[-1]
        name += '.jpg'  # store image in jpeg format
        image.name = name
        with open('image.txt', 'w+') as file:
            file.write(str(name))
        default_storage.save('C:/Users/admin/Desktop/corona_project/media/a.jpg', ContentFile(urlopen(image_path).read()))
        return HttpResponse('Done!')
    return render(request, 'corona/moz.html')
