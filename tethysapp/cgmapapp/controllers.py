from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tethys_sdk.gizmos import Button
from tethys_sdk.gizmos import ToggleSwitch
from tethys_sdk.gizmos import RangeSlider

@login_required()
def home(request):
    """
    Controller for the app home page.
    """
    save_button = Button(
        display_text='',
        name='save-button',
        icon='glyphicon glyphicon-floppy-disk',
        style='success',
        attributes={
            'data-toggle':'tooltip',
            'data-placement':'top',
            'title':'Save'
        }
    )

    edit_button = Button(
        display_text='',
        name='edit-button',
        icon='glyphicon glyphicon-edit',
        style='warning',
        attributes={
            'data-toggle':'tooltip',
            'data-placement':'top',
            'title':'Edit'
        }
    )

    remove_button = Button(
        display_text='',
        name='remove-button',
        icon='glyphicon glyphicon-remove',
        style='danger',
        attributes={
            'data-toggle':'tooltip',
            'data-placement':'top',
            'title':'Remove'
        }
    )

    previous_button = Button(
        display_text='Previous',
        name='previous-button',
        attributes={
            'data-toggle':'tooltip',
            'data-placement':'top',
            'title':'Previous'
        }
    )

    next_button = Button(
        display_text='Next',
        name='next-button',
        attributes={
            'data-toggle':'tooltip',
            'data-placement':'top',
            'title':'Next'
        }
    )

    context = {
        'save_button': save_button,
        'edit_button': edit_button,
        'remove_button': remove_button,
        'previous_button': previous_button,
        'next_button': next_button
    }


    return render(request, 'cgmapapp/home.html', context)

def about(request):
    context = {

    }

    return render(request, 'cgmapapp/about.html', context)


def dataservices(request):
    context = {

    }

    return render(request, 'cgmapapp/dataservices.html', context)


def mapview(request):

    utah_roads = ToggleSwitch(display_text='Utah Roads:',
                              name='utah_roads',
                              on_label='Yes',
                              off_label='No',
                              on_style='success',
                              off_style='danger',
                              initial=True,
                              attributes={'onchange':'toggle_roads();'})

    utah_dem = ToggleSwitch(display_text='Utah DEM:',
                            name='utah_dem',
                            on_label='Yes',
                            off_label='No',
                            on_style='success',
                            off_style='danger',
                            initial=True,
                            attributes={'onchange':'toggle_dem()'})

    context = {
        'utah_roads': utah_roads,
        'utah_dem': utah_dem,
    }

    return render(request, 'cgmapapp/mapview.html', context)

def proposal(request):

    brc_button = Button(
        display_text='Bike Report Card',
        name='brc-button',
        style='info',
        attributes={
            'onclick': 'brc();'
    }
    )

    context = {
        'brc_button': brc_button,
    }

    return render(request, 'cgmapapp/proposal.html', context)


def mockup(request):
    slider_grade = RangeSlider(display_text='Desired Average Grade (ft/ft)',
                          name='slider_grade',
                          min=0.0001,
                          max=2,
                          initial=0.1,
                          step=0.0001,
                          attributes={
                              'onchange': 'get_grade_value();'
                          })

    context = {
        'slider_grade': slider_grade,
    }

    return render(request, 'cgmapapp/mockup.html', context)
