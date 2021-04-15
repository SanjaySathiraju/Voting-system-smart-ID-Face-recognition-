# Voting-system-smart-ID-Face-recognition-

This is a python project for Windows. This code does not work on MacOS and still needs some development. 
Before getting started with the project, there are few libraries that needs to be installed. 
This project shows a voting system based on Unique ID and Iris Recognition. 
The system iimplementation is shown below:

<img width="442" alt="Screen Shot 2021-04-15 at 3 52 25 AM" src="https://user-images.githubusercontent.com/80937013/114834594-b3b04780-9d9e-11eb-94e3-80bec156950d.png">


The above figure depicts our proposed system model. In this model, the admin can log in and add the nominees and voters to the
database. Moreover, the admin can view the nominee and voters' details and election results. The voter also will log in with valid voter id and Iris images, and he/she can poll the vote if authenticated successfully, otherwise denied. 

DESIGN::

The design of the system is primarily divided into two functionalities: Admin and voters. In the system, the admin, once given access, can operate various functions like adding a nominee, voters, and their iris images. Admin can also view results. When it comes to the voter, the only action that is allowed is casting a vote. Voters can log in with valid credentials such as Smart-ID and iris.

In this project, the iris recognition process is done in the following way:
HOUGH TRANSFORMATION

DOUGMAN'S RUBBER SHEET MODEL

DATA CONVERSION(Raw data obatined from above 2 steps convereted to binary)

HAMMING DISTANCE(If the bit shifting is 0, i.e., Hamming distance is 0, it is a perfect match. If it is 0.5 or more, then the two strings are different.)

The idea of data flow diagrams is to perform system analysis efficiently. The figure below shows how the system is going to be performed.

<img width="453" alt="Screen Shot 2021-04-15 at 4 04 21 AM" src="https://user-images.githubusercontent.com/80937013/114835561-b2334f00-9d9f-11eb-8212-22ce3b69f31f.png">

SOFTWARE CONFIG::

<img width="442" alt="Screen Shot 2021-04-15 at 4 01 50 AM" src="https://user-images.githubusercontent.com/80937013/114835240-5b2d7a00-9d9f-11eb-9505-3ee1a95ffcf1.png">

PYQT5:It is a framework in python to build GUI(Graphical User Interface) apps. It usually facilitates python to work as an altered application development language. It offers a wide range of features like a dialog box, pushbuttons, labels, and other GUI app components.
