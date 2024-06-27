from AI.BrainTumors import BrainTumorsPredictImage
from AI.LungCancer import LungCancerPredictImage
from AI.KidneyStone import KidneyStonePredictImage
from AI.ToRecognize import ToRecognizePredictImage
from AI import ToRecognizeAndPredictImage



import os
os.system("cls" or "clear")


# import time

# def clear(): os.system("cls" or "clear")

# start = time.time()
# anser1 = BrainTumorsPredictImage(r"D:\Parsia Works\python\Project\AI\BrainTumors\datasets\Testing\notumor\Te-no_0144.jpg")
# _time1 = time.time() - start


# start = time.time()
# anser2 = LungCancerPredictImage(r"D:\Parsia Works\python\Project\TestingData\Lung-Benign_Tissue.jpeg")
# _time2 = time.time() - start


# start = time.time()
# anser3 = KidneyStonePredictImage(r"D:\Parsia Works\python\Project\TestingData\Tumor- (342).jpg")
# _time3 = time.time() - start


# start = time.time()
# anser4 = ToRecognizePredictImage(r"D:\Parsia Works\python\Project\TestingData\Lung-Benign_Tissue.jpeg")
# _time4 = time.time() - start


# start = time.time()
# anser5 = ToRecognizeAndPredictImage(r"D:\Parsia Works\python\Project\TestingData\Lung-Benign_Tissue.jpeg")
# _time5 = time.time() - start


# os.system("cls" or "clear")


# print(30*"-")
# print()
# print(f"Time    : {_time1}")
# print(f"Predict : {anser1}")
# print()
# print(30*"-")
# print()
# print(f"Time    : {_time2}")
# print(f"Predict : {anser2}")
# print()
# print(30*"-")
# print()
# print(f"Time    : {_time3}")
# print(f"Predict : {anser3}")
# print()
# print(30*"-")
# print()
# print(f"Time    : {_time4}")
# print(f"Predict : {anser4}")
# print()
# print(30*"-")
# print()
# print(f"Time    : {_time5}")
# print(f"Predict : {anser5}")
# print()
# print(30*"-")
# print()
# print(f"All time    : {_time1+_time2+_time3+_time4+_time5}")
# print(30*"-")

# OUTPUT:
#------------------------------
#
#Time    : 1.0277082920074463
#Predict : notumor
#
#------------------------------
#Time    : 0.645604133605957
#Predict : Lung-Benign_Tissue
#
#------------------------------
#
#Time    : 0.5206775665283203
#Predict : Tumor
#------------------------------
#
#Time    : 0.5028464794158936
#Predict : LungCancer
#
#------------------------------
#
#Time    : 1.158289909362793Predict : LungCancer : Lung-Benign_Tissue
#------------------------------
#All time    : 3.85512638092041
#------------------------------
