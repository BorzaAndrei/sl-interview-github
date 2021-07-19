from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
import requests

# Create your views here.
def index(request):
    return render(request, "gists/base.html")


def search_username(request, pagination_index: int):
    if request.method == 'POST':
        username = request.POST.get('username')
        r = requests.get(f"https://api.github.com/users/{username}/gists?per_page={settings.GISTS_PER_PAGE}&page={pagination_index}", headers={"Accept": "application/vnd.github.v3+json"})
        content = r.json()
        if r.status_code == 200:
            for gist in content:
                # Get languages used in files
                languages = []
                files_content = {}
                for file in gist["files"]:
                    p_file = gist["files"][file]
                    languages.append(p_file['language'])

                    filename = p_file['filename'].replace('.', '--')
                    files_content[filename] = requests.get(p_file['raw_url']).text
                gist["languages"] = list(set(languages))
                gist["files_content"] = files_content

                # Get owners of forks
                r_forks = requests.get(gist["forks_url"], headers={"Accept": "application/vnd.github.v3+json"})
                # TODO: Sort for last used
                forks = []
                for fork in r_forks.json():
                    print(fork)
                    forks.append(fork["owner"]["login"])
                gist["forks"] = forks[:3]
            if len(content) < settings.GISTS_PER_PAGE:
                next_pagination_index = -1
            else:
                next_pagination_index = pagination_index + 1
            return render(request, "gists/base.html", {"username": username, "json_content": content, "next_pagination_index": next_pagination_index, "prev_pagination_index": pagination_index - 1})
        else:
            print("Error!")
            print(r.text)
    return render(request, "gists/base.html")