from django import forms
from .models import Container
from sshpubkeys import (SSHKey, TooShortKeyException, TooLongKeyException,
                        InvalidTypeException, MalformedDataException, InvalidKeyException)


def is_valid_ssh(ssh_key):
    try:
        SSHKey(ssh_key)
        return True
    except (InvalidKeyException,
            TooShortKeyException,
            TooLongKeyException,
            InvalidTypeException,
            MalformedDataException):
        return False


class ContainerForm(forms.ModelForm):

    class Meta:
        model = Container
        fields = ('name_owner', 'ssh_key')
        widgets = {
            'ssh_key': forms.Textarea(),
        }

    def clean_ssh_key(self):
        data = self.cleaned_data['ssh_key']

        if not is_valid_ssh(data):
            raise forms.ValidationError("Wrong SSH Key!")

        return data
