import unittest
import AI_methods


class TesAIFuncs (unittest.TestCase) :
    
    # BrainTumor Test
    def test_BrainTumorsPredictImage (self):

        self.assertEqual(
            AI_methods.BrainTumorsPredictImage(r"D:\Parsia Works\python\Project\AI\BrainTumors\datasets\Testing\notumor\Te-no_0144.jpg"),
            "notumor"
        )

        self.assertEqual(
            AI_methods.BrainTumorsPredictImage(r"D:\Parsia Works\python\Project\AI\BrainTumors\datasets\Testing\glioma\Te-gl_0286.jpg"),
            "glioma"   
        )

        self.assertEqual(
            AI_methods.BrainTumorsPredictImage(r"D:\Parsia Works\python\Project\AI\BrainTumors\datasets\Testing\pituitary\Te-pi_0014.jpg"),
            "pituitary"
        )


    # LungCanceer Test
    def test_LungCancerPredictImage (self):

        self.assertEqual(
            AI_methods.LungCancerPredictImage(r"D:\Parsia Works\python\Project\TestingData\Lung-Benign_Tissue.jpeg"),
            "Lung-Benign_Tissue"
        )

    # KidneyStone Test
    def test_KidneyStonePredictImage (self):

        self.assertEqual(
            AI_methods.KidneyStonePredictImage(r"D:\Parsia Works\python\Project\TestingData\Tumor- (342).jpg"),
            "Tumor"
        )

    # ToRecognize Test
    def test_ToRecognizePredictImage (self):

        self.assertEqual(
            AI_methods.ToRecognizePredictImage(r"D:\Parsia Works\python\Project\AI\BrainTumors\datasets\Testing\notumor\Te-no_0023.jpg"),
            "BrainTumor"
        )

        self.assertEqual(
            AI_methods.ToRecognizePredictImage(r"D:\Parsia Works\python\Project\TestingData\Lung-Benign_Tissue.jpeg"),
            "LungCancer"
        )

    # ToRecognizeAndPredict Test
    def test_ToRecognizeAndPredictImage (self):

        self.assertEqual(
            AI_methods.ToRecognizeAndPredictImage(r"D:\Parsia Works\python\Project\TestingData\Lung-Benign_Tissue.jpeg"),
            "LungCancer : Lung-Benign_Tissue"
        )


# To run this file : 
# python -m unittest .\test_AI_methods.py