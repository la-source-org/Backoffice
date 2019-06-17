from django.shortcuts import render

# Create your views here.


def annuaire_list(request):

    supplier_details = None
    return render(request, 'annuaire/index.html', {'supplier_details': supplier_details})
