from __future__ import unicode_literals

from django.db import models
from ..login_app.models import User

# Create your models here.
class QuoteManager(models.Manager):
    def addQuote(self, postData, userId):      
        results = {'status':True, 'errors':[]}
        if not postData['quotedBy'] or len(postData['quotedBy'])<4:
            results['status']=False
            results['errors'].append('Quoted By field must be at least 4 characters.')
        if not postData['quote'] or len(postData['quote'])<11:
            results['status']=False
            results['errors'].append('Message must be more than 10 characters.')
        else:
            user = User.objects.get(id=userId)
            newQuote = Quote.objects.create(quotedBy=postData['quotedBy'], content=postData['quote'], owner=user)
            return results
        return results

    def addFavorite(self, postData, userId):
        quote = Quote.objects.get(id=postData['quoteId'])
        user = User.objects.get(id=userId)
        user.fave.add(quote)
        return quote

    def removeFavorite(self, postData, userId):
        quote = Quote.objects.get(id=postData['quoteId'])
        user = User.objects.get(id=userId)
        user.fave.remove(quote)
        return quote

class Quote(models.Model):
    quotedBy = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    owner = models.ForeignKey(User, related_name = 'owner')
    favorite = models.ForeignKey(User, related_name = 'fave', null=True, blank=True)
    objects = QuoteManager()

