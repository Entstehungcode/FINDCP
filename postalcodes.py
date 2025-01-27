class PostalCodeManager:
    def __init__(self):
        self.data = {
            33403: [1, 3],
            33404: [2, 3],
            33460: [2],
            33468: ["2"],
            33470: ["2"],
            33402: ["3", "4", "6", "7"],
            33411: ["3"],
            33412: ["3"],
            33416: ["3"],
            33401: ["4", "6"],
            33405: ["8", "9"],
            33450: ["8", "9"],
            33012: ["10"],
            33013: ["11"],
            33005: ["12", "14"],
            33006: ["12"],
            33011: ["13", "16"],
            33001: ["13", "14"],
            33002: ["14"],
            33003: ["14"],
            33004: ["14"],
            33008: ["14", "17"],
            33009: ["14", "17"],
            33010: ["15", "17"],
            33140: ["18"],
            33170: ["18"],
            33191: ["18"],
            33192: ["18", "19"],
            33193: ["18"],
            33422: ["19", "20"],
            33424: ["19"],
            33428: ["19"],
            33420: ["20", "29"],
            33209: ["21", "24", "26", "35"],
            33210: ["21", "23", "24", "27", "28"],
            33211: ["21", "23", "24", "25", "34"],
            33212: ["22", "31"],
            33292: ["25"],
            33393: ["25", "36"],
            33201: ["26"],
            33202: ["26", "27", "30"],
            33205: ["26", "27", "33"],
            33208: ["26", "35"],
            33206: ["27"],
            33207: ["28"],
            33203: ["30", "36"],
            33204: ["30", "33"],
            33213: ["31", "32"],
            33290: ["31"],
            33299: ["31"],
            33691: ["31"],
            33697: ["31"],
            33209: ["33", "35"],
            33350: ["36"],
            33390: ["36"],
            33391: ["36"],
            33392: ["36"],
            33394: ["36"],
            33300: ["37"],
            33560: ["38"],
            33500: ["39", "40"],
            33590: ["39", "40"],
            33597: ["39", "40"],
            33500: ["41", "42", "43"],
            33310: "44",
            33520: "44",
            33529: "44",
            33580: "44",
            33582: "44",
            33199: "45",
            33510: "45",
            33700: "47",
            33780: "47",
            33782: "47",
            33785: "47",
            33788: "47",
            33789: "47",
            33791: "47",
            33792: "47",
            33900: "48",
            33929: "48",
            33949: "49",
            33930: "50",
            33939: "50",
            33940: "51",
            33980: "51",
            33612: "52",
            33680: "52",
            33681: "52",
            33683: "52",
            33689: "52",
            33620: "53",
            33640: "53",
            33694: "53",
            33695: "53",
            33600: "54",
            33650: "54",
            33682: "54",
            33600: "55",
            33660: "55",
            33160: "56",
            33161: "56",
            33171: "56",
            33610: "57",
            33619: "57",
            33683: "57",
            33820: "58",
            33820: "59",
            33100: "60",
            33119: "60",
            33190: "60",
            "LUANCO Y CANDAS": "61",
            "X": "62",
            33120: "63",
            33125: "63",
            33126: "63",
            33127: "63",
            33128: "63",
            33130: "63",
            33150: "64",
            33400: "64",
            33401: "64",
            33417: "64",
            33418: "64",
            "X": "65",
            "X": "66",
            33208: "67",
            33209: "67",
            33210: "67",
            33716: "68",
            33719: "68",
            33740: "68",
            33959: "68",
            338: "69",
            338: "70",
            338: "71",
            33008: "73",
            33009: "73",
            33180: "74",
            33186: "74",
            33187: "74",
            33189: "74",
            33007: "75",
            33010: "75",
            33205: "76",
            33209: "76",
            33203: "78",
            33394: "78",
            33314: "78"
        }

    def expand_range(self, rango):
        if isinstance(rango, str) and "-" in rango:
            start, end = map(int, rango.split("-"))
            return set(range(start, end + 1))
        elif isinstance(rango, str) and rango.startswith("[") and rango.endswith("]"):
            return {int(cp) for cp in rango.strip("[]").split(",")}
        else:
            return {int(rango)}

    def get_routes_for_postal_code(self, postal_code):
        return self.data.get(postal_code, [])
