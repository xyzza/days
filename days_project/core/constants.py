import pycountry

COUNTRY_CHOICES = [(it.alpha_2, it.name) for it in pycountry.countries]
COUNTRY_CHOICES_DICT = {it.alpha_2: it.name for it in pycountry.countries}
