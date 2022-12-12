from flask import Flask, render_template, url_for,request
import jinja2


app = Flask(__name__)





@app.route('/' , methods=("POST","GET"))
def inicio():

    if request.method == 'POST':



        pontoazul = request.args['pontoazul']
        pontoazul = int(pontoazul)

        pontored = request.args['pontored']
        pontored = int(pontored)


        try:
            try:
                if request.form['maisazul'] == "+ponto":
                    pontoazul = pontoazul + 10

            except:
                if request.form['menosazul'] == "-ponto":
                    pontoazul = pontoazul - 10

        except:

                try:
                    if request.form['maisred'] == "+ponto":
                        pontored = pontored + 10
                except:

                    if request.form['menosred'] == "-ponto":
                        pontored = pontored - 10


        finally:
                pass

        return render_template('index.html', pontored=pontored, pontoazul=pontoazul)




    pontored= 0
    pontoazul = 0
    return render_template('index.html', pontored=pontored , pontoazul=pontoazul)



if __name__ == '__main__':
    app.run(debug=True)