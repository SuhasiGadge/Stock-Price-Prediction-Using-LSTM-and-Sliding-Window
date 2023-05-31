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


# WebApp Screenshots:

## WebApp Page 01: Main Prediction Page


![image](https://github.com/SuhasiGadge/Stock-Price-Prediction-Using-LSTM-and-Sliding-Window/assets/97603532/bb27346a-191f-4f46-ba4a-c4b13600b8fd)


![image](https://github.com/SuhasiGadge/Stock-Price-Prediction-Using-LSTM-and-Sliding-Window/assets/97603532/9095bfda-a642-4843-b3d7-ec606f2ab677)


![image](https://github.com/SuhasiGadge/Stock-Price-Prediction-Using-LSTM-and-Sliding-Window/assets/97603532/baacfef2-97c7-4553-b3e2-dfb3474e0678)


![image](https://github.com/SuhasiGadge/Stock-Price-Prediction-Using-LSTM-and-Sliding-Window/assets/97603532/4618cd3c-c856-4865-af4b-5699c0cbef2a)



## WebApp Page 02: Overview of Selected Stock Symbol

![image](https://github.com/SuhasiGadge/Stock-Price-Prediction-Using-LSTM-and-Sliding-Window/assets/97603532/ff49248c-b5cf-4cd0-a67d-45afc7bebf39)


![image](https://github.com/SuhasiGadge/Stock-Price-Prediction-Using-LSTM-and-Sliding-Window/assets/97603532/0dc93a71-e9de-4ee2-b32c-300940a71e23)


![image](https://github.com/SuhasiGadge/Stock-Price-Prediction-Using-LSTM-and-Sliding-Window/assets/97603532/73e24be9-fa3d-4383-9bf2-4fa35edcde96)

 

## WebApp Page 03: Resource Hub

![image](https://github.com/SuhasiGadge/Stock-Price-Prediction-Using-LSTM-and-Sliding-Window/assets/97603532/f9df7cdb-7c67-49e0-acfb-d5fc255519f8)


![image](https://github.com/SuhasiGadge/Stock-Price-Prediction-Using-LSTM-and-Sliding-Window/assets/97603532/71dc2cdd-becf-45e3-b3dd-f49c0f979e43)


![image](https://github.com/SuhasiGadge/Stock-Price-Prediction-Using-LSTM-and-Sliding-Window/assets/97603532/822c2683-bfc8-42bf-bea9-605ca02e9c6e)


## WebApp Page 04: Contact Page

![image](https://github.com/SuhasiGadge/Stock-Price-Prediction-Using-LSTM-and-Sliding-Window/assets/97603532/1311ba7d-2788-4573-b551-779e89dddb95)






