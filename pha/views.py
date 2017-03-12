from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import PhaItem, PhaAction, Node, Hierachy, PhaStudy
# Create your views here.
def index(request):
    pha_study_list = PhaStudy.objects.all()
    directory = Hierachy.objects.all()
    template = loader.get_template('pha/index.html')
    context = { 'pha_study_list': pha_study_list, 'directory': directory }
    return HttpResponse(template.render(context, request))

def phaStudy(request, phastudy_id):
    pha_study = PhaStudy.objects.get(pk=phastudy_id)
    template = loader.get_template('pha/phaStudy.html')
    context = { 'pha_study': pha_study}
    return HttpResponse(template.render(context, request))
      

def phaItemDetail(request, phaItem_id):
    return HttpResponse("You're looking at question %s." % phaItem_id)
    
def phaActionList(request):
    pha_action_list = PhaAction.objects.all()
    template = loader.get_template('pha/actionlist.html')
    context = { 'pha_action_list': pha_action_list}
    return HttpResponse(template.render(context, request))
    
def phaActionDetail(request, phaAction_id):
    return HttpResponse("You're looking at phaAction %s." % phaAction_id)