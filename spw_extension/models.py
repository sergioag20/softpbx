# -*- coding:utf-8 -*-
from django.db import models
import choices


class GroupExtension(models.Model):
    """ This class will be responsable of storing the group of extensions """
    spw_group_name = models.CharField(u'Group name', max_length=80, unique=True)
    spw_group_type = models.IntegerField(u'Group type', choices=choices.GROUP_TYPE)

    def __unicode__(self):
        return self.spw_group_name


class Extension(models.Model):
    """ Class that will hold the extensions informations """
    spw_display_name = models.CharField(u'Display name', max_length=80, unique=True, db_index=True)
    spw_username = models.IntegerField(u'Username', unique=True)
    spw_passwd = models.CharField(u'Password', max_length=80)
    spw_email = models.EmailField(u'E-mail', max_length=150, blank=True, null=True)
    spw_call_group = models.ForeignKey(GroupExtension, related_name='call_group')
    spw_pickup_group = models.ForeignKey(GroupExtension, related_name='pick_up_group')
    spw_active = models.BooleanField(u'Active', default=True)
    # @ TODO --> Verificar heritage (Campo que herda as permissões de acordo com o grupo selecionado)

    def __unicode__(self):
        return "[ " + self.spw_display_name + " ] - " + str(self.spw_username)

    class Meta:
        verbose_name = u'Extension'
        verbose_name_plural = u'Extension'
        db_table = 'spw_ramais'
