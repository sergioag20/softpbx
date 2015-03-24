# -*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.template import RequestContext
from django.http import HttpResponse

from spw_extension.forms import ExtensionForm
from spw_extension.models import Extension

"""
    @TODO LIST:
    All views should and would be login required.
    Loggin routine.
    Finish deletion action on datatable.
    Still only showing the confirm box =D
    spw_display_name should accept only numbers if language = pt-br (To confirm yet!)
"""


def add_extension(request):
    """
        Add a extension to the database.
        If request.method == POST, that means that we are sending something to be saved.
        If form.is_valid() than, we save the data and return the user to an empty form, just in case he wants to add more extensions.
        If not valid, we show to the user which input are invalid and why.

        If not request.method == POST we show an empty form to the user put his data.
        @TODO --> login_required
    """
    if request.method == 'POST':
        form = ExtensionForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)
            message = "Extension saved!"
            form = ExtensionForm()
        else:
            message = "An error ocurred!"
    else:
        form = ExtensionForm()
    return render_to_response('spw_extension/add_extension.html', locals(), context_instance=RequestContext(request))


def edit_extension(request, extension_id):
    """
        Edit an existend extension that will be searched by extension_id parameter.
        If it exists, we will return the same form used to add a new extension but we will pass the instance (ext) to the form.
        That way, the form will be displayed with all data of the desired extension.

        if form.is_valid() we save the updated info and redirect the user to the previous view (list-extension).
        if not, we show errors (@TODO --> Not tested.)

        If not a post, we are beginning to edit, so show the form with original data.
        @TODO --> login_required
    """
    ext = get_object_or_404(Extension, pk=extension_id)
    if request.method == 'POST':
        form = ExtensionForm(request.POST, instance=ext)
        if form.is_valid():
            form.save()
            return redirect('list-extension')
        else:
            messages = "Error. Check the values and try again."
    else:
        form = ExtensionForm(instance=ext)
    return render_to_response('spw_extension/add_extension.html', locals(), context_instance=RequestContext(request))


def change_status_extension(request, extension_id):
    """
        Change to True or False the values of spw_active depending on previous value.
        After saving, redirects to list-extension url and show the table with all data.
        @TODO --> login_required
    """
    ext = get_object_or_404(Extension, pk=extension_id)
    if ext:
        if ext.spw_active:
            ext.spw_active = False
        else:
            ext.spw_active = True
        ext.save()
    return redirect('list-extension')


def list_extension(request):
    """
        Get all extensions and show a data table that can be: 
        1 - Ordered
        2 - searched
        @TODO --> login_required
    """
    ext = Extension.objects.all()
    return render_to_response('spw_extension/list_extensions.html', locals(), context_instance=RequestContext(request))
