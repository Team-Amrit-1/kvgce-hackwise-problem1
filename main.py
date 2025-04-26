import cv2 as cv
import numpy as np
import zipfile

with zipfile.ZipFile("satellite_images.zip", 'r') as zip_ref:    # Change the path as per directory
    zip_ref.extractall()


# Converting Images to GrayScALE using cv2.IMREAD_GRAYSCALE and Calculating Global AVg for each image array
def GlobalAverage():
    images_load_grayscale = []                          # store the image grayscale data
    image_indices = []                                  # Store the Image number which is Available
    missing_input_img = []                              # Store the Misssing Image Number

    for i in range(1,11):
        img = cv.imread(f"test cases/sample_input/image{i}.png", cv.IMREAD_GRAYSCALE)
        """   To read the image file .....
        change the path for hidden test case according to your location         
        """
        
        if img is not None:
            images_load_grayscale.append(img)
            image_indices.append(i)                     # track the present image number AS index   
        else:
            missing_input_img.append(i)                 # track the missing image number As index


    all_pixels = np.concatenate([img.flatten() for img in images_load_grayscale])

    global_avg = np.mean(all_pixels)
    return global_avg, images_load_grayscale, image_indices, missing_input_img


# Normalizing the images and checking whether absolute(diff. bet. each img mean and global_avg ) is <= 1
def NormImages_Output(global_avg, images_load_grayscale, image_indices, missing_images):

    # Step - 1 Converting Images to normalized_Images
    normalized_images = []
    for img in images_load_grayscale:
        current_avg = img.mean()

        factor = global_avg /current_avg

        normalized = img * factor

        normalized = np.clip(normalized,0,255)

        normalized = normalized.astype(np.uint8)

        normalized_images.append(normalized)


    # Step-2 Saving the File output as in desired manner =>  (Ex.  normalized_images1.png  ) in NormalizedImages folder
        """  Note ->

            For Particular Test Case
            To save the normalized_image{i}.png use below path as per test case

            for satellite_images_Output for normalized_images{i}.png ==> f"NormalizedImages/Satellite_images_Output/{filename}"

            Test Case 1: sample_input ==> f"NormalizedImages/TestCaseOutputSample/{filename}"
            Test Case 2: HiddenTestCase1 ==> f"NormalizedImages/HiddenTestCase1/{filename}"    
            Test Case 3: HiddenTestCase2 ==> f"NormalizedImages/HiddenTestCase2/{filename}"
            
            Note -> Create HiddenTestCase1 and HiddenTestCase2 folder if not present in NormalizedImages folder
        """ 

    for i, img in zip(image_indices, normalized_images):
        filename = f"normalized_image{i}.png"

        if not filename.startswith("normalized_image") and not filename.endswith("f{i}.png"):     
            return 0                                # If name does not follow the name of img as per required return score as 0

        cv.imwrite(f"NormalizedImages/SampleOutputTestCase/{filename}", img)

    # step - 3 : Check all imgs have [ abs(avg - global_avg) <= 1 ] , if not then score is by default to be zero
    count_correct = 0
    for i, img in zip(image_indices, normalized_images):

        avg = img.mean()
        if abs(avg - global_avg) <= 1:
            count_correct += 1
            # print(f"The Images having diff of AVG and global_avg <= 1 is : image{i}.png having value {abs(avg - global_avg)} ")
        else:
            print(f"image {i}.png have score absolute > 1 with value {abs(avg - global_avg)}")
        
        print(f"image{i}.png: avg={avg:.2f} (within ±1 of {global_avg:.2f})")
    
    return count_correct


# Calculating Score
def CalculateScore(correct):
    if correct != 10:                           # comparison done with 10 because Images given are only 10
        return 0                                # return 0 score as if any img has correct count > or < 10
    score = (correct / 10) * 10 
    return score



GlobalAvg, images_load, image_indices, missing_images = GlobalAverage()
print("Missing Images:", missing_images)
print(f"GLobal Average = {GlobalAvg:.2f}")


correct = NormImages_Output(GlobalAvg, images_load, image_indices, missing_images)
score = CalculateScore(correct)
print(f"Score for Sample Test Case = {int(score)}")



