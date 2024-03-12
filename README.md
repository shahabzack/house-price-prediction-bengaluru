# house-price-prediction-bengaluru
This is my first machine learning project utilizing Linear Regression for predicting house prices in Bengaluru. Additionally, I've developed a Django web application to showcase the predictions. Explore the code and project details to delve into the process!

# Bengaluru House Price Prediction

## Overview
This project focuses on predicting house prices in Bengaluru using machine learning techniques. The dataset used for this project is collected from Kaggle, containing various features such as area, number of bedrooms, location, etc. The goal is to develop a predictive model that can accurately estimate house prices based on these features.

## Supervised Learning
The project follows a supervised learning approach, where historical data with known outcomes (house prices) is used to train a machine learning model. In this case, we employ linear regression as our predictive model, utilizing the scikit-learn library in Python.

## Dataset
The dataset used in this project is sourced from Kaggle's "Bengaluru House Price Data" repository. It consists of real estate listings in Bengaluru, India, with features like total area, number of bedrooms, location, and price. This data is explored, preprocessed, and analyzed in a Jupyter Notebook to gain insights and prepare it for model training.

## Development Environment
The project is developed using Python programming language and its various libraries:
- Jupyter Notebook for data exploration, analysis, and visualization
- scikit-learn for implementing machine learning algorithms
- Django web framework for building the web application

## Project Structure
The project directory is organized as follows:
- `data/`: Contains the dataset files.
- `notebooks/`: Includes Jupyter Notebook files for data exploration and model training.
- `webapp/`: Django web application directory.
- `README.md`: This file providing an overview of the project.

## Installation and Setup
To set up the project locally, follow these steps:
1. Clone the repository: `git clone https://github.com/your-username/bengaluru-house-price-prediction.git`
2. Navigate to the project directory: `cd bengaluru-house-price-prediction`
3. Install dependencies: `pip install -r requirements.txt`
4. Run the Django development server: `python manage.py runserver`
5. Access the web application in your browser: `http://localhost:8000`

## Usage
1. After setting up the project, navigate to the web application's URL in your browser.
2. Enter the required details such as area, number of bedrooms, and location.
3. Click on the "Predict" button to view the estimated house price based on the input data.
4. Explore different features and scenarios to understand how the model behaves.

## Demo
For a live demo of the web application, visit [Demo Link](#) (Replace with your demo link if available).

## Contributing
Contributions to the project are welcome! If you have any ideas for improvements or find any issues, please open an issue or submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgments
- Kaggle for providing the Bengaluru House Price dataset.
- The scikit-learn development team for their excellent machine learning library.
- Django community for the powerful web framework.
