from django.shortcuts import redirect
from django.core.mail import send_mail

# Create your views here.

#send_login_email views and redirect to homepage later
def send_login_email(request):
	email = request.POST['email']
	send_mail(
		'Your log in link from todolist',
		'body text tbc',
		'test@mockfrom.com',
		[email],
	)
	return redirect('/')

