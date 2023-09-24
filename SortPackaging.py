# Author: [Noureddine SHRIFFE]
# Date: [14th - Aug - 2023]
# Description: [Map the sorting process in plastic recycling in Luxembourg]

from SortLux import Main as SortLuxMain
from SortGerman import Main as SortGerMain
from Packaging import Packaging


class SortPackaging:    
    def __init__(self):
        self.P = Packaging()
        self.chooseCountry()

    def chooseCountry(self):
        while True:  
            country = input(
                "Which country would you like to go through? (Luxembourg, Germany): ")
            if country == "Luxembourg":
                SortLuxMain.process(self.P)
                break
            elif country == "Germany":
                SortGerMain.process(self.P)
                break  
            else:
                print(f"Country '{country}' is not recognized")

sort_package = SortPackaging()
