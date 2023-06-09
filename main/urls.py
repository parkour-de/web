from django.urls import path
import main.views as views

urlpatterns = [
    path("", views.index, name="main_index"),
    path("mitmachen", views.NewsletterSubscribeView.as_view(), name="main_newsletter"),
    path("nicht-mitmachen", views.newsletter_unsubscribe_view, name="main_newsletter_out"),
]
