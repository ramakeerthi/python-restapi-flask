from flask import Flask,request

app = Flask(__name__)

stores = [
    {
        "name": "My Store",
        "items":[
            {
                "name":"Chair",
                "price":1500
            }
        ]
    }
]


# http://127.0.0.1:5000/store
@app.get("/store")
def get_stores():
    return{"stores":stores}

@app.post("/store")
def create_store():
    request_data = request.get_json()
    new_store = {"name":request_data['name'],"items":[]}
    stores.append(new_store)
    return new_store, 201

@app.post("/store/<string:name>/item")
def create_item(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            item = {
                "name":request_data["name"],
                "price":request_data["price"]
            }
            store["items"].append(item)
            return item, 201
    return {"message":"Store not found"},404

@app.get("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return store
    return {"message":"Store not found"},404

@app.get("/store/<string:name>/item/<string:item_name>")
def get_item(name,item_name):
    for store in stores:
        if store["name"] == name:
            items = store["items"]
            for item in items:
                if item["name"]==item_name:
                    return item
    return {"message":"Store not found"},404