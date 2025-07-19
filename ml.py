from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import pandas as pd 
import numpy as np

# Global variables to store the trained model and ensure it's trained only once
model = None

def train_model():
    """Trains the model and stores it in the global variable."""
    global model  # Make 'model' a global variable so it can be reused later

    # Load dataset and perform preprocessing
    df = pd.read_csv("Datasets.csv")
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df[['bhks', 'per_sq_ft_area', 'price_per_sq_ft_area']])
    df[['bhks', 'per_sq_ft_area', 'price_per_sq_ft_area']] = scaled_data

    # Drop unwanted columns
    df = df.drop(['appt_name', 'appt_link', 'construction_status'], axis=1)
    df = pd.get_dummies(data=df)  # Convert categorical variables

    # Separate features and target variable
    y = df['price']
    x = df.drop('price', axis=1)

    # Split data into training and testing sets
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    # Train the model
    lr = LinearRegression()
    model = lr.fit(x_train, y_train)  # Store the trained model globally

def predict_price(user_input):
    """Predicts price based on user input."""
    global model  # Access the global model variable

    # Train the model if it hasn't been trained yet
    if model is None:
        train_model()

    # Initialize all locality values as 0
    locality_dict = {
        "bhks": 0,
        "per_sq_ft_area": 0,
        "price_per_sq_ft_area": 0,
        "locality_name_ambavadi": 0,
        "locality_name_ambli": 0,
        "locality_name_bodakdev": 0,
        "locality_name_bopal": 0,
        "locality_name_chandkheda": 0,
        "locality_name_ghatlodiya": 0,
        "locality_name_ghuma": 0,
        "locality_name_gota": 0,
        "locality_name_gurukul": 0,
        "locality_name_jagatpur": 0,
        "locality_name_jodhpur village": 0,
        "locality_name_makarba": 0,
        "locality_name_maninagar": 0,
        "locality_name_memnagar": 0,
        "locality_name_motera": 0,
        "locality_name_naroda": 0,
        "locality_name_navrangpura": 0,
        "locality_name_nikol": 0,
        "locality_name_paldi": 0,
        "locality_name_prahlad nagar": 0,
        "locality_name_ranip": 0,
        "locality_name_sanand": 0,
        "locality_name_sanathal": 0,
        "locality_name_satellite": 0,
        "locality_name_sg highway": 0,
        "locality_name_shela": 0,
        "locality_name_shilaj": 0,
        "locality_name_sola": 0,
        "locality_name_south bopal": 0,
        "locality_name_thaltej": 0,
        "locality_name_tragad": 0,
        "locality_name_vasna": 0,
        "locality_name_vastral": 0,
        "locality_name_vastrapur": 0,
        "locality_name_vejalpur": 0
    }

    # Update the dictionary with the user input
    locality_key = f"locality_name_{user_input['locality_name']}"
    if locality_key in locality_dict:
        locality_dict[locality_key] = 1
    else:
        raise ValueError(f"Locality '{user_input['locality_name']}' not found in dataset")

    # Load dataset for calculating mean values (if needed for standardization)
    df = pd.read_csv("Datasets.csv")

    # Calculate necessary statistics for standardization
    price_per_sq_ft_mean = np.array(df[(df['bhks'] == int(user_input['bhk'])) & 
                                       (df['locality_name'] == user_input['locality_name'])].price_per_sq_ft_area).mean()
    per_sq_ft_area_mean = df[(df['bhks'] == user_input['bhk'])&(df['locality_name']==user_input['locality_name'])].per_sq_ft_area.mean()

    # Standardize the input values
    bhk_scaled = (user_input['bhk'] - df['bhks'].min()) / (df['bhks'].max() - df['bhks'].min())
    per_sq_ft_area_scaled = (per_sq_ft_area_mean - df['per_sq_ft_area'].min()) / (df['per_sq_ft_area'].max() - df['per_sq_ft_area'].min())
    price_per_sq_ft_scaled = (price_per_sq_ft_mean - df['price_per_sq_ft_area'].min()) / (df['price_per_sq_ft_area'].max() - df['price_per_sq_ft_area'].min())

    # Update standardized values in the dictionary
    locality_dict["bhks"] = bhk_scaled
    locality_dict["per_sq_ft_area"] = per_sq_ft_area_scaled
    locality_dict["price_per_sq_ft_area"] = price_per_sq_ft_scaled

    # Convert the dictionary into a DataFrame for prediction
    input_df = pd.DataFrame([locality_dict])

    # Use the trained model to predict
    return model.predict(input_df)[0]  # Return the predicted price

# Example usage
user_input = {
    'bhk': 3,
    'locality_name': 'bopal'
}
result = predict_price(user_input)
print(f"Predicted price: {result}")
