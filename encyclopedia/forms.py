from django import forms

class EditPageForm(forms.Form):
    entry = forms.CharField(widget=forms.Textarea())

class NewPageForm(forms.Form):
    title = forms.CharField(label="title", 
                            required=True, 
                            widget=forms.TextInput(
                                    attrs={"placeholder":"title",}
                            ))
    entry = forms.CharField(widget=forms.Textarea(attrs={
                                "rows":5, 
                                "cols":5,
                                "placeholder":"Write entry here in markdown",}))
    # entry = forms.CharField(widget=forms.Textarea())