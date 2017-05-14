from django.contrib import admin

from django.contrib.admin import ModelAdmin, TabularInline, StackedInline

from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext_noop
from django.utils.translation import ugettext 

from .models import *

from .defReadDB import *

import simplejson as json

from datetime import datetime

from django.conf import settings

#--------------------------------------------

admin.site.site_header = 'Test Blog  administration'
admin.site.site_title = 'Test Blog administration'


#====================================================================================
class AdminReadUser(ModelAdmin):
    
    list_display = [
        'user',
        'signuser',
        ]
    

    ordering = (
        'user',
        'signuser',
        )

    search_fields = ['user']


    #------------------------------------------------
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "signuser":
            #kwargs["queryset"] = User.objects.exclude(username=request.user).exclude(is_superuser=True)
            kwargs["queryset"] = User.objects.exclude(username=request.user)
        return super(AdminReadUser, self).formfield_for_foreignkey(db_field, request, **kwargs)

    #------------------------------------------------
    def get_search_results(self, request, queryset, search_term):
        if request.user.is_superuser:
            qsearch_term = search_term
        else:
            qsearch_term = str(request.user)
        
        queryset, use_distinct = super(AdminReadUser, self).get_search_results(request, queryset, qsearch_term)
        
        return queryset, use_distinct

    #------------------------------------------------
    def save_model(self, request, obj, form, change):      
        obj.user = str(request.user)

        (error, q) = getReadUser(obj.user, obj.signuser)
        
        if error == 0:
            messages.error(request, str(_('Не записано. Запись с такими значениями уже есть')) )
        elif error == 1:
            obj.save()
        else:
            messages.error(request, str(_('Ошибка ')) + str(error) )
                

        
#====================================================================================
class AdminBlogPost(ModelAdmin):
    
    fieldsets = (
        (None, {
            'fields': ('header', 'content', )
        }),
    )

    list_display = [
        'user',
        'header',
        'content',
        #'qdate',
        'format_date',
        ]
    

    ordering = (
        'user',
        '-qdate',
        )

    search_fields = ['user']

    
    #------------------------------------------------    
    def format_date(self, obj):
        return obj.qdate.strftime('%d.%m.%Y %H:%M:%S')
    format_date.short_description = _("Date")
    format_date.admin_order_field = 'qdate'
    
    #------------------------------------------------
    def get_search_results(self, request, queryset, search_term):
        if request.user.is_superuser:
            qsearch_term = search_term
        else:
            qsearch_term = str(request.user)
            
        queryset, use_distinct = super(AdminBlogPost, self).get_search_results(request, queryset, qsearch_term)
        
        return queryset, use_distinct

    #------------------------------------------------
    def save_model(self, request, obj, form, change):
        if change:
            pass    
        else:
            obj.user = str(request.user)
        
        obj.save()

        
        
        
#====================================================================================
admin.site.register(ReadUser, AdminReadUser)
admin.site.register(BlogPost, AdminBlogPost)
#admin.site.register(ReadPost)


