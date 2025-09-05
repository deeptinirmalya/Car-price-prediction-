import streamlit as st
import pandas as pd
import joblib
import time

ml_model = joblib.load("ford_l_model_3.pkl")
scaler = joblib.load("ford_scaler_3.pkl")
expected_columns = joblib.load("ford_column_3.pkl")
# Removes duplicates, keeps order
# ...existing code...

# print(ml_model)
# print(scaler)
# print(expected_columns)

# 'year', 'mileage', 'tax', 'mpg', 'engineSize', 'model_ C-MAX', 'model_ EcoSport', 'model_ Edge', 'model_ Escort', 'model_ Fiesta', 'model_ Focus', 'model_ Fusion', 'model_ Galaxy', 'model_ Grand C-MAX', 'model_ Grand Tourneo Connect', 'model_ KA', 'model_ Ka+', 'model_ Kuga', 'model_ Mondeo', 'model_ Mustang', 'model_ Puma', 'model_ Ranger', 'model_ S-MAX', 'model_ Streetka', 'model_ Tourneo Connect', 'model_ Tourneo Custom', 'model_ Transit Tourneo', 'model_Focus',
# 'year', 'mileage', 'tax', 'mpg', 'engineSize', 'model_ C-MAX', 'model_ EcoSport', 'model_ Edge', 'model_ Escort', 'model_ Fiesta', 'model_ Focus', 'model_ Fusion', 'model_ Galaxy', 'model_ Grand C-MAX', 'model_ Grand Tourneo Connect', 'model_ KA', 'model_ Ka+', 'model_ Kuga', 'model_ Mondeo', 'model_ Mustang', 'model_ Puma', 'model_ Ranger', 'model_ S-MAX', 'model_ Streetka', 'model_ Tourneo Connect', 'model_ Tourneo Custom', 'model_ Transit Tourneo', 'model_ Focus',

# model	year	price	transmission	mileage	fuelType	tax	mpg	engineSize

st.title("predict car price by Deepti🐦‍🔥")
st.markdown("enter the given details✒️")

year = st.number_input("chose year", 1996,2060,2000)
mileage = st.number_input("enter mileage", 1.000000, 177644.0, 60.0)
tax = st.number_input("enter tax ammount", 0.00, 580.000, 420.00)
mpg = st.number_input("enter mpg", 20.80, 201.80, 30.0)
engineSize = st.number_input("enter the engine size", 0.0, 5.0, 2.0 )
in_model = st.selectbox("model name",["Fiesta", "Focus", "Kuga", "EcoSport", "C-MAX", "Ka+", "Mondeo", "B-MAX", "S-MAX", "Grand C-MAX", "Galaxy", "Edge", "KA", "Puma", "Tourneo Custom", "Grand Tourneo Connect", "Mustang", "Tourneo Connect", "Fusion", "Streetka", "Ranger", "Escort", "Transit Tourneo", "Focus"])
transmission = st.selectbox("select transmission", ["Manual", "Automatic", "Semi-Auto"])
fuelType = st.selectbox("chose fuelType", ["Petrol", "Hybrid", "Electric", "Other"])

if st.button("predict"):
    raw_data = {
        "year": year,
        "mileage": mileage,
        "tax": tax,
        "mpg": mpg,
        "engineSize": engineSize,
        "model_ " + in_model: 1,
        "transmission_" + transmission: 1,
        "fuelType_" + fuelType: 1
    }

    input_data = pd.DataFrame([raw_data])
    # st.write(raw_data)

    for col in expected_columns:
        if col not in input_data.columns:
            input_data[col] = 0

    input_data = input_data[expected_columns]
    # st.write(input_data)

    numeric_col  = [ 'year', 'mileage', 'tax', 'mpg']

    input_data[numeric_col] = scaler.transform(input_data[numeric_col])

    result = ml_model.predict(input_data)[0]

    with st.spinner("Processing... please wait ⏳"):
        time.sleep(2)

    st.success(f"result is:=  {result}")




# ...existing code...

# if st.button("predict"):
#     raw_data = {
#         "year": year,
#         "mileage": mileage,
#         "tax": tax,
#         "mpg": mpg,
#         "engineSize": engineSize,
#     }

#     # Add all possible model columns, set 1 for selected, 0 for others
#     for model_col in [col for col in expected_columns if col.startswith("model_")]:
#         raw_data[model_col] = 1 if model_col == f"model_{in_model}" else 0

#     # Add all possible transmission columns
#     for trans_col in [col for col in expected_columns if col.startswith("transmission_")]:
#         raw_data[trans_col] = 1 if trans_col == f"transmission_{transmission}" else 0

#     # Add all possible fuelType columns
#     for fuel_col in [col for col in expected_columns if col.startswith("fuelType_")]:
#         raw_data[fuel_col] = 1 if fuel_col == f"fuelType_{fuelType}" else 0

#     input_data = pd.DataFrame([raw_data])
#     st.write(input_data)

#     for col in expected_columns:
#         if col not in input_data.columns:
#             input_data[col] = 0

#     input_data = input_data[expected_columns]

#     numeric_col  = [ 'year', 'mileage', 'tax', 'mpg']
#     input_data[numeric_col] = scaler.transform(input_data[numeric_col])

#     result = ml_model.predict(input_data)[0]

#     with st.spinner("Processing... please wait ⏳"):
#         time.sleep(2)

#     st.success(f"result is:- {result}")
# # ...existing code...
