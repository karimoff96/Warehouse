import requests


def check(request):
    response = requests.get("http://127.0.0.1:8000/api/check")
    print(response)

