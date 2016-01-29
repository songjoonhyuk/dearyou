from django.shortcuts import redirect, render
from letter.models import Letter
from letter.forms import PostLetter

# Create your views here.
def index(request):
	return render(request, 'index.html')


def letter_new(request):
	if request.method == 'POST':
		form = PostLetter(request.POST)
		if form.is_valid():
			letter = form.save()
			return redirect('letter.views.index')

	else:
		form = PostLetter()
	return render(request, 'write_letter.html', {'form':form,})
