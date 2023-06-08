from django.shortcuts import render, reverse
from django.views.generic import CreateView
from main.models import *
from django.contrib import messages


# Create your views here.
def index(request):
    # this is the static main page
    return render(request, "main/index.html", {})


class NewsletterSubscribeView(CreateView):
    model = Contact
    fields = ["name", "email", "telnr", "notes"]
    template_name = "main/newsletter/newsletter_subscribe.html"

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Du hast dich erfolgreich angemeldet")
        return reverse("main_index")
