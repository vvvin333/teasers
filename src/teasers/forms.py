from django import forms

from teasers.models import Teaser
from users.choices import GroupChoices
from users.models import Author


class TeaserForm(forms.ModelForm):
    author = forms.ModelChoiceField(
        queryset=Author.objects.select_related("user").filter(
            user__is_active=True
        ),
        required=True,
    )

    def __init__(self, *args, instance=None, **kwargs):
        super().__init__(*args, instance=instance, **kwargs)

        if (
            instance is None
            and GroupChoices.authors in self.request_user.groups.all().values_list("name", flat=True)
            and hasattr(self.request_user, "author")
        ):
            self.fields["author"].initial = self.request_user.author
            self.fields["author"].disabled = True

    class Meta:
        model = Teaser
        fields = forms.ALL_FIELDS
