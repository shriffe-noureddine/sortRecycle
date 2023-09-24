# Author: [Noureddine SHRIFFE]
# Date: [14th - Aug - 2023]
# Description: [Map the sorting process in plastic recycling in Germany]

class Main:
    endSorting = "FROM SORTING: "

    @staticmethod
    def process(P):
        Bag_Opener.process(P)
        print(P.result)

############################################################################################


class Bag_Opener:

    @staticmethod
    def process(P):
        P.result += Bag_Opener.__name__ + "-> "
        Drum1.process(P)

############################################################################################


class Drum1:

    @staticmethod
    def process(P):
        P.result += Drum1.__name__ + "-> "
        if P.size < 22.5:
            return Drum2.process(P)
        elif P.size >= 22.5:
            return WindSifter2.process(P)


############################################################################################


class Drum2:

    @staticmethod
    def process(P):
        P.result += Drum2.__name__ + "-> "
        if P.size >= 15:
            return WindSifter1.process(P)
        elif P.size < 15:
            return Drum3.process(P)
############################################################################################


class WindSifter1:

    @staticmethod
    def process(P):
        P.result += WindSifter1.__name__ + "-> "
        if P.form == "1":
            return PGA_Seperator.process(P)
        elif P.form in {'2', '3'}:
            return Magnetic_Seperator1.process(P)

############################################################################################


class WindSifter2:

    @staticmethod
    def process(P):
        P.result += WindSifter2.__name__ + "-> "
        if P.form == "1":
            return Re_Sorting_Up.process(P)
        elif P.form in {'2', '3'}:
            return Drum1.process(P)
############################################################################################


class Drum3:

    @staticmethod
    def process(P):
        P.result += Drum3.__name__ + "-> "
        if 6 < P.size < 15:
            return WindSifter3.process(P)
        elif P.size <= 6:
            return Vibrating_Sieve.process(P)

############################################################################################


class Magnetic_Seperator1:

    @staticmethod
    def process(P):
        P.result += Magnetic_Seperator1.__name__ + "-> "
        if P.material == "6":
            return Can_Press.process(P)
        else:
            return FKN1.process(P)


############################################################################################


class PGA_Seperator:

    @staticmethod
    def process(P):
        P.result += PGA_Seperator.__name__ + "-> "
        if P.material == "?":
            return FKN2.process(P)
        else:
            return Plastics_Mix.process(P)
############################################################################################


class Plastics_Mix:

    @staticmethod
    def process(P):
        P.result += Plastics_Mix.__name__ + "-> "

############################################################################################


class FKN2:

    @staticmethod
    def process(P):
        P.result += FKN2.__name__ + "-> "
        if P.material == "?":
            return WindSifter4.process(P)
        else:
            return Foucault_Current_Seperator2.process(P)

############################################################################################


class FKN1:

    @staticmethod
    def process(P):
        P.result += FKN1.__name__ + "-> "
        if P.material == "?":
            return FKN.process(P)
        else:
            return Foucault_Current_Seperator1.process(P)

############################################################################################


class Can_Press:

    @staticmethod
    def process(P):
        P.result += Can_Press.__name__ + "-> "
        Tin_Plate.process(P)
############################################################################################


class Tin_Plate:

    @staticmethod
    def process(P):
        P.result += Tin_Plate.__name__ + "-> "

############################################################################################


class FKN:

    @staticmethod
    def process(P):
        P.result += FKN.__name__ + "-> "

############################################################################################


class Foucault_Current_Seperator1:

    @staticmethod
    def process(P):
        P.result += Foucault_Current_Seperator1.__name__ + "-> "
        if P.material == "8":
            return Aluminium.process(P)
        else:
            return NIR_Plastics.process(P)
############################################################################################


class Foucault_Current_Seperator2:

    @staticmethod
    def process(P):
        P.result += Foucault_Current_Seperator2.__name__ + "-> "
        if P.material == '8':
            return Aluminium.process(P)
        else: NIR_Plastics3.process(P)

############################################################################################


class NIR_Plastics:

    @staticmethod
    def process(P):
        P.result += NIR_Plastics.__name__ + "-> "
        if P.material in {'1', '2', '5', '10'}:
            return Ballistic_Seperator1.process(P)
        else:
            return NIR_Plastics2.process(P)
############################################################################################


class Ballistic_Seperator1:

    @staticmethod
    def process(P):
        P.result += Ballistic_Seperator1.__name__ + "-> "
        if P.form == '1':
            return NIR_Plastics4.process(P)
        elif P.form in {'2', '3'}:
            return PE_Seperator.process(P)
############################################################################################


class NIR_Plastics2:
    @staticmethod
    def process(P):
        P.result += NIR_Plastics2.__name__ + "-> "
        if P.material == '?':
            return NIR_Plastics3.process(P)
        else:
            return Resources_Seperator.process(P)
############################################################################################

class NIR_Plastics3:

    @staticmethod
    def process(P):
        P.result += NIR_Plastics3.__name__ + "-> "
        if P.material in {'1', '2', '5', '10'}:
            return Ballistic_Seperator1.process(P)
############################################################################################


class Resources_Seperator:

    @staticmethod
    def process(P):
        P.result += Resources_Seperator.__name__ + "-> "
        if P.material == '?':
            FKN2.process(P)
        else: 
            return PPK_Seperator.process(P)
############################################################################################


class PPK_Seperator:

    @staticmethod
    def process(P):
        P.result += PPK_Seperator.__name__ + "-> "
        if P.material == '2':
            return Remains_Middle.process(P)
        elif P.material == '3':
            return PPK.process(P)
############################################################################################


class Remains_Middle:

    @staticmethod
    def process(P):
        P.result += Remains_Middle.__name__ + "-> "
############################################################################################


class PPK:

    @staticmethod
    def process(P):
        P.result += PPK.__name__ + "-> "
############################################################################################


class NIR_Plastics4:

    @staticmethod
    def process(P):
        P.result += NIR_Plastics4.__name__ + "-> "
        if P.material == '?':
            return Remains_Middle.process(P)
        else:
            return Plastics_Mix.process(P)
############################################################################################


class Plastics_Mix:

    @staticmethod
    def process(P):
        P.result += Plastics_Mix.__name__ + "-> "

############################################################################################

############################################################################################


class PE_Seperator:

    @staticmethod
    def process(P):
        P.result += PE_Seperator.__name__ + "-> "
        if P.material == "10":
            return Re_Sorting_Down.process(P)
        else:
            return PP_Seperator.process(P)
############################################################################################


class PP_Seperator:

    @staticmethod
    def process(P):
        P.result += PP_Seperator.__name__ + "-> "
        if P.material == "2":
            return Re_Sorting_Down.process(P)
        else:
            return PET_Seperator.process(P)
############################################################################################


class PET_Seperator:

    @staticmethod
    def process(P):
        P.result += PET_Seperator.__name__ + "-> "
        if P.material == "1":
            return Re_Sorting_Down.process(P)
        else:
            return PS_Seperator.process(P)
############################################################################################


class Re_Sorting_Down:

    @staticmethod
    def process(P):
        P.result += Re_Sorting_Down.__name__ + "-> "
        if P.material == '1':
            return PET.process(P)
        elif P.material == '2':
            return PP.process(P)
        elif P.material == '10':
            return Sort_PE.process(P)
############################################################################################


class PET:

    @staticmethod
    def process(P):
        P.result += PET.__name__ + "-> "

############################################################################################


class PP:

    @staticmethod
    def process(P):
        P.result += PP.__name__ + "-> "

############################################################################################


class Sort_PE:

    @staticmethod
    def process(P):
        P.result += Sort_PE.__name__ + "-> "


############################################################################################


class PS_Seperator:

    @staticmethod
    def process(P):
        P.result += PS_Seperator.__name__ + "-> "
        if P.material == '5':
            return PS.process(P)

############################################################################################


class PS:

    @staticmethod
    def process(P):
        P.result += PS.__name__ + "-> "


############################################################################################
class Re_Sorting_Up:

    @staticmethod
    def process(P):
        P.result += Re_Sorting_Up.__name__ + "-> "
        if P.form == '1':
            return Foils.process(P)
        else:
            return Remains_Middle.process(P)
############################################################################################


class WindSifter3:

    @staticmethod
    def process(P):
        P.result += WindSifter3.__name__ + "-> "
        if P.form == "2":
            return Magnetic_Seperator2.process(P)
############################################################################################


class Vibrating_Sieve:

    @staticmethod
    def process(P):
        P.result += Vibrating_Sieve.__name__ + "-> "
        if P.size < 2:
            return Remains_Small.process(P)
        else: Magnetic_Seperator2.process(P)
############################################################################################


class Foils:

    @staticmethod
    def process(P):
        P.result += Foils.__name__ + "-> "
############################################################################################


class Magnetic_Seperator2:

    @staticmethod
    def process(P):
        #FE stands for iron
        P.result += Magnetic_Seperator2.__name__ + "-> "
        if P.material == "7":
            return Can_Press.process(P)
        else: 
            return FKN2.process(P)
############################################################################################


class Remains_Small:

    @staticmethod
    def process(P):
        P.result += Remains_Small.__name__ + "-> "
############################################################################################


class WindSifter4:

    @staticmethod
    def process(P):
        P.result += WindSifter4.__name__ + "-> "
        return FKN.process(P)

############################################################################################


class Aluminium:

    @staticmethod
    def process(P):
        P.result += Aluminium.__name__ + "-> "

############################################################################################
