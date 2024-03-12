from django.shortcuts import render
from django.http import JsonResponse
import pickle
import json
import numpy as np

def predict_price(location, sqft, bath, bhk):
    # Load the trained model
    with open('banglore_home_prices_model.pickle', 'rb') as f:
        lr_clf = pickle.load(f)

    # Load the column names
    with open('columns.json', 'r') as f:
        columns = json.load(f)
    
    # Create an array to hold the input data
    x = np.zeros(len(columns['data_columns']))

    # Set values for known features
    x[0] = sqft
    x[1] = bath
    x[2] = bhk

    # Find the index of the location in the columns array
    loc_index = columns['data_columns'].index(location.lower())

    # If the location is found, set the corresponding index in x to 1
    if loc_index >= 0:
        x[loc_index] = 1
    
    # Make the prediction
    prediction = round( lr_clf.predict([x])[0],1)
    
    return prediction

def index(request):
    return render(request, 'index.html')

def predict(request):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        # Extract form data
        location = request.POST.get('location')
        sqft = float(request.POST.get('sqft'))
        bath = float(request.POST.get('bath'))
        bhk = float(request.POST.get('bhk'))
        
        # Call prediction function
        prediction = predict_price(location, sqft, bath, bhk)
        
        # Return JSON response with prediction
        return JsonResponse({'prediction': prediction})
    else:
        # Return JSON response indicating invalid request
        return JsonResponse({'error': 'Invalid request'})

def locations(request):
    with open('columns.json', 'r') as f:
        columns = json.load(f)
    locations = columns['data_columns'][3:]  # Exclude first 3 columns which are not locations
    return JsonResponse({'locations': locations})
