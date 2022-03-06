# I have created this file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "home.html")
def contact(request):
    return render(request, "contact.html")
def analyze(request):
    text = request.POST.get('text', 'off') #Grabbing the text

    # checking the checkbox
    removepunc = request.POST.get('removepunctuation', 'off')  
    uppercase = request.POST.get('uppercase', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charactercount = request.POST.get('charactercount', 'off')
    # print(removepunc, remove)
    if removepunc =="on":

        analyzer = ""
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        for char in text:
            if char not in punctuations:
                analyzer = analyzer + char
        params = {"Purpose" : "Punctuations removed", "analyzed_text" : analyzer}
        text = analyzer
        
    if uppercase == "on":
        analyzer =""
        for char in text:
            analyzer = analyzer + char.upper()
        params = {"Purpose" : "Uppercase", "analyzed_text" : analyzer}
        text = analyzer
        
    if newlineremover == "on":
        analyzer =""
        for char in text:
            if char != "\n"and char != "\r":

                analyzer = analyzer + char
        params = {"Purpose" : "New line removed", "analyzed_text" : analyzer}
        text = analyzer
        
    if extraspaceremover =="on":
        analyzer =""
        for index, char in enumerate(text):
            if not(text[index] == " " and text[index+1] == " "):
                analyzer = analyzer+char
        params = {"Purpose" : "Extra spaces removed", "analyzed_text" : analyzer}
        text = analyzer
        
    if charactercount == "on":
        analyzer= ""
        for char in text:
                analyzer = analyzer+char
        count = len(analyzer)
        params = {"Purpose" : "Extra spaces removed", "analyzed_text" : count}
        text = analyzer
        
    if(charactercount != "on" and extraspaceremover != "on" and removepunc != "on" and uppercase != "on" and newlineremover != "on" ):
        return HttpResponse("Error")
    
    return render(request, "analyze.html", params)
        

   
    