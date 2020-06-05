from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    kdo= url_for('static', filename='./icons/cadeau.jpg')
    logo = url_for('static', filename='./icons/Logo.svg')
    image_file = url_for('static', filename='./img/imgHead.png')
    cartel_file  = url_for('static', filename='./img/logoCartel.png')
    casse_file = url_for('static', filename='./img/casse.png')
    illusion_file = url_for('static', filename='./img/illusion.png')
    return render_template('index.html',cartel =cartel_file,illusion =illusion_file,casse =casse_file, img1 =image_file,log =logo)



@app.route('/reservation')
def reservation():
    logo = url_for('static', filename='Logo.svg')
    return render_template('reservation.html',log =logo)

@app.route('/entreprises')
def entreprises():
    return render_template('entreprises.html',log =logo)

@app.route('/cadeaux')
def cadeaux():
    logo = url_for('static', filename='Logo.svg')
    return render_template('cadeaux.html',log =logo)

@app.route('/jeux')
def jeux():
    logo = url_for('static', filename='Logo.svg')
    return render_template('jeux.html',log =logo)

@app.route('/faq')
def faq():
    logo = url_for('static', filename='Logo.svg')
    return render_template('faq.html',log =logo)

@app.route('/contact')
def contact():
    logo = url_for('static', filename='Logo.svg')
    return render_template('contact.html',log =logo)

if __name__ == '__main__':
    app.run(debug=True)


