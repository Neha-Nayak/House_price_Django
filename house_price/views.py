from django.shortcuts import render, HttpResponse
import numpy as np
import json, pickle, pandas as pd
from .models import Predict

# Create your views here.
    
global __data_columns
def predict(request):
    model = pd.read_pickle(r"./banglore_home_prices_model.pickle")
    with open("./columns.json", 'r')as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]
    context={'location':__locations}
    if request.method=="POST":
        location=request.POST.get('location')
        area=int(request.POST.get('area'))
        size=int(request.POST.get('size'))
        bathroom=int(request.POST.get('bathroom'))
        
        try:
            loc_index = __data_columns.index(location.lower())
        except:
            loc_index = -1

        x = np.zeros(len(__data_columns))
        x[0] = area
        x[1] = bathroom
        x[2] = size
        if loc_index >= 0:
            x[loc_index] = 1
        result = round(model.predict([x])[0],2)
        print (result)
        # classification = result[0]

        # Predict.objects.create(location=location,area=area,size=size,bathroom=bathroom, classification=classification)
        # context={'result': result, 'location': __locations,'area': area, 'size': size, 'bathroom': bathroom}
        return render(request,'predict.html',{'result': result, 'location': __locations,'area': area, 'size': size, 'bathroom': bathroom})
    return render(request,'predict.html',{'location':__locations})

# def get_estimated_price(location, sqft, bhk, bath):
#     print(location, sqft, bhk, bath)
#     try:
#         loc_index = __data_columns.index(location.lower())
#     except:
#         loc_index = -1

#     x = np.zeros(len(__data_columns))
#     x[0] = sqft
#     x[1] = bath
#     x[2] = bhk
#     if loc_index >= 0:
#         x[loc_index] = 1
#     price=round(__model.predict([x])[0], 2)
#     return price
# def get_location_names():
#     return __locations

# def load_saved_artifacts():
#     global __locations
#     global __data_columns
    # with open("columns.json", 'r')as f:
    #     __data_columns = json.load(f)['data_columns']
    #     __locations = __data_columns[3:]
    # global __model
    # with open("banglore_home_prices_model.pickle", 'rb') as f:
    #     __model = pickle.load(f)

# load_saved_artifacts()