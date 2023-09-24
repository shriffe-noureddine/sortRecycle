# Author: [Noureddine SHRIFFE]
# Date: [12th - Aug - 2023]
# Description: [Map the sorting process in plastic recycling in Luxembourg]

from GraphUpdater import GraphUpdater
from RecycleLux import Main as RecMainLux

graph_updater = GraphUpdater()


class Main:
    endSorting = "FROM SORTING: "
    @staticmethod
    def process(P):
        graph_updater.highlight_node(Main.__name__)
        Truck_Scale.process(P)
        print(P.result)
        print(P.recommendations())
############################################################################################


class Truck_Scale:

    @staticmethod
    def process(P):
        graph_updater.highlight_node(Truck_Scale.__name__)
        P.result += Truck_Scale.__name__ + "-> "
        Drum.process(P)
        
############################################################################################


class Drum:

    @staticmethod
    def process(P):
        graph_updater.highlight_node(Drum.__name__)

        P.NRG += 3
        P.result += Drum.__name__ + "-> "
        if P.size < 6:
            return Drum_IronMagnet.process(P)
        elif 6 <= P.size < 30:
            return Drum_WindSifter.process(P)
        elif P.size >= 30:
            return Drum_ManualSorting.process(P)

############################################################################################


class Drum_WindSifter:

    @staticmethod
    def process(P):
        graph_updater.highlight_node(Drum_WindSifter.__name__)

        P.NRG += 4.5
        P.result += Drum_WindSifter.__name__ + "-> "

        if P.form == "1":
            return WindSifter_NIR_PP.process(P)
        elif P.form == "2":
            return WindSifter_Ferrous_nonFerrous.process(P)
        elif P.form == "3":
            return WindSifter_Ferrous_nonFerrous.process(P)

############################################################################################


class Drum_IronMagnet:

    @staticmethod
    def process(P):
        graph_updater.highlight_node(Drum_IronMagnet.__name__)

        P.result += Drum_IronMagnet.__name__ + "-> "
        if P.material == "7":
            P.NRG += 3.5
            return IRON.process(P)
        elif P.material == "8":
            P.NRG += 3.5
            return Aluminium.process(P)
        else:
            return Remains_Middle.process(P)

############################################################################################


class Drum_ManualSorting:

    @staticmethod
    def process(P):
        graph_updater.highlight_node(Drum_ManualSorting.__name__)

        P.result += Drum_ManualSorting.__name__ + "-> "
        # Foils is 2D (option 1)
        if P.form in {'2', '3'}:
            return Remains_over.process(P)
        elif P.form == "1":
            return Foils_PE_and_others.process(P)

############################################################################################


class WindSifter_Ferrous_nonFerrous:

    @staticmethod
    def process(P):
        graph_updater.highlight_node(
            WindSifter_Ferrous_nonFerrous.__name__)

        P.result += WindSifter_Ferrous_nonFerrous.__name__ + "-> "
        if P.material == "7":
            P.NRG += 3.5
            return IRON.process(P)
        elif P.material == "8":
            P.NRG += 3.5
            return Aluminium.process(P)
        else:
            return NIR_PET.process(P)

############################################################################################


class WindSifter_NIR_PP:

    @staticmethod
    def process(P):
        graph_updater.highlight_node(WindSifter_NIR_PP.__name__)

        P.result += WindSifter_NIR_PP.__name__ + "-> "

        if P.material == "2":
            return Foils_PP.process(P)
        else:
            return Foils_PE_and_others.process(P)

############################################################################################


class Other:
    @staticmethod
    def process(P):
        graph_updater.highlight_node(Other.__name__)

        P.result += Other.__name__ + "-> "
        Main.endSorting += "W: 95% | D: N/A km | DF: 1/week | NRG " + \
            str(P.NRG)
        print(Main.endSorting)
        
############################################################################################


class IRON(Other):
        
    @staticmethod
    def process(P):
        graph_updater.highlight_node(IRON.__name__)

        P.result += IRON.__name__ + "-> "
        Other.process(P)

############################################################################################


class Aluminium(Other):

    @staticmethod
    def process(P):
        graph_updater.highlight_node(Aluminium.__name__)

        P.result += Aluminium.__name__ + "-> "
        Other.process(P)

############################################################################################


class Remains_over(Other):
        
    @staticmethod
    def process(P):
        graph_updater.highlight_node(Remains_over.__name__)

        P.result += Remains_over.__name__ + "-> "
        Other.process(P)

############################################################################################


class Foils_PE_and_others(Other):

    @staticmethod
    def process(P):
        graph_updater.highlight_node(Foils_PE_and_others.__name__)

        P.result += Foils_PE_and_others.__name__ + "-> "
        Other.process(P)

############################################################################################


class Foils_PP(Other):

    @staticmethod
    def process(P):
        graph_updater.highlight_node(Foils_PP.__name__)

        P.result += Foils_PP.__name__ + "-> "
        Other.process(P)

############################################################################################


class Remains_Middle(Other):

    @staticmethod
    def process(P):
        graph_updater.highlight_node(Remains_Middle.__name__)

        P.result += Remains_Middle.__name__ + "-> "
        Other.process(P)

############################################################################################

class PE(Other):

    @staticmethod
    def process(P):
        graph_updater.highlight_node(PE.__name__)

        P.result += PE.__name__ + "-> "
        Other.process(P)
        
############################################################################################

class PP(Other):

    @staticmethod
    def process(P):
        graph_updater.highlight_node(PP.__name__)

        P.result += PP.__name__ + "-> "
        Other.process(P)
        
############################################################################################

class Disposal:
    @staticmethod
    def process(P):
        graph_updater.highlight_node(Disposal.__name__)

        P.result += Disposal.__name__ + "-> "
        Main.endSorting += "W: 90% | D: 30 km | DF: 2/month | NRG " + \
            str(P.NRG)
        print(Main.endSorting)
############################################################################################

class PET_Trays(Disposal):

    @staticmethod
    def process(P):
        graph_updater.highlight_node(PET_Trays.__name__)

        P.result += PET_Trays.__name__ + "-> "
        Disposal.process(P)
        
############################################################################################

class Energy_rec:
    @staticmethod
    def process(P):
        graph_updater.highlight_node(Energy_rec.__name__)

        P.result += Energy_rec.__name__ + "-> "
        Main.endSorting += "W: 90% | D: 35 km | DF: 2/month | NRG " + \
            str(P.NRG)

############################################################################################

class PET_Color(Energy_rec):

    @staticmethod
    def process(P):
        graph_updater.highlight_node(PET_Color.__name__)

        P.result += PET_Color.__name__ + "-> "
        Energy_rec.process(P)
        
############################################################################################

class Foam:
    @staticmethod
    def process(P):
        graph_updater.highlight_node(Foam.__name__)

        P.result += Foam.__name__ + "-> "
        Main.endSorting += "W: 95% | D: 90 km | DF: 2/month | NRG " + \
            str(P.NRG)
        print(Main.endSorting)
        
############################################################################################

class PET_Green_Blue(Foam):
        
    @staticmethod
    def process(P):
        graph_updater.highlight_node(PET_Green_Blue.__name__)

        P.result += PET_Green_Blue.__name__ + "-> "
        Foam.process(P)
        
############################################################################################

class BtB: 

    @staticmethod
    def process(P):
        graph_updater.highlight_node(BtB.__name__)

        P.result += BtB.__name__ + "-> "
        Main.endSorting += "W: 95% | D: 300 km | DF: 1/week | NRG " + \
            str(P.NRG)
        print(Main.endSorting)
        RecMainLux.process(P)
        
############################################################################################


class PET_Transparent(BtB):

    @staticmethod
    def process(P):
        graph_updater.highlight_node(PET_Transparent.__name__)

        P.result += PET_Transparent.__name__ + "-> "
        BtB.process(P)
        
############################################################################################

class NIR_PET:

    @staticmethod
    def process(P):
        graph_updater.highlight_node(NIR_PET.__name__)

        P.result += NIR_PET.__name__ + "-> "
        if P.label_size == "2" or P.color == "6":
            return Remains_Middle.process(P)
        elif P.material == "1":
            P.NRG += 3
            return NIR_Transparent.process(P)
        else:
            P.NRG += 3
            return NIR_PP.process(P)

############################################################################################

class NIR_PP:

    @staticmethod
    def process(P):
        graph_updater.highlight_node(NIR_PP.__name__)

        P.result += NIR_PP.__name__ + "-> "
        if P.material == "2":
            return PP.process(P)
        else:
            return NIR_PE.process(P)

############################################################################################


class NIR_Transparent:

    @staticmethod
    def process(P):
        graph_updater.highlight_node(NIR_Transparent.__name__)

        P.result += NIR_Transparent.__name__ + "-> "

        if P.label_size == "3":
            return PET_Color.process(P)
        elif P.color == "1":
            P.NRG += 3
            return PET_Transparent.process(P)
        else:
            P.NRG += 3
            return NIR_GREEN_BLUE.process(P)
        
############################################################################################


class NIR_PE:

    @staticmethod
    def process(P): 
        graph_updater.highlight_node(NIR_PE.__name__)

        P.result += NIR_PE.__name__ + "-> "
        if P.material == "10":
            return PE.process(P)
        else:
            return Remains_Middle.process(P)

############################################################################################


class NIR_GREEN_BLUE:

    @staticmethod
    def process(P):
        graph_updater.highlight_node(NIR_GREEN_BLUE.__name__)

        P.result += NIR_GREEN_BLUE.__name__ + "-> "
        if P.color in {"2", "3", "4"}:
            return PET_Green_Blue.process(P)
        else:
            return NIR_Green_Blue_ManualSorting.process(P)

############################################################################################

class NIR_Green_Blue_ManualSorting:

    @staticmethod
    def process(P):
        graph_updater.highlight_node(
            NIR_Green_Blue_ManualSorting.__name__)

        P.NRG += 1.5
        P.result += NIR_Green_Blue_ManualSorting.__name__ + "-> "
        if P.form in {'1', '2'}:
            return PET_Color.process(P)
        else:
            return PET_Trays.process(P)

############################################################################################