class PeriodicTable:
    def __init__(self):
        self.elements = {
            1: {"symbol": "H", "name": "Hydrogen", "atomic_mass": 1.008},
            2: {"symbol": "He", "name": "Helium", "atomic_mass": 4.0026},
            3: {"symbol": "Li", "name": "Lithium", "atomic_mass": 6.94},
            4: {"symbol": "Be", "name": "Beryllium", "atomic_mass": 9.0122},
            5: {"symbol": "B", "name": "Boron", "atomic_mass": 10.81},
            6: {"symbol": "C", "name": "Carbon", "atomic_mass": 12.011},
            7: {"symbol": "N", "name": "Nitrogen", "atomic_mass": 14.007},
            8: {"symbol": "O", "name": "Oxygen", "atomic_mass": 15.999},
            9: {"symbol": "F", "name": "Fluorine", "atomic_mass": 18.998},
            10: {"symbol": "Ne", "name": "Neon", "atomic_mass": 20.18},
            11: {"symbol": "Na", "name": "Sodium", "atomic_mass": 22.99},
            12: {"symbol": "Mg", "name": "Magnesium", "atomic_mass": 24.305},
            13: {"symbol": "Al", "name": "Aluminum", "atomic_mass": 26.982},
            14: {"symbol": "Si", "name": "Silicon", "atomic_mass": 28.085},
            15: {"symbol": "P", "name": "Phosphorus", "atomic_mass": 30.974},
            16: {"symbol": "S", "name": "Sulfur", "atomic_mass": 32.06},
            17: {"symbol": "Cl", "name": "Chlorine", "atomic_mass": 35.45},
            18: {"symbol": "Ar", "name": "Argon", "atomic_mass": 39.948},
            19: {"symbol": "K", "name": "Potassium", "atomic_mass": 39.098},
            20: {"symbol": "Ca", "name": "Calcium", "atomic_mass": 40.078},
            21: {"symbol": "Sc", "name": "Scandium", "atomic_mass": 44.956},
            22: {"symbol": "Ti", "name": "Titanium", "atomic_mass": 47.867},
            23: {"symbol": "V", "name": "Vanadium", "atomic_mass": 50.942},
            24: {"symbol": "Cr", "name": "Chromium", "atomic_mass": 51.996},
            25: {"symbol": "Mn", "name": "Manganese", "atomic_mass": 54.938},
            26: {"symbol": "Fe", "name": "Iron", "atomic_mass": 55.845},
            27: {"symbol": "Co", "name": "Cobalt", "atomic_mass": 58.933},
            28: {"symbol": "Ni", "name": "Nickel", "atomic_mass": 58.693},
            29: {"symbol": "Cu", "name": "Copper", "atomic_mass": 63.546},
            30: {"symbol": "Zn", "name": "Zinc", "atomic_mass": 65.38},
            31: {"symbol": "Ga", "name": "Gallium", "atomic_mass": 69.723},
            32: {"symbol": "Ge", "name": "Germanium", "atomic_mass": 72.63},
            33: {"symbol": "As", "name": "Arsenic", "atomic_mass": 74.922},
            34: {"symbol": "Se", "name": "Selenium", "atomic_mass": 78.971},
            35: {"symbol": "Br", "name": "Bromine", "atomic_mass": 79.904},
            36: {"symbol": "Kr", "name": "Krypton", "atomic_mass": 83.798},
            37: {"symbol": "Rb", "name": "Rubidium", "atomic_mass": 85.468},
            38: {"symbol": "Sr", "name": "Strontium", "atomic_mass": 87.62},
            39: {"symbol": "Y", "name": "Yttrium", "atomic_mass": 88.906},
            40: {"symbol": "Zr", "name": "Zirconium", "atomic_mass": 91.224},
            41: {"symbol": "Nb", "name": "Niobium", "atomic_mass": 92.906},
            42: {"symbol": "Mo", "name": "Molybdenum", "atomic_mass": 95.95},
            43: {"symbol": "Tc", "name": "Technetium", "atomic_mass": 98},
            44: {"symbol": "Ru", "name": "Ruthenium", "atomic_mass": 101.07},
            45: {"symbol": "Rh", "name": "Rhodium", "atomic_mass": 102.91},
            46: {"symbol": "Pd", "name": "Palladium", "atomic_mass": 106.42},
            47: {"symbol": "Ag", "name": "Silver", "atomic_mass": 107.87},
            48: {"symbol": "Cd", "name": "Cadmium", "atomic_mass": 112.41},
            49: {"symbol": "In", "name": "Indium", "atomic_mass": 114.82},
            50: {"symbol": "Sn", "name": "Tin", "atomic_mass": 118.71},
            51: {"symbol": "Sb", "name": "Antimony", "atomic_mass": 121.76},
            52: {"symbol": "Te", "name": "Tellurium", "atomic_mass": 127.6},
            53: {"symbol": "I", "name": "Iodine", "atomic_mass": 126.9},
            54: {"symbol": "Xe", "name": "Xenon", "atomic_mass": 131.29},
            55: {"symbol": "Cs", "name": "Cesium", "atomic_mass": 132.91},
            56: {"symbol": "Ba", "name": "Barium", "atomic_mass": 137.33},
            57: {"symbol": "La", "name": "Lanthanum", "atomic_mass": 138.91},
            58: {"symbol": "Ce", "name": "Cerium", "atomic_mass": 140.12},
            59: {"symbol": "Pr", "name": "Praseodymium", "atomic_mass": 140.91},
            60: {"symbol": "Nd", "name": "Neodymium", "atomic_mass": 144.24},
            61: {"symbol": "Pm", "name": "Promethium", "atomic_mass": 145},
            62: {"symbol": "Sm", "name": "Samarium", "atomic_mass": 150.36},
            63: {"symbol": "Eu", "name": "Europium", "atomic_mass": 151.96},
            64: {"symbol": "Gd", "name": "Gadolinium", "atomic_mass": 157.25},
            65: {"symbol": "Tb", "name": "Terbium", "atomic_mass": 158.93},
            66: {"symbol": "Dy", "name": "Dysprosium", "atomic_mass": 162.5},
            67: {"symbol": "Ho", "name": "Holmium", "atomic_mass": 164.93},
            68: {"symbol": "Er", "name": "Erbium", "atomic_mass": 167.26},
            69: {"symbol": "Tm", "name": "Thulium", "atomic_mass": 168.93},
            70: {"symbol": "Yb", "name": "Ytterbium", "atomic_mass": 173.04},
            71: {"symbol": "Lu", "name": "Lutetium", "atomic_mass": 174.97},
            72: {"symbol": "Hf", "name": "Hafnium", "atomic_mass": 178.49},
            73: {"symbol": "Ta", "name": "Tantalum", "atomic_mass": 180.95},
            74: {"symbol": "W", "name": "Tungsten", "atomic_mass": 183.84},
            75: {"symbol": "Re", "name": "Rhenium", "atomic_mass": 186.21},
            76: {"symbol": "Os", "name": "Osmium", "atomic_mass": 190.23},
            77: {"symbol": "Ir", "name": "Iridium", "atomic_mass": 192.22},
            78: {"symbol": "Pt", "name": "Platinum", "atomic_mass": 195.08},
            79: {"symbol": "Au", "name": "Gold", "atomic_mass": 196.97},
            80: {"symbol": "Hg", "name": "Mercury", "atomic_mass": 200.59},
            81: {"symbol": "Tl", "name": "Thallium", "atomic_mass": 204.38},
            82: {"symbol": "Pb", "name": "Lead", "atomic_mass": 207.2},
            83: {"symbol": "Bi", "name": "Bismuth", "atomic_mass": 208.98},
            84: {"symbol": "Po", "name": "Polonium", "atomic_mass": 209},
            85: {"symbol": "At", "name": "Astatine", "atomic_mass": 210},
            86: {"symbol": "Rn", "name": "Radon", "atomic_mass": 222},
            87: {"symbol": "Fr", "name": "Francium", "atomic_mass": 223},
            88: {"symbol": "Ra", "name": "Radium", "atomic_mass": 226},
            89: {"symbol": "Ac", "name": "Actinium", "atomic_mass": 227},
            90: {"symbol": "Th", "name": "Thorium", "atomic_mass": 232.04},
            91: {"symbol": "Pa", "name": "Protactinium", "atomic_mass": 231.04},
            92: {"symbol": "U", "name": "Uranium", "atomic_mass": 238.03},
            93: {"symbol": "Np", "name": "Neptunium", "atomic_mass": 237},
            94: {"symbol": "Pu", "name": "Plutonium", "atomic_mass": 244},
            95: {"symbol": "Am", "name": "Americium", "atomic_mass": 243},
            96: {"symbol": "Cm", "name": "Curium", "atomic_mass": 247},
            97: {"symbol": "Bk", "name": "Berkelium", "atomic_mass": 247},
            98: {"symbol": "Cf", "name": "Californium", "atomic_mass": 251},
            99: {"symbol": "Es", "name": "Einsteinium", "atomic_mass": 252},
            100: {"symbol": "Fm", "name": "Fermium", "atomic_mass": 257},
            101: {"symbol": "Md", "name": "Mendelevium", "atomic_mass": 258},
            102: {"symbol": "No", "name": "Nobelium", "atomic_mass": 259},
            103: {"symbol": "Lr", "name": "Lawrencium", "atomic_mass": 262},
            104: {"symbol": "Rf", "name": "Rutherfordium", "atomic_mass": 267},
            105: {"symbol": "Db", "name": "Dubnium", "atomic_mass": 270},
            106: {"symbol": "Sg", "name": "Seaborgium", "atomic_mass": 271},
            107: {"symbol": "Bh", "name": "Bohrium", "atomic_mass": 270},
            108: {"symbol": "Hs", "name": "Hassium", "atomic_mass": 277},
            109: {"symbol": "Mt", "name": "Meitnerium", "atomic_mass": 278},
            110: {"symbol": "Ds", "name": "Darmstadtium", "atomic_mass": 281},
            111: {"symbol": "Rg", "name": "Roentgenium", "atomic_mass": 282},
            112: {"symbol": "Cn", "name": "Copernicium", "atomic_mass": 285},
            113: {"symbol": "Nh", "name": "Nihonium", "atomic_mass": 286},
            114: {"symbol": "Fl", "name": "Flerovium", "atomic_mass": 289},
            115: {"symbol": "Mc", "name": "Moscovium", "atomic_mass": 290},
            116: {"symbol": "Lv", "name": "Livermorium", "atomic_mass": 293},
            117: {"symbol": "Ts", "name": "Tennessine", "atomic_mass": 294},
            118: {"symbol": "Og", "name": "Oganesson", "atomic_mass": 294},
        }

    def get_element(self, atomic_number):
        element = self.elements.get(atomic_number)
        if element:
            return f"Atomic Number: {atomic_number}\nSymbol: {element['symbol']}\nName: {element['name']}\nAtomic Mass: {element['atomic_mass']}"
        else:
            return "Element not found."

    def list_elements(self):
        return "\n".join([f"{num}: {data['symbol']} ({data['name']})" for num, data in self.elements.items()])

# Usage
if __name__ == "__main__":
    table = PeriodicTable()

    # List all elements
    print("Periodic Table:")
    print(table.list_elements())

    # Get details of a specific element
    atomic_number = int(input("\nEnter the atomic number of an element: "))
    print(table.get_element(atomic_number))
