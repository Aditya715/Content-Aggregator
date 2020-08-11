from django import forms

class ModalForm(forms.Form):
    author_name = forms.CharField(label="Author Name", 
                                    max_length=40, 
                                    required=False)
    date = forms.DateField(label="Date", 
                            widget=forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}),
                            required=False
                        )