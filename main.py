<<<<<<< HEAD
from src.generators.story_generator import StoryGenerator


if __name__ == "__main__":
    try:
        theme = "Una triste historia de amor"
        characters = {
            "Diana": {
                "descripcion_fisica": "una señorita de 21 años, cabello negro y largo, ojos azules, piel clara, sonrisa encantadora, viste un vestido blanco sencillo."
            },
            "Jairo": {
                "descripcion_fisica": "un chico de 22 años, cabello negro, ojos marrones, piel bronceada, sonrisa encantadora, viste una camisa negra y jeans azules."
            },
        }
        plot = "Diana y Jairo se conocen en un concierto y se enamoran, pero un trágico accidente los separa, dejando a uno de los enamorados llorando y con un final de una tumba."

        story_generator = StoryGenerator()
        story_generator.run(theme, characters, plot)

    except KeyboardInterrupt:
        print("\nBye!")
    except Exception as e:
        print(f"An error occurred: {e}")
=======
import streamlit as st
from src.generators.story_generator import StoryGenerator

st.title("Generador de Cuentos")

theme = st.text_input("Introduce el tema de la historia", "Una triste historia de amor")

st.subheader("Personajes")
character_names = st.text_area(
    label="Introduce los nombres de los personajes (separados por comas)",
    placeholder="Para cargar los personajes debe dar Crtl + Enter",
    value="Diana, Jairo",
)
characters_input = {}

for name in character_names.split(","):
    name = name.strip()
    description = st.text_area(f"Descripción física de {name}", "")
    if description:
        characters_input[name] = {"descripcion_fisica": description}

plot = st.text_area(
    label="Introduce la trama de la historia",
    placeholder="Aquí puedes escribir la trama general de tu historia. Por ejemplo, puedes comenzar con: 'Había una vez...'",
)

if st.button("Generar Historia"):
    try:
        story_generator = StoryGenerator()
        story = story_generator.run(theme, characters_input, plot)
        st.subheader("Historia Generada")
        st.write(f"La historia se quedo grabada en: {story}")
        # Leer el contenido del archivo para pasarlo al botón de descarga
        with open(story, "rb") as file:
            story_content = file.read()

        # Crear el botón de descarga con el contenido correcto
        st.download_button(
            label="Descargar historia",
            data=story_content,
            file_name="historia_generada.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        )

    except Exception as e:
        st.error(f"An error occurred: {e}")
>>>>>>> e17cb796e1b2bb9e2cb8a833397249661a93835d
