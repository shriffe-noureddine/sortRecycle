# Author: [Noureddine SHRIFFE]
# Date: [09th - Aug - 2023]
# Description: [Map the sorting process in plastic recycling in Luxembourg]

class Main:
    endRecycle = "FROM RECYCLE: "
    @staticmethod
    def process(P):
        BottlesStorage.process(P)
        print(Main.endRecycle)
        
############################################################################################


class BottlesStorage:

    @staticmethod
    def process(P):
        P.result += BottlesStorage.__name__ + "-> "
        Drum.process(P)

############################################################################################


class Drum:

    @staticmethod
    def process(P):
        P.result += Drum.__name__ + "-> "
        NIR_PET.process(P)

############################################################################################

class NIR_PET:

    @staticmethod
    def process(P):
        P.result += NIR_PET.__name__ + "-> "
        if P.material == "1":
            return Iron_Magnet.process(P)
        else:
            return OtherHill.process(P)

###########################################################################################

class Iron_Magnet:

    @staticmethod
    def process(P):
        P.result += Iron_Magnet.__name__ + "-> "
        if P.material in {"7", "8"}:
            return OtherHill.process(P)
        else:
            return Pre_Washing.process(P)

############################################################################################

class Other:
    @staticmethod
    def process(P):
        P.result += Other.__name__ + "-> "
        Main.endRecycle+="W: 85% | D: 25 km | DF: 2/week | Quality: "+str(P.quality)+ "% | NRG: "+ str(P.NRG)
        
############################################################################################

class OtherHill(Other):

    @staticmethod
    def process(P):
        P.result += OtherHill.__name__ + "-> "
        Other.process(P)

############################################################################################

class Disposal:
    @staticmethod
    def process(P):
        P.result += Disposal.__name__ + "-> "
        Main.endRecycle += "W: 85% | D: 30 km | DF: 1/week | Quality: " + \
            str(P.quality) + "% | NRG: " + str(P.NRG)

############################################################################################

class DisposalHill(Disposal):
    @staticmethod
    def process(P):
        P.result += DisposalHill.__name__ + "-> "
        Disposal.process(P)

############################################################################################

class Pre_Washing:

    @staticmethod
    def process(P):
        P.result += Pre_Washing.__name__ + "-> "
        if P.glue == "1":
            P.WC += 0.9
            P.NRG += 90
            P.label_material = None
        return Granulator.process(P)

############################################################################################

class Granulator:

    @staticmethod
    def process(P):
        P.result += Granulator.__name__ + "-> "
        if P.closure_density == "3":
            P.WC += 0.1
            P.NRG += 100
            P.quality -= 25
        return Washing.process(P)

############################################################################################

class Washing:

    @staticmethod
    def process(P):
        P.result += Washing.__name__ + "-> "
        Swim_Sink.process(P)

############################################################################################

class Swim_Sink:

    @staticmethod
    def process(P):
        P.result += Swim_Sink.__name__ + "-> "
        if P.closure_density == "2":
            P.WC += 1.1
            P.NRG += 110
            P.quality -= 25
        if P.label_material == "2":
            P.quality -= 25
        if P.ink == "1":
            P.quality -= 10
        if P.label_size == "3":
            P.quality -= 10
        return Granulator2.process(P)

############################################################################################

class Granulator2:

    @staticmethod
    def process(P):
        P.result += Granulator2.__name__ + "-> "
        Flake_sorter.process(P)
        
############################################################################################

class Flake_sorter:

    @staticmethod
    def process(P):
        P.result += Flake_sorter.__name__ + "-> "
        P.NRG += 10
        Extrusion.process(P)
        
############################################################################################

class Cryst_polycond:

    @staticmethod
    def process(P):
        P.result += Cryst_polycond.__name__ + "-> "
        P.WC += 0.1
        P.NRG += 140
        R_PET_Granulates.process(P)
        
############################################################################################

class Extrusion:

    @staticmethod
    def process(P):
        P.result += Extrusion.__name__ + "-> "
        if P.material_mixing == "2":
            P.quality -= 10
            P.WC += 0.3
            P.NRG += 130
        if P.material_mixing == "3":
            P.quality -= 25
            P.WC += 0.3
            P.NRG += 130
        if P.label_material == "3":
            P.quality -= 10
            P.WC += 0.3
            P.NRG += 130
        if P.label_material == "4":
            P.quality -= 25
            P.WC += 0.3
            P.NRG += 130
        return Cryst_polycond.process(P)
    
############################################################################################

class Perform:
    @staticmethod
    def process(P):
        P.result += Perform.__name__ + "-> "
        Main.endRecycle+="W: 100% | D: 100 km | DF: 2/month | Quality: "+str(P.quality)+ "% | NRG: " + str(P.NRG)
        
############################################################################################

class R_PET_Granulates(Perform):
    @staticmethod
    def process(P):
        P.result += R_PET_Granulates.__name__ + "-> "
        Perform.process(P)
        
############################################################################################