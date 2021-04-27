from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Country(models.Model):
    name = models.CharField(max_length=100)
    languages = models.ManyToManyField(Language)


# lang1 = Language(name='russian')
# lang2 = Language(name='english')
# lang1.save()
# lang2.save()
#
# country = Country(name="Russia")
# country.save()
#
# country.languages.add(lang1, lang2)
# country.languages.add(lang2)
