from django.http import HttpResponse
from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
    now = datetime.datetime.now()
    html = '<html><body bgcolor="#FFCCE1"><h1><center>This is a Trail Website for checking deployment process Only.</center><br><br><center>It is now %s.</center></h1></body></html>' % now
    
    return HttpResponse(html)





    