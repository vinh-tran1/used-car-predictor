from flask import Flask, request, jsonify, make_response, render_template, abort
import database as db
import pandas as pd
# Instantiate Flask App
#-----------------------------------------------------------------------
app = Flask(__name__, template_folder='./templates')
#-----------------------------------------------------------------------

# ROUTES
#-----------------------------------------------------------------------
@app.route('/', methods=['GET'])
def search_form():
    """ GET request
        render search form that takes in user input
    """

    error_msg = request.args.get('error_msg', '')
    html = render_template('index.html', error_msg=error_msg)
    response = make_response(html)

    return response

@app.route('/search', methods=['GET'])
def search_results():
    try:
        # get user input parameters
        user_params = request.args

        # separate valid and invalid query parameters
        user_params_dict = {param: user_params.get(param, '') for param in user_params}

        # get individual parameters from the valid ones
        brand = user_params_dict.get('brand', '')
        model = user_params_dict.get('model', '')
        age = user_params_dict.get('age', '')
        milage = user_params_dict.get('milage', '')
        horsepower = user_params_dict.get('horsepower', '')
        engine = user_params_dict.get('engine', '')
        fuel = user_params_dict.get('fuel', '')
        transmission = user_params_dict.get('transmission', '')
        ext_color = user_params_dict.get('ext_color', '')
        int_color = user_params_dict.get('int_color', '')

        features = {
            'brand': brand,
            'model': model,
            'age': age,
            'milage': milage,
            'horsepower': horsepower,
            'engine': engine,
            'fuel': fuel,
            'transmission': transmission,
            'ext_color': ext_color,
            'int_color': int_color
        }

        # database call here
        prediction = db.predict(features)
        price = round(prediction[0], 2)

        return jsonify({'response': price})

    except SystemExit as e:
        return jsonify({'error': e})
