from django.http import request
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from markdown2 import Markdown
from random import randint

from . import util
from .forms import NewPageForm

markdowner = Markdown()

def createNewPage(request):
    if request.method == "POST":
        title = request.POST.get('title', None)
        content = request.POST.get('entry', None)
        print(f"title: {title}")
        print(f"markdown: {content}")
        if util.entry_exists(title):
            return render(request, "encyclopedia/createNewPage.html", {
                    "message": f"Error, page {title} already exist. Try to edit it!",
                    })
        util.save_entry(title, content)
        
        return HttpResponseRedirect(reverse("entry", kwargs={"title":title}))
    else:
        form = NewPageForm()
        return render(request, "encyclopedia/createNewPage.html", {
                    "form":form,
                    })

def random(request):
    entries = util.list_entries()
    title = entries[randint(0, len(entries)-1)]

    return HttpResponseRedirect(reverse("entry", kwargs={"title":title}))


def index(request):
    entries = util.list_entries()
    print(f"entries are {entries}")
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title):
    entry = util.get_entry(title)
    if entry:
        entry = markdowner.convert(entry)
    else:
        title = f"Not found: {title}"

    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "entry": entry,
    })


def search(request):
    if request.method == 'POST':
        query = request.POST.get('q', None)
        entries = util.list_entries()
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