from django import forms
from cms.models import ServicesBlock, PortfolioBlock, AboutBlock

class ServicesBlockForm(forms.Form):
    pic = forms.CharField(max_length=30)
    title = forms.CharField(max_length=30)
    content = forms.CharField(max_length=100)
    sequence_num = forms.IntegerField(default=1)

    class Meta:
        model = ServicesBlock
        fields = ('sequence_num', 'title', 'content')

class PortfolioBlockForm(forms.Form):
    title = forms.CharField(max_length=30)
    tag = forms.CharField(max_length=30)
    content = forms.CharField(max_length=100)
    sequence_num = forms.IntegerField(default=1)
    
    class Meta:
        model = PortfolioBlock
        fields = ('sequence_num', 'title', 'content')