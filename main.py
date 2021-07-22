from Automine import *
import time

# position = GetCoordinates()
# lst = position.cord()
# print(lst)       

coordinates = [(742, 857), (215, 352), (86, 351), (287, 84), (318, 52), (352, 52)]
search = ['python.org', 'youtube.com', 'Cyclotron', 'How does an aeroplane fly?', 'aplha particle']

new_tab = Automine("NewTab", coordinates[-1])
close_tab = Automine("CloseTab", coordinates[-2])
Automine.openBrowser("/Applications/Brave\ Browser.app/Contents/MacOS/Brave\ Browser")

while 1:
    time.sleep(2)
    new_tab.click(0)
    time.sleep(2)
    new_tab.search(search, 0.2)
    time.sleep(2)

    for i in range(5):
        new_tab.scroll(-100, coordinates[0][0], coordinates[0][1])
    for i in range(5):
        new_tab.scroll(100, coordinates[0][0], coordinates[0][1])

    close_tab.click(0)
    time.sleep(0.2)

    Automine.log("BatMinr/log")
    time.sleep(1)
