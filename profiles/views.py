from django.shortcuts import render
from .models import Profile


# Sed placerat quam in pulvinar commodo. Nullam laoreet consectetur ex, sed consequat libero pulvinar eget. Fusc
# faucibus, urna quis auctor pharetra, massa dolor cursus neque, quis dictum lacus d

def index(request):
    """
        Renders profiles list page with all Profile objects from the database.
        Fetches Profiles, places them into context, and serves the rendered view.

        :param request: http request object.
        :type request: object
        :return: http response with context
        :rtype: tuple[request, html, dict[list[dict]]
        """

    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles/index.html", context)


# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac
# laoreet neque quis, pellentesque dui. Nullam facilisis pharetra vulputate.
# Sed tincidunt, dolor id facilisis fringilla, eros leo tristique lacus,
# it. Nam aliquam dignissim congue. Pellentesque habitant morbi tristique senectus et netus et males

def profile(request, username):
    '''
    Renvoie les informations d'une instance de Profile.

    Parameters:
        request: objet contenant toutes les informations de la requête.
        profile_id : id d'une instance de Profile à partir duquel des informations vont être extraites.

    Returns:
        tupple contenant : toutes les informations de la requête, le template de la page html,un dictionnaire
         des informations d'une instance de Profile.
    '''
    profile = Profile.objects.get(user__username=username)
    context = {"profile": profile}
    return render(request, "profiles/profile.html", context)
