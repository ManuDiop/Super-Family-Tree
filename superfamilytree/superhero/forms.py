from django import forms
from .models import SuperHero

class SuperHeroForm(forms.ModelForm):
    class Meta:
        model = SuperHero
        fields = ['name', 'description', 'skill1', 'skill2', 'skill3', 'parent']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3, 'cols': 40}),
            'skill1': forms.TextInput(attrs={'placeholder': 'Enter Skill 1'}),
            'skill2': forms.TextInput(attrs={'placeholder': 'Enter Skill 2 (optional)'}),
            'skill3': forms.TextInput(attrs={'placeholder': 'Enter Skill 3 (optional)'}),
        }
