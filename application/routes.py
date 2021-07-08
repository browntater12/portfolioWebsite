from flask import render_template, flash, redirect, url_for, request
from flask import current_app as app
from datetime import date

@app.template_filter()
def currentYear(now):
    now = date.today()
    now = now.year
    cYear = str(now) + "-" + str(now+1)
    return(cYear)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', home=True)


@app.route('/aboutme')
def aboutme():
    return render_template('aboutme.html', about=True)


@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html', portfolio=True)


@app.route('/impossible')
def impossible():
    return render_template('impossible.html', impossible=True)