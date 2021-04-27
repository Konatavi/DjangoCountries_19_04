import json
from django.core.management.base import BaseCommand
from CountriesApp.models import Country, Language


class Command(BaseCommand):
    help = 'Create DB object from json'

    def handle(self, *args, **options):
        with open("data/country-by-languages.json") as f:
            countries_data = json.load(f)
            for country_dict in countries_data:
                country = Country(name=country_dict["country"])
                country.save()
                for language_name in country_dict["languages"]:
                    language = Language(name=language_name)
                    language.save()
                    country.languages.add(language)
