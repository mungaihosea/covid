from django.shortcuts import render
import requests
import json


def index(request):
    url = "https://covid-193.p.rapidapi.com/statistics"

    headers = {
        'x-rapidapi-key': "2d3cd3d8e8mshc3d3dcfc034a8efp1afdd5jsnbb772383c7af",
        'x-rapidapi-host': "covid-193.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers)

    data = json.loads(response.text)['response']

    context = {
        "data":data,
    }
    # for x in data:
    #     print(x['country'], x['population'], x['tests']['total'], x['cases']['total'], x['deaths']['total'])
    return render(request, "index.html", context)