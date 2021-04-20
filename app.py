import tensorflow as tf
import numpy as np
from PIL import Image
from weights import download_weights
from model import download_model
import cv2
import gradio as gr

def main():
  def load_model():
    download_model()
    model=tf.keras.models.load_model("model/model.h5")
    model.compile(optimizer =tf.keras.optimizers.Adam(learning_rate=0.00001,decay=0.0001),metrics=["accuracy"],
                  loss= tf.keras.losses.CategoricalCrossentropy(label_smoothing=0.1))
    download_weights()
    model.load_weights("weights/modeldense1.h5")
    return model

  model=load_model()
  
  def preprocess(image):
    kernel = np.array([[0,-1,0], [-1,5,-1], [0,-1,0]])
    im = cv2.filter2D(image, -1, kernel)
    return im
  
  image=gr.inputs.Image(shape=(224,224))
  label=gr.outputs.Label(num_top_classes=8)
  
  class_name=['Benign with Density=1','Malignant with Density=1','Benign with Density=2','Malignant with Density=2','Benign with Density=3','Malignant with Density=3','Benign with Density=4','Malignant with Density=4']
  
  def predict_img(img):
    img=preprocess(img)
    img=img/255.0
    im=img.reshape(-1,224,224,3)
    pred=model.predict(im)[0]
    return {class_name[i]:float(pred[i]) for i in range(8)}
  
  gr.Interface(fn=predict_img,inputs=image,outputs=label,capture_session=True).launch(debug='True',share=True)
  
if __name__=='__main__':
    main()
    
