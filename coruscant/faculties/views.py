from django.http import HttpResponse
from django.shortcuts import render

from .forms import UploadFileForm


def index(request):
    return render(request, 'faculties/index.html')


def upload_file(request):
    print(request.method)
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # handle_uploaded_file(request.FILES['file'])
            # return HttpResponseRedirect('/success/url/')
            return HttpResponse("good")
    else:
        form = UploadFileForm()
    return render(request, 'faculties/upload.html', {'form': form})