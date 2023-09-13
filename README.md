# Pyvoussoir-GUI
A GUI batch processing application for [pyvoussoir](https://github.com/hnesk/pyvoussoir). 

Pyvoussoir is an automatic de-keystoning/page-splitting tool for single camera book scanners. It is a python CLI implementation of the C++ based [voussoir](https://github.com/publicus/voussoir) by Jacob Levernier.


## Usage
Make sure pyvoussoir is installed, you can do so by running the following command.
```
pip install pyvoussoir
```


Follow the instructions given in [voussoir usage](https://github.com/jglev/voussoir#usage) when setting up your captures, they should look something like this.
![1](https://github.com/YellowTeamRobot/Pyvoussoir-GUI/assets/107053197/c8c3721b-c6b3-44db-ba2a-3cff0d3de028)

Then, when your done taking your pictures, move them to a folder on your computer and run Pyvoussoir-GUI.py

Select your input folder and desired output folder, select/change desired settings and click "Process Images", when the button returns to green the files should now be in the output folder de-keystoned and split into left and right.


![h](https://github.com/YellowTeamRobot/Pyvoussoir-GUI/assets/107053197/a3c0b082-792f-4337-abfc-ce0901223aa1)
