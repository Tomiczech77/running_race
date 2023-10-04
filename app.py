from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField

app = Flask(__name__) # Argument __name__ je jméno modulu – Flask podle něj hledá soubory, které k aplikaci patří (static a templates).
app.secret_key = "secretKey"  # Secret key pro CSRF ochranu, měl by být unikátní pro tvou aplikaci

# Definice formuláře
class RegisterForm(FlaskForm):
    first_name = StringField("Jméno")
    second_name = StringField("Příjmení")
    birthdate = DateField('Datum narození')
    club_town = StringField("Oddíl/Město")
    submit = SubmitField("Odeslat")

# Routing pro zobrazení a zpracování formuláře
@app.route("/", methods=["GET", "POST"]) # na „domovské stránce“ bude k dispozici obsah, který vrátí funkce index
def index():
    title_page = "Registrace"
    form = RegisterForm()  # Vytvoření instance formuláře

    if form.validate_on_submit():  # Pokud byl formulář odeslán a data jsou validní
        first_name = form.first_name.data
        second_name = form.second_name.data
        birthdate = form.birthdate.data
        club_town = form.club_town.data

        return f"Vítej, {first_name}, {second_name}, {birthdate}, {club_town}!"

    return render_template("index.html", title = title_page, form=form)