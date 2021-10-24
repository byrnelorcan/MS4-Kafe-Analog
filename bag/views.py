from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages

from products.models import Products

# Create your views here.


def view_bag(request):
    """ A view that renders the shopping bag """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add the specified product to the shopping bag """

    products = Products.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {products.name} to your cart!')

    request.session['bag'] = bag
    return redirect(redirect_url)



def edit_bag(request, item_id):
    """ Edit the quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
    else:
        bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ Remove specified product from the shopping bag """

    try:
        bag = request.session.get('bag', {})
        bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)