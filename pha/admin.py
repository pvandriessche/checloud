from django.contrib import admin

# Register your models here.
from .models import PhaItem, Node, GuideWord, PhaAction, Hierachy, PhaStudy
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory


class MyAdmin(TreeAdmin):
    form = movenodeform_factory(Hierachy)
    
admin.site.register(PhaItem)
admin.site.register(Node)
admin.site.register(GuideWord)
admin.site.register(PhaAction)
admin.site.register(PhaStudy)
admin.site.register(Hierachy, MyAdmin)