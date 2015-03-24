# -*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse

from spw_extension.forms import ExtensionForm


def add_extension(request):
    if request.method == 'POST':
        form = ExtensionForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            message = "Extension saved!"
            # return render_to_response('spw_extension/add_extension.html', {'message': message}, context_instance=RequestContext(request))
        else:
            # The supplied form contained errors - just print them to the terminal.
            message = "An error ocurred!"        
        return render_to_response('spw_extension/add_extension.html', locals(), context_instance=RequestContext(request))
    else:
        # If the request was not a POST, display the form to enter details.
        form = ExtensionForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    # return render_to_response('cdr/add_user.html', {'form': form}, context_instance=RequestContext(request))
    return render_to_response('spw_extension/add_extension.html', {'form': form}, context_instance=RequestContext(request))
