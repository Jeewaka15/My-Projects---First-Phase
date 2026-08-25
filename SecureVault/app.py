import webbrowser
import threading

from flask import Flask, render_template, request, redirect, session, url_for

from pathlib import Path

from services.auth import (
    generate_salt,
    save_salt,
    load_salt,
    derive_key,
    save_master_password,
    verify_master_password
)

from services.vault_service import VaultService

from config import VAULT_FILE

app = Flask(__name__)
app.secret_key = "securevault-dev-key"  # later move to config


vault_instance = None


# ---------------- HOME ----------------

@app.route("/")
def home():
    if "logged_in" in session:
        return redirect("/dashboard")
    return redirect("/login")





# ---------------- LOGIN ----------------

@app.route("/login", methods=["GET", "POST"])
def login():

    global vault_instance

    if request.method == "POST":

        master_password = request.form["password"]

        # FIRST TIME SETUP
        if not Path(VAULT_FILE).exists():

            salt = generate_salt()
            save_salt(salt)

            save_master_password(master_password)

            key = derive_key(master_password, salt)

            vault = VaultService(key)
            vault.create_empty_vault()

            vault_instance = vault

            session["logged_in"] = True

            return redirect("/dashboard")

        # LOGIN FLOW
        if not verify_master_password(master_password):
            return render_template("login.html", error="Wrong password")

        salt = load_salt()
        key = derive_key(master_password, salt)

        vault = VaultService(key)
        vault.load()

        vault_instance = vault

        session["logged_in"] = True

        return redirect("/dashboard")

    return render_template("login.html")


# ---------------- DASHBOARD ----------------

@app.route("/dashboard")
def dashboard():

    if "logged_in" not in session:
        return redirect("/login")

    accounts = vault_instance.get_accounts()

    return render_template("dashboard.html", accounts=accounts)



@app.route("/add", methods=["POST"])
def add_password():

    if "logged_in" not in session:
        return redirect("/login")

    website = request.form["website"]
    username = request.form["username"]
    password = request.form["password"]

    vault_instance.add_account(
        website,
        username,
        password
    )

    return redirect("/dashboard")


@app.route("/delete/<website>")
def delete_password(website):

    if "logged_in" not in session:
        return redirect("/login")

    vault_instance.delete_account(website)
    vault_instance.save()

    return redirect("/dashboard")





# ---------------- LOGOUT ----------------

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000/login")


if __name__ == "__main__":
    threading.Timer(1.5, open_browser).start()
    app.run(debug=True)