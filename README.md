# 🌬️ Air Quality Index Web Application

-----

## ✨ Project Overview

This project is a simple web application that allows users to check the **Air Quality Index (AQI)** for their current location. It leverages the **OpenWeatherMap API** to fetch real-time air pollution data and presents it through a user-friendly interface. The application provides the overall AQI, specific pollutant levels (PM2.5, PM10), and a health message based on the air quality status.

-----

## 🚀 Features

  * **Location-Based AQI:** Automatically detects the user's latitude and longitude to fetch localized air quality data.
  * **Real-time Data:** Displays current AQI, PM2.5, and PM10 values.
  * **Health Recommendations:** Provides a simple message indicating whether it's advisable to wear a mask based on the AQI level.
  * **Responsive Design:** A basic responsive layout to ensure usability across different devices.
  * **Clear Status Indicators:** Uses color-coded status messages to quickly convey air quality levels.

-----

## 🛠️ Technologies Used

The project is built using a **Flask** backend for handling API requests and serving the frontend, and a **pure HTML, CSS, and JavaScript** frontend for the user interface.

  * **Backend:**
      * **Python 3:** The programming language for the server.
      * **Flask:** A micro web framework for Python.
      * **Requests:** A Python library for making HTTP requests to external APIs.
      * **`os` module:** Used to access environment variables for API keys.
  * **Frontend:**
      * **HTML5:** Structures the web page content.
      * **CSS3:** Styles the application for a clean and intuitive look.
      * **JavaScript:** Handles user interaction, geolocation, and fetching data from the backend API.
      * **Web Geolocation API:** Used to get the user's current location.
      * **Fetch API:** For asynchronous communication with the Flask backend.
  * **External API:**
      * **OpenWeatherMap Air Pollution API:** Provides the air quality data.

-----

## ⚙️ Installation

To set up and run this project on your local machine, follow these steps:

### Prerequisites

  * **Python 3.x** installed.
  * **`pip`** (Python package installer) installed.
  * An **OpenWeatherMap API Key**. You can obtain one by signing up at [OpenWeatherMap](https://openweathermap.org/api).

### Steps

1.  **Clone the repository (or save the files):**
    If you have a Git repository, clone it:

    ```bash
    git clone <https://github.com/Omkar-Kashid23/AQI-Air-Quality-Index->
    cd <repository-directory>
    ```

    Otherwise, create a project folder (e.g., `air_quality_app`) and save the backend Python code as `app.py` and the frontend HTML code as `templates/index.html`. Also, create a `static` folder inside your project directory. The HTML references an image `138631.jpg` in the `static` folder. You'll need to place a placeholder image there or remove the `background` property from the CSS in `index.html`.

2.  **Install Python dependencies:**
    Open your terminal or command prompt, navigate to the project's root directory (where `app.py` is located), and install the required libraries:

    ```bash
    pip install Flask requests
    ```

3.  **Set up your OpenWeatherMap API Key:**
    The Flask application expects the API key to be set as an environment variable named `OPENWEATHER_API_KEY`.

      * **On Linux/macOS:**
        ```bash
        export OPENWEATHER_API_KEY="YOUR_OPENWEATHER_API_KEY_HERE"
        ```
      * **On Windows (Command Prompt):**
        ```cmd
        set OPENWEATHER_API_KEY="YOUR_OPENWEATHER_API_KEY_HERE"
        ```
      * **On Windows (PowerShell):**
        ```powershell
        $env:OPENWEATHER_API_KEY="YOUR_OPENWEATHER_API_KEY_HERE"
        ```

    **Note:** Replace `"YOUR_OPENWEATHER_API_KEY_HERE"` with your actual API key. For persistent environment variables, refer to your operating system's documentation.

4.  **Run the Flask application:**
    From the project's root directory, execute:

    ```bash
    python app.py
    ```

    You should see output indicating that the Flask development server is running, typically on `http://127.0.0.1:5000/`.

-----

## 🏃‍♀️ Usage

1.  **Open your web browser** and navigate to the address provided by the Flask server (e.g., `http://127.0.0.1:5000/`).
2.  The application will prompt you to **allow location access**. Grant permission for the app to fetch your coordinates.
3.  The AQI data for your current location will be displayed.
4.  Click the **"Refresh Data"** button to update the air quality information.

-----

## 🤝 Contributing

Contributions, issues, and feature requests are welcome\! Feel free to check the [issues page](https://www.google.com/search?q=https://github.com/your-username/your-repo/issues) (if applicable) or open a new one.

-----

## 📄 License

This project is open-source and available for everyone

-----

## 📧 Contact

For any questions or feedback, please reach out.
