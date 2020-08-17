# seterra-TAS-tool
A TAS tool for Seterra Map quiz games.

This is a tool made for fun that semi automatically completes a Seterra map quiz. It requires an initial user input and uses Tesseract-OCR with pyautogui to automatically click the locations.

## How it works:
As of now it is quite inefficient as it requires the user to do the quiz first. Essentially, since screen resolutions and browser zoom varies among computers, a fixed set of coordinates that works for everyone cannot be made. Hence, I decided to make it so that the user completes the map quiz first, then the script registers all the values and next it completes the quiz by reading the "Click on " part with Tesseract-OCR and using pyautogui to click on the screen coordinates that were previously registered and were associated with the country name values. To make it more User friendly I decided to implement a very basic GUI using tkinter.

## Installation:
(Python 3 is required)

The following python Libraries are required to make the script work: 
```
pytesseract, pyautogui, difflib, re, pynput.mouse, PIL, tkinter, time, os.path
```
Many of which should be already included in your Python 3 installation.
To install the packages use the command:
```
pip3 install pytesseract pyautogui pynput pillow
```
Pytesseract requires Tesseract-OCR to be installed, which is an external software that can be installed following the instructions in the [official Tesseract Github repository](https://github.com/tesseract-ocr/tesseract) .
After Installation it is **Fundamental** to check that the location of the Tesseract.exe file needed for the script to run is the same of the one written in the  `Tesseract_location.txt` text file; if it's not the same then edit the file writing the appropriate directory (Note: Double backlashes `\\` must be used). The default directory in the script is the default Windows directory for the .exe file, which is `C:\\Program Files\\Tesseract-OCR\\tesseract.exe`.

As for `tkinter` it cannot be simply installed with pip. It's the library that allows the GUI and it can be installed following the [Instructions](https://tkdocs.com/tutorial/install.html) on the docs page for your operative system and for python, with its latest version.

## Usage:
To Run the script just open a console in the folder where the files have been downloaded and do:
```
python Seterra_TAS.py
```
It's fairly simple to use. When you run the script after all the packages have been installed and set up properly, a window with some buttons will appear. Before explaining the various function, an explanation of the whole procedure is needed. The first thing the user has to do is seelecting the "box", a rectangle that surrounds the "click on " part of the seterra quiz **Including** a wide space, wide enough to fit all the possible words in the quiz; this box is needed as it's what Tesseract will read to know which country to click on. Afterwards the position of the Restart button must be given. After all this the procedure of registering the various coordinates begins and the user has to complete the quiz; if you made mistakes in the quiz during this procedure it's completely fine, the script has enough resilience so that you can generally make as many mistakes as you want and it'll still work in the end. Finished this phase, after clicking "Ok" on the first quiz test results, the script can start to automatically complete the quiz. ***It is important that you NEVER scroll down, move the browser window or put another window above the "click on" and "Restart" parts of the quiz at any point from the selection of the box to the completion of the map***. The meanings of the buttons are:
- Position 1: It's the first button you have to press. After you press this button you will need to click on the **top left corner** of the box.
- Position 2: It's the second button you have to press. After you press this button you will need to click on the **bottom right corner** of the box, it must not be above the coordinates you clicked for Position 1.
- Restart Button Position: It's the third button you have to press. After you press this you will need to click on the "Restart" button of the Seterra quiz.
- Map Places: It's the fourth button you have to press. After pressing this button the script will start registering the various quiz answers and you'll have to complete the quiz. Always restart the quiz before doing this step otherwise you'll risk not registering some values.
- Complete Map: it's the lasst button you have to press. It's the button that will start the completion of the quiz by the tool. After the completion you can complete the quiz again as many times you want as long as the position of the quiz is the same and all the requisites listed before are met.
- Reset: Will Reset all values. It's highly suggested to press this button whenever you accidentally scroll down/up or move the window during the setup procedure (From Position 1 to Complete Map). It's also suggested to use it if you want to complete another quiz.
- Debug: A developer option. It'll print values on the console needed for debugging.
