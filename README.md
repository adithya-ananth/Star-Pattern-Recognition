# Star-Pattern-Recognition
This repo contains files and codes for Star Recognition Project

## Executed Code
The folder 'Extracting Coordinates' contains the code for processing the neat night sky images to get a clear binary image where stars are clearly visible. Any other pixels are nullified. The code is available in the file 'star_processing.py'. The code is written in Python and uses torchv, numpy and pillow libraries. The code is executed in Jupyter Notebook.  

The code for extracting the coordinates is present here: [Constellation_Coordinates.py](https://colab.research.google.com/drive/11E-gpTeyI1Jm2BPf-n-pI-1YvP2SxBQG?usp=sharing)
    The link for the dataset of coordinates of the stars in the 88 constellations is present here: [Constellation_Coordinates](https://drive.google.com/drive/folders/1ozhX8YHyqRBWTqofdgujxbHtCg_-sAxY)
Other four folders inside 'Extracting Coordinates' are the images from different sources for testing the code. The images are named as 'image1.jpg', 'image2.jpg', 'image3.jpg', etc.  

Sample Case:   
Input1:   
![image](https://github.com/astroclubiitt/Star-Pattern-Recognition/assets/84005308/dbc70fec-0e98-4c5a-9fd0-be4334cf3b00)  

Processed Image1:   
![image](https://github.com/astroclubiitt/Star-Pattern-Recognition/assets/84005308/9dff23a9-ee2a-4735-8b4f-c0041fb587fb)  

Coordinates Extracted1:  
![image](https://github.com/astroclubiitt/Star-Pattern-Recognition/assets/84005308/fe22f3b0-99cc-4cf6-8624-b90ddcebc368)  

 
```
Number of stars: 14  
Coordinates of stars: [(35.666666666666664, 35.666666666666664), (55.0, 110.0), (59.5, 109.0), (68.0, 173.0), (72.0, 65.0), (73.0, 86.5), (75.66666666666667, 88.66666666666667), (78.0, 91.5), (79.33333333333333, 109.33333333333333), (92.0, 106.0), (93.0, 72.5), (105.0, 93.0), (107.0, 144.0), (149.0, 163.0)]
```
