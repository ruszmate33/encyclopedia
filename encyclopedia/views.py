from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


from . import util


def index(request):
    entries = util.list_entries()
    print(f"entries are {entries}")
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    if request.method == 'POST':
        title = request.POST.get("q")
    entry = util.get_entry(title)
    print(f"entry: {entry}")
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "entry": entry,
    })