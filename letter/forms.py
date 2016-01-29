from django import forms
from letter.models import Letter

class PostLetter(forms.ModelForm):
	is_agree = forms.BooleanField(label='접수된 편지는 수정이 불가능합니다.', error_messages={'required':'발송 및 수정에 관한 안내를 확인해주세요.'})
	class Meta:
		model = Letter
		fields = '__all__'