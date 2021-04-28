# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
import sys
from django.views.decorators.csrf import csrf_exempt

from opencage.geocoder import OpenCageGeocode
from opencage.geocoder import InvalidInputError, RateLimitExceededError, UnknownError
import pandas as pd
from django.http import HttpResponse
import json
import os

@csrf_exempt
def mapLoad(request):
    map_html = 'map.html'
    return render(request,map_html)#to render the login page

@csrf_exempt
def  addressService(request): 
    key = 'deccf3b07191435ab3be48da9c0c883d'
    geocoder = OpenCageGeocode(key)
    #Reading The data from Excel
    getting_current_path = r'%s' % os.getcwd().replace('\\','/')

    df = pd.read_excel(getting_current_path+'/File/Input.xlsx')
    latitude = []
    longitude =  []
    recent_address = []
    try: 
        for single_address in df['Address']:
            address = single_address.strip()
            address_results = geocoder.geocode(address, no_annotations='1')
            if address_results and len(address_results):
                recent_address.append(address)
                latitude.append( address_results[0]['geometry']['lat'])
                longitude.append(address_results[0]['geometry']['lng'])
            else:
                sys.stderr.write("not found: %s\n" % address)
        #Creating Dataframe
        output_df = pd.DataFrame({'Address':recent_address, 'latitude': latitude,'longitude':longitude})
        #Writing DataFrame into Excel
        output_df.to_excel(getting_current_path+'/File/Output.xlsx')
        result_data =  output_df.T.to_dict().values() #Convert Datadrame into List Of Dict
    except IOError:
        print('Error: File %s does not appear to exist.' % df )
    except RateLimitExceededError as ex:
        print(ex)
    return HttpResponse(json.dumps(result_data))


