from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import requests
from bs4 import BeautifulSoup
from time import sleep
from convert104 import Ui_Dialog
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMessageBox,QApplication, QMainWindow, QPushButton,QWidget
import sys
import certifi


app=QApplication(sys.argv)
widget=QWidget()
ui=Ui_Dialog()
ui.setupUi(widget)
ca = certifi.where()

def showMessageBox():
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText("恭喜你，查詢完畢!尊貴的可莉玩家!")
    msgBox.setWindowTitle("偷偷的，桑貝比")
    msgBox.exec_()

def connectDatabase():
    print("Connect")
    uri = "mongodb+srv://im_idiot:ur_idiot@cluster0.zzjp4bk.mongodb.net/?retryWrites=true&w=majority"
    global client
    client = MongoClient(uri, server_api=ServerApi('1'),tlsCAFile=ca)
    try:
        client.admin.command('ping')
        ui.output.setText("連線成功！")
        global resultsalaryyes
        global resultsalaryno
        resultsalaryyes=1
        resultsalaryno=1
        sleep(0.5)
    except Exception as e:
        print(e)
        ui.output.setText("連線失敗，哭哭超可悲！")


def goSearch():
    global page
    print("Search")
    db=client["104大數據職缺清單"]
    col=db.爬到的資料
    col.drop()
    searchinput=ui.lineEdit.text()
    ui.output.setText("輸入內容："+searchinput+"，啟動！")

    res=requests.get('https://www.104.com.tw/jobs/search/?ro=0&keyword='+searchinput+'&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&order=1&asc=0&page=1&mode=s&jobsource=2018indexpoc&langFlag=0&langStatus=0&recommendJob=1&hotJob=1')
    soup=BeautifulSoup(res.text)
    db=client["104大數據職缺清單"]
    col=db.爬到的資料

    page=1
    while soup.find_all('article',class_="b-block--top-bord job-list-item b-clearfix js-job-item")!=[]:
        print('=======================')
        print('現正讀取第',page,'頁')
        #單頁爬蟲
        for job in soup.find_all('article',class_="b-block--top-bord job-list-item b-clearfix js-job-item"):
            a1 = str(job.a.text)
            b1 = str('https:'+job.a['href'])
            c1 = str(job.ul.a.text.strip())
            d1 = str(job.select('ul')[1].li.text)
            
            if  job.find('div',class_="job-list-tag b-content").select('span')!=[] and job.find('div',class_="job-list-tag b-content").select('span')[0].text=='待遇面議':
                e1 = str(job.find('div',class_="job-list-tag b-content").span.text)
                
            else:
                e1 = str(job.find('div',class_="job-list-tag b-content").a.text)
            job1 = {
                '職缺名稱':a1,
                '職缺連結':b1,
                '公司名稱':c1,
                '工作地區':d1,
                '薪資待遇':e1
            }
            col.insert_one(job1)
        page+=1    
        res=requests.get('https://www.104.com.tw/jobs/search/?ro=0&keyword='+searchinput+'&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&order=1&asc=0&page='+str(page)+'&mode=s&jobsource=2018indexpoc&langFlag=0&langStatus=0&recommendJob=1&hotJob=1')
        soup=BeautifulSoup(res.text)
        sleep(0.5)
    ui.jobresult.setText("我是可莉玩家")
    showMessageBox()
def salaryYesCheck():
    print("Salary yes")
    global resultsalaryyes
    if ui.salaryyes.isChecked()==1:
        resultsalaryyes=1
    else:
        resultsalaryyes=0
def salaryNoCheck():
    print("Salary no")
    global resultsalaryno
    if ui.salaryno.isChecked()==1:
        resultsalaryno=1
    else:
        resultsalaryno=0
def goFilter():
    print("Filter")
    db=client["104大數據職缺清單"]
    col=db.爬到的資料
    
    if ui.lineEdit_2.text()=="":
        resultarea=list(col.find())
    else:
        resultarea=list(col.find({"工作地區":ui.lineEdit_2.text()}))
    filtersalary=[]
    if resultsalaryno==1:
        filtersalary+=list(col.find({"薪資待遇":"待遇面議"}))
    if resultsalaryyes==1:
        tmp=list(col.find({"薪資待遇":"待遇面議"}))
        filtersalary+=[value for value in list(col.find()) if value not in tmp]
    result=[value for value in resultarea if value in filtersalary]
    stringtogether=""
    for i in result:
        stringtogether+=i["職缺名稱"]+"\n"
        stringtogether+=i["職缺連結"]+"\n"
        stringtogether+=i["公司名稱"]+"\n"
        stringtogether+=i["工作地區"]+"\n"
        stringtogether+=i["薪資待遇"]+"\n\n"
    ui.jobresult.setText(stringtogether)

ui.pushButton_2.clicked.connect(connectDatabase)
ui.activate.clicked.connect(goSearch)
ui.salaryyes.clicked.connect(salaryYesCheck)
ui.salaryno.clicked.connect(salaryNoCheck)
ui.filter.clicked.connect(goFilter)


widget.show()
app.exec_()

uri = "mongodb+srv://im_idiot:ur_idiot@cluster0.zzjp4bk.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))
try:
    client.admin.command('ping')
except Exception as e:
    print(e)
db=client["104大數據職缺清單"]
col=db.爬到的資料
col.drop()



# '''
# A1="職缺名稱"
# B1="職缺連結"
# C1="公司名稱"
# D1="工作地區"
# E1="薪資待遇"
# '''














