from django.shortcuts import render,HttpResponse
from webinar.forms import UserForm,EditForm
from django.views.generic.edit import FormView
from django.core.mail import send_mail
from django.template.loader import render_to_string
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create your views here.
class Index(FormView):
	template_name = 'index.html'
	form_class = UserForm
	success_url = '/thanks/'

	def form_valid(self, form):
		to_mail = form.cleaned_data['email']
		sub = render_to_string('subject.txt',{})
		msg = render_to_string('halo.txt',{})
		send_mail(sub ,msg ,'info@codegnan.com',[to_mail],fail_silently=False)
		return super().form_valid(form)

def editView(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EditForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            subject = form.cleaned_data['subject']
            body = form.cleaned_data['body']
            with open(os.path.join(BASE_DIR, 'webinar/templates/subject.txt'),'w') as f:
            	f.write(subject)
            with open(os.path.join(BASE_DIR, 'webinar/templates/halo.txt'),'w') as f:
            	f.write(body)
            # redirect to a new URL:
            return HttpResponse('successfully edited subject and body')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = EditForm()

    return render(request, 'edit.html', {'form': form})

def thanks(request):
	return render(request,'thanks.html')