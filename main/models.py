from django.db import models


# lets start with the newsletter/Contact-list
## Define contacts
### The contact is used for the NEWSLETTER --> Its in essence only the email adress
class Contact(models.Model):
    contact_type = models.CharField("Typ", max_length=300, null=True, blank=True)
    name = models.CharField("Name", max_length=500, null=True, blank=True)
    email = models.EmailField("Email", max_length=300)
    telnr = models.CharField("Telefon", max_length=300, null=True, blank=True)
    notes = models.TextField("Notizen", null=True, blank=True)

    def __str__(self):
        return self.email


### inherited classes: Used for more finegrained contact information!
class Group(Contact):
    city = models.CharField("Stadt", max_length=300, blank=True, null=True)
    website = models.URLField("Website", max_length=2000, blank=True, null=True)
    # logo: todo for community pages
    main_contact = models.ManyToManyField("Person", blank=True, related_name="leading_group")

    def __str__(self):
        return f"{self.name} ({self.city})"


class Person(Contact):
    # add affiliations (if necessary)
    group = models.ManyToManyField(Group, blank=True, related_name="member")

    def __str__(self):
        return self.name if self.name else self.email


## And the newsletter
class Newsletter(models.Model):
    name = models.CharField("Newsletter Name", max_length=300)
    subscribers = models.ManyToManyField(Contact, blank=True, related_name="newsletter")

    def __str__(self):
        return self.name
