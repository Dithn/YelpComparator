from django import forms

class YelpBusinessForm(forms.Form):
  businesses = forms.MultipleChoiceField()

  def __init__(self, businesses, *args, **kwargs):
    super(YelpBusinessForm, self).__init__(*args, **kwargs)
    businessList = businesses
    self.fields['businesses'] = forms.MultipleChoiceField(
        choices=[(i['id'], i['name']) for i in businessList],
        widget=forms.widgets.CheckboxSelectMultiple(attrs={
            'style':'list-style: none;',
        }),
        )
