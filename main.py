import streamlit as st
from postalcodes import PostalCodeManager

postal_code_manager = PostalCodeManager()

def main():
    st.title("Consulta de Códigos Postales")

    postal_code = st.text_input("Introduce el Código Postal", help="El CP deb tener 5 dígitos")

    if postal_code:
        try:
            postal_code = int(postal_code)
            routes = postal_code_manager.get_routes_for_postal_code(postal_code)
            if routes:
                st.success(f"Código Postal {postal_code} asociado a: ")
                st.info(f" Jaula: {' , '.join(map(str, routes))}")
            else:
                st.error(f"No se encontró información para el código postal {postal_code}")
        except ValueError:
            st.warning("Por favor, ingresa un código postal válido (5 dígitos)")

if __name__ == "__main__":
    main()
