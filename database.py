import joblib
import pandas as pd

# global vars
encoder = joblib.load('model/target_encoder.pkl')
model = joblib.load('model/regression_model.pkl')

def predict(X):
    encode_map = {
        'brand': X['brand'],
        'model': X['model'],
        'fuel_type': X['fuel'],
        'transmission': X['transmission'],
        'ext_col': X['ext_color'],
        'int_col': X['int_color']
    }

    non_encoded = {
        'age': X['age'],
        'milage': X['milage'],
        'horsepower': X['horsepower'],
        'engine_displacement': X['engine']
    }

    input_encoded_df = pd.DataFrame([encode_map])
    encoded_df = encoder.transform(input_encoded_df)
    non_encoded_df = pd.DataFrame([non_encoded])

    df = pd.concat([encoded_df, non_encoded_df], axis=1)
    predicted_price = model.predict(df)
    return predicted_price