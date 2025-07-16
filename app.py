from flask import Flask, render_template, request, redirect
import urllib.parse

app = Flask(__name__)

products = [
    {
        'name': 'Desengrasante Industrial',
        'image': 'product1.png',
        'description': 'Potente desengrasante para maquinaria y superficies industriales.'
    },
    {
        'name': 'Limpiador Multiusos',
        'image': 'product2.png',
        'description': 'Fórmula versátil para limpieza general en ambientes industriales.'
    },
    {
        'name': 'Ácido Clorhídrico',
        'image': 'product3.png',
        'description': 'Utilizado en procesos industriales y limpieza de metales.'
    }
]

@app.route('/')
def home():
    return render_template('home.html', products=products)

@app.route('/producto/<int:index>', methods=['GET', 'POST'])
def product_detail(index):
    product = products[index]
    if request.method == 'POST':
        name = request.form['name']
        company = request.form['company']
        phone = request.form['phone']

        message = f"Hola, soy {name} de {company}. Estoy interesado en el producto '{product['name']}'. Mi número es {phone}."
        message_encoded = urllib.parse.quote(message)
        whatsapp_url = f"https://wa.me/573245946745?text={message_encoded}"
        return redirect(whatsapp_url)

    return render_template('product.html', product=product)

if __name__ == '__main__':
    app.run(debug=True)
