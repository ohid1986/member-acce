from django import forms
from django.forms import ModelForm,Textarea
from pagedown.widgets import PagedownWidget
from django.forms.models import inlineformset_factory


from .models import Person, ExecMember, Membership, Constitution, News, Event, Gallery
from django.conf import settings

from django.core.exceptions import ValidationError
from django.core.mail import BadHeaderError, mail_managers

from django.utils.translation import ugettext_lazy as _


from django.core.validators import RegexValidator

# for Land phone

class PhoneNumberWidget(forms.MultiWidget):
    def __init__(self, *args, **kwargs):

        widgets = [
            forms.TextInput(attrs={'placeholder':'code:00880'}),
            forms.TextInput(attrs={'placeholder':'number:29211111'})
        ]
        super(PhoneNumberWidget, self).__init__(widgets, *args, **kwargs)
    def decompress(self, value):
        if value:
            return value.split(' ')
        return [None, None]

class PhoneNumberField(forms.MultiValueField):
    widget = PhoneNumberWidget


    def __init__(self, *args, **kwargs):
        # Define one message for all fields.
        error_messages = {
            'incomplete': 'Enter a country calling code and a phone number.',
        }
        # Or define a different message for each field.
        fields = (
            forms.CharField(
                error_messages={'incomplete': 'Enter a country calling code.'},
                validators=[
                    RegexValidator(r'^[0-9]+$', 'Enter a valid country calling code.'),
                ],
            ),
            forms.CharField(
                error_messages={'incomplete': 'Enter a phone number.'},
                validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')],
            ),
            forms.CharField(
                validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid extension.')],
                required=False,
            ),
        )
        super(PhoneNumberField, self).__init__(
            error_messages=error_messages, fields=fields,
            require_all_fields=False, *args, **kwargs
        )

    def compress(self, data_list):
        return ''.join(data_list)

# for Cell phone
class PhoneWidget(forms.MultiWidget):
    def __init__(self, *args, **kwargs):

        widgets = [
            forms.TextInput(),
            forms.TextInput()
        ]
        super(PhoneWidget, self).__init__(widgets, *args, **kwargs)
    def decompress(self, value):
        if value:
            return value.split(' ')
        return [None, None]

class CellPhoneNumberField(forms.MultiValueField):

    widget = PhoneWidget

    def __init__(self, *args, **kwargs):
        # Define one message for all fields.
        error_messages = {
            'incomplete': 'Enter a country calling code and a phone number.',
        }
        # Or define a different message for each field.
        fields = (
            forms.CharField(
                error_messages={'incomplete': 'Enter a country calling code.'},
                validators=[
                    RegexValidator(r'^[0-9]+$', 'Enter a valid country calling code.'),
                ],
            ),
            forms.CharField(
                error_messages={'incomplete': 'Enter a phone number.'},
                validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')],
            ),
            forms.CharField(
                validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid extension.')],
                required=False,
            ),
        )
        super(CellPhoneNumberField, self).__init__(
            error_messages=error_messages, fields=fields,
            require_all_fields=False, *args, **kwargs
        )

    def compress(self, data_list):
        return ''.join(data_list)

from django.contrib.auth import get_user

class MemberForm(ModelForm):
    # tele_land = PhoneNumberField()
    # tele_cell = CellPhoneNumberField()
    birth_date = forms.DateField(widget=forms.widgets.DateInput(format="%m/%d/%Y"))
    member_since = forms.DateField(widget=forms.widgets.DateInput(format="%m/%d/%Y"))

    class Meta:
        model = Person
        exclude = ('user',)
        widgets = {
            'tele_land': forms.TextInput(attrs={'placeholder': 'Start with '+', e.g., +8802...'}),
            'tele_cell': forms.TextInput(attrs={'placeholder': 'Start with ' + ', e.g., +8802...'}),




        }

    def __init__(self, *args, **kwargs):
        super(MemberForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['placeholder'] = 'Your full name'
        self.fields['tele_land'].label = 'Land phone'
        self.fields['tele_cell'].label = 'Cell phone'
        self.fields['passing_year'].label = 'Passing year'
        self.fields['passing_year'].help_text = 'According to your session year'


    def save(self, request, commit=True):
        person = super().save(commit=False)
        if not person.pk:
            person.user = get_user(request)
        if commit:
            person.save()
            self.save_m2m()
        return person

class ExeCommMemberForm(ModelForm):
    member_start_date = forms.DateField(widget=forms.widgets.DateInput(format="%m/%d/%Y"))
    member_end_date = forms.DateField(widget=forms.widgets.DateInput(format="%m/%d/%Y"))

    class Meta:
        model = ExecMember
        fields = '__all__'
        widgets = {
            'committee_position': forms.TextInput(attrs={'placeholder': 'Designation in Exe. Comm.'}),
            'rank': forms.TextInput(attrs={'placeholder': 'Rank order in Exe. Comm.'}),

        }

    def __init__(self, *args, **kwargs):
        super(ExeCommMemberForm, self).__init__(*args, **kwargs)
        self.fields['name'].queryset = Person.objects.filter(category__id="1")


class MembershipForm(ModelForm):

    class Meta:
        model = Membership
        fields = '__all__'

class ConstitutionForm(ModelForm):

    content = forms.CharField(widget=PagedownWidget)

    class Meta:
        model = Constitution
        fields = [
            'title',
            'content',
            'docfile',

        ]

class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = '__all__'
        widgets = {
            'news': Textarea(attrs={'cols': 80, 'rows': 20}),
        }


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ('name','description', )

class GalleryForm(ModelForm):
    class Meta:
        model= Gallery
        fields = ('title', 'event',  'image')

GalleryFormSet = inlineformset_factory(Event, Gallery, extra=0, min_num=1, fields=('title', 'image' ))


