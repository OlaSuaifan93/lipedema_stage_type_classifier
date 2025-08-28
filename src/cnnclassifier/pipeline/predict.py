import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os



class PredictionPipeline:
    def __init__(self,filename):
        self.filename =filename


    
    def predict(self):
        # load model
        model = load_model(os.path.join("artifacts","training", "model.h5"))

        imagename = self.filename
        test_image = image.load_img(imagename, target_size = (224,224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = np.argmax(model.predict(test_image), axis=1)
        print(result)

        if result == [0]:
            prediction = "Stage1_Type1"
        elif result == [1]:
                prediction = "Stage1_Type2"
        elif result == [2]:
                prediction = "Stage1_Type3"
        elif result == [3]:
                prediction = "Stage1_Type4"
        elif result == [4]:
                prediction = "Stage1_Type5"
        elif result == [5]:
                prediction = "Stage2_Type1"
        elif result == [6]:
                prediction = "Stage2_Type2"
        elif result == [7]:
                prediction = "Stage2_Type3"
        elif result == [8]:
                prediction = "Stage2_Type4"
        elif result == [9]:
                prediction = "Stage2_Type5"
        elif result == [10]:
                prediction = "Stage3_Type1"
        elif result == [11]:
                prediction = "Stage3_Type2"
        elif result == [12]:
                prediction = "Stage3_Type3"
        elif result == [13]:
                prediction = "Stage3_Type4"
        elif result == [14]:
                prediction = "Stage3_Type5"
        elif result == [15]:
                prediction = "Stage4_Type1"
        elif result == [16]:
                prediction = "Stage4_Type2"
        elif result == [17]:
                prediction = "Stage4_Type3"
        elif result == [18]:
                prediction = "Stage4_Type4"
        elif result == [19]:
                prediction = "Stage4_Type5"
        else:
                prediction = "Unknown"

        return [{"image": prediction}]


