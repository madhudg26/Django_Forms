from django import forms
#g=[('MALE','male'),('FEMALE','female')]

class Student_Details(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField(min_value=5)
    url=forms.URLField()
    email=forms.EmailField(min_length=5)
    time=forms.TimeField()
    date=forms.DateField()
    datetime=forms.DateTimeField()
    password=forms.CharField(max_length=100,widget=forms.PasswordInput)
    address=forms.CharField(max_length=1000,widget=forms.Textarea(attrs={'cols':3,'rows':3}))
    #gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)