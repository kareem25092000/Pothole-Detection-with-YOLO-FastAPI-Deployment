from roboflow import Roboflow
from dotenv import load_dotenv
load_dotenv()
import os

rf = Roboflow(api_key= os.environ["api"])
project = rf.workspace("yolov8-uav").project("potholes-detect-uytky")
version = project.version(358)
dataset = version.download("yolov11")
                