from django.shortcuts import render, reverse
from django.views.generic import CreateView
from django.http import HttpResponseRedirect
from main.models import *
from django.contrib import messages
from main.forms import EmailForm


# Create your views here.
def index(request):
    # this is the static main page
    return render(request, "main/index.html", {})


class NewsletterSubscribeView(CreateView):
    model = Contact
    fields = ["name", "email", "telnr", "notes"]
    template_name = "main/newsletter/newsletter_subscribe.html"

    # TODO: unique email adressess

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Du hast dich erfolgreich angemeldet")
        return reverse("main_index")


def newsletter_unsubscribe_view(request):
    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            # TODO: make sure only newsletter are removed, not members
            Contact.objects.filter(email=email).delete()
            messages.add_message(request, messages.SUCCESS, "Du hast dich erfolgreich abgemeldet")
            return HttpResponseRedirect(reverse("main_index"))
        return render(request, "main/newsletter/newsletter_unsubscribe.html", {"form": form})
    form = EmailForm()
    return render(request, "main/newsletter/newsletter_unsubscribe.html", {"form": form})
