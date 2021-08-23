from . import src
from flask import render_template, request
from .helpers import get_distance_to_mkad, get_coordinates

'''Route to the success page'''
@src.route("/success", methods=['POST'])
def success():
    if request.method == 'POST':
        print(request)
        # Extract the address form input
        address = request.form['address']
        
        # Call function to get the coordinates
        coordinates, number_of_results_found = get_coordinates(address)

        # Conditional to check if the geocoder found any result
        if number_of_results_found == 0:
            return render_template('index.html', text="Sorry, we didn't find any address")

        # Call function to calculate the distance
        distance = get_distance_to_mkad(coordinates)

        # Render the success page and pass the distance to the context
        return render_template('success.html', distance=distance)

    return render_template('index.html')
