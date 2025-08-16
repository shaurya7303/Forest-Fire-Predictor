🌲 Forest Fire Prediction – Flask Web App

A Machine Learning + Flask application that predicts the risk of forest fires in Algeria based on environmental parameters such as temperature, humidity, wind speed, and more.
The model is trained using the Algerian Forest Fires Dataset, with preprocessing, EDA, and model building included in the project.

🚀 Features

Interactive Web Form – Input environmental conditions and get instant predictions.

Real-Time Prediction – Uses a trained Linear Regression model.

Risk Level Display – Shows whether the fire risk is High or Low with animated visuals.

Data Science Pipeline – Includes dataset cleaning, exploratory data analysis, and model training notebooks.

Responsive UI – Works across devices.

📂 Project Structure
.
├── application.py                      # Flask app for fire prediction
├── requirements.txt                     # All dependencies
├── Algerian_forest_fires_dataset.csv    # Original dataset
├── Algerian_forestfires_cleaned.csv     # Cleaned dataset after preprocessing
├── eda.ipynb                            # Exploratory Data Analysis
├── model.ipynb                          # Model training & saving
├── models/
│   ├── linear.pkl                       # Saved trained Linear Regression model
│   ├── scaler.pkl                       # Saved StandardScaler object
├── templates/
│   ├── index.html                       # User input form page
│   ├── home.html                        # Prediction result page

⚙️ Installation & Setup

1️⃣ Clone the repository

git clone https://github.com/shaurya7303/forest-fire-predictor.git
cd forest-fire-prediction


2️⃣ Create a virtual environment

python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows


3️⃣ Install dependencies

pip install -r requirements.txt


4️⃣ Run the Flask app

python application.py


5️⃣ Open in browser

http://127.0.0.1:5000

📊 Input Parameters
Parameter	Description
Temperature (°C)	Ambient temperature
Relative Humidity (%)	Air moisture content
Wind Speed (km/h)	Wind flow rate
Rain (mm)	Rainfall amount
DMC	Duff Moisture Code
ISI	Initial Spread Index
Classes	Fire class category
Region	Region code
🧠 Machine Learning Workflow

Data Collection – Algerian Forest Fires Dataset.

Data Cleaning – Removal of missing/invalid values, formatting.

EDA (eda.ipynb) – Visualization and statistical insights.

Feature Scaling – StandardScaler used for normalization.

Model Training (model.ipynb) – Linear Regression model trained and saved as .pkl.

Deployment – Flask app integrates the model for real-time predictions.

🛠 Tech Stack

Backend: Python, Flask

Frontend: HTML, CSS

Machine Learning: scikit-learn

Data Processing: Pandas, NumPy

Visualization: Matplotlib, Seaborn

📜 License

This project is licensed under the MIT License – you are free to use and modify it
