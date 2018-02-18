"""
Definition of views.
"""

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest, HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime
from django.core.mail import send_mail, BadHeaderError

def home(request):
    """Renders the home page."""
    return render(
        request,
        'home/base.html',
    )

def resume(request):
    """Renders the resume page."""
    return render(
        request,
        'home/resume.html',
    )
