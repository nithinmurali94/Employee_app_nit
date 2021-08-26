from django.contrib import admin

from .models import Employee
from django.urls import path
from django.shortcuts import render
from django import forms
from django.contrib import messages
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
import pandas as pd 

# Register your models here.

class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_code','employee_name','department','age','experience')

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls

    def upload_csv(self, request):

        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]

            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'The wrong file type was uploaded')
                return HttpResponseRedirect(request.path_info)
        
            #===> if any column mismatch occurs
            try:
                df = pd.read_csv(csv_file,header=None)
            except Exception as ex:
                messages.warning(request, str(ex))
                return HttpResponseRedirect(request.path_info)

            total_rows = len(df.axes[0]) #===> rowcount
            total_cols = len(df.axes[1])  #===>column count
        
            if total_rows > 20: 
                messages.warning(request, 'The csv file contains more than 20 rows')
                return HttpResponseRedirect(request.path_info)
            if total_cols > 5 or total_cols < 5: 
                messages.warning(request, 'There must be 5 columns in the csv file')
                return HttpResponseRedirect(request.path_info)
            objs = [
                    Employee(
                        employee_code=e[0],
                        employee_name=e[1],
                        department=e[2],
                        age=e[3],
                        experience=e[4])
                    for i,e in df.iterrows()]
            #insert as bulk
            msg = Employee.objects.bulk_create(objs)

            url = reverse('admin:index')
            return HttpResponseRedirect(url)

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)

admin.site.register(Employee,EmployeeAdmin)
