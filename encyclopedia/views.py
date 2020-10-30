from django.shortcuts import render

from . import util


def index(request):
    entries = util.list_entries()
    print(f"entries are {entries}")
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })