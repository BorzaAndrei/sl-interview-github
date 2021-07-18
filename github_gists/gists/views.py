from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
import requests

# Create your views here.
def index(request):
    return render(request, "gists/base.html")


def search_username(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        r = requests.get(f"https://api.github.com/users/{username}/gists", headers={"Accept": "application/vnd.github.v3+json"})
        # TODO: paging
        content = r.json()
        if r.status_code == 200:
            for gist in content:
                # Get languages used in files
                languages = []
                for file in gist["files"]:
                    languages.append(gist["files"][file]['language'])
                gist["languages"] = list(set(languages))

                # Get owners of forks
                r_forks = requests.get(gist["forks_url"], headers={"Accept": "application/vnd.github.v3+json"})
                # TODO: Sort for last used
                forks = []
                for fork in r_forks.json():
                    forks.append(fork["owner"]["login"])
                gist["forks"] = forks[:3]
            return render(request, "gists/base.html", {"username": username, "json_content": content})
    return render(request, "gists/base.html")