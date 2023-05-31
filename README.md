# Stock-Price-Prediction-Using-LSTM-and-Sliding-Window
PROJECT INSTALLATION MANUAL
FOR
“SYSTEM FOR PREDICTION OF STOCK PRICE PREDICTION USING 6-LAYER STACKED LSTM AND SLIDING WINDOW APPROACH”

The following detailed installation manual provides step-by-step instructions to set up and deploy the Stock Price Prediction Website, which includes the backend LSTM model and the frontend Streamlit web application. Please follow these instructions carefully to ensure a successful installation.

Prerequisites:
1.	Python 3.7 or higher installed on your system.
2.	Anaconda or Mini-conda installed for managing Python environments (optional but recommended).

Step 1: Clone the Project Repository
1.	Open a command prompt or terminal.
2.	Navigate to the directory where you want to clone the project repository.
3.	Run the following command to clone the repository:

   ```
   git clone <https://github.com/SuhasiGadge/Stock-Price-Prediction-Using-LSTM-and-Sliding-Window>
   ```
   Alternatively, you can download the project source code as a ZIP file and extract it to your desired directory.

Step 2: Set Up Python Environment
1.	Open a command prompt or terminal.
2.	Navigate to the project directory:


   ```
   cd stock-price-prediction-website
   ```
3.	(Optional) Create a new conda environment (recommended):
   ```
   conda create -n stock_prediction_env python=3.7
   conda activate stock_prediction_env
   ```
   Note: If you are not using conda, create and activate a virtual environment using your preferred method.

Step 3: Install Required Dependencies
1.	Ensure you are in the project directory with the activated Python environment.
2.	Run the following command to install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

Step 4: Download Pretrained LSTM Model Weights
1.	Download the pretrained LSTM model weights (in .h5 format) from the provided source.
2.	Place the downloaded model weights file inside the project directory.

Step 5: Start the Web Application
1.	Ensure you are in the project directory with the activated Python environment.
2.	Run the following command to start the Streamlit web application:
   ```
   streamlit run app.py
   ```

3.	After executing the command, the web application will start running.
4.	Open your web browser and navigate to the displayed local URL (usually http://localhost:8501).
a)	The first page will show the prediction for the next 5 days, along with graphs and tables for predicted prices and moving averages.
b)	he second page will provide an overview of the selected stock symbol, displaying historical prices and additional company data.
c)	The third page will offer hyperlinks to other important websites related to the stock market.
d)	The last page will contain a contact form for users to submit suggestions or queries.

Congratulations! You have successfully installed and deployed the Stock Price Prediction Website. You can now explore the various functionalities and features provided by the web application.

Note: Make sure to update the model weights periodically to incorporate the latest training data and improve prediction accuracy.
