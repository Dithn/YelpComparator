# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.generic.simple import direct_to_template

from yelp import get_yelp_business, search_yelp
from forms import YelpBusinessForm

def home(request):
  #return HttpResponse('Hello World!')
  return direct_to_template(request, 'home.html', locals())

def search(request):
  username = "Davy Kay"
  search_results = search_yelp(
      'burritos',
      40.768056, -73.981944 # Columbus circle
      )
  businesses = search_results['businesses']
  form = YelpBusinessForm(businesses)

  return direct_to_template(request, 'search.html', locals())

def compare(request):
  print "GET request PARAMS: " + str(request.GET)
  #business_ids = request.GET['businesses']
  business_ids = request.GET.getlist('businesses')

  businesses = [ ]
  for business_id in business_ids:
    #import pdb; pdb.set_trace()
    business = get_yelp_business(business_id)
    businesses.append(business)

  return direct_to_template(request, 'compare.html', locals())
