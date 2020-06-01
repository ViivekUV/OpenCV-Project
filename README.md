# OpenCV-Project
<h3>What is the Project about</h3>
This project gives a good understanding of the OpenCV Library of python. 
I have worked on Face Detection, Face Detection from a Webcam, Virtual Paint and Number Plate detection

<h3>What OpenCV?</h3>
OpenCV is a open-source library of Python designed to solve computer vision, machine learning, and image processing problems.
It can process images and videos to identify objects, faces, or even the handwriting of a human. 
When it is integrated with various libraries, such as Numpy which is a highly optimized library for numerical operations, then the number of weapons increases in your Arsenal 
It means that whatever operations one can do in Numpy can be combined with OpenCV. 

<h3>Face Detection</h3>
This is a very simple project, that makes use of a haarcascade file.
Haar Cascade is a machine learning-based approach where a lot of positive and negative images are used to train the classifier.
    <ul>
      <li>
        Positive images – These images contain the images which we want our classifier to identify.
      </li>
      <li>
        Negative Images – Images of everything else, which do not contain the object we want to detect.
      </li>
    </ul>
 The "haarcascade_frontalface_default" XML file is used as a classifier.
 Input is given in the form of face(count).jpg
 Output is the image with a rectangle box around faces detected.
 
 <h3>Face Detection from a Webcam</h3>
 Process is similar to that of simple Face Detection, but, the input is read live from Webcam.
 Each frame of the live video is passed as an img input to a function, which identifies faces and indicates by rectangles around them.
 
 <h3>Virtual Paint</h3>
 Live feed from Webcam is taken to identify colours like orange, green, purple, etc.
 The identified colors leave behind marks at their identified position, giving up a feeling of marking on screen using the color.
 
 <h3>Number Plate Detection</h3>
 Number Plates are detected using a haarcascade classifier by the name "haarcascade_russian_plate_number", an XML file.
 Input images are given as car(count).jpg
 Also, if a number plate is detected, a clear, cropped picture of the number plate is displayed on screen.
 We can save the number plate, by pressing key "s" on keyboard.
 The saved images are stored in Scanned folder.
    
