from django import forms
from django.forms import widgets
from django.forms import ModelForm
from project.models import Project

class ProjectForm(ModelForm):
	class Meta:
		model=Project

	# def __init__(self, *args, **kwargs):
 #    user = kwargs.pop('user','')
 #    super(ProjectForm, self).__init__(*args, **kwargs)
 #    self.fields['user_defined_code']=forms.ModelChoiceField(queryset=UserDefinedCode.objects.filter(owner=user))

		"""widgets={
                      "name":forms.TextInput(attrs={'placeholder':'Project Name','class':'input-sm form-control'}),
                      "desc":forms.TextInput(attrs={'placeholder':'description','class':'input-sm form-control'}),
                      "money_req":forms.TextInput(attrs={'placeholder':'100000','class':'input-sm form-control'}),
                      "days_req":forms.TextInput(attrs={'placeholder':'100','class':'input-sm form-control'}),
                      "photo":CustomClearableFileInput(attrs={'value':'Select image','class':'btn btn-md btn-primary'}),
                      "video_link":forms.URLField(attrs={'placeholder':'www.youtube.com/watch?aJd23Xw','class':'input-sm form-control'}),
                      "details":forms.Textarea(attrs={'class':'input-sm form-control','rows':5}),
                      "project_use":forms.TextInput(attrs={'placeholder':'Ex: Technology','class':'input-sm form-control'}),
                      "pledge1":forms.TextInput(attrs={'placeholder':'100','class':'input-sm form-control'}),
                      "pledge2":forms.TextInput(attrs={'placeholder':'1000','class':'input-sm form-control'}),
                      "pledge3":forms.TextInput(attrs={'placeholder':'10000','class':'input-sm form-control'}),
                      "pledge4":forms.TextInput(attrs={'placeholder':'100000','class':'input-sm form-control'})
                  }  """