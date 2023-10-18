from flask import Flask, jsonify, request, make_response
from functions import calculate_penalty,possession

app = Flask(__name__)


@app.route('/')
def index():
    return 'This is index page'



@app.route('/penalties', methods={'POST'})
def getpenalities():

        drug_class=request.form.get('drug_class')
        culpability = request.form.get('culpability')
        harm = request.form.get('harm')
        print((drug_class,culpability,harm))
            
        result = calculate_penalty(drug_class,culpability,int(harm))
        return jsonify( response = result, status=200,message="success" )


@app.route('/possession_of_a_drug', methods={'POST'})
def possession_of_a_drugapi():
    drug_class = request.form.get('drug_class')
    result = possession(drug_class)
    return jsonify(response=result, status=200, message="success")



if __name__ == "__main__":
    app.run(debug=True)
