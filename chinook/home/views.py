from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Review
from .forms import ReviewForm


def home(request):
    '''
    Landing Page
    '''
    return render(request, 'home/home.html')

def about(request):
    '''
    About Page
    '''
    return render(request, 'home/about.html')

def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user 
            review.save()
            return redirect('reviews')
    else:
        form = ReviewForm()
    return render(request, 'home/add_review.html', {'form': form})

def reviews(request):
    '''
    Customer review page
    '''
    reviews = Review.objects.all()
    return render(request, 'home/reviews.html', {'reviews': reviews})

def our_work(request):
    '''
    The work we do maintaining rivers, training guides, school field trips and movie filming
    '''
    return render(request, 'home/ourWork.html')