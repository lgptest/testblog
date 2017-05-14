from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = 'blog'

    # LGP 
    def ready(self):
    	import blog.signals 