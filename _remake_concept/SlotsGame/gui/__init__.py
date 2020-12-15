from configparser import ConfigParser

config = ConfigParser()
config.read("settings.ini")


cnf_header = {
    "fg": "gold",
    "text": "$  L  O  T  $",
    "font": "Impact 48",
}

cnf_button = {
    "font": ("Lucida Sans Typewriter", 16, "bold"),
}
