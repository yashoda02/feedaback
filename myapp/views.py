from django.shortcuts import render, redirect
from .forms import FeedbackForm
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def home_view(request):
    return render(request, 'home.html')
def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback_success')
    else:
        form = FeedbackForm()
    return render(request, 'feedback_form.html', {'form': form})

def feedback_success(request):
    return render(request, 'feedback_success.html')
