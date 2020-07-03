from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def analyze(request):
    djtext = request.GET.get('text', 'default')

    # Check checkbox values
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')
    analyzed = ""
    # Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        # analyzed = ""
        if(analyzed!=""):
            djtext=analyzed
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        # params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)

    if (fullcaps == "on"):
        # analyzed = ""
        if(analyzed!=""):
            djtext = analyzed
        am=""
        for char in djtext:
            am = am + char.upper()
        analyzed=am

        # params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        # Analyze the text
        # return render(request, 'analyze.html', params)

    if (extraspaceremover == "on"):
        # analyzed = ""
        djtext = analyzed
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        # params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        # return render(request, 'analyze.html', params)

    if (newlineremover == "on"):
        # analyzed = ""
        djtext = analyzed
        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char

        # params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        # return render(request, 'analyze.html', params)
    if analyzed == "":
        return HttpResponse("Error")

    else:
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)



