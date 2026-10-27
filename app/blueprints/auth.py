# Stuff from Flask
from flask import Blueprint, render_template, redirect, flash, request, url_for
from flask_login import login_user, login_required, logout_user

# Stuff we wrote
from app.extensions import db
from app.models import User

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        is_admin = request.form.get('is_admin') == 'on'

        # First check if the user exists
        if User.query.filter_by(username=username).first(): 
            flash(f"Username already exists.", "error")
            return redirect(url_for('auth.register'))

        new_user = User(username=username, is_admin=is_admin)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        flash("Account created successfully!", "success")
        return redirect(url_for('auth.login'))

    return render_template("auth/register.jinja")


@auth_bp.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            flash('Logged in successfully!', 'success')
            return redirect(url_for('auth.login'))

        flash('Invalid username or password.', 'error')
        return redirect(url_for('auth.login'))

    return render_template('auth/login.jinja')


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "success")
    return redirect(url_for("auth.login"))
