from django.shortcuts import render, redirect
from .models import User, Quote
from django.contrib import messages

# Create your views here.

def home(request):
    if not request.session['userId']:
        return redirect('/')
    user = User.objects.get(id=request.session['userId'])
    normQuotes = Quote.objects.all().exclude(favorite=user)
    favQuotes = Quote.objects.filter(favorite=user)
    context = {
        'user':user,
        'normQuotes':normQuotes,
        'favQuotes':favQuotes,
    }
    return render(request, 'quotes_app/home.html', context)

def addQuote(request):
    if not request.session['userId']:
        return redirect('/')
    results = Quote.objects.addQuote(request.POST, request.session['userId'])
    if results['status']==False:
        for error in results['errors']:
            messages.error(request, error)
    return redirect('/home')

def logout(request):
    request.session['userId']=None
    return redirect('/')

def show(request, id):
    if not request.session['userId']:
        return redirect('/')
    ownerOfQuote = User.objects.get(id=id)
    quotes = Quote.objects.filter(owner=ownerOfQuote)
    count = len(quotes)
    context = {
    'ownerOfQuote':ownerOfQuote,
    'quotes':quotes,
    'count':count,
    }
    return render(request, 'quotes_app/show.html', context)

def addFavorite(request):
    if not request.session['userId']:
        return redirect('/')
    results = Quote.objects.addFavorite(request.POST, request.session['userId'])
    return redirect('/home')

def removeFavorite(request):
    if not request.session['userId']:
        return redirect('/')
    results = Quote.objects.removeFavorite(request.POST, request.session['userId'])
    return redirect('/home')
