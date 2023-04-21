# this is created by me
from django.http  import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html') 

def about(request):
    return HttpResponse("Mr.Mo2 about page")

def analyze(request):
    gettext = request.GET.get('text','default')  # get the text asreturn in the the text box as name=text in textarea in index.html
    remove_punc = request.GET.get('removepunc','off') # to check checkbox is clicked or not 
    full_caps = request.GET.get('fullcaps','off')
    newlineremove = request.GET.get('newlineremove','off')
    extraspaceremove = request.GET.get('extraspaceremove','off')
    charcount = request.GET.get('charcount','off')
    print("punc: ",remove_punc)
    print("caps: ",full_caps)
    print("text: ",gettext)
    
    if remove_punc == 'on':
        analyzed=""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in gettext:
            if char not in punctuations:
                analyzed+=char

        params= {'purpose':'Remove the punctuation', 'analyzed_text':analyzed}
        gettext=analyzed
    
    if full_caps == "on":
        analyzed=""
        for char in gettext:
                analyzed+=char.upper()
        
        params= {'purpose':'Capatilize', 'analyzed_text':analyzed}
        gettext=analyzed
    
    if newlineremove == "on":
        analyzed=""
        for char in gettext:
                if char != "\n" and char != "\r":
                    analyzed+=char
        
        params= {'purpose':'Remove the new line', 'analyzed_text':analyzed}
        gettext=analyzed

    if extraspaceremove == "on":
        analyzed=""
        for index,char in enumerate(gettext):      
                if not(gettext[index] == " " and gettext[index+1] == " "):
                    analyzed+=char
        
        params= {'purpose':'Remove extra space', 'analyzed_text':analyzed}
        gettext=analyzed
    
    if charcount == "on":
        analyzed=""
        x=gettext.split()
        print(x)
        analyzed=gettext
        params= {'purpose':'Count the number of characters', 'analyzed_text':f'{analyzed} \nThe number of character is {len(x)}'}
        gettext=analyzed
        
    if remove_punc != 'on' and full_caps != "on" and newlineremove != "on" and extraspaceremove != "on" and charcount != "on":
        return HttpResponse("<h2>Error !!!!</h2><br>Forgot to click on check box <br><a href='/'>Back")
    
    return render(request, 'analyze.html', params)

#---------------------------
# for my future improvent, to be continue.... 

# def capitalize(request):
#     return HttpResponse("capatilize first<a href='/'>Back")

# def removepunc(request):
#     gettext = request.GET.get('text','default')  # get the text
#     print(gettext)
#     return HttpResponse("Remove Punc <a href='/'>Back")

# def newlineremove(request):
#     return HttpResponse("Remove new line <a href='/'>Back")

# def spaceremove(request):
#     return HttpResponse("remove space <a href='/'>Back")

# def charcount(request):
#     return HttpResponse("count character<a href='/'>Back")
#-----------------------------
