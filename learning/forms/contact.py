from django import forms


class Contact(forms.Form):

    name = forms.CharField(
        label='İsim',
        max_length=50,
        min_length=5,
        required=True,
        initial='isminizi giriniz...',
        disabled=False,
        widget=forms.TextInput(
            attrs={
                'class': 'special',
                'size': '40',
                'title': 'İsminiz',
                'required': True
            }
        )
    )
    email = forms.EmailField(label='Email Adresi')
    content = forms.CharField(widget=forms.Textarea)

    '''
    Widgets
    TextInput, Textarea, NumberInput, EmailInput, URLInput, PasswordInput, HiddenInput, DateInput, DateTimeInput, TimeInput
    CheckboxInput, Select, NullBooleanSelect, SelectMultiple, RadioSelect, CheckboxSelectMultiple
    FileInput, ClearableFileInput
    MultipleHiddenInput, SplitDateTimeWidget, SplitHiddenDateTimeWidget, SelectDateWidget, 
    '''


