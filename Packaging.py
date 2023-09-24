# Author: [Noureddine SHRIFFE]
# Date: [09th - Aug - 2023]
# Description: [Map the sorting process in plastic recycling in Luxembourg]

class Packaging:
    name = None
    quality = 100
    result = ""
    NRG = 0
    WC = 0

    size = None,
    form = None,
    material = None,
    material_mixing = None,
    color = None

    closure_density = None,
    label_size = None,
    label_material = None,
    glue = None,
    ink = None,
    watermark = None

    form_options = {
        "1": "2D",
        "2": "3D",
        "3": "Tray"
    }

    material_options = {
        "1": "PET",
        "2": "PP",
        "3": "HDPE",
        "4": "LDPE",
        "5": "PS",
        "6": "Tetra-Pak",
        "7": "IRON",
        "8": "Aluminium",
        "9": "rPET",
        "10": "PE"
    }

    material_mixing_options = {
        "1": "Mono-Material",
        "2": "Barriers",
        "3": "Multi-Layers"
    }

    color_options = {
        "1": "Transparent",
        "2": "Light Blue (t>Q)",
        "3": "Dark Blue (t<Q)",
        "4": "Green",
        "5": "White",
        "6": "Carbon-Black",
        "7": "No-Color"
    }
    closure_density_options = {
        "1": "d < 1g/cm3",
        "2": "d > 1g/cm3",
        "3": "Metal"
    }

    label_size_options = {
        "1": "sz < 50%",
        "2": "sz > 50%",
        "3": "Sleeve"
    }

    label_material_options = {
        "1": "d < 1g/cm3",
        "2": "d > 1g/cm3",
        "3": "Paper",
        "4": "PVC"
    }

    glue_options = {
        "1": "Glue1 (easy s.)",
        "2": "Glue2 (medium s.)",
        "3": "Glue3 (difficult s.)",
        "4": "Glue4 (expensive)"
    }

    watermark_options = {
        "1": "YES",
        "2": "NO"
    }
    ink_options = {
        "1": "non_solvent",
        "2": "solvent"
    }

    def __init__(self):
        self.name = input("Packaging Name: ")

        while True:
            try:
                user_input = input("What size does the packaging have: ")
                self.size = int(user_input)
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        self.form = self.get_choice_key("form", self.form_options)
        self.material = self.get_choice_key("material", self.material_options)
        self.material_mixing = self.get_choice_key(
            "material mixing", self.material_mixing_options)
        self.color = self.get_choice_key("color", self.color_options)

        self.closure_density = self.get_choice_key(
            "closure density", self.closure_density_options)
        self.label_size = self.get_choice_key(
            "label size", self.label_size_options)
        self.label_material = self.get_choice_key(
            "label material", self.label_material_options)
        self.glue = self.get_choice_key(
            "glue", self.glue_options)
        self.ink = self.get_choice_key(
            "ink", self.ink_options)
        self.watermark = self.get_choice_key(
            "watermark", self.watermark_options)

        self.packagingDetails()

    def get_choice_key(self, choice_name, options):
        print(f"What {choice_name} does the packaging have:")
        for key, value in options.items():
            print(f"\t{key}] {value}")

        user_input = input()

        while user_input not in options:
            print(f"Invalid choice. Choose a valid {choice_name}:")
            user_input = input()

        return user_input

    def recommendations(self):
        recommendation = "RECOMENDATIONS: Ensure the following:\n"
        has_recommendation = False  # Flag to track if any recommendation is added

        if self.size < 6 or self.size >= 30:
            recommendation += "size: middle\n"
            has_recommendation = True
        if self.form == "1":
            recommendation += "form: 3D or Tray\n"
            has_recommendation = True
        if self.material != "1":
            recommendation += "material: PET\n"
            has_recommendation = True
        if self.color != "1":
            recommendation += "color: transparent\n"
            has_recommendation = True
        if self.label_size != "1":
            recommendation += "label size: < 50%\n"
            has_recommendation = True
        if self.closure_density in {'2', '3'}:
            recommendation += "closure density: d < 1g/cm3\n"
            has_recommendation = True
        if self.label_material in {'2', '4'}:
            recommendation += "label material: d < 1g/cm3 or Paper\n"
            has_recommendation = True
        if self.label_material == "3":
            recommendation += "label material: d < 1g/cm3\n"
            has_recommendation = True
        if self.material_mixing == "2":
            recommendation += "material_mixing: Mono-Material\n"
            has_recommendation = True
        if self.material_mixing == "3":
            recommendation += "material_mixing: Mono-Material or Barriers\n"
            has_recommendation = True
        if self.ink == "1":
            recommendation += "ink: solvent\n"
            has_recommendation = True
        if self.label_size == "3":
            recommendation += "label_size: sz < 50%\n"
            has_recommendation = True

        if not has_recommendation:
            recommendation = ""  # If no recommendations, set the string to empty

        return recommendation

    def packagingDetails(self):
        print("Packaging Details:")
        print(f"Name: {self.name}")
        print(f"Main Body Options:")
        print(f"Size: {self.size}")
        print(f"Form: {self.form_options[self.form]}")
        print(f"Material: {self.material_options[self.material]}")
        print(
            f"Material Mixing: {self.material_mixing_options[self.material_mixing]}")
        print(f"Color: {self.color_options[self.color]}")
        print(f"Closure System Details:")
        print(
            f"Closure Density: {self.closure_density_options[self.closure_density]}")
        print(f"sub_system Details:")
        print(f"Label Size: {self.label_size_options[self.label_size]}")
        print(
            f"Label Material: {self.label_material_options[self.label_material]}")
        print(f"Glue: {self.glue_options[self.glue]}")
        print(f"Ink: {self.ink_options[self.ink]}")
        print(f"Watermark: {self.watermark_options[self.watermark]}")
