
from flask import Flask, render_template, request, redirect, url_for


#inizializza l'app Flask
app = Flask(__name__)
lista_spesa = []

@app.route('/')
def home():
    return render_template('index.html')


#avvio dell'app Flask
if __name__ == '__main__':
    app.run(debug=True)