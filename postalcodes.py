import streamlit as st
class PostalCodeManager:
    def __init__(self):
        self.data = {
            # Oviedo y alrededores
            "33012": [{"jaula": "10", "nombre": "XAVI OVD"}, {"jaula": "R4", "nombre": "ARI OVIEDO"}],
            "33013": [{"jaula": "11", "nombre": "ERICK OVIEDO"}],
            "33005": [{"jaula": "12", "nombre": "WILSON ANDRÉS"}, {"jaula": "14", "nombre": "RUBÉN OVIEDO"}],
            "33006": [{"jaula": "12", "nombre": "WILSON ANDRÉS"}],
            "33001": [{"jaula": "13", "nombre": "ÓSCAR PUMARÍN"}, {"jaula": "14", "nombre": "RUBÉN OVIEDO"}],
            "33011": [{"jaula": "13", "nombre": "ÓSCAR PUMARÍN"}, {"jaula": "16", "nombre": "XAVI CORREDORIA"}, {"jaula": "78", "nombre": "ANY OVIEDO"}],
            "33002": [{"jaula": "14", "nombre": "RUBÉN OVIEDO"}],
            "33003": [{"jaula": "14", "nombre": "RUBÉN OVIEDO"}],
            "33004": [{"jaula": "14", "nombre": "RUBÉN OVIEDO"}],
            "33008": [{"jaula": "14", "nombre": "RUBÉN OVIEDO"}, {"jaula": "17", "nombre": "ASTURSOTO OVIEDO"}, {"jaula": "73", "nombre": "DANI ASTURSOTO"}, {"jaula": "75", "nombre": "GONZALO CASES"}],
            "33009": [{"jaula": "14", "nombre": "RUBÉN OVIEDO"}, {"jaula": "17", "nombre": "ASTURSOTO OVIEDO"}, {"jaula": "73", "nombre": "DANI ASTURSOTO"}],
            "33010": [{"jaula": "14", "nombre": "RUBÉN OVIEDO"}, {"jaula": "15", "nombre": "ICÍAR"}, {"jaula": "17", "nombre": "ASTURSOTO OVIEDO"}, {"jaula": "75", "nombre": "GONZALO CASES"}, {"jaula": "78", "nombre": "ANY OVIEDO"}],
            "33007": [{"jaula": "75", "nombre": "GONZALO CASES"}],

            # Avilés y zona
            "33403": [{"jaula": "1", "nombre": "KELVIN"}],
            "33410": [{"jaula": "1", "nombre": "KELVIN"}, {"jaula": "3", "nombre": "KELVIN"}],
            "33404": [{"jaula": "2", "nombre": "PEDRO AVILÉS"}, {"jaula": "3", "nombre": "KELVIN"}],
            "33416": [{"jaula": "2", "nombre": "PEDRO AVILÉS"}, {"jaula": "3", "nombre": "KELVIN"}],
            "33460": [{"jaula": "2", "nombre": "PEDRO AVILÉS"}, {"jaula": "61", "nombre": "CRIS CANDÁS"}],
            "33470": [{"jaula": "2", "nombre": "PEDRO AVILÉS"}, {"jaula": "19", "nombre": "BELÉN"}],
            "33400": [{"jaula": "3", "nombre": "KELVIN"}],
            "33412": [{"jaula": "3", "nombre": "KELVIN"}],
            "33401": [{"jaula": "4", "nombre": "IVÁN AVILÉS"}, {"jaula": "6", "nombre": "FLORIAN (ENOL)"}, {"jaula": "64", "nombre": "CIPRI"}],
            "33402": [{"jaula": "4", "nombre": "IVÁN AVILÉS"}, {"jaula": "6", "nombre": "FLORIAN (ENOL)"}, {"jaula": "7", "nombre": "DANIELA SCARLETT"}],
            "33405": [{"jaula": "8", "nombre": "HENRY AVILÉS"}, {"jaula": "9", "nombre": "HENRY AVILÉS"}],
            "33450": [{"jaula": "8", "nombre": "HENRY AVILÉS"}, {"jaula": "9", "nombre": "HENRY AVILÉS"}, {"jaula": "63", "nombre": "BORIS PRAVIA"}],
            "33417": [{"jaula": "64", "nombre": "CIPRI"}],

            # Gijón
            "33206": [{"jaula": "22", "nombre": "JOHANA NATAHOYO"}, {"jaula": "R8", "nombre": "DIEGO GIJÓN"}],
            "33207": [{"jaula": "22", "nombre": "JOHANA NATAHOYO"}, {"jaula": "28", "nombre": "CARLOS ALEXIS"}, {"jaula": "R8", "nombre": "DIEGO GIJÓN"}],
            "33212": [{"jaula": "22", "nombre": "JOHANA NATAHOYO"}, {"jaula": "31", "nombre": "JOHANA"}],
            "33210": [{"jaula": "23", "nombre": "DAVID RUTA GIJÓN"}, {"jaula": "24", "nombre": "JOHANA(ANDRÉS)"}, {"jaula": "28", "nombre": "CARLOS ALEXIS"}, {"jaula": "34", "nombre": "WILSON GIJÓN"}, {"jaula": "35", "nombre": "ONDINA GIJÓN"}, {"jaula": "67", "nombre": "HANSEL GIJÓN"}],
            "33211": [{"jaula": "23", "nombre": "DAVID RUTA GIJÓN"}, {"jaula": "24", "nombre": "JOHANA(ANDRÉS)"}, {"jaula": "25", "nombre": "PEDRO GIJÓN"}, {"jaula": "34", "nombre": "WILSON GIJÓN"}],
            "33209": [{"jaula": "24", "nombre": "JOHANA(ANDRÉS)"}, {"jaula": "26", "nombre": "FERNANDO GIJÓN"}, {"jaula": "33", "nombre": "VITI GIJÓN"}, {"jaula": "35", "nombre": "ONDINA GIJÓN"}, {"jaula": "67", "nombre": "HANSEL GIJÓN"}, {"jaula": "79", "nombre": "PEDRO CRISTIAN"}],
            "33391": [{"jaula": "25", "nombre": "PEDRO GIJÓN"}, {"jaula": "36", "nombre": "DAVID HANSEL"}],
            "33393": [{"jaula": "25", "nombre": "PEDRO GIJÓN"}, {"jaula": "36", "nombre": "DAVID HANSEL"}],
            "33202": [{"jaula": "26", "nombre": "FERNANDO GIJÓN"}, {"jaula": "79", "nombre": "PEDRO CRISTIAN"}],
            "33205": [{"jaula": "26", "nombre": "FERNANDO GIJÓN"}, {"jaula": "33", "nombre": "VITI GIJÓN"}, {"jaula": "79", "nombre": "PEDRO CRISTIAN"}],
            "33203": [{"jaula": "30", "nombre": "BYRON"}, {"jaula": "77", "nombre": "ROBERT HANSEL"}],
            "33204": [{"jaula": "30", "nombre": "BYRON"}, {"jaula": "33", "nombre": "VITI GIJÓN"}],
            "33213": [{"jaula": "31", "nombre": "JOHANA"}, {"jaula": "32", "nombre": "JHONSON"}],
            "33290": [{"jaula": "31", "nombre": "JOHANA"}],
            "33299": [{"jaula": "31", "nombre": "JOHANA"}],
            "33691": [{"jaula": "31", "nombre": "JOHANA"}],
            "33208": [{"jaula": "35", "nombre": "ONDINA GIJÓN"}, {"jaula": "67", "nombre": "HANSEL GIJÓN"}, {"jaula": "79", "nombre": "PEDRO CRISTIAN"}],
            "33201": [{"jaula": "79", "nombre": "PEDRO CRISTIAN"}, {"jaula": "R8", "nombre": "DIEGO GIJÓN"}],

            # Otras zonas
            "33140": [{"jaula": "18", "nombre": "IVÁN SAN CLAUDIO"}],
            "33170": [{"jaula": "18", "nombre": "IVÁN SAN CLAUDIO"}, {"jaula": "56", "nombre": "RUBÉN RIOSA"}],
            "33190": [{"jaula": "18", "nombre": "IVÁN SAN CLAUDIO"}, {"jaula": "60", "nombre": "SERGIO REGUERAS"}],
            "33191": [{"jaula": "18", "nombre": "IVÁN SAN CLAUDIO"}],
            "33193": [{"jaula": "18", "nombre": "IVÁN SAN CLAUDIO"}],
            "33194": [{"jaula": "18", "nombre": "IVÁN SAN CLAUDIO"}],
            "33195": [{"jaula": "18", "nombre": "IVÁN SAN CLAUDIO"}],
            "33196": [{"jaula": "18", "nombre": "IVÁN SAN CLAUDIO"}],
            "33192": [{"jaula": "19", "nombre": "BELÉN"}, {"jaula": "20", "nombre": "BELÉN"}],
            "33422": [{"jaula": "19", "nombre": "BELÉN"}, {"jaula": "20", "nombre": "BELÉN"}],
            "33423": [{"jaula": "19", "nombre": "BELÉN"}, {"jaula": "20", "nombre": "BELÉN"}],
            "33424": [{"jaula": "19", "nombre": "BELÉN"}, {"jaula": "20", "nombre": "BELÉN"}],
            "33425": [{"jaula": "19", "nombre": "BELÉN"}, {"jaula": "20", "nombre": "BELÉN"}],
            "33426": [{"jaula": "19", "nombre": "BELÉN"}, {"jaula": "20", "nombre": "BELÉN"}],
            "33427": [{"jaula": "19", "nombre": "BELÉN"}, {"jaula": "20", "nombre": "BELÉN"}],
            "33428": [{"jaula": "19", "nombre": "BELÉN"}, {"jaula": "20", "nombre": "BELÉN"}],
            "33429": [{"jaula": "19", "nombre": "BELÉN"}, {"jaula": "20", "nombre": "BELÉN"}],
            "33690": [{"jaula": "19", "nombre": "BELÉN"}, {"jaula": "20", "nombre": "BELÉN"}],
            "33420": [{"jaula": "29", "nombre": "HERMINIO LUGONES"}],
            "33314": [{"jaula": "77", "nombre": "ROBERT HANSEL"}],
            "33394": [{"jaula": "77", "nombre": "ROBERT HANSEL"}],
            "33350": [{"jaula": "36", "nombre": "DAVID HANSEL"}],
            "33392": [{"jaula": "36", "nombre": "DAVID HANSEL"}],
            "33300": [{"jaula": "37", "nombre": "CRISTIAN VILLAVICIOSA"}],
            "33330": [{"jaula": "38", "nombre": "ÓSCAR RIBADESELLA"}],
            "33340": [{"jaula": "38", "nombre": "ÓSCAR RIBADESELLA"}],
            "33560": [{"jaula": "38", "nombre": "ÓSCAR RIBADESELLA"}],
            "33500": [{"jaula": "39", "nombre": "CARLOS LLANES"}, {"jaula": "40", "nombre": "ÓSCAR ISRAEL"}],
            "33590": [{"jaula": "39", "nombre": "CARLOS LLANES"}, {"jaula": "40", "nombre": "ÓSCAR ISRAEL"}],
            "33540": [{"jaula": "41", "nombre": "PASCUAL"}],
            "33550": [{"jaula": "41", "nombre": "PASCUAL"}, {"jaula": "42", "nombre": "LUIS MARTINO"}],
            "33570": [{"jaula": "41", "nombre": "PASCUAL"}],
            "33530": [{"jaula": "43", "nombre": "LUIS MARTINO(INFIESTO)"}],
            "33583": [{"jaula": "43", "nombre": "LUIS MARTINO(INFIESTO)"}],
            "33584": [{"jaula": "43", "nombre": "LUIS MARTINO(INFIESTO)"}],
            "33520": [{"jaula": "44", "nombre": "HANSEL NAVA"}],
            "33580": [{"jaula": "44", "nombre": "HANSEL NAVA"}],
            "33310": [{"jaula": "44", "nombre": "HANSEL NAVA"}],
            "33199": [{"jaula": "45", "nombre": "IVÁN SIERO"}],
            "33510": [{"jaula": "45", "nombre": "IVÁN SIERO"}],
            "33189": [{"jaula": "46", "nombre": "JOSE SIERO"}],
            "33519": [{"jaula": "46", "nombre": "JOSE SIERO"}],
            "33936": [{"jaula": "46", "nombre": "JOSE SIERO"}],
            "33937": [{"jaula": "46", "nombre": "JOSE SIERO"}],
            "33938": [{"jaula": "46", "nombre": "JOSE SIERO"}],
            "33180": [{"jaula": "74", "nombre": "RILE SIERO"}],
            "33186": [{"jaula": "74", "nombre": "RILE SIERO"}],
            "33187": [{"jaula": "74", "nombre": "RILE SIERO"}],
            "33188": [{"jaula": "74", "nombre": "RILE SIERO"}],
            "33518": [{"jaula": "74", "nombre": "RILE SIERO"}],
            "33900": [{"jaula": "48", "nombre": "CHESCO SAMA"}, {"jaula": "27", "nombre": "PIÑON"}],
            "33930": [{"jaula": "49", "nombre": "JAIRO FELGUERA"}],
            "33940": [{"jaula": "50", "nombre": "JONI EL ENTREGO"}],
            "33950": [{"jaula": "50", "nombre": "JONI EL ENTREGO"}],
            "33960": [{"jaula": "50", "nombre": "JONI EL ENTREGO"}],
            "33970": [{"jaula": "51", "nombre": "ROBER LAVIANA"}],
            "33980": [{"jaula": "51"}]
    
     }
    
    def get_info_for_postal_code(self, postal_code):
        return self.data.get(postal_code, [])

def main():
    st.title("Consulta de Códigos Postales")
    postal_code = st.text_input("Introduce el Código Postal", help="El CP debe tener 5 dígitos")
    
    if postal_code:
        postal_code = postal_code.strip()
        results = postal_code_manager.get_info_for_postal_code(postal_code)
        
        if results:
            st.success(f"Información para el Código Postal {postal_code}:")
            for entry in results:
                st.info(f"Jaula: {entry['jaula']}, Nombre: {entry['nombre']}")
        else:
            st.error(f"No se encontró información para el código postal {postal_code}")

if __name__ == "__main__":
    postal_code_manager = PostalCodeManager()
    main()