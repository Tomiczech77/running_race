from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__) # Argument __name__ je jméno modulu – Flask podle něj hledá soubory, které k aplikaci patří (static a templates).
app.secret_key = "secretKey"  # Secret key pro CSRF ochranu, měl by být unikátní pro tvou aplikaci

# Definice formuláře
class MyForm(FlaskForm):
    name = StringField("Jméno")
    submit = SubmitField("Odeslat")

# Routing pro zobrazení a zpracování formuláře
@app.route("/", methods=["GET", "POST"]) # na „domovské stránce“ bude k dispozici obsah, který vrátí funkce index
def index():
    title_page = "Registrace"
    form = MyForm()  # Vytvoření instance formuláře

    if form.validate_on_submit():  # Pokud byl formulář odeslán a data jsou validní
        name = form.name.data
        return f"Vítej, {name}!"

    return render_template("index.html", title = title_page, form=form)