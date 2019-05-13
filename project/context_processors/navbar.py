from project.models import Distributor, Dealer

def get_navbar(request):

    role_id = request.session.get('role_id', False)
    role_page = request.session.get('role_page', False)

    if role_page == 'distributor':
        distributor = Distributor.objects.get(pk=role_id)

        if distributor.author_id == role_id:
            author = True

    elif role_page == 'dealer':
        dealer = Dealer.objects.get(pk=role_id)

        if dealer.author_id == role_id:
            author = True
    else:
        author = False



    return {
        "navbar": {
            'author': True
        }
    }
