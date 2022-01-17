from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from corona.analyzer import main
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

@csrf_exempt
def save_image(request):
	if request.POST:
		# save it somewhere
		f = open(settings.MEDIA_ROOT + '/webcamimages/someimage.jpg', 'wb')
		f.write(request.raw_post_data)
		f.close()
		# return the URL
		return HttpResponse('site_media/webcamimages/someimage.jpg')
	else:
		return render(request, 'corona/direct.html')

def index(request):
    if request.method == 'POST':
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        file_path = myfile.name
        filename = fs.save(file_path, myfile)
        res = main(file_path)
        if res[0] == 0:
            return HttpResponse(f' {res} You are Healthy!')
        else:
            return HttpResponse(f' {res} You are possible a corona positive one!')
    else:
        return render(request, 'corona/main.html')


# Import these methods
from django.core.files import File
from django.core.files.base import ContentFile
from django.core.files.temp import NamedTemporaryFile
from urllib.request import urlopen
from django.core.files.storage import default_storage


def image_upload(request):
    if request.method == 'POST':
        image_path = request.POST["src"]  # src is the name of input attribute in your html file, this src value is set in javascript code
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
    return render(request, 'corona/moz.html')  # context is like respose data we are sending back to user, that will be rendered with specified 'html file'.

def moz(request):
    return render(request, 'corona/moz.html')