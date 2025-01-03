import streamlit as st
import pandas as pd

# Add an image at the top
st.image("C:\\Users\\USER\\Documents\\streamlit_car_price_prediction\\car.jpg", use_column_width=True)


# Title and introduction
st.title('Car Price Prediction')
st.write('Welcome to the Car Price Prediction page! Enter the required car details below to get an instant price estimate based on your inputs.')

# Define features for the car dataset
features = [
    'mileage', 'standard_colour', 'standard_make', 'standard_model',
    'vehicle_condition', 'year_of_registration', 'body_type',
    'crossover_car_and_van', 'fuel_type', 'Age', 'mileage_per_year',
    'mileage_squared', 'vehicle_age_squared', 'standard_name', 'standard_description'
]

# Input form for the user to enter car details
st.header('Enter Car Details:')
feature_inputs = {}

# Numeric inputs
feature_inputs['mileage'] = st.number_input('Mileage', min_value=0.0, step=1.0)
feature_inputs['Age'] = st.number_input('Age', min_value=0.0, step=1.0)
feature_inputs['year_of_registration'] = st.number_input('Year of Registration', min_value=1900.0, step=1.0)
feature_inputs['mileage_per_year'] = st.number_input('Mileage Per Year', min_value=0.0, step=1.0)

# Text inputs
feature_inputs['standard_colour'] = st.text_input('Standard Colour')
feature_inputs['standard_make'] = st.text_input('Standard Make')
feature_inputs['standard_model'] = st.text_input('Standard Model')
feature_inputs['vehicle_condition'] = st.text_input('Vehicle Condition')
feature_inputs['body_type'] = st.text_input('Body Type')
feature_inputs['fuel_type'] = st.text_input('Fuel Type')

# Boolean input
feature_inputs['crossover_car_and_van'] = st.selectbox('Crossover Car and Van', [True, False])

# Automatically generate derived fields
feature_inputs['mileage_squared'] = feature_inputs['mileage'] ** 2
feature_inputs['vehicle_age_squared'] = feature_inputs['Age'] ** 2
feature_inputs['standard_name'] = f"{feature_inputs['standard_make']} {feature_inputs['standard_model']}"
feature_inputs['standard_description'] = f"{feature_inputs['standard_colour']} {feature_inputs['body_type']}"

# Button to trigger prediction
if st.button('Predict'):
    # Create a DataFrame with the user's input
    user_data = pd.DataFrame({feature: [value] for feature, value in feature_inputs.items()})

    # Display the input data as a preview
    st.header('Input Data Preview:')
    st.write(user_data)

    # Simulate prediction (replace with actual model logic if available)
    try:
        # Example prediction logic (dummy implementation)
        prediction = user_data['mileage'][0] * 0.05 + user_data['Age'][0] * -100 + 20000
        st.header('Prediction Result:')
        st.write(f'The predicted price for the car is: ${prediction:,.2f}')
    except Exception as e:
        st.error(f'An error occurred during prediction: {str(e)}')
