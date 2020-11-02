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


def entry(request, title):
    entry = util.get_entry(title)
    if entry == None:
        title = f"Not found: {title}"
    
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "entry": entry,
    })


def search(request):
    if request.method == 'POST':
        query = request.POST.get('q', None)
        entries = list_entries()
        results = []
        for title in entries:
            # full match
            if title.lower() == query.lower():
                return HttpResponseRedirect(reverse("entry", kwargs={"title":title}))
    
            # partial match
            if not title.lower().find(query.lower()) == -1:
                results.append(title)
    
        return render(request, "encyclopedia/search.html", {
                "query":query,
                "results": results,
    })