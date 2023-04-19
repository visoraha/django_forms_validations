from django import forms
g=[('male','MALE'),('female','FEMALE')]
c=[('java','JAVA'),('python','PYTHON')]

class Student_Form(forms.Form):
    name=forms.CharField(max_length=100)
    mono=forms.IntegerField()
    age=forms.IntegerField()
    email=forms.EmailField()
    date=forms.DateField()
    password=forms.CharField(max_length=100,widget=forms.PasswordInput)
    address=forms.CharField(max_length=100,widget=forms.Textarea(attrs={'cols':5,'rows':5}))
    #gender=forms.ChoiceField(choices=g)
    gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    course=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)