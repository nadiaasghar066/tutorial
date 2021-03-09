from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])



class auther(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    bookname = models.ForeignKey('book', on_delete=models.CASCADE)
class Meta:
    ordering = ['created']

class book(models.Model):
    bookname = models.CharField(max_length=100, blank=None, default='None', primary_key = True)
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
highlighted = models.TextField()
def save(self, *args, **kwargs):
    self.highlighted = highlight(self.code, lexer, formatter)
    super(book, self).save(*args, **kwargs)

class Meta:
        ordering = ['created']
