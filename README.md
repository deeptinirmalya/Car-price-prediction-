🚀 Project Title & Tagline
=========================
### **Ford Vehicle Price Predictor** 🚗
> Predicting the prices of Ford vehicles with precision and accuracy, making informed purchasing decisions easier for customers 📊

📖 Description
-------------
The Ford Vehicle Price Predictor is a Python-based project that utilizes machine learning algorithms to predict the prices of Ford vehicles. This project aims to provide an accurate and reliable tool for customers to determine the prices of Ford vehicles based on various factors such as model, year, mileage, and condition. The project uses a pre-trained machine learning model, which is loaded using the `joblib` library, to make predictions on new, unseen data.

The project is built using the Streamlit framework, which allows for the creation of interactive web applications with ease. The application takes in user input for various features of the vehicle, such as model, year, mileage, and condition, and then uses the pre-trained model to predict the price of the vehicle. The predicted price is then displayed to the user in a user-friendly format.

The Ford Vehicle Price Predictor project has numerous applications in the automotive industry, including helping customers make informed purchasing decisions, assisting dealerships in pricing their vehicles competitively, and providing a tool for insurance companies to determine the value of vehicles. With its robust machine learning model and user-friendly interface, the Ford Vehicle Price Predictor is an essential tool for anyone involved in the automotive industry 🚗

📖 Additional Description
------------------------
The project code is well-structured and concise, making it easy to understand and modify. The `app.py` file is the main entry point of the application, where the Streamlit app is created and the machine learning model is loaded. The model is loaded using the `joblib` library, which allows for the loading of pre-trained models and other Python objects. The `expected_columns` variable is used to store the expected columns of the input data, which is used to ensure that the input data is in the correct format.

The project also includes a `ford_l_model_3.pkl` file, which contains the pre-trained machine learning model, and a `ford_scaler_3.pkl` file, which contains the scaler used to scale the input data. The `ford_column_3.pkl` file contains the expected columns of the input data, which is used to ensure that the input data is in the correct format. These files are loaded using the `joblib` library and are used to make predictions on new, unseen data.

📖 Conclusion
--------------
In conclusion, the Ford Vehicle Price Predictor is a powerful tool that uses machine learning algorithms to predict the prices of Ford vehicles. With its user-friendly interface and robust machine learning model, the project is an essential tool for anyone involved in the automotive industry. The project code is well-structured and concise, making it easy to understand and modify. The project has numerous applications in the automotive industry, including helping customers make informed purchasing decisions, assisting dealerships in pricing their vehicles competitively, and providing a tool for insurance companies to determine the value of vehicles.

✨ Features
---------
The following are some of the key features of the Ford Vehicle Price Predictor project:

1. **Pre-trained Machine Learning Model**: The project uses a pre-trained machine learning model to make predictions on new, unseen data.
2. **User-friendly Interface**: The project has a user-friendly interface that allows users to input various features of the vehicle and view the predicted price.
3. **Streamlit Framework**: The project is built using the Streamlit framework, which allows for the creation of interactive web applications with ease.
4. **Joblib Library**: The project uses the `joblib` library to load the pre-trained machine learning model and other Python objects.
5. **Pandas Library**: The project uses the `pandas` library to handle and manipulate data.
6. **Scikit-learn Library**: The project uses the `scikit-learn` library to build and train the machine learning model.
7. **Interactive Web Application**: The project creates an interactive web application that allows users to input various features of the vehicle and view the predicted price.
8. **Real-time Predictions**: The project makes predictions in real-time, allowing users to view the predicted price as soon as they input the various features of the vehicle.

🧰 Tech Stack Table
-------------------
| Technology | Description |
| --- | --- |
| **Frontend** | Streamlit |
| **Backend** | Python |
| **Machine Learning Library** | Scikit-learn |
| **Data Manipulation Library** | Pandas |
| **Model Loading Library** | Joblib |
| **Web Framework** | Streamlit |

📁 Project Structure
-------------------
The project structure is as follows:
```markdown
ford-vehicle-price-predictor/
|-- app.py
|-- ford_l_model_3.pkl
|-- ford_scaler_3.pkl
|-- ford_column_3.pkl
|-- requirements.txt
|-- README.md
```
* `app.py`: The main entry point of the application, where the Streamlit app is created and the machine learning model is loaded.
* `ford_l_model_3.pkl`: The pre-trained machine learning model used to make predictions.
* `ford_scaler_3.pkl`: The scaler used to scale the input data.
* `ford_column_3.pkl`: The expected columns of the input data.
* `requirements.txt`: The file containing the dependencies required to run the project.
* `README.md`: The file containing the documentation and instructions for the project.

⚙️ How to Run
-------------
To run the project, follow these steps:

1. **Install Dependencies**: Install the dependencies required to run the project by running `pip install -r requirements.txt` in the terminal.
2. **Load Model**: Load the pre-trained machine learning model by running `joblib.load("ford_l_model_3.pkl")` in the Python interpreter.
3. **Create Streamlit App**: Create the Streamlit app by running `streamlit run app.py` in the terminal.
4. **View App**: View the app by navigating to `http://localhost:8501` in the web browser.
5. **Input Features**: Input the various features of the vehicle, such as model, year, mileage, and condition, to view the predicted price.

🧪 Testing Instructions
---------------------
To test the project, follow these steps:

1. **Test Model**: Test the pre-trained machine learning model by running `joblib.load("ford_l_model_3.pkl")` in the Python interpreter and making predictions on new, unseen data.
2. **Test App**: Test the Streamlit app by running `streamlit run app.py` in the terminal and viewing the app in the web browser.
3. **Test Input Features**: Test the input features by inputting various features of the vehicle and viewing the predicted price.

📸 Screenshots
-------------
<img width="1813" height="908" alt="Image" src="https://github.com/user-attachments/assets/7a57dc2d-b5c9-45b1-9120-6095e71f3335" />


📦 API Reference
----------------
The API reference for the project is as follows:
```python
import streamlit as st
import pandas as pd
import joblib

# Load model
ml_model = joblib.load("ford_l_model_3.pkl")
scaler = joblib.load("ford_scaler_3.pkl")
expected_columns = joblib.load("ford_column_3.pkl")

# Create Streamlit app
st.title("Ford Vehicle Price Predictor")

# Input features
st.write("Input features:")
model = st.selectbox("Model", ["Mustang", "F-150", "Explorer"])
year = st.slider("Year", 2010, 2022, 2020)
mileage = st.slider("Mileage", 0, 100000, 50000)
condition = st.selectbox("Condition", ["Excellent", "Good", "Fair"])

# Make prediction
if st.button("Predict"):
    # Create input data
    input_data = pd.DataFrame({"model": [model], "year": [year], "mileage": [mileage], "condition": [condition]})

    # Scale input data
    scaled_input_data = scaler.transform(input_data)

    # Make prediction
    prediction = ml_model.predict(scaled_input_data)

    # Display prediction
    st.write("Predicted price:", prediction)
```
👤 Author
-------
The author of the Ford Vehicle Price Predictor project is Deeptinirmalya 🙋‍♂️

📝 License
-------
The Ford Vehicle Price Predictor project is licensed under the [MIT License](https://opensource.org/licenses/MIT) 📄
