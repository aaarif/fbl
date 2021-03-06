from flask import Flask, json, render_template, request, redirect, Response, url_for
from models import models

app = Flask(__name__, template_folder="templates")


obj_mod = models()


@app.route("/")
def main():
    return render_template('page1.html')


@app.route("/page2", methods=['GET'])
def to_page2():
    datals = obj_mod.process_detail()
    return render_template('page2.html', size=len(datals), prod_list=datals)


@app.route("/page3", methods=['POST', 'GET'])
def to_page3():
    app.logger.debug("Masuk to page3: ")
    return render_template(('page3.html'))


@app.route('/submitProductLink', methods=['POST', 'GET'])
def submitProduct():
    app.logger.debug(
        "Isi request form: {}".format(request.form))
    if request.method == 'POST':
        product_link = request.form['productLink']
        if product_link:
            obj_mod.add_link(product_link)
            return product_link


@app.route('/detailProduct', methods=['POST', 'GET', 'PUT'])
def detailProduct():
    if request.method == 'GET':
        app.logger.debug("Masuk GET ")
        url = request.url
        return render_template('page3.html', pesan=url)

if __name__ == "__main__":
    app.run(debug=True)
