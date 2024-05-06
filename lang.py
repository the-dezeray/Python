class Lang():
    default_lang = 'en'
    options = ["en","sp"]
    lang_dict = {
        "place_selection": {
            "en": "Select where you want to place your",
            "sp": "seleccione donde desea colocar su"
        },
        "select_team": {
            "en": "select your team",
            "sp": "seleccione su equipo"
        },
        "enter_name1": {
            "en": "Player 1, enter your name",
            "sp": "Jugador 1, ingrese su nombre"
        },
        "enter_name2": {
            "en": "Player 2, enter your name",
            "sp": "Jugador 2, ingrese su nombre"
        },        
        "select_team_found_here": {
            "en": "select your team found here",
            "sp": "Seleccione su equipo, que se encuetre aqui"
        },
    }

    @staticmethod
    def get_string(text_id: str = "", lang: str = "") -> str:
        text_dict =Lang.lang_dict.get(text_id, {})
        string = text_dict.get(lang,"")
        return string

    @staticmethod
    def prompt_default_lang() :
        user_input = input(f"🌐🌐Language: {Lang.options} ")
        Lang.default_lang = user_input
        from terminal import Terminal
        Terminal.clear()