from flask import Flask,request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/phen2gene', methods=['GET'])
def phen2gene():
    # call phen2gene API
    # curl -i -H "Accept: application/json" -H "Content-Type: application/json" "https://phen2gene.wglab.org/api?HPO_list=HP:0002459;HP:0010522;HP:0001662"
    # get parameter from GET
    HPO_list = request.args.getlist('HPO_list')
    print(HPO_list)
    response = requests.get('https://phen2gene.wglab.org/api', params={"HPO_list": HPO_list})
    # select top 10 genes from response
    if response.status_code == 200:
        if 'results' in response.json():
            genes = response.json()['results']
            # print(genes)
            return jsonify({'results': genes[:10]})
if __name__ == '__main__':
    app.run(ssl_context=('cert.pem', 'key.pem'),host='0.0.0.0', port=443)
    # app.run(host='127.0.0.1', port=5000)