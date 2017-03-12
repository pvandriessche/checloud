from __future__ import unicode_literals

from django.db import models
from treebeard.mp_tree import MP_Node

# Create your models here.
class Hierachy(MP_Node):
    name = models.CharField(max_length =200)
    node_order_by = ['name']
    def __unicode__(self):
        return self.name

class GuideWord(models.Model):
    guideWord_text = models.CharField(max_length =200)
    def __str__(self):
        return self.guideWord_text
  
class user (models.Model):
    name = models.CharField(max_length =200)
    
class Participant(models.Model):
    user = models.ForeignKey(Hierachy, on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=False)

class PhaAction(models.Model):
    phaAction_text = models.CharField(max_length =200)
    phaAction_resolution = models.CharField(max_length =200)
    def __str__(self):
        return self.phaAction_text
        
class PhaItem(models.Model):
    guideWord = models.ForeignKey(GuideWord, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('Date Published')
    phaItem_cause = models.CharField(max_length =200)
    phaItem_consequence = models.CharField(max_length =200)
    phaItem_action = models.ManyToManyField(PhaAction, blank=True)
    def __str__(self):
        return self.phaItem_cause
        
class Node(models.Model):
    node_text = models.CharField(max_length =200)
    phaItems = models.ManyToManyField(PhaItem, blank=True)
    def __str__(self):
        return self.node_text
        
class PhaStudy(models.Model):
    nodes =  models.ManyToManyField(Node)
    particpants = models.ManyToManyField(Participant, blank=True)
    name = models.CharField(max_length =200)
    Hiearchy = models.ForeignKey(Hierachy, on_delete=models.CASCADE)


        

        
