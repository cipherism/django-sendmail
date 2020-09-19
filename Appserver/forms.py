from django import forms

class Subscribe(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control col-md-2'}))
    message = forms.CharField(widget=forms.Textarea(
        attrs={'class':'form-control col-md-4'})
                              )

    def __str__(self):
        return self.email
