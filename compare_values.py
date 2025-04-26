"""
THis Code file compare_values.py is particularly for comparing our outocme result img mean() with expected image mean()

NOTE -> Run this Code file only if All 10 image files are present in both Expected outcome folder and our outcome result folder
        Give the Desired path for both as necessary !!
"""


import cv2
import numpy as np

for i in range(1, 11):
    # read the path for expected Norm imgs and our result norm imgs
    path1 = f"NormalizedImages/SampleOutputTestCase/normalized_image{i}.png"
    path2 = f"test cases/sample_expected/normalized_image{i}.png"
    
    # Read images in grayscale
    img1 = cv2.imread(path1, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(path2, cv2.IMREAD_GRAYSCALE)
    
    # Compute and print the means
    mean1 = np.mean(img1)
    mean2 = np.mean(img2)

    mean1 = f"{mean1:.2f}"
    mean2 = f"{mean2:.2f}"
    
    if mean1 == mean2: 
        print("Expected outcome and My result Outcome are the same")
    else:
        print("They are not Same")
    
    print(f"Image {i}: {mean1}   {mean2}")


    """
    COMPARE Your test Case Result by Cal. Avg on Expected images of Test Case with Your Output Images

    path1 : participants outcome result path
    path2 : Expected outcome result path

    Test Case 1: Sample Output Expected 
    path1 = f"NormalizedImages/SampleOutputTestCase/normalized_image{i}.png"
    path2 = f"test cases/sample_expected/normalized_image{i}.png"

    Test Case 2: HiddenTestCase1 Expected
    path1 = f"NormalizedImages/HiddenTestCase1/normalized_image{i}.png"        
    path2 = f" "       <-- Hidden Test Case 1 Expected Outcome images Path

    Test Case 3: HiddenTestCase2 Expected
    path1 = f"NormalizedImages/HiddenTestCase2/normalized_image{i}.png"
    path2 = f" "       <-- Hidden Test Case 2 Expected Outcome images Path
    """
