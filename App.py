from flask import *
from db import *

product = Salgadinhos

App = Flask('__name__')

@app.route('/Salgadinhos', method=[''])
def product(self):
    return make_response(
        jsonify(Produtos)
    )


if __name__=='__main__':
    App.run()
