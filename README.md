# RealEstate-Price-Prediction02
This project, "HouseWise," is a web application built with Django that leverages machine learning to predict house prices. It integrates web scraped data from Makaan.com to train a Multiple Linear Regression model, providing users with an estimated property value based on various features.

**Key Features:**

  * **Web Scraping (Makaan.com):** The project includes functionality to scrape real estate data from Makaan.com, gathering essential features for house price prediction.
  * **Data Preprocessing:** The scraped dataset undergoes cleaning and preprocessing to ensure data quality and suitability for model training.
  * **Machine Learning Model:** A Multiple Linear Regression model is trained on the preprocessed data to identify relationships between house features and their prices.
  * **Django Web Application:**
      * **User Interface:** The application provides a user-friendly interface using Django templates, allowing users to input property details for prediction.
      * **Price Prediction:** Users can submit property specifications, and the trained model will provide an estimated house price.
      * **Authentication (Login/Signup):** The system includes user authentication features, allowing users to register and log in to access the prediction service.
      * **Styling:** Responsive and modern design is achieved using CSS, ensuring a consistent experience across different devices. [cite\_start](See `styles.css`, `price_predictor.css`, and `style.css` for styling details)[cite: 1, 2].
  * **Interactive Elements:** The landing page features a typewriter effect using JavaScript to display a welcome message, enhancing user engagement.

**Technologies Used:**

  * **Django:** Web framework for building the application.
  * **Python:** Programming language used for backend logic, web scraping, and machine learning.
  * **Scikit-learn:** Python library for implementing the Multiple Linear Regression model.
  * **Beautiful Soup/Scrapy (Implied):** For web scraping Makaan.com (specific library not explicitly stated in provided files but implied by "web scraped from makaan.com").
  * **HTML/CSS/JavaScript:** For the front-end user interface and interactive elements.
      * [cite\_start]`styles.css`: Handles the overall layout, navigation bar, and video background[cite: 1].
      * [cite\_start]`price_predictor.css`: Styles the form container, input labels, dropdowns, and buttons for the price prediction interface[cite: 2].
      * `style.css`: Provides general styling for login, signup, home, and result containers, including alert messages and result display.
      * `scripts.js`: Implements the typewriter effect for the welcome message on the landing page.

**Setup Instructions:**

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd HouseWise
    ```
2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt # (assuming a requirements.txt file exists with Django, scikit-learn, etc.)
    ```
4.  **Database Setup:**
      * Configure your database settings in Django's `settings.py`.
      * Run migrations:
        ```bash
        python manage.py makemigrations
        python manage.py migrate
        ```
5.  **Run the web scraping script:**
      * Execute the script responsible for scraping data from Makaan.com and saving it for model training.
6.  **Train the model:**
      * Run the Python script that trains the Multiple Linear Regression model using the scraped dataset.
7.  **Run the Django development server:**
    ```bash
    python manage.py runserver
    ```
8.  Access the application in your browser at `http://127.0.0.1:8000`.

**Project Structure (Expected):**

  * `manage.py`
  * `HouseWise/` (main Django project directory)
      * `settings.py`
      * `urls.py`
      * ...
  * `price_prediction_app/` (Django app for prediction logic)
      * `views.py` (contains prediction logic)
      * `models.py`
      * `templates/` (Django templates)
          * `price_predictor.html`
          * `login.html`
          * `signup.html`
          * `home.html`
          * `result.html`
          * ...
      * `static/`
          * `css/`
              * [cite\_start]`styles.css` [cite: 1]
              * [cite\_start]`price_predictor.css` [cite: 2]
              * `style.css`
          * `js/`
              * `scripts.js`
      * `dataset/` (directory for scraped data)
      * `ml_model/` (directory for trained model, e.g., `model.pkl`)
  * `scraper/` (separate scripts for web scraping)
  * `requirements.txt`

This project serves as a comprehensive example of building a full-stack web application with machine learning integration, from data acquisition to deployment.
