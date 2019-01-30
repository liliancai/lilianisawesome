from django.shortcuts import redirect
from django.core.mail import send_mail
from django.contrib import messages
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
	messages.success(
		request,
		"Check your email, we've sent you a link you can use to log in."
	)
	return redirect('/')

