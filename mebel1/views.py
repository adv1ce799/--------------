from django.shortcuts import get_object_or_404, render, redirect
from .models import Card, Category
from .models import Comment
from .forms import CommentForm

def home(request):
    return render(request, 'base.html')

def sale(request):
    goods = Card.objects.all()
    categories = Category.objects.all()
    context = {
        'goods': goods,
        'categories': categories,
    }
    return render(request, 'sale.html', context)

def category_view(request, category_id):
    goods = Card.objects.filter(category_id=category_id) 
    categories = Category.objects.all()
    context = {
        'goods': goods,
        'categories': categories,
    }
    return render(request, 'sale.html', context)

def product(request, post_slug):
    post = get_object_or_404(Card, slug=post_slug)

    context = {
        'post': post,
    }

    return render(request, 'product.html', context)

def kontakt(request):
    return render(request, 'kontakt.html')

def otziv(request):
    comments = Comment.objects.all().order_by('-created_at')
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('otziv') 
    else:
        form = CommentForm()

    return render(request, 'otziv.html', {'form': form, 'comments': comments})
