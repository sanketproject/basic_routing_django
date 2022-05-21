from urllib import request
from django.http import HttpResponse
from django.shortcuts import render

def index(req):
    params = {'name':'sanket','place':'earth'}
    return render(req,'index.html',params)
   # return HttpResponse('hi </br> <a href = "http://127.0.0.1:8000/about">about' )
   
def about(req):
    dtext = req.GET.get('atext','default')
    print(dtext)
    return HttpResponse('about')


def removepun(req):
    checkpun = req.GET.get('analyzetext','of')
    check_cap = req.GET.get('capatalize','of')
    dtext = req.GET.get('atext','of')
    firstcap = req.GET.get('firstcap','of')
    print(dtext)
    final_text = ""
    if(checkpun =="on"):
         punclist = ''' ":;'"/.#@$%^&*! '''
         final_text = ""
         for words in dtext:
            if words not in punclist:
             final_text = final_text+ words
         return render(req,'removepun.html',{'text':final_text})
     
    elif(check_cap == 'on'):
         for words in dtext:
            final_text = final_text+ words.upper()
         return render(req,'removepun.html',{'text':final_text})
     
    elif(firstcap == 'on'):
         a = dtext[:1].upper()
         return render(req,'removepun.html',{'text':a})
    else:
        return HttpResponse("check box was not clicked")
   

def capfirst(req):
    return HttpResponse('capfirst')

def spaceremove(req):
    return HttpResponse('spaceremove')
def charcount(req):
    return HttpResponse('charcount')