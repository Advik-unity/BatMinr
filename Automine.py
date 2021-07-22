import pyautogui, datetime, keyboard, time, random, os

class GetCoordinates:
    @staticmethod
    def cord() -> list:
        cords = []
        while 1:
            if keyboard.is_pressed('q'):
                print("Coordinates Taken! ;)")
                break
        
            elif keyboard.is_pressed('s'):
                x, y = pyautogui.position()
                time.sleep(0.3)
                cords.append((x,y))
                print(x,y)
        return cords

class Automine():
    def __init__(self, name, coordinates):
        self.name = name
        self.x, self.y = coordinates[0], coordinates[1]
        self.coordinates = (self.x, self.y)

    def details(self) -> str:
        """Prints the details of the object"""
        print(self.name, self.coordinates)
        
    def click(self, interval) -> None:
        pyautogui.click(self.x, self.y, clicks=1, interval=interval)

    @staticmethod
    def log(filepath, ext="txt"):
        """Makes a File and stores your history"""
        with open(f"{filepath}.{ext}", "a") as f:
            f.write(f"{datetime.datetime.now()}:: Successfully CLicked!\n")
    
    def search(self, searches, interval) -> str:
        """This func takes a list of searches and randomly searches things in the list"""
        searches = random.choice(searches)
        pyautogui.click(x=self.x, y=self.y)
        time.sleep(2)
        pyautogui.write(searches, interval=interval)
        time.sleep(0.2)
        pyautogui.hotkey('Enter')

    def scroll(self, scrollAmt, x, y) -> None:
        """Use '-' with scrollAmt if u want to scroll in downwards direction"""
        pyautogui.scroll(scrollAmt ,x, y)

    def idle(self):
        """This function idles on the opened tab"""
        pyautogui.moveTo((self.x + random.randrange(20, 500)), (self.y + random.randrange(20, 500)))
        time.sleep(random.randrange(2,7))
        pyautogui.moveTo((self.x + random.randrange(20, 500)), (self.y + random.randrange(20, 500)))
        time.sleep(random.randrange(1,6))
        


    
    @staticmethod
    def openBrowser(browserpath) -> None:
        """Tries To open your browser"""
        try:
            try:
                os.system(browserpath)
            except:
                print("Cannot Open The Browser! ")
        except:
            print("Cannot Open Broswer")
    

if __name__ == '__main__':
    new_tab = Automine("New Tab", (200, 600))
    new_tab.details()