from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import urllib.parse
from fpdf import FPDF
from google.cloud import storage
import gcsfs
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

json_path='/home/ubuntu/whatsapp/testing-f1218-firebase-adminsdk-wn3g1-5c95ae835f.json'


cred = credentials.Certificate(json_path)
firebase_admin.initialize_app(cred, name = 'database')

firebase_admin.initialize_app(cred, {'databaseURL' : 'https://testing-f1218-default-rtdb.asia-southeast1.firebasedatabase.app/'})
ref = db.reference('recommendation/')
button_ref = ref.child('buttonValue')
phone_ref = ref.child('number')
History = ref.child('History')
sleep(3)
inp_temp= ref.child("History").get()
history = (list(inp_temp.values())[0])
'''
pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.add_page()
pdf.set_font("Arial", size = 15)

with open("/home/ubuntu/whatsapp/myfile.txt","w") as file:
          file.write("User_data: "+ history)
file.close()
# open the text file in read mode
f = open("/home/ubuntu/whatsapp/myfile.txt","r")



# insert the texts in pdf
for x in f:
    pdf.cell(200, 10, txt = x, ln = 1, align = 'C')
  
# save the pdf with name .pdf
pdf.output("/home/ubuntu/whatsapp/user_data.pdf") 
'''
driver = webdriver.Chrome()
Link = "https://web.whatsapp.com/"
wait = None

def whatsapp_login():
    global wait, driver, Link
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    wait = WebDriverWait(driver, 20)
    print("SCAN QR CODE FOR WHATSAPP WEB IF DISPLAYED")
    driver.get(Link)
    driver.maximize_window()
    print("QR CODE SCANNED")

def send_attachment_to_unsavaed_contact(number, file_name):
    print("In send_attachment_to_unsavaed_contact method")
    params = {'phone': str(number)}
    end = urllib.parse.urlencode(params)
    final_url = Link + 'send?' + end
    print(final_url)
    driver.get(final_url)
    WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//div[@title = "Menu"]')))
    print("Page loaded successfully.")
    for retry in range(3):
        try:
            sleep(5)
            wait.until(EC.presence_of_element_located((By.XPATH, '//div[@title = "Attach"]'))).click()
            break
        except Exception as e:
            print("Fail during click on Attachment button.")
            if retry==2:return
    attachment = driver.find_element(By.XPATH, '//input[@accept="*"]')
    attachment.send_keys(file_name)
    sleep(5)
    send = wait.until(EC.presence_of_element_located((By.XPATH, '//span[@data-icon="send"]')))
    send.click()
    print("File sent successfully.")


if __name__ == "__main__":

    print("Web Page Open")
    # Let us login and Scan
    whatsapp_login()
    while True:
        pdf = FPDF(orientation='P', unit='mm', format='A4')
        pdf.add_page()
        pdf.set_font("Arial", size = 15)

        with open("C:\\Users\\JENILPATEL\\Desktop\\myfile.txt","w") as file:
            file.write("User_data: "+ history)
            file.save(
        file.close()
        # open the text file in read mode
        f = open("/home/ubuntu/whatsapp/myfile.txt","r")



        # insert the texts in pdf
        for x in f:
            pdf.cell(200, 10, txt = x, ln = 1, align = 'C')
  
        # save the pdf with name .pdf
        pdf.output("/home/ubuntu/whatsapp/"+number+".pdf") 
        inp_tempp= ref.child("buttonValue").get()
        inp = (list(inp_tempp.values())[1])
        flag = (list(inp_tempp.values())[2])
        if(inp==5 and flag == "true"):
            inp_number= ref.child("number").get()
            number = (list(inp_number.values())[0])
            number = '91' + number
            send_attachment_to_unsavaed_contact(number, "/home/ubuntu/whatsapp/"+number+".pdf")
            button_ref.update({
                'flag': "false"
                })
            sleep(5)
    driver.close() # Close the Open tab
    driver.quit()
#8347161222

