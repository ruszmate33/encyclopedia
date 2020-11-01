from encyclopedia.util import list_entries
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

def entry(request, title=None):
    entry = util.get_entry(title)
    print(f"entry: {entry}")
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "entry": entry,
    })


def search(request):
    if request.method == 'POST':
        query = request.POST.get('q', None)
        entries = list_entries()
        results = []
        for entry in entries:
            if not entry.lower().find(query.lower()) == -1:
                results.append(entry)
    
        return render(request, "encyclopedia/search.html", {
                "query":query,
                "results": results,
    })