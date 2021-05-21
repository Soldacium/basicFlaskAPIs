# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)
# for, well, pretty json
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

stores = [
    {
        'name':'lol',
        'items': [
            {
                'name':'item1',
                'price': 15.99
            }
        ]
    }
]


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/store',methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

@app.route('/store/<string:name>', methods=['GET'])
def get_store(name: str):
    # get stores
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message':'store not found'})

@app.route('/store', methods=['GET'])
def get_stores():
    return jsonify({'stores' : stores})

@app.route('/store/<string:name>/items', methods=['POST'])
def create_item_in_store(name: str):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message':'store not found'})

@app.route('/store/<string:name>/items', methods=['GET'])
def get_items_from_store(name: str):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message':'store not found'})

app.run(port=5000)