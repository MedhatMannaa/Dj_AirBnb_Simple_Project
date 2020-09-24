from django.shortcuts import render
from .models import Unit
   
#class Meta:
#    db_table = ''
#        verbose_name=''
#        verbose_name_plural=verbose_name
#    def __str__(self):
#        return self.

# Create your views here.

def all_units(request):
	## Logic to get all units in one html page
	all_units = Unit.objects.all()
	return render(request,'unit/all_units.html' ,{'units':all_units})
		
	## unit/all_units.html = save place/html page name which saved in this place
	## units               = name which we will send to the FrontEnd
	## all_units           = Name of the Variable

def single_unit(request,id):
	## Logic to get all units in one html page
	single_unit = Unit.objects.get(id=id)
	return render(request,'unit/single_unit.html' ,{'unit':single_unit})
		
	## unit/single_unit.html = save place/html page name which saved in this place
	## unit                  = name which we will send to the FrontEnd
	## single_unit           = Name of the Variable    




