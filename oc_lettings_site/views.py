from django.shortcuts import render


# Lorem ipsum dolor sit amet, consectetur adipiscing elit.
# Quisque molestie quam lobortis leo consectetur ullamcorper non id est.
# Praesent dictum, nulla eget feugiat sagittis, sem mi convallis eros,
# vitae dapibus nisi lorem dapibus sem.
# Maecenas pharetra purus ipsum, eget consequat ipsum lobortis quis. Phasellus eleifend ex auctor venenatis tempus.
# Aliquam vitae erat ac orci placerat luctus.
# Nullam elementum urna nisi, pellentesque iaculis enim cursus in.
# Praesent volutpat porttitor magna, non finibus neque cursus id.
def index(request):
    '''
    Affiche la page index.

    Parameters:
        request: objet contenant toutes les informations de la requête.

    Returns:
        tupple contenant : toutes les informations de la requête, le template de la page html.
    '''
    return render(request, "index.html")


def sentry_debug(request):
    division_by_zero = 1 / 0
