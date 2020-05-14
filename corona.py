from flask import Flask,render_template
import requests
from bs4 import BeautifulSoup

page= requests.get("https://www.mygov.in/covid-19")
app = Flask(__name__)
soup=BeautifulSoup(page.content,"html.parser")
li1=[]
li2=[]
dic={}
info=soup.find_all(class_="iblock_text")
for ele in info:
    li1.append(ele.find(class_="icount").get_text())
    li2.append(ele.find(class_="info_label").get_text())

date=soup.find(class_="info_title")
data=date.span.get_text()
for i in range(len(li1)):
    dic[li2[i]]=li1[i]
print(dic)

@app.route("/")
def corona():
    return render_template("Corona.html",data=data,dic=dic)

if __name__=="__main__":
	app.run(debug=True)