from django.http import Http404
from django.contrib import messages
from django.shortcuts import redirect

class LoginRequiredMixin:
	def dispatch(self, request, *args, **kwargs):
		if self.request.user.is_authenticated:
			return super().dispatch(request, *args, **kwargs)
		else:
			messages.info(request,'Please login First')
			return redirect('/')