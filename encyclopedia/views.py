from django.shortcuts import render
from django.http import HttpResponse, HttpResponseServerError
from django import forms
import markdown2
import random as rand  #Had to change the name because it collided with my own function

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
    return render(request, "encyclopedia/error.html", {
        "empty_string": True
    })

def entry(request, input):
    if not util.get_entry(input):
        return render(request, "encyclopedia/error.html", {
            "title": input,
            "entry_notfound": True
        })
    else:
        return render(request, "encyclopedia/entry.html", {
        "output": md_to_html(util.get_entry(input)),    
        "title": input
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
            possible_entries= [entry for entry in util.list_entries() if data.upper() in entry.upper()]
            if possible_entries:
                return render(request, "encyclopedia/index.html", {
                    "entries": possible_entries,
                    "search_check": True
                })
            else:
                return render(request, "encyclopedia/error.html", {
                    "title": data,
                    "entry_notfound": True
                })
           
def NewEntry(request):
    return render(request, "encyclopedia/new.html")

def SaveEntry(request):
    if request.method == "POST":
        NewTitle = request.POST["NewTitle"]
        NewContent = request.POST["NewContent"]
        if request.POST["edit_check"]:
            util.save_entry(NewTitle, NewContent)
            return render(request, "encyclopedia/entry.html", {       # If we are editing, we let the util function replace the exiting one
                "output": md_to_html(NewContent),
                "title": NewTitle
            })
        else:                                                     # If we are not editing:     
            if util.get_entry(NewTitle):                                        # We check if the entry already exists, and if it does
                return render(request, "encyclopedia/error.html", {
                    "title": NewTitle,                                          # It renders an error page, alongside the duplicate key word to know which
                    "duplicate": True                                           # error to load
                })  
            else:                                                               # If it does not exist:
                util.save_entry(NewTitle, NewContent)                               # We save the file normally
                return render(request, "encyclopedia/entry.html", {
                "output": md_to_html(NewContent),
                "title": NewTitle
                })

def edit(request):
    if request.method == "POST":
        title = request.POST["title"]
        return render(request, "encyclopedia/new.html", {
            "title": title,
            "content": util.get_entry(title),
            "edit_check": True
        })

def random(request):
    random_choice = rand.choice(util.list_entries())
    return render(request, "encyclopedia/entry.html", {
        "output": md_to_html(util.get_entry(random_choice)),
        "title": random_choice
    })
#any(data in entry for data in util.list_entries())

#for entry in util.list_entries():                                 
#if data in entry:                                  
#------
    