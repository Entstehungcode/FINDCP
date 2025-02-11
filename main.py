import streamlit as st
from postalcodes import PostalCodeManager  # Asegúrate de que este archivo contenga la clase actualizada

postal_code_manager = PostalCodeManager()

def main():
    st.title("Consulta de Códigos Postales")

    postal_code = st.text_input("Introduce el Código Postal", help="El CP debe tener 5 dígitos")

    if postal_code:
        postal_code = postal_code.strip()  # Eliminamos espacios en blanco
        results = postal_code_manager.get_info_for_postal_code(postal_code)

        if results:
            st.success(f"Información para el Código Postal {postal_code}:")
            for entry in results:
                st.info(f"**Jaula:** {entry['jaula']}  \n**Nombre:** {entry['nombre']}")
        else:
            st.error(f"No se encontró información para el código postal {postal_code}")

if __name__ == "__main__":
    main()

