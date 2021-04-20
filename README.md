# Breast-Cancer-Detection
# Overview
Among many cancers, breast cancer is the second most common cause of death in women. Early detection and early treatment reduce breast cancer mortality. Mammography plays an important role in breast cancer screening because it can detect early breast masses or calcification regions.
## Signs of Breast Cancer:
#### 1. Weight loss
#### 2. Skin changes
#### 3. Pain
#### 4. Breast changes

This project uses mammograms for breast cancer detection using deep learning techniques.

For the diagnosis of breast cancer doctors often use additional tests to find or diagnose breast cancer. ``A mammogram is an X-ray picture of the breast``. Doctors use a mammogram to look for ``early signs of breast cancer``. Regular mammograms are the best tests doctors have to find breast cancer early, sometimes up to three years before it can be felt.
A mammogram shows ``how dense the breasts are``. Women with dense breasts have a higher risk of getting breast cancer.

# Dataset
The dataset contains breast mammography images(224,24,3). With labels of:
#### 1. Density 
The levels of density are:
A: ``(1)`` Almost entirely fatty indicates that the breasts are almost entirely composed of fat. About 1 in 10 women has this result.
B: ``(2)`` Scattered areas of fibroglandular density indicates there are some scattered areas of density, but the majority of the breast tissue is nondense. About 4 in 10 women have this result.
C: ``(3)`` Heterogeneously dense indicates that there are some areas of nondense tissue, but that the majority of the breast tissue is dense. About 4 in 10 women have this result.
D: ``(4)`` Extremely dense indicates that nearly all of the breast tissue is dense. About 1 in 10 women has this result.
#### 2. Tumour 
A: ``Benign`` (noncancerous)
B: ``Malignant`` (cancerous)

# Training Images for each Class
#### Benign 
![alt text](https://github.com/hrsht-13/Breast-Cancer-Detection/blob/main/image/Begign.png)
#### Malignant
![alt text](https://github.com/hrsht-13/Breast-Cancer-Detection/blob/main/image/malignant.png)
# Image Processing
Since the mammograms looks blury and dull, image preprocessing has been done to increase the sharpness and contrast of the image.
![atl text](https://github.com/hrsht-13/Breast-Cancer-Detection/blob/main/image/processing.png)
# Model Deployment using Streamlit
>!git clone https://github.com/hrsht-13/Breast-Cancer-Detection.git

>%cd Breast-Cancer-Detection/

>pip install -r requirements.txt

>!ngrok authtoken 1mWgwxghOSQ2x0LfNFTzYTnJ9zK_81vqRPDdijfPjq8ozBdGq

>from pyngrok import ngrok

>public_url = ngrok.connect(port=8501)

>print (public_url)

>!streamlit run app.py >/dev/null (use the link to access the app)

>ngrok.kill()

