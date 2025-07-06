import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import re

# Placeholder for full DXCC dictionary
DXCC_LOOKUP = {
    0: "None",
    1: "United States",
    2: "Canada",
    3: "Mexico",
    4: "Bermuda",
    5: "Bahamas",
    6: "Cuba",
    7: "Puerto Rico",
    8: "U.S. Virgin Islands",
    9: "St. Pierre & Miquelon",
    10: "Greenland",
    11: "Dominican Republic",
    12: "Haiti",
    13: "Jamaica",
    14: "Netherlands Antilles",
    15: "Aruba",
    16: "Barbados",
    17: "Antigua and Barbuda",
    18: "Martinique",
    19: "Guadeloupe",
    20: "Saint Lucia",
    21: "Dominica",
    22: "St. Vincent",
    23: "Grenada",
    24: "Trinidad and Tobago",
    25: "Anguilla",
    26: "British Virgin Islands",
    27: "Montserrat",
    28: "St. Kitts and Nevis",
    29: "Turks and Caicos Islands",
    30: "Cayman Islands",
    31: "British Honduras (Belize)",
    32: "Falkland Islands",
    33: "South Georgia",
    34: "South Sandwich Islands",
    35: "Argentina",
    36: "Brazil",
    37: "Chile",
    38: "Colombia",
    39: "Ecuador",
    40: "French Guiana",
    41: "Guyana",
    42: "Paraguay",
    43: "Peru",
    44: "Suriname",
    45: "Uruguay",
    46: "Venezuela",
    47: "Ascension Island",
    48: "Saint Helena",
    49: "Tristan da Cunha",
    50: "Falkland Islands (Islas Malvinas)",
    51: "Bouvet Island",
    52: "South Orkney Islands",
    53: "South Shetland Islands",
    54: "Antarctica",
    55: "Western Sahara",
    56: "Morocco",
    57: "Algeria",
    58: "Tunisia",
    59: "Libya",
    60: "Egypt",
    61: "Sudan",
    62: "Eritrea",
    63: "Djibouti",
    64: "Somalia",
    65: "Ethiopia",
    66: "Mali",
    67: "Mauritania",
    68: "Senegal",
    69: "Gambia",
    70: "Guinea-Bissau",
    71: "Guinea",
    72: "Sierra Leone",
    73: "Liberia",
    74: "Ivory Coast",
    75: "Burkina Faso",
    76: "Ghana",
    77: "Togo",
    78: "Benin",
    79: "Nigeria",
    80: "Niger",
    81: "Chad",
    82: "Central African Republic",
    83: "Cameroon",
    84: "Equatorial Guinea",
    85: "Gabon",
    86: "Republic of the Congo",
    87: "Democratic Republic of the Congo (Zaire)",
    88: "Angola",
    89: "Zambia",
    90: "Malawi",
    91: "Mozambique",
    92: "Zimbabwe",
    93: "Botswana",
    94: "Namibia",
    95: "South Africa",
    96: "Lesotho",
    97: "Swaziland",
    98: "Madagascar",
    99: "Mauritius",
    100: "Comoros",
    101: "Seychelles",
    102: "Mayotte",
    103: "Reunion",
    104: "St. Pierre and Miquelon",
    105: "Canary Islands",
    106: "Madeira Islands",
    107: "Azores",
    108: "Cape Verde Islands",
    109: "Malta",
    110: "Cyprus",
    111: "Israel",
    112: "Jordan",
    113: "Lebanon",
    114: "Syria",
    115: "Iraq",
    116: "Kuwait",
    117: "Saudi Arabia",
    118: "Yemen",
    119: "Oman",
    120: "United Arab Emirates",
    121: "Qatar",
    122: "Bahrain",
    123: "Iran",
    124: "Turkey",
    125: "Armenia",
    126: "Azerbaijan",
    127: "Georgia",
    128: "Russia (European part)",
    129: "Belarus",
    130: "Ukraine",
    131: "Moldova",
    132: "Kazakhstan",
    133: "Uzbekistan",
    134: "Turkmenistan",
    135: "Kyrgyzstan",
    136: "Tajikistan",
    137: "Afghanistan",
    138: "Pakistan",
    139: "India",
    140: "Nepal",
    141: "Bhutan",
    142: "Bangladesh",
    143: "Sri Lanka",
    144: "Maldives",
    145: "China",
    146: "Mongolia",
    147: "North Korea",
    148: "South Korea",
    149: "Japan",
    150: "Taiwan",
    151: "Hong Kong",
    152: "Macau",
    153: "Brunei",
    154: "Philippines",
    155: "Vietnam",
    156: "Thailand",
    157: "Cambodia",
    158: "Laos",
    159: "Malaysia",
    160: "Singapore",
    161: "Indonesia",
    162: "East Timor",
    163: "Papua New Guinea",
    164: "Australia",
    165: "New Zealand",
    166: "Fiji",
    167: "Solomon Islands",
    168: "Vanuatu",
    169: "New Caledonia",
    170: "French Polynesia",
    171: "Cook Islands",
    172: "Niue",
    173: "Samoa",
    174: "Tonga",
    175: "American Samoa",
    176: "Guam",
    177: "Northern Mariana Islands",
    178: "Palau",
    179: "Micronesia",
    180: "Marshall Islands",
    181: "Wake Island",
    182: "Johnston Atoll",
    183: "Midway Islands",
    184: "Hawaii",
    185: "Alaska",
    186: "Aleutian Islands",
    187: "Canada (Northern Territories)",
    188: "Greenland",
    189: "Iceland",
    190: "Faroe Islands",
    191: "Svalbard",
    192: "Jan Mayen",
    193: "Azores",
    194: "Madeira",
    195: "Canary Islands",
    196: "Cape Verde Islands",
    197: "Mauritania",
    198: "Senegal",
    199: "Gambia",
    200: "Guinea-Bissau",
    201: "Guinea",
    202: "Sierra Leone",
    203: "Liberia",
    204: "Ivory Coast",
    205: "Burkina Faso",
    206: "Ghana",
    207: "Togo",
    208: "Benin",
    209: "Nigeria",
    210: "Niger",
    211: "Chad",
    212: "Central African Republic",
    213: "Cameroon",
    214: "Equatorial Guinea",
    215: "Gabon",
    216: "Republic of the Congo",
    217: "Democratic Republic of the Congo",
    218: "Angola",
    219: "Zambia",
    220: "Malawi",
    221: "Mozambique",
    222: "Zimbabwe",
    223: "Botswana",
    224: "Namibia",
    225: "South Africa",
    226: "Lesotho",
    227: "Swaziland",
    228: "Madagascar",
    229: "Mauritius",
    230: "Comoros",
    231: "Seychelles",
    232: "Mayotte",
    233: "Reunion",
    234: "St. Pierre and Miquelon",
    235: "Canary Islands",
    236: "Madeira Islands",
    237: "Azores",
    238: "Cape Verde Islands",
    239: "Malta",
    240: "Cyprus",
    241: "Israel",
    242: "Jordan",
    243: "Lebanon",
    244: "Syria",
    245: "Iraq",
    246: "Kuwait",
    247: "Saudi Arabia",
    248: "Yemen",
    249: "Oman",
    250: "United Arab Emirates",
    251: "Qatar",
    252: "Bahrain",
    253: "Iran",
    254: "Turkey",
    255: "Armenia",
    256: "Azerbaijan",
    257: "Georgia",
    258: "Russia (European part)",
    259: "Belarus",
    260: "Ukraine",
    261: "Moldova",
    262: "Kazakhstan",
    263: "Uzbekistan",
    264: "Turkmenistan",
    265: "Kyrgyzstan",
    266: "Tajikistan",
    267: "Afghanistan",
    268: "Pakistan",
    269: "India",
    270: "Nepal",
    271: "Bhutan",
    272: "Bangladesh",
    273: "Sri Lanka",
    274: "Maldives",
    275: "China",
    276: "Mongolia",
    277: "North Korea",
    278: "South Korea",
    279: "Japan",
    280: "Taiwan",
    281: "Hong Kong",
    282: "Macau",
    283: "Brunei",
    284: "Philippines",
    285: "Vietnam",
    286: "Thailand",
    287: "Cambodia",
    288: "Laos",
    289: "Malaysia",
    290: "Singapore",
    291: "Indonesia",
    292: "East Timor",
    293: "Papua New Guinea",
    294: "Australia",
    295: "New Zealand",
    296: "Fiji",
    297: "Solomon Islands",
    298: "Vanuatu",
    299: "New Caledonia",
    300: "French Polynesia",
    301: "Cook Islands",
    302: "Niue",
    303: "Samoa",
    304: "Tonga",
    305: "American Samoa",
    306: "Guam",
    307: "Northern Mariana Islands",
    308: "Palau",
    309: "Micronesia",
    310: "Marshall Islands",
    311: "Wake Island",
    312: "Johnston Atoll",
    313: "Midway Islands",
    314: "Hawaii",
}


def parse_adif(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read().lower()

    # Split by individual QSO records
    records = re.findall(r'<.*?>', content, re.DOTALL)
    entries = content.split('<eor>')

    dxcc_per_band = {}
    qso_per_band = {}
    qso_per_entity = {}
    all_dxcc = set()

    for entry in entries:
        dxcc_match = re.search(r'<dxcc:\d+>(\d+)', entry)
        band_match = re.search(r'<band:\d+>([a-z0-9]+)', entry)

        if not dxcc_match:
            continue

        dxcc = int(dxcc_match.group(1))
        band = band_match.group(1) if band_match else "unknown"
        dxcc_name = DXCC_LOOKUP.get(dxcc, f"Unknown ({dxcc})")

        all_dxcc.add(dxcc_name)

        # DXCC per band
        if band not in dxcc_per_band:
            dxcc_per_band[band] = set()
        dxcc_per_band[band].add(dxcc_name)

        # QSO count per band
        qso_per_band[band] = qso_per_band.get(band, 0) + 1

        # QSO per DXCC entity
        qso_per_entity[dxcc_name] = qso_per_entity.get(dxcc_name, 0) + 1

    return {
        "all_dxcc": sorted(all_dxcc),
        "dxcc_per_band": dxcc_per_band,
        "qso_per_band": qso_per_band,
        "qso_per_entity": qso_per_entity
    }

def show_results(results):
    root = tk.Tk()
    root.title("DXCC Statistics by SV1EEX")

    text = scrolledtext.ScrolledText(root, width=100, height=40)
    text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    text.insert(tk.END, f"Total DXCC Entities (Mixed): {len(results['all_dxcc'])}\n")
    text.insert(tk.END, "\nEntities Worked:\n")
    for dxcc in results['all_dxcc']:
        text.insert(tk.END, f" - {dxcc}\n")

    text.insert(tk.END, "\nDXCC Entities per Band:\n")
    for band, dxccs in sorted(results['dxcc_per_band'].items()):
        text.insert(tk.END, f" {band}: {len(dxccs)} entities\n")
        for entity in sorted(dxccs):
            text.insert(tk.END, f"   • {entity}\n")

    text.insert(tk.END, "\nQSO Count per Band:\n")
    for band, count in sorted(results['qso_per_band'].items()):
        text.insert(tk.END, f" {band}: {count} QSOs\n")

    text.insert(tk.END, "\nQSO Count per DXCC Entity:\n")
    for entity, count in sorted(results['qso_per_entity'].items(), key=lambda x: x[1], reverse=True):
        text.insert(tk.END, f" {entity}: {count} QSOs\n")

    text.config(state='disabled')
    root.mainloop()

def main():
    filepath = filedialog.askopenfilename(
        title="Select ADIF File",
        filetypes=[("ADIF files", "*.adi *.adif"), ("All files", "*.*")]
    )

    if not filepath:
        messagebox.showinfo("Cancelled", "No file selected.")
        return

    try:
        results = parse_adif(filepath)
        show_results(results)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to parse file:\n{str(e)}")

if __name__ == "__main__":
    main()
