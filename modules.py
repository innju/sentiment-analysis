# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 19:59:16 2023

@author: User
"""

import pandas as pd
import re
import string
import nltk
from spellchecker import SpellChecker
import streamlit as st
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#%%
class Load_csv_file:
    def read_file(uploaded_file):
        dataframe = pd.read_csv(uploaded_file,encoding='unicode_escape')
        return dataframe

class Text_preprocessing:
    def remove_punctuation(self,text):
            punctuationfree="".join([i for i in text if i not in string.punctuation])
            return punctuationfree
        
    def remove_stopwords(self,text):
        stopwords = nltk.corpus.stopwords.words('english')
        output= [i for i in text if i not in stopwords]
        return output

    def correct_spelling(self,tokens):
        spell = SpellChecker()
        corrected_tokens = []
        for token in tokens:
            corrected_token = spell.correction(token)
            corrected_tokens.append(corrected_token)
        return corrected_tokens

    def join_string(self,list_string):
        # Join the string based on ' '
        string=' '.join([i for i in list_string if i is not None])
        return string
    
    def preprocessing_steps(self,dataframe):
        dataframe = dataframe.drop_duplicates()
        dataframe = dataframe.dropna()
        dataframe = dataframe.str.lower()
        dataframe = dataframe.apply(lambda x:re.sub(r'[^A-Za-z0-9\s]', '', x))
        dataframe = dataframe.apply(lambda x:self.remove_punctuation(x))
        dataframe = dataframe.apply(lambda x: x.split())
        dataframe = dataframe.apply(lambda x:self.remove_stopwords(x))
        dataframe = dataframe.apply(lambda x:self.correct_spelling(x))
        dataframe = dataframe.apply(lambda x:self.join_string(x))
        dataframe = pd.DataFrame(dataframe)
        return dataframe
    
class Model:
    def pretrained_model(self):
        self.model = SentimentIntensityAnalyzer()
        return self.model
    
    def polarity(self,strings):
        preprocessed_texts = []
        for line in strings:
            preprocessed_text = self.model.polarity_scores(line)
            preprocessed_texts.append(preprocessed_text)
        return preprocessed_texts
    
    def polarity_result(self,dataframe):
        dataframe['scores'] = dataframe.apply(lambda x: self.polarity(x))
        #create new columns scores using polarity scores function
        dataframe['compound']=dataframe['scores'].apply(lambda score_dict:score_dict['compound'])
        dataframe['pos']=dataframe['scores'].apply(lambda pos_dict:pos_dict['pos'])
        dataframe['neg']=dataframe['scores'].apply(lambda neg_dict:neg_dict['neg'])
        dataframe['neu']=dataframe['scores'].apply(lambda neg_dict:neg_dict['neu'])
        #creat new column to indicate whether review is pos, neg or neutral
        dataframe['type']=''
        dataframe.loc[dataframe.compound>=0.05,'type']='POS'
        dataframe.loc[(dataframe['compound'] > -0.05) & (dataframe['compound'] < 0.05), 'type'] = 'NEU'
        dataframe.loc[dataframe.compound<=-0.05,'type']='NEG'
        return dataframe

class Visualization:
    def percentages(self,dataframe):
        # calculate total no. of pos, neg and neu
        self.total_counts =dataframe['type'].value_counts()
        total_entries = len(dataframe)
        # Calculate the percentage of each category
        self.percentages = [(count / total_entries) * 100 for count in self.total_counts]
        return self.total_counts,self.percentages
    
    def pie_chart(self):
        labels = self.total_counts.index
        colors = ['#ff9999','#66b3ff','#99ff99']
        fig1, ax1 = plt.subplots(figsize=(3,3))
        ax1.pie(self.percentages, labels=labels, colors=colors, autopct='%1.1f%%',textprops={'fontsize': 6})
        ax1.axis('equal')
        return st.pyplot(fig1)
    
    def wordcloud_overall(self,dataframe,column_selected):
        self.text= " ".join(word for word in dataframe[column_selected])
        word_cloud = WordCloud(collocations = False, background_color = 'white',
                                  width = 2048, height = 1080).generate(self.text)
        fig, ax = plt.subplots()
        ax.imshow(word_cloud)
        ax.axis("off")
        return st.pyplot(fig)
    
    def wordcloud_filtered(self,dataframe,sentiment_category,column_selected):
        self.filtered_dataframe = dataframe[dataframe['type'] == sentiment_category]
        self.is_exist = sentiment_category in dataframe['type'].values
        if self.is_exist == True:
            filtered_sentiment_text= " ".join(word for word in self.filtered_dataframe[column_selected])
            word_cloud_filtered = WordCloud(collocations = False, background_color = 'white',
                                    width = 2048, height = 1080).generate(filtered_sentiment_text)
            fig, ax = plt.subplots()
            ax.imshow(word_cloud_filtered)
            ax.axis("off")
            return st.pyplot(fig)
        else:
            return st.write('Not detected')
    
    
    
    
    
    
    
    
    
    
    