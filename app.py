from flask import Flask,render_template
import requests

app = Flask(__name__)

@app.route("/hundredImage")
def hello_world():
    x=requests.get('https://jsonplaceholder.typicode.com/photos')
    temp = x.json()
    #print(temp)
    print(type(temp))
    print(type(temp[0]))
    # print(type(x.text))
    # #temp = "".join(x.text)
    # print(type(temp))
    #temp2 = list(temp)
    #print(temp)
    # for val in temp:
    #     print(val)
    mylist=[]
    for i in range(100):
        mylist.append(temp[i].get("url"))


    
    return render_template('index.html',mylist=mylist)
