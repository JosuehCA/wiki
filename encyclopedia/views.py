from django.shortcuts import render
from django.http import HttpResponse, HttpResponseServerError
from django import forms
import markdown2

from . import util
import encyclopedia

#  class Search_Encyclopedia(forms.Form):
#      query = forms.CharField()

def md_to_html(mdcontent):
    return markdown2.markdown(mdcontent)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def error(request):
    return render(request, "encyclopedia/error.html")

def entry(request, input):
    if not util.get_entry(input):
        return render(request, "encyclopedia/error.html", {
            "title": input
        })
    else:
        return render(request, "encyclopedia/entry.html", {
        "output": md_to_html(util.get_entry(input)),
        "title": input.upper()
    })
    
def search(request):
    if request.method == "POST":
        data = request.POST["entry_asked"]
        if util.get_entry(data):
            return render(request, "encyclopedia/entry.html", {
                "output": md_to_html(util.get_entry(data)),
                "title": data.upper()
            })
        else:
            possible_entries= [entry for entry in util.list_entries() if data in entry]
            if possible_entries:
                return render(request, "encyclopedia/index.html", {
                    "entries": possible_entries
                })
            else:
                return render(request, "encyclopedia/error.html", {
                    "title": data
                })
           



        #any(data in entry for data in util.list_entries())

        #for entry in util.list_entries():                                 
            #if data in entry:                                  
                #------
    