import os
import sys
import selenium
import time
from datetime import datetime
from time import strftime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



page_url = 'https://results.it.minedu.gov.gr/'
student_code = '19065982' #ΚΩΔΙΚΟΣ ΥΠΟΨΗΦΙΟΥ <--- ΕΔΩ ΑΛΛΑΓΕΣ ΜΕ ΤΑ ΔΙΚΑ ΣΑΣ ΣΤΟΙΧΕΙΑ
student_begins = 'ΤΓΑΣ' #ΑΡΧΙΚΑ ΓΡΑΜΜΑΤΑ <--- ΕΔΩ ΑΛΛΑΓΕΣ ΜΕ ΤΑ ΔΙΚΑ ΣΑΣ ΣΤΟΙΧΕΙΑ
#page_url = 'file:///C:/Users/georg/Desktop/%CE%A0%CE%91%CE%9D%CE%95%CE%9B%CE%9B%CE%91%CE%94%CE%99%CE%9A%CE%95%CE%A3%20%CE%95%CE%9E%CE%95%CE%A4%CE%91%CE%A3%CE%95%CE%99%CE%A3%202016%20-%20%CE%95%CE%AF%CF%83%CE%BF%CE%B4%CE%BF%CF%82.html'


#driver.get("file:///C:/Users/georg/Desktop/%CE%A0%CE%91%CE%9D%CE%95%CE%9B%CE%9B%CE%91%CE%94%CE%99%CE%9A%CE%95%CE%A3%20%CE%95%CE%9E%CE%95%CE%A4%CE%91%CE%A3%CE%95%CE%99%CE%A3%202016%20-%20%CE%95%CE%AF%CF%83%CE%BF%CE%B4%CE%BF%CF%82.html")
print('[' + str(datetime.now())[11:-10] + ']', '  [WELCOME]  ', "ΡΟΜΠΟΤ ΑΠΟΤΕΛΕΣΜΑΤΩΝ ΠΑΝΕΛΛΑΔΙΚΕΣ 2019 :)")


while True:
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
    options_browser = webdriver.ChromeOptions()
    #options_browser.add_argument('headless')
    # specify the desired user agent
    options_browser.add_argument(f'user-agent={user_agent}')
    driver = webdriver.Chrome(chrome_options=options_browser)
    print('[' + str(datetime.now())[11:-10] + ']', '  [✓]  ', "Άνοιγμα Σελίδας " + page_url)
    driver.get(str(page_url))
    time.sleep(6)
    try:
        pagetitle = driver.title
        print('[' + str(datetime.now())[11:-10] + ']', '  [✓]  ', "Τίτλος σελίδας: " + pagetitle)
        try:
            offline_icon = driver.find_element_by_xpath('/html/body/img[2]')
            print('[' + str(datetime.now())[11:-10] + ']', '  [***]  ',
                  "Σελίδα εκτός λειτουργίας δοκιμάζω ξανά σε 30 λεπτά")
            time.sleep(1800)
            print('[' + str(datetime.now())[11:-10] + ']', '  [***]  ', "Ανανέωση σελίδας")
        except:
            continue
        if "Εκτός Λειτουργίας" in pagetitle and ("ΠΑΝΕΛΛΑΔΙΚΕΣ ΕΞΕΤΑΣΕΙΣ" not in pagetitle) and("Πανελλαδικές - Αποτελέσματα" not in pagetitle) :
            print('[' + str(datetime.now())[11:-10] + ']', '  [***]  ',
                  "Σελίδα εκτός λειτουργίας δοκιμάζω ξανά σε 30 λεπτά")
            time.sleep(1800)
            print('[' + str(datetime.now())[11:-10] + ']', '  [***]  ', "Ανανέωση σελίδας")
        else:
            try:
                panelel_title = element = WebDriverWait(driver, 2).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="logo"]/center')))
                if "ΠΑΝΕΛΛΑΔΙΚΕΣ ΕΞΕΤΑΣΕΙΣ" in panelel_title.text:
                    print('[' + str(datetime.now())[11:-10] + ']', '  [OK]  ',
                          "Η σελίδα φορτώθηκε και είναι προσβάσιμη")
                    time.sleep(2)
                    kodikos = driver.find_element_by_xpath('//*[@id="LoginForm_username"]')
                    arxika = driver.find_element_by_xpath('//*[@id="LoginForm_password"]')
                    print('[' + str(datetime.now())[11:-10] + ']', '  [@]  ', "Εισαγωγή στοιχείων υποψηφίου")
                    kodikos.send_keys(student_code)
                    print('[' + str(datetime.now())[11:-10] + ']', '  [>>]  ',
                          "Κωδικός Υποψηφίου: " + str(student_code))
                    time.sleep(2)
                    arxika.send_keys(student_begins)
                    print('[' + str(datetime.now())[11:-10] + ']', '  [>>]  ',
                          "Αρχικά Υποψηφίου: " + str(student_begins))
                    time.sleep(2)
                    send_btn = driver.find_element_by_xpath('//*[@id="login-form"]/center/div[3]/input')
                    print('[' + str(datetime.now())[11:-10] + ']', '  [!!!!!]  ', "Αναζήτηση Αποτελεσμάτων Υποψηφίου")
                    send_btn.click()
                    time.sleep(6)
                    driver.save_screenshot("APOTELESMATA_SCREENSHOT.png")
                    print('[' + str(datetime.now())[11:-10] + ']', '  [!!!!!]  ', "SCREENSHOT :)")
                    time.sleep(1.5)
                    driver.quit()
                    print('[' + str(datetime.now())[11:-10] + ']', '  [RESULTS]  ',
                          "Λογικα τα αποτελεσματα βγηκαν φωτογραφια οποτε θα ξαναδουμε μετα απο 30 λεπτα")
                    time.sleep(1800)
                else:
                    print('[' + str(datetime.now())[11:-10] + ']', '  [Χ]  ',
                          "Η σελίδα έχει πρόβλημα μαλλον (1), προσπαθώ ξανά σε 1 λεπτο")
                    time.sleep(60)
                    driver.quit()
            except:
                print('[' + str(datetime.now())[11:-10] + ']', '  [Χ]  ',
                      "Η σελίδα έχει πρόβλημα μαλλον (2), προσπαθώ ξανά σε 1 λεπτο")
                time.sleep(5)
                driver.quit()
    except:
        print('[' + str(datetime.now())[11:-10] + ']', '  [Χ]  ',
              "Η σελίδα έχει πρόβλημα μαλλον (3), προσπαθώ ξανά σε 1 λεπτο")
        time.sleep(60)
        driver.quit()




