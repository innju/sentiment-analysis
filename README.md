![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Anaconda](https://img.shields.io/badge/Anaconda-%2344A833.svg?style=for-the-badge&logo=anaconda&logoColor=white)
![Spyder](https://img.shields.io/badge/Spyder-838485?style=for-the-badge&logo=spyder%20ide&logoColor=maroon)

# sentiment-analysis
Sentiment analysis using a pretrained model (VADER) Sentiment can be classified into positive, negative, and neutral categories. One of the uses of sentiment analysis is that it can help organisations look into customer reviews for improvements to products or services in the future.

The python scripts uploaded had been tested and run using Spyder(Python 3.8.13).
<br>The source of the data used for this analysis is:
<br>[Women's E-Commerce Clothing Reviews](https://www.kaggle.com/datasets/nicapotato/womens-ecommerce-clothing-reviews)

### FOLDERS AND FILES
| File | Description |
| --- | --- |
| images folder | images of the streamlit web page interface |
| clothing_reviews.csv | self filtered sample dataset (In this case, the ID was filtered by ClothingID = 861, which is a knit)  |
| modules.py | all the classes and functions created to ease the running process |
| sentiment_streamlit.py | python script for demonstration using streamlit |

<br>*Streamlit is an open-source Python library that makes it easy to create and share beautiful, custom web apps for machine learning and data science.*

### ABOUT THE MODEL
VADER (Valence Aware Dictionary and Sentiment Reasoner) is a pretrained model that specifically designed for social media text, which often includes informal language and emoticons. It calculates sentiment scores for individual words and then combines them using specific rules to generate an overall sentiment score for the entire text. 

### VIEW THE APP
If you have anaconda installed on your device, you can view the application by follow the steps below:
Open Anaconda prompt > conda activate (name of ur environment) > cd (main folder path) > streamlit run (file name for deployment).

You can also refer to the link below for tutorial:
[Simple Tutorial to Run Streamlit Script](https://docs.streamlit.io/knowledge-base/using-streamlit/how-do-i-run-my-streamlit-script)

#### Dataset Tab
There are two tabs on the app interface that the user can use for analysis with different inputs, either in dataset form (a csv file) or text form. The user can have a preview of the uploaded data and select the column that contains the texts for analysis.

<p align="center">
  <img src="https://github.com/innju/sentiment-analysis/blob/main/images/1_file_uploader.png" width=50% height=50%>
</p>

<p align="center">
  <img src="https://github.com/innju/sentiment-analysis/blob/main/images/2_data_preview.png" width=50% height=50%>
</p>

<p align="center">
  <img src="https://github.com/innju/sentiment-analysis/blob/main/images/3_piechart.png" width=50% height=50%>
</p>

<p align="center">
  <img src="https://github.com/innju/sentiment-analysis/blob/main/images/4_wordcloud.png" width=50% height=50%>
</p>

<br>Based on the dataset uploaded, the result shows the highest proportion in positive categories, which is 93.4%. This indicates most of the customers are satisfied with the product purchased. Worldcloud shows the overall, positive, and negative feedback of customers. The smaller figures (positive / negative) can be enlarged by clicking on the expansion icon while hovering the mouse over the smaller figure. Larger words indicate a higher frequency of the word mentioned. Since 3.9% of the datasets are classified as negative, this means there is some unsatisfaction among customers, and based on the negative wordcloud, the reasons are mostly because the knit they purchased is thin and they feel terrible with the design.

#### Text Tab
Another tab would be the section for user to play with. This allows user to test the polarity of the text input. User can key in the texts for analysis. Result is displayed below as positive, negative or neutral.

<p align="center">
   <img src="https://github.com/innju/sentiment-analysis/blob/main/images/5_text_input.png" width=50% height=50%>
</p>

### CONCLUSION
Pretrained model can save time and effort in developing a sentiment analysis model from scratch. VADER's lexicons and rule-based approach allow it to handle slang, abbreviations, and emoticons. However, it has its limitations, particularly in understanding context and handling more complex language patterns. It's essential to consider the specific use case and requirements before deciding whether to use VADER or other sentiment analysis models based on the needs of your project. 

Thanks for reading.

