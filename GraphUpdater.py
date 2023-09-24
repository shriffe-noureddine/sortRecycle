# Author: [Noureddine SHRIFFE]
# Date: [12th - Aug - 2023]
# Description: [Graph for SortLux process with update in red color for any visited process]


from graphviz import Digraph

# Create edges based on the process flow
edges = [
    ('Main', 'Truck_Scale', None),
    ('Truck_Scale', 'Drum', None),

    # Drum relationships
    ('Drum', 'Drum_IronMagnet', 'main size < 6'),
    ('Drum', 'Drum_WindSifter', 'size < 30'),
    ('Drum', 'Drum_ManualSorting', 'size >= 30'),

    # Drum_WindSifter relationships
    ('Drum_WindSifter', 'WindSifter_NIR_PP', 'form = 2D'),
    ('Drum_WindSifter', 'WindSifter_Ferrous_nonFerrous', 'form = 3D or Tray'),

    # Drum_IronMagnet relationships
    ('Drum_IronMagnet', 'IRON', 'material = Iron'),
    ('Drum_IronMagnet', 'Aluminium', 'material = Aluminium'),
    ('Drum_IronMagnet', 'Remains_Middle', 'else'),

    # Drum_ManualSorting relationships
    ('Drum_ManualSorting', 'Remains_over', 'form = 3D or Tray'),
    ('Drum_ManualSorting', 'Foils_PE_and_others', 'form = 2D'),

    # WindSifter_Ferrous_nonFerrous relationships
    ('WindSifter_Ferrous_nonFerrous', 'IRON', 'material = Iron'),
    ('WindSifter_Ferrous_nonFerrous', 'Aluminium', 'material = Aluminium'),
    ('WindSifter_Ferrous_nonFerrous', 'NIR_PET', 'else'),

    # WindSifter_NIR_PP relationships
    ('WindSifter_NIR_PP', 'Foils_PP', 'material = PP'),
    ('WindSifter_NIR_PP', 'Foils_PE_and_others', 'else'),

    # NIR_PET relationships
    ('NIR_PET', 'Remains_Middle', 'label_size = sz > 50% or color = Carbon-Black'),
    ('NIR_PET', 'NIR_Transparent', 'material = PET'),
    ('NIR_PET', 'NIR_PP', 'else'),

    # NIR_PP relationships
    ('NIR_PP', 'PP', 'material = PP'),
    ('NIR_PP', 'NIR_PE', 'else'),

    # NIR_Transparent relationships
    ('NIR_Transparent', 'PET_Color', 'label_size = Sleeve'),
    ('NIR_Transparent', 'PET_Transparent', 'color = Transparent'),
    ('NIR_Transparent', 'NIR_GREEN_BLUE', 'else'),

    # NIR_GREEN_BLUE relationships
    ('NIR_GREEN_BLUE', 'PET_Green_Blue',
     'color in {Light Blue (t>Q), Dark Blue (t<Q), Green}'),
    ('NIR_GREEN_BLUE', 'NIR_Green_Blue_ManualSorting', 'else'),

    # NIR_Green_Blue_ManualSorting relationships
    ('NIR_Green_Blue_ManualSorting', 'PET_Color', 'form = Tray'),
    ('NIR_Green_Blue_ManualSorting', 'PET_Trays','else'),

    # The following classes all point to Other, based on your code
    ('IRON', 'Other', None),
    ('Aluminium', 'Other', None),
    ('Remains_over', 'Other', None),
    ('Foils_PE_and_others', 'Other', None),
    ('Foils_PP', 'Other', None),
    ('Remains_Middle', 'Other', None),
    ('PE', 'Other', None),
    ('PP', 'Other', None),

    # PET_Trays, PET_Color, PET_Green_Blue, and PET_Transparent all have further paths as well
    ('PET_Trays', 'Disposal', None),
    ('PET_Color', 'Energy_rec', None),
    ('PET_Green_Blue', 'Foam', None),
    ('PET_Transparent', 'BtB', None),

    # # Recycling
    # ('Rec_Main', 'Rec_BottlesStorage'),
    # ('Rec_BottlesStorage', 'Rec_Drum'),
    # ('Rec_Drum', 'Rec_NIR_PET'),

    # ('Rec_NIR_PET', 'Rec_Iron_Magnet'),
    # ('Rec_NIR_PET', 'Rec_OtherHill'),


    # ('Rec_Iron_Magnet', 'Rec_OtherHill'),
    # ('Rec_Iron_Magnet', 'Rec_Pre_Washing'),

    # ('Rec_Other', 'Rec_Main'),
    # ('Rec_OtherHill', 'Rec_Other'),

    # ('Rec_DisposalHill', 'Rec_Disposal'),

    # ('Rec_Pre_Washing', 'Rec_Granulator'),


    # ('Rec_Granulator', 'Rec_Washing'),

    # ('Rec_Washing', 'Rec_Swim_Sink'),

    # ('Rec_Swim_Sink', 'Rec_Granulator2'),

    # ('Rec_Granulator2', 'Rec_Flake_sorter'),

    # ('Rec_Flake_sorter', 'Rec_Extrusion'),

    # ('Rec_Cryst_polycond', 'Rec_R_PET_Granulates'),

    # ('Rec_Extrusion', 'Rec_Cryst_polycond'),

    # ('Rec_R_PET_Granulates', 'Rec_Perform'),


]


class GraphUpdater:
    def __init__(self):
        self.dot = Digraph('G', filename='process.gv')
        self.initialize_graph()

    def initialize_graph(self):
        for source, target, label in edges:
            if label:
                self.dot.edge(source, target, label=label)
            else:
                self.dot.edge(source, target)
        self.dot.save()

    def highlight_node(self, node_name):
        self.dot.node(node_name, color='red')
        # Save the updated dot file without rendering or viewing
        self.dot.save()
