import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import requests
from io import BytesIO
from weights import download_weights
from model import download_model
import cv2

def main():

  st.set_option("deprecation.showfileUploaderEncoding",False)
  @st.cache(allow_output_mutation=True)
  def load_model():
    #model=download_model()
    model=tf.keras.models.load_model("model/model.h5")
    model.compile(optimizer =tf.keras.optimizers.Adam(learning_rate=0.00001,decay=0.0001),metrics=["accuracy"],
                  loss= tf.keras.losses.CategoricalCrossentropy(label_smoothing=0.1))
    download_weights()
    model.load_weights("weights/modeldense1.h5")

    return model

  model=load_model()
  st.title("Breast-Cancer-Detection")
  st.header("use mammograms for breast cancer detection using deep learning techniques.")
  #photo=Image.open("burger-icon-with-slice-pizza-soda-icon-illustration_138676-132.jpg")
  st.image(photo,use_column_width=True)
  file=st.file_uploader("Please Upload PHOTO", type=["jpg","png"])
  from PIL import Image,ImageOps
  
  def preprocess(image):
    kernel = np.array([[0,-1,0], [-1,5,-1], [0,-1,0]])
    im = cv2.filter2D(image, -1, kernel)
    return im

  def import_predict(image_data,model):
    size=(224,224)
    image=ImageOps.fit(image_data,size,Image.ANTIALIAS)
    img=np.asarray(image)
    img=preprocess(img)
    img=img/255.0
    img_reshape=np.expand_dims(img, axis = 0)
    prediction=model.predict(img_reshape)
    return prediction

  if file is None:
    i=2
  else:
    image=Image.open(file)
    st.image(image,use_column_width=True)
    predictions=import_predict(image,model)
    class_name=['Benign with Density=1','Malignant with Density=1','Benign with Density=2','Malignant with Density=2','Benign with Density=3','Malignant with Density=3','Benign with Density=4','Malignant with Density=4']
    string="From the mammogram the model detects that the tumour is : "+class_name[np.argmax(predictions)]
    st.success(string)
    
if __name__=='__main__':
    main()
    
