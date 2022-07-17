from django.shortcuts import render
from django.http import HttpResponse
import datetime
import os,time
from django.core.files.storage import FileSystemStorage
from .models import Document
import ezdxf
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def home(request):
    
    if request.method == 'POST':
        filenames=[]
        filelayers=[]
        lst=[]
        filelist=request.FILES.getlist('documentttt[]')
        print(len(filelist))
        for i in filelist:
            obj = Document(docfile=i)
            print(obj)
            obj.save()
        
            print(i,'filenameeeeeeee')
            mm='media/'+str(i)
            dwg = ezdxf.readfile(mm)
            # print(dwg.layers)
            
            filenames.append(i)
            for layer in dwg.layers:
                lst.append(layer.dxf.name)
            print(type(lst),"lstlstlstlstlstlstlstlst")
            filelayers.append(lst)
            print(filelayers,'ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd')
            
        finallist=zip(filenames,filelayers)   
        # context={"finallist":finallist,}      
        return render(request, 'filedetails.html',{'finallists':finallist})
    return render(request, 'index.html')

def fileread(request):
    pass
   
   
    