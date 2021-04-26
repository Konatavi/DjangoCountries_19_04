import json
import string
from django.shortcuts import render, Http404

with open("data/country-by-languages.json") as f:
    countries_data = json.load(f)


def main(request):
    return render(request, 'index.html')


def countries(request):
    alphabet = string.ascii_uppercase
    country_names = []
    for country_dict in countries_data:
        country_names.append(country_dict["country"])
    return render(request, 'countries.html', {"country_names": country_names, "alphabet": alphabet})


def countries_filter_by_word(request, word):
    alphabet = string.ascii_uppercase
    country_names = []
    for country_dict in countries_data:
        country_names.append(country_dict["country"])
    country_names = filter(lambda name: name[0] == word, country_names)
    return render(request, 'countries.html', {"country_names": country_names, "alphabet": alphabet})


def countries_filter_by_lang(request, language):
    alphabet = string.ascii_uppercase
    country_names = []
    for country_dict in countries_data:
        if language in country_dict["languages"]:
            country_names.append(country_dict["country"])
    return render(request, 'countries.html', {"country_names": country_names, "alphabet": alphabet})


def country_page(request, country_name):
    country = {}

    for country_dict in countries_data:
        if country_dict["country"] == country_name:
            country["name"] = country_dict["country"]
            country["languages"] = country_dict["languages"]
            return render(request, 'country_page.html', {"country": country})
    raise Http404


def languages(request):
    langs = set()
    for country_dict in countries_data:
        langs.update(country_dict["languages"])

    return render(request, 'languages.html', {"languages": sorted(langs)})