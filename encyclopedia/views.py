from django.shortcuts import render
from django.http import HttpResponse, HttpResponseServerError
import markdown2

from . import util

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
        "output": markdown2.markdown(util.get_entry(input)),
        "title": input.upper()
    })
