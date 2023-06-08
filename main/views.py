from django.shortcuts import render, reverse
from django.views.generic import CreateView
from main.models import *


# Create your views here.
def index(request):
    # this is the static main page
    return render(request, "main/index.html", {})


class NewsletterSubscribeView(CreateView):
    model = Contact
    fields = ["name", "email", "telnr", "notes"]
    template_name = "main/newsletter_subscribe.html"

    def get_success_url(self):
        ## TODO: success toast
        return reverse("main_index")
