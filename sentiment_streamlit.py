# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 00:13:21 2023

@author: User
"""

import streamlit as st
from PIL import Image
from modules import Load_csv_file,Text_preprocessing,Model,Visualization

#%%
image = Image.open('sentiment_image.png')
st.image(image)
tab1, tab2 = st.tabs(["Dataset", "Text"])

with tab1:
    st.subheader('File uploader')
    uploaded_file = st.file_uploader('Please upload your CSV file here')
    if uploaded_file is not None:
        df = Load_csv_file.read_file(uploaded_file)
        st.subheader('**Data uploaded**')
        st.write(df)
        st.write('---')
        column_selected = st.radio('**Select one column for analysis:**',(df.columns))
        form1 = st.form(key='my-form')
        submit = form1.form_submit_button('Submit for analysis')
        if submit:
            df = df[column_selected]
            df = Text_preprocessing().preprocessing_steps(df)
            # Create an instance of the Model class and get the pretrained model
            model_instance = Model()
            model = model_instance.pretrained_model()
            df = model_instance.polarity_result(df)
            # visualization
            visualization_instance = Visualization()
            percentages = visualization_instance.percentages(df)
            # Pie chart
            st.write('---')
            st.subheader('**Result**')
            st.write('Result is presented in the pie chart below')
            st.write('POS= Positive, NEG= Negative, NEU= Neutral')
            # Display Pie Chart
            visualization_instance.pie_chart()
            # Wordcloud
            st.write('---')
            st.subheader('Wordcloud')
            st.write('Larger word indicate higher frequency of the word in a body of text')
            st.write('**Overall**')
            # Display wordcloud
            visualization_instance.wordcloud_overall(df,column_selected)
            # filter wordcloud by pos/neg/neu
            col1, col2 = st.columns(2)
            with col1:
                st.write('**Positive**')
                visualization_instance.wordcloud_filtered(df,'POS',column_selected)
            with col2:
                st.write('**Negative**')
                visualization_instance.wordcloud_filtered(df,'NEG',column_selected)

        
with tab2:
    form2 = st.form(key='my-form2')
    text_entered = form2.text_area('**Please enter your text here for analysis**')
    submit2 = form2.form_submit_button('Submit')
    if submit2:
        sentiment_model = Model().pretrained_model()
        sentiment_dict = sentiment_model.polarity_scores(text_entered)
        st.write("Sentence Overall Classified As", end = " ")
    # decide sentiment as positive, negative and neutral
        if sentiment_dict['compound'] >= 0.05 :
            st.write('**Positive**')
        elif sentiment_dict['compound'] <= - 0.05 :
            st.write('**Negative**')
        else :
            st.write('**Neutral**')
    



