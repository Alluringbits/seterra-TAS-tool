try:
        import pytesseract, pyautogui, time, difflib, re, os.path, sys
        from pynput.mouse import Listener
        from PIL import ImageGrab
        import tkinter as tk
        
except ModuleNotFoundError as ModuleError:
        print(f"ERROR!\nLooks Like you are missing this module:\n\n{str(ModuleError)[17:-1]}\n\nFor more information read the installation guide at https://github.com/Alluringbits/seterra-TAS-tool")
        quit()
        
det_pos = {"Temp" : "temp"}
end = False
RestartPressed = False
x0, x1, y0, y1, z0, z1 = 0, 0, 0, 0, 0, 0
word = None

if not os.path.exists(f"{open('Tesseract_location.txt', 'r+').read()}"):
        print("The Tesseract exe file doesn't exist OR the directory of the file is different than the default one (C:\\Program Files\\Tesseract-OCR\\tesseract.exe). Please change the directory to the appropriate one in the 'Tesseract_location.txt' file.")
        quit()
try:
        pytesseract.pytesseract.tesseract_cmd = f"{open('Tesseract_location.txt', 'r+').read()}"
except pytesseract.pytesseract.TesseractNotFoundError as PytesseractMissing:
        print("ERROR\nEither you didn't install Tesseract-OCR or 'str({PytesseractMissing}).replace(\"is not installed or it's not in your PATH\", \"\")' isn't the correct path for the Tesseract-OCR exe.")

window = tk.Tk()
def setbox1():
        def on_click(x, y, button, pressed):
                global y0, x0
                x0 = x
                y0 = y
                #print(x0, y0)
                time.sleep(0.2)
                return False
        with Listener(on_click=on_click) as listener:
                listener.join()
                
def setbox2():
        def on_click(x, y, button, pressed):
                global x1, y1
                x1 = x
                y1 = y
                #print(x1, y1)
                time.sleep(0.2)
                return False
        with Listener(on_click=on_click) as listener:
                listener.join()

def RestartButtonPos():
        def on_click(x, y, button, pressed):
                global z0, z1
                z0 = x
                z1 = y
                #print(z0, z1)
                time.sleep(0.2)
                return False
        with Listener(on_click=on_click) as listener:
                listener.join()
                
def GetWords():
        try:
                global word
                word = pytesseract.image_to_string(ImageGrab.grab(bbox=(x0, y0, x1, y1)))
                word = re.sub(r"\W+", "", word).lower().replace("clickon", "")
                word = "".join(i for i in word if not i.isdigit())
        except SystemError:
                print("The selected box is invalid. The order of the two positions is first the top left corner of the box, secondly the bottom right corner. The first always has to be above the second in terms of height")
        
def complete_map():
        try:
                global RestartPressed
                #print(RestartPressed, z0, z1)
                if not RestartPressed and z0 != 0 and z1 != 0:
                        pyautogui.click(x=int(z0), y=int(z1))
                        RestartPressed = True
                        time.sleep(0.2)
                GetWords()
                #print(det_pos.keys())
                #print(word)
                wordCheck = difflib.get_close_matches(word, det_pos.keys() , n=1, cutoff =0.8)
                if len(wordCheck) != 0:
                        #print(int(det_pos[wordCheck[0]][0:4].replace(" ", "")))
                        pyautogui.click(x=int(det_pos[wordCheck[0]][0:4].replace(" ", "")), y=int(det_pos[wordCheck[0]][-3:]))
                        complete_map()
                elif word == "":
                        RestartPressed = False
        except TypeError:
                print("No places have been selected.")
        except:
                print("The selected area is invalid")
                
def detect_mouse():
        global end
        try:
                while not end:
                        #print(x0, y0, x1, y1)
                        #print(det_pos)
                        GetWords()
                        if word == "":
                                end = True
                        else:
                                def on_click(x, y, button, pressed):
                                        global det_pos
                                        global word
                                        wordCheck = difflib.get_close_matches(word, det_pos.keys() , n=1, cutoff =0.9)
                                        if len(wordCheck) != 0:
                                                if len(str(x)) == 4:
                                                        det_pos[wordCheck[0]] = f"{x}{y}"
                                                else:
                                                        det_pos[wordCheck[0]] = f"{x} {y}"
                                        else:
                                                if len(str(x)) == 4:
                                                        det_pos[word] = f"{x}{y}"
                                                else:
                                                        det_pos[word] = f"{x} {y}"
                                        return False
                                with Listener(on_click=on_click) as listener:
                                        listener.join()
                                #print(det_pos)
                                time.sleep(0.2)
        except:
                print("You have to select the box region first through the position 1 and position 2 buttons")

def reset():
        global x0, x1, y0, y1, z0, z1, end, RestartPressed, det_pos
        det_pos = {"Temp" : "temp"}
        end = False
        x0, x1, y0, y1, z0, z1 = 0, 0, 0, 0, 0, 0
        RestartPressed = False
        print("All values have been reset to default.")

def debug():
        print("\n" + str(pytesseract.image_to_string("test.png")))
        GetWords()
        print(x0, x1, y0, y1, z0, z1)
        print("Restart Pressed: " + str(RestartPressed))
        print("end: " + str(end))
        print(det_pos)
        print(word)
        

tk.Label(text="Seterra TAS Tool", font="None, 15").pack()
tk.Button(text="Position 1", width=25, height=3, bg="white", font=(None, 15), command=setbox1).pack()
tk.Button(text="Position 2", width=25, height=3, bg="white", font=(None, 15), command=setbox2).pack()
tk.Button(text="Restart Button Position", width=25, height=3, bg="white", font=(None, 15), command=RestartButtonPos).pack()
tk.Button(text="Map places", width=25, height=3, bg="white", font=(None, 15), command=detect_mouse).pack()
tk.Button(text="Complete Map", width=25, height=3, bg="white", font=(None, 15), command=complete_map).pack()
tk.Button(text="Reset", width=25, height=3, bg="white", font=(None, 15), command=reset).pack()
tk.Button(text="Debug", width=25, height=3, bg="white", font=(None, 15), command=debug).pack()
window.mainloop()