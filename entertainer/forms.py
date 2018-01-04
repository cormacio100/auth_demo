from django import forms
from entertainer.models import Entertainer


class EntertainerRegistrationForm(forms.ModelForm):

    #   User Object required to be created before Entertainer object
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(EntertainerRegistrationForm,self).__init__(*args,**kwargs)

    #   Custom save function to include the User
    def save(self,commit=True):
        #   save(commit=False prevents the form from auto saving
        instance = super(EntertainerRegistrationForm,self).save(commit=False)

        # auto set the user instance to that provided by the view
        instance.user = self.user

        if commit:
            instance.save()

        return instance

    #   Fields to include on form from the Entertainer model
    class Meta:
        model = Entertainer
        fields = ('title',
                  'description',
                  'genre',
                  'profileImage')