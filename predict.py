from ultralytics import YOLO
import os
from PIL import Image



path_model_nano = os.path.join("runs" ,"detect" ,"train" 
                          ,"weights" ,"best.pt")

model_nano = YOLO(path_model_nano)

def predict_nano(image):
    result =  (model_nano.predict(image)[0]).plot()
    result = Image.fromarray(result)
    return result


path_model_small = os.path.join("runs" ,"detect" ,"train-2" 
                          ,"weights" ,"best.pt")

model_small = YOLO(path_model_small)

def predict_small(image):
    result = model_small.predict(image)[0].plot()
    result = Image.fromarray(result)
    return result


if __name__ == "__main__":
    path_image = os.path.join("potholes-detect-358" ,"test" ,"images"
                    ,"7_jpg.rf.3b547a8824468a91124d60f25706a7b4.jpg")
    predict_small(path_image).show()
    predict_nano(path_image).show()
