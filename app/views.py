import csv

from django.core.files.storage.filesystem import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render
from . import extractInfo
from .forms import UploadFileForm

# Create your views here.

def uploadData(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            data = request.FILES['file']
            fs = FileSystemStorage()
            filename = fs.save(data.name, data)
            extracted_data = extractInfo.check_file_type(filename)

            # Convert the extracted text to a CSV file
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="extracted_data.csv'
            write = csv.writer(response)
            for line in extracted_data.split('\n'):
                write.writerow([line])
            return response
    else:
        form = UploadFileForm()

    return render(request, 'uploadData.html', {'form': form})