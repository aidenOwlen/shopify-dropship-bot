from selenium import webdriver  
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.options import Options 
from selenium.common.exceptions import NoSuchElementException 
import bs4 as bs 
from PyQt4.QtCore import *
from PyQt4.QtGui import * 
from PyQt4 import QtCore,QtGui 
from PyQt4.QtCore import QThread 
from threading import Thread 
import time 
import sqlite3 
from datetime import datetime 
import random 
import urllib.request 
import re 
import Functions
from urllib.request import Request, urlopen 
from shopInterface import *


FirstTimer = True
if FirstTimer == True:
    coo = sqlite3.connect("database.db")
    cuu = coo.cursor()
    query = "CREATE TABLE IF NOT EXISTS PRODUCTS(ID INTEGER PRIMARY KEY AUTOINCREMENT, Title VARCHAR , OldPrice VARCHAR , NewPrice VARCHAR, Date TEXT, Images VARCHAR, Url VARCHAR, Page VARCHAR,Statut VARCHAR)"
    try:
        cuu.execute(query)
        coo.commit()
    except Exception as E:
        coo.rollback()
    finally:
        coo.close()


def name(name):
    return driver.find_element_by_name(name)

def path(name):
    return driver.find_element_by_xpath(name)

def Class(name):
    return driver.find_element_by_class_name(name)

def id(name):
    return driver.find_element_by_id(name)

def t(sth):
    try:
        sth 
    except Exception as E:
        print("E")

def check_if_exists(Title):
    c = sqlite3.connect("database.db")
    cu = c.cursor()
    q = """SELECT Title FROM PRODUCTS WHERE Title = '{}' """.format(str(Title))
    try:
        cu.execute(q)
        c.commit()
        b = cu.fetchall()
        #print(b)
    except Exception as KFF:
        c.rollback()
        print(KFF)
    finally:
        c.close()
    return b


def updateDatabase(Title,OldPrice,NewPrice,Images,Url,Page="0",Statut="NotPosted"):
    c = sqlite3.connect("database.db")
    cu = c.cursor()
    q = """UPDATE PRODUCTS SET Title = '{}', OldPrice = '{}', NewPrice = '{}', Date = Datetime('now','localtime'), Images = '{}', Url = '{}', Page = '{}', Statut = '{}' WHERE Title = '{}' """.format(str(Title),str(OldPrice),str(NewPrice),str(Images),str(Url),str(Page),str(Statut),str(Title))
    try:
        cu.execute(q)
        c.commit()
        print("INSERTED !!! ")
    except Exception as KFF:
        c.rollback()
        print(KFF)
    finally:
        c.close()

def InsertingDatabase(Title,OldPrice,NewPrice,Images,Url,Page="0",Statut="NotPosted"):
    c = sqlite3.connect("database.db")
    cu = c.cursor()
    q = """INSERT INTO PRODUCTS VALUES(NULL,"{}","{}","{}",Datetime('now','localtime'),"{}","{}","{}","{}")""".format(str(Title),str(OldPrice),str(NewPrice),str(Images),str(Url),str(Page),str(Statut))
    try:
        cu.execute(q)
        c.commit()
        print("INSERTED !!! ")
    except Exception as KFF:
        c.rollback()
        print(KFF)
    finally:
        c.close()

class MainBot(QThread):
    def __init__(self):
        QThread.__init__(self)
    def run(self):
        global driver,wait15,wait2
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        driver = webdriver.Chrome(chrome_options = chrome_options)
        wait15 = WebDriverWait(driver,15)
        wait2 = WebDriverWait(driver,2)
       

class Kinguin(QThread):
    def __init__(self):
        QThread.__init__(self)
    def run(self):
        global driver 
       
        driver.get("https://www.kinguin.com")
        t(wait15.until(EC.presence_of_element_located((By.CLASS_NAME,"c-badge__title"))))

        try:
            driver.find_element_by_xpath("""//*[@id="app"]/div[4]/div/p/button""").click()
        except:
            pass

        i = 0
        links = []
        try:
            for a in driver.find_elements_by_tag_name("a"):
                if re.search("https://www.kinguin.net/category/[0-9]+/[a-zA-Z0-9-]+/",str(a.get_attribute("href"))):
                        if str(a.get_attribute("href")) not in links:
                            links.append(str(a.get_attribute("href")))
        except Exception as K:
            pass
        j = 0
        for cha in links:
            global OldPrice,title,url,NewPrice,Page,Statut 
            Page = "None"
            Statut = "Not posted"
            try:
                r = urllib.request.urlopen(cha).read()
                #print("this is the url with problems .. " + str(cha) + " number : " + str(j))
                OldPrice = re.search('data-no-tax-price="(?P<fd>[0-9]{0,3}.?[0-9]{0,5})"',str(r))
                OldPrice = str(OldPrice.group("fd"))
             
                j+=1
                OldPrice = float(OldPrice)
                NewPrice = OldPrice * 2
               
                N1 = re.search("https://www.kinguin.net/category/[0-9]{1,8}/(?P<title>[a-zA-Z0-9-]+)/",cha)

                title = N1.group("title")
               
                url = cha 
                InsertingDatabase(title,OldPrice,NewPrice,"Nope",url,"0","NotPosted")
                self.emit(SIGNAL("bhh"),"fds")
            except Exception as B:
                print(B)
               
class G2a(QThread):
    def __init__(self):
        QThread.__init__(self)
    def run(self):
        global driver,OldPrice,title,url,NewPrice,Page,Statut 
        si = int(pageMin)
        links = []
        if sortBy == "Price":
            linkof = "https://www.g2a.com/category/all?sort=price-lowest-first%3Fpage%3D3&"
        else:
            linkof = "https://www.g2a.com/category/all?"
        while si <= int(pageMax):
            driver.get(linkof + "page={}".format(str(si)))
            si+= 1 
            a = driver.find_elements_by_tag_name("li")
            for j in a: 
                if j.get_attribute("class") == "products-grid__item":
                    try:
                        h = j.find_elements_by_tag_name("a")
                        for hh in h:
                            hj = hh.get_attribute("href")
                            if hj not in links:
                                links.append(hj)
                    except:
                        pass
        for cha in links:
            Page = str(si)
            Statut = "Not posted"
            try:
                driver.get(cha)
                r = driver.page_source

                OldPrice = re.search('<div class="product-page-v2-price__price">(?P<fd>[0-9]{0,3}.?[0-9]{0,5})',str(r))
                print("hi")
                OldPrice = str(OldPrice.group("fd"))
                print("nope")
                OldPrice = float(OldPrice)
           
                NewPrice = OldPrice * 2
                print(cha)

                N1 = re.search("https://www.g2a.com/(?P<title>[a-zA-Z0-9-]+)",cha)
                print(N1.group("title"))

                title = N1.group("title")
                url = cha 
                img = re.findall('{"name":"original","url":"(https://images.g2a.com/.*?)"',driver.page_source)
                img = "*".join(img)
                print(img)
                
                try:
                    InsertingDatabase(title,OldPrice,NewPrice,img,url,str(si),"NotPosted")
                except Exception as KK:
                    raise KK
                    print(KK)
                self.emit(SIGNAL("bhhG2a"),"fds")
                print("we here ")

            except Exception as Ko:
                print(Ko)

class updateAllkey(QThread):
    def __init__(self):
        QThread.__init__(self)
        
        for cha in links:
           
            Page = "None"
            Statut = "Not posted"
            try:
                r = urllib.request.urlopen(cha).read()
         
                OldPrice = re.search('<meta itemprop="lowPrice" content="(?P<fd>[0-9]{0,3}.?[0-9]{0,5})"',str(r))
                OldPrice = str(OldPrice.group("fd"))
                OldPrice = float(OldPrice)
                NewPrice = OldPrice * 1.4

                N1 = re.search("https://www.allkeyshop.com/blog/(?P<title>[a-zA-Z0-9-]+)/",cha)

                title = N1.group("title")
                url = cha 
                soup = bs.BeautifulSoup(str(r),"lxml")
                ssA = soup.find_all("div", class_="gallery-slider")
                img = [elt.img["src"] for elt in ssA]
                #img = re.findall('data-lazy-type="image" data-lazy-src="(https://www.allkeyshop.com/.*?)"',str(r))
                img = "*".join(img)
               
                try:
                     if len(check_if_exists(title)) == 0:
                            print(  "This is the length : " + len(check_if_exists(title)))

                            InsertingDatabase(title,OldPrice,NewPrice,img,url,str(si),category)
                            print("Yup")
                     else:
                        print("Updating database")
                        updateDatabase(title,OldPrice,NewPrice,img,url,str(si),category)
                        
                except Exception as KK:
                    print(KK)
                self.emit(SIGNAL("bhhAllKey"),"fds")
               
            except Exception as Ko:
                print(Ko)

class AllKey(QThread):
    def __init__(self):
        QThread.__init__(self)
    def run(self):
        global driver,OldPrice,title,url,NewPrice,Page,Statut 

        print(pageMin, pageMax)
        for loo in ["pc-software-all","action","adventure","fps","Management","mmorpg","racing","role playing","simulation"]:
            
	        si = int(pageMin)
	        links = []

	        if sortBy == "Price":
	            linkof = "https://www.allkeyshop.com/blog/catalogue/sort-price-asc"
	        else:
	            #linkof = "https://www.allkeyshop.com/blog/catalogue/sort-rating-desc"
	            linkof = "https://allkeyshop.com/blog/catalogue/category-" + loo

	        while si <= int(pageMax):
	            driver.get(linkof+"/page-{}/".format(str(si)))
	            si+= 1
	            a = driver.find_elements_by_tag_name("li")
	            
	            for j in a:
	                if j.get_attribute("class") == "search-results-row":
	                    
	                    try:
	                        h = j.find_element_by_class_name("search-results-row-link")
	                        c = h.get_attribute("href")
	                        links.append(c)

	                    except Exception as K:
	                        raise K
	            time.sleep(2)
	        for cha in links:
	           
	            Page = "None"
	            Statut = "Not posted"


	            try:
	                r = urllib.request.urlopen(cha).read()
	         
	                OldPrice = re.search('<meta itemprop="lowPrice" content="(?P<fd>[0-9]{0,3}.?[0-9]{0,5})"',str(r))
	                OldPrice = str(OldPrice.group("fd"))
	                OldPrice = float(OldPrice)
	                NewPrice = OldPrice * 1.5

	                N1 = re.search("https://www.allkeyshop.com/blog/(?P<title>[a-zA-Z0-9-]+)/",cha)

	                title = N1.group("title")
	                url = cha 
	                soup = bs.BeautifulSoup(str(r),"lxml")
	                ssA = soup.find_all("div", class_="gallery-slider")
	                img = [elt.img["src"] for elt in ssA if "video" not in elt.img["src"] and "trailer" not in elt.img["src"]]
	                #img = re.findall('data-lazy-type="image" data-lazy-src="(https://www.allkeyshop.com/.*?)"',str(r))
	                img = "*".join(img)
	               
	                try:
	                     if len(check_if_exists(title)) == 0:
	                            InsertingDatabase(title,OldPrice,NewPrice,img,url,str(si),loo)
	                            print("Yup")
	                     else:
	                        updateDatabase(title,OldPrice,NewPrice,img,url,str(si),loo)
	                        print("Updating database")
	                except Exception as KK:
	                    print(KK)
	                self.emit(SIGNAL("bhhAllKey"),"fds")
	               
	            except Exception as Ko:
	                print(Ko)

	            time.sleep(2)

class MainInterface(Ui_MainWindow):
    def retranslateUi(self,MainWindow):
        super(__class__,self).retranslateUi(MainWindow)
        header = self.mainTable.horizontalHeader()
        header.setResizeMode(1, QtGui.QHeaderView.Stretch)
        header.setResizeMode(6, QtGui.QHeaderView.Stretch)
        header.setResizeMode(5, QtGui.QHeaderView.Stretch)
        header.setResizeMode(4, QtGui.QHeaderView.Stretch)
        self.convert.clicked.connect(self.convertt)
        self.Scrap.clicked.connect(self.scrap)
        self.From.clear()
        self.From.addItems(["Action","Adventure","FPS","Management","MMORPG","Racing","Role playing","Simulation","Sport","Strategy","XBOX 360", "XBOX Live", "XBOX One", "Nintendo","Playstation", "Game cards","Software","ALL"])
        for i in range(100):
            self.P1.addItem(str(i))
            self.P2.addItem(str(i))
        XPresc = Functions.Selecting_All_Data("PRODUCTS")
        if len(XPresc) >=1:
            self.mainTable.setRowCount(0)
        for row_number,row_data in enumerate(XPresc):
            self.mainTable.insertRow(row_number)
            for colum_number,data in enumerate(row_data):
                self.mainTable.setItem(row_number,colum_number,QTableWidgetItem(str(data)))
    def do(self):
        s = datetime.now().strftime("%H:%M:%S")

        cur = self.mainTable.rowCount()
        try:
            iddd = self.mainTable.item(cur-1,0).text()
            iddd = int(iddd)
            iddd += 1
            iddd = str(iddd)
        except:
            iddd = "1"
        self.mainTable.insertRow(cur)
        self.mainTable.setItem(cur, 0, QTableWidgetItem(str(iddd)))
        self.mainTable.setItem(cur,1,QTableWidgetItem(str(title)))
        self.mainTable.setItem(cur,2,QTableWidgetItem(str(OldPrice)))
        self.mainTable.setItem(cur,3,QTableWidgetItem(str(NewPrice)))
        self.mainTable.setItem(cur,6,QTableWidgetItem(str(url)))
        self.mainTable.setItem(cur,7,QTableWidgetItem(str(Page)))
        self.mainTable.setItem(cur,8,QTableWidgetItem(str(Statut)))
    def convertt(self):
        self.txt = self.textConvert.toPlainText()
        self.txt = self.txt.replace("*","\n")
        self.textConvert.clear()
        self.textConvert.setText(self.txt)
    def scrap(self):

        
        global pageMax,pageMin, sortBy,category
        category = self.From.currentText()
        self.website = self.webFetch.currentText()
        self.p1 = self.P1.currentText()
        self.p2 = self.P2.currentText()
        pageMax = self.p2 
        pageMin = self.p1
        if self.Rating.isChecked():
            self.sort = "Rating"
            sortBy = "Rating"
        else:
            self.sort = "Price"
            sortBy = "Price"
        self.mainbot = MainBot()
        self.mainbot.start()
        self.mainbot.wait()
        if self.website == "Kinguin":
            print("scraping kinguin")
            self.kinguin = Kinguin()
            self.kinguin.start()
            MainWindow.connect(self.kinguin,SIGNAL("bhh"),self.do)
        if self.website == "G2a":
            print("scraping G2a")
            self.g2a = G2a()
            self.g2a.start()
            MainWindow.connect(self.g2a,SIGNAL("bhhG2a"),self.do)
        if self.website =="Allkeyshop":
            print("scraping allkey")
            self.allkey = AllKey()
            self.allkey.start()
            MainWindow.connect(self.allkey,SIGNAL("bhhAllKey"),self.do)

            







if __name__ == "__main__":
    import sys 
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = MainInterface() 
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())