from flask import Flask, request
from flask.templating import render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/encode", methods=["GET", "POST"])
def encode():
    # armazenar o codigo morse do alfabeto usando um dicionario
    morse_dict = {'A': '.-', 'B': '-...',
                  'C': '-.-.', 'D': '-..', 'E': '.',
                  'F': '..-.', 'G': '--.', 'H': '....',
                  'I': '..', 'J': '.---', 'K': '-.-',
                  'L': '.-..', 'M': '--', 'N': '-.',
                  'O': '---', 'P': '.--.', 'Q': '--.-',
                  'R': '.-.', 'S': '...', 'T': '-',
                  'U': '..-', 'V': '...-', 'W': '.--',
                  'X': '-..-', 'Y': '-.--', 'Z': '--..',
                  '1': '.----', '2': '..---', '3': '...--',
                  '4': '....-', '5': '.....', '6': '-....',
                  '7': '--...', '8': '---..', '9': '----.',
                  '0': '-----', ', ': '--..--', '.': '.-.-.-',
                  '?': '..--..', '/': '-..-.', '-': '-....-',
                  '(': '-.--.', ')': '-.--.-'}

# Esta função pega a mensagem de texto e retorna o código morse convertido.
    def encrypt(text):
        morse_code = ""
        # Converter cada letra em código morse:
        for letter in text:
            if letter != " ":
                morse_code = morse_code + morse_dict[letter]+" "
        # Substitui caracteres não reconhecidos por um espaço
            else:
                morse_code += " "

        return morse_code

    if request.method == "POST":
        morse_text = request.form["morse_text"]
        # Converte todos os caracteres minúsculos em maiúsculas
        upper_morse = morse_text.upper()
        result = encrypt(upper_morse)

    else:
        result = " "
    return render_template("encode.html", result=result)


@app.route("/decode", methods=["GET", "POST"])
def decode():

    morse_dict = {'A': '.-', 'B': '-...',
                  'C': '-.-.', 'D': '-..', 'E': '.',
                  'F': '..-.', 'G': '--.', 'H': '....',
                  'I': '..', 'J': '.---', 'K': '-.-',
                  'L': '.-..', 'M': '--', 'N': '-.',
                  'O': '---', 'P': '.--.', 'Q': '--.-',
                  'R': '.-.', 'S': '...', 'T': '-',
                  'U': '..-', 'V': '...-', 'W': '.--',
                  'X': '-..-', 'Y': '-.--', 'Z': '--..',
                  '1': '.----', '2': '..---', '3': '...--',
                  '4': '....-', '5': '.....', '6': '-....',
                  '7': '--...', '8': '---..', '9': '----.',
                  '0': '-----', ', ': '--..--', '.': '.-.-.-',
                  '?': '..--..', '/': '-..-.', '-': '-....-',
                  '(': '-.--.', ')': '-.--.-'}

# Decodificar -> inverter o dicionário (trocar a chave e o valor do dicionário)
    morse_dict_inverse = {value: key for key, value in morse_dict.items()}
    morse_dict_inverse[""] = " "

# Esta função pega a cifra do código morse e retorna a mensagem de texto
    def decrypt(morse_code):
        text = ""
        morse_text = ""
        morse_list = []
        morse_code += " "

        for morse in morse_code:
        # conferir os espaços
            if morse != " ":
                morse_text += morse
            else:
                morse_list.append(morse_text)
                morse_text = ""
        for item in morse_list:
            text += morse_dict_inverse[item]
        return text.title()

    if request.method == "POST":
        morse_code = request.form["morse_code"]
        result = decrypt(morse_code)
    else:
        result = ""

    return render_template("decode.html", result=result)


if __name__ == '__main__':
    app.run
