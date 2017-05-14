from django.contrib.syndication.views import Feed
from django.utils import feedgenerator
from django.core.urlresolvers import reverse

from .models import *

from .defReadDB import *

#------------------------------------------------------------------
class PostFeed(Feed):

    description_template = 'blog/postfeed.html'
    feed_type = feedgenerator.Rss201rev2Feed
    title = "Лента новостей"
    description = "Последние новости"
    link = '/'
    

    def get_object(self, request): 
        print("feedListSignUser")
        user = str(request.user)   

        (error, qset) = readListSignUser(user)

        return qset
    

    def items(self, obj):
        # obj - список подписпнных пользователей
        print("feedSignPost") 

        (error, qset) = readSignPost(obj)         
        
        return qset

    
    def item_title(self, item):
        return item.header

    def item_description(self, item):
        return item.content

    