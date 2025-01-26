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
