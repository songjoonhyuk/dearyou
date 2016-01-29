from django.contrib import admin
from letter.models import Letter
# models.py에서 정의한 함수를 불러옴
# Register your models here.

class LetterAdmin(admin.ModelAdmin):
  list_display = ['id', 'title', 'get_content_length']
  list_display_links = ['id', 'title']

  def get_content_length(self, letter):
    return len(letter.content)

admin.site.register(Letter, LetterAdmin)
