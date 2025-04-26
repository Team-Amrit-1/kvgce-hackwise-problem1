# kvgce-hackwise-problem1
#### Team Name - Team Amrit
#### Problem Number and Title - Problem 1 - Satellite Image Brightness Normalizer
#### Command Instructions to run the Code are as below:

Step 1 - Activate Virtual env
    command - .\myvenv\Scripts\activate      ---> for windows
                source myvenv/bin/activate   ---> for Linux
    To Deactivate,
    command - deactivate 

Step 2 - Install Necessary Libraries using 
    command - pip install -r requirements.txt

Step 3 - Run the main.py file after Activation of venv
    command - python main.py     ( for linux use --> python3 main.py  )

Step 4 - If want to check the that we have got same mean for Expected Outcome and Our result Outcome
    Run the compare_values.py
    command - python compare_values.py       ( for linux use --> python3 compare_values.py  )

#### Dependencies: All required python libraries can be download as per above command instruction to run the code focusing on step 2 after activating virtual Environment

#### Expected input filename for satellite images is satellite_images.zip, which is extracted first and then read.
#### All outputs of image files are stored in normalized_image{i}.png   i-> 1-10 ( Exact location of storing those images mentioned in brief below.... )

#### Image file outputs
NOTE -> If HiddenTestCase1 and HiddenTestCase2 folders are not present just Create the folders inside NormalizedImages folder

    NormalizedImages folder is created inside which there are 4 folders named as 
    HiddenTestCase1, HiddenTestCase2, SampleOutputTestCase, Satellite_images_Output

    In each above folder particular output normalized_images are stored
    Ex. NormalizedImages/SampleOutputTestCase/normalized_image1.png

#### flowchart.excalidraw is the file showing the flowchart/workflow of Implementation.
#### To see it, install Excalidraw ( by pomdtr ) in visual studio code Extensions

#### compare_values.py file is used for comparing our outcome result of all 10 images with expected outcome of 10 images by calculating the mean, If both results have same mean then our outcome result is matching with expected outcome result.


