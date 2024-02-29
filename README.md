# seterra-TAS-tool
A TAS tool for Seterra Map quiz games.

This is a tool made for fun that semi-automatically completes a Seterra map quiz. It requires an initial user input and uses Tesseract-OCR with pyautogui to automatically click the locations.

Table of Contents:
- [How it works](#how-it-works)
- Installation
- Ussage
- Video Explanation
- Additional Notes

<a name="how-it-works"></a>
## How it works:
As of now it is quite inefficient as it requires the user to do the quiz first. Essentially, since screen resolutions and browser zoom varies among computers, a fixed set of coordinates that works for everyone cannot be made. Hence, I decided to make it so that the user completes the map quiz first, then the script registers all the values and next it completes the quiz by reading the "Click on " part with Tesseract-OCR and using pyautogui to click on the screen coordinates that were previously registered and were associated with the country name values. To make it more User friendly I decided to implement a very basic GUI using tkinter.

## Installation:
(Python 3 is required)

The following python Libraries are required to make the script work: 
```
pytesseract, pyautogui, difflib, re, pynput.mouse, PIL, tkinter, time, os.path
```
Many of which should be already included in your Python 3 installation.
To install the remaining packages use the command:
```
pip3 install pytesseract pyautogui pynput pillow
```
Pytesseract requires Tesseract-OCR to be installed, which is an external software that can be installed following the instructions in the [official Tesseract Github repository](https://github.com/tesseract-ocr/tesseract) .
After the Installation it is **Fundamental** to check that the location of the Tesseract.exe file needed for the script to run is the same of the one written in the  `Tesseract_location.txt` text file; if it's not the same then edit the file writing the appropriate directory (Note: Double backlashes `\\` must be used). The default directory in the script is the default Windows directory for the .exe file, which is `C:\\Program Files\\Tesseract-OCR\\tesseract.exe`. For Linux users the default directory should be `/usr/bin/tesseract`.

As for `tkinter` it cannot be simply installed with pip. It's the library that allows the GUI and it can be installed following the [Instructions](https://tkdocs.com/tutorial/install.html) on the docs page for your operative system and for python, choosing the latest version.

## Usage:
To Run the script just open a console in the folder where the files have been downloaded and do:
```
python Seterra_TAS.py
```
Once you have run the script (assuming all previous steps have been completed), a window with containing buttons will appear:
https://imgur.com/a/MTmY6tl  

The first thing the user has to do is selecting the "box", a rectangle that surrounds the "click on " part of the seterra quiz **Including** a wide space, wide enough to fit all the possible words in the quiz; this box is needed as it's what Tesseract will read to know which country to click on. 

Afterwards the position of the **Restart** button must be given. After all this, the procedure of registering the various coordinates begins and the user must complete the quiz. The script has enough resilience that you can generally make as many mistakes as needed, without any complications. (Note: It's important that you **do not click too fast** as the script might not detect some clicks, making the script obsolete during the completion phase). 

Once you are done with the quiz, you should click "Play Again". After this, the script can start to automatically complete the quiz. ***It is important that you NEVER scroll down, move the browser window or put another window above the "click on" and "Restart" parts of the quiz at any point from the selection of the box to the completion of the map***. The meanings of the buttons are:

- Position 1: The first button you have to press. After you press this button you will need to click on the **top left corner** of the box.

 ![Step1](https://i.imgur.com/gBMEkL2.png)
- Position 2: It's the second button you have to press. After you press this button you will need to click on the **bottom right corner** of the box, it must not be above the coordinates you clicked for Position 1.

![Step2](https://i.imgur.com/BJdn0lP.png)
- Restart Button Position: It's the third button you have to press. After you press this you will need to click on the "Restart" button of the Seterra quiz.

![Step3](https://i.imgur.com/poydoHR.png)
- Map Places: It's the fourth button you have to press. After pressing this button the script will start registering the various quiz answers and you'll have to complete the quiz. Always restart the quiz before doing this step otherwise you'll risk not registering some values.

![Step4](https://i.imgur.com/u5UFFjH.png)
- Complete Map: it's the lasst button you have to press. It's the button that will start the completion of the quiz by the tool. After the completion you can complete the quiz again as many times you want as long as the position of the quiz is the same and all the requisites listed before are met.

![Step5](https://i.imgur.com/RFaMIca.png)
- Reset: Will Reset all values. It's highly suggested to press this button whenever you accidentally scroll down/up or move the window during the setup procedure (From Position 1 to Complete Map). It's also suggested to use it if you want to complete another quiz.

![Step6](https://i.imgur.com/DHRPRUo.png)
- Debug: A developer option. It'll print values on the console needed for debugging.

![Step7](https://i.imgur.com/MBh0cet.png)
## Video Explanation:
I also made a quick video to explain and demonstrate the script, click this [Link](https://youtu.be/psO7mF0Mgrc) to watch it.

## Additional Notes:
The script increases of performance with faster CPUs as Tesseract relies on it to read and analyze images; tesseract will also have problems if the resolution of your screen is too low and the words are too small. The script is probably really inefficient in terms of how it's written and it could be definitely optimized by anyone better than me at python. 
