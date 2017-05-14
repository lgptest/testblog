from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.dispatch import receiver
from .models import BlogPost

from .email import *

from .feeds import *


@receiver(post_save, sender=BlogPost)
def savesignal(sender, **kwargs):
    #print('savesignal')
    """ 
    kwargs:
    
    {'using': 'default', 
    'created': True, 
    'update_fields': None, 
    'raw': False, 
    'instance': <BlogPost: admin, hello 4>, 
    'signal': <django.db.models.signals.ModelSignal object at 0x02F3C970>}
    """
    #print(kwargs)

    created = kwargs['created']

    if created:
        q = kwargs['instance']
        #(q.user, str(q.pk), q.header, q.content)

        # формирование RSS
        #
        #PostFeed()

        # рассылка почты
        sendSignMail(q)


@receiver(post_delete, sender=BlogPost)
def delsignal(sender, **kwargs):
    pass
    """
    kwargs

    {'instance': <BlogPost: admin, h4>, 
    'using': 'default', 
    'signal': <django.db.models.signals.ModelSignal object at 0x03C0CAB0>}
    """

    
    
