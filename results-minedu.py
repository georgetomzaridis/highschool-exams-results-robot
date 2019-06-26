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
print('[' + str(datetime.now())[11:-10] + ']', '  [WELCOME]  ', "ΡΟΜΠΟΤ ΑΠΟΤΕΛΕΣΜΑΤΩΝ ΠΑΝΕΛΛΑΔΙΚΕΣ 2019 :)")
print('[@] Σκοπός του προγράμματος είναι η διευκόλυνση των υποψηφίων την ημέρα των αποτελεσμάτων, με την αυτοματοποίηση της διαδικασίας ελέγχου των αποτελεσμάτων ακόμα και σε περιπτώσεις κατάρρευσης της σελίδας η μεγάλου φόρτου')
print('[!!!] ΠΡΟΣΟΧΗ: Το πρόγραμμα εκτελείται συνέχεια και αποθηκεύει μια εικόνα των αποτελεσμάτων σας (screenshot), μέχρι να το τερματίσετε εσείς')
print('[#] Αν αντιμετωπίζεται προβλήματα με την εκτέλεση του προγράμματος παρακαλώ αναφέρεται τα εδώ https://github.com/georgetomzaridis/highschool-exams-results-robot/issues')
print('------------------------------------------------------------------')
student_code = input('Κωδικός Υποψηφίου: ')
student_begins = input('Αρχικά Υποψηφίου: ')

if student_code != '' and student_begins != '' or student_code != '' or student_begins != '':
    page_url = 'https://results.it.minedu.gov.gr/'

    while True:
        options_browser = webdriver.ChromeOptions()
        options_browser.add_argument("--incognito")  # incognito mode για να μην μπλεκουμε με cookies
        options_browser.add_argument("--start-maximized")  # Αν θέλουμε να αρχίζει maximized το παράθυρο
        driver = webdriver.Chrome(chrome_options=options_browser)
        print('[' + str(datetime.now())[11:-10] + ']', '  [OK]  ', "Άνοιγμα Σελίδας " + page_url)
        driver.start_client()
        driver.get(str(page_url))
        time.sleep(3)
        try:
            pagetitle = driver.title
            print('[' + str(datetime.now())[11:-10] + ']', '  [OK]  ', "Τίτλος σελίδας: " + pagetitle)
            if "Εκτός Λειτουργίας" in pagetitle and ("ΠΑΝΕΛΛΑΔΙΚΕΣ ΕΞΕΤΑΣΕΙΣ" not in pagetitle) :
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
                        driver.save_screenshot("APOTELESMATA-"+ str(student_code) + ".png")
                        print('[' + str(datetime.now())[11:-10] + ']', '  [!!!!!]  ', "SCREENSHOT :)")
                        time.sleep(1.5)
                        driver.quit()
                        print('[' + str(datetime.now())[11:-10] + ']', '  [RESULTS]  ',
                              "Λογικα τα αποτελεσματα βγηκαν φωτογραφια και αποθηκεύτηκαν με ονομα APOTELESMATA-"+ str(student_code) + " οποτε θα ξαναδουμε μετα απο 30 λεπτα")
                        time.sleep(1800)
                    else:
                        print('[' + str(datetime.now())[11:-10] + ']', '  [ERROR]  ',
                              "Η σελίδα έχει πρόβλημα μαλλον (1), προσπαθώ ξανά σε 1 λεπτο")
                        time.sleep(60)
                        driver.quit()
                except:
                    print('[' + str(datetime.now())[11:-10] + ']', '  [ERROR]  ',
                          "Η σελίδα έχει πρόβλημα μαλλον (2), προσπαθώ ξανά σε 1 λεπτο")
                    time.sleep(60)
                    driver.quit()
        except:
            print('[' + str(datetime.now())[11:-10] + ']', '  [ERROR]  ',
                  "Η σελίδα έχει πρόβλημα μαλλον (3), προσπαθώ ξανά σε 1 λεπτο")
            time.sleep(60)
            driver.quit()
else:
    print("[!!!] Παρακαλώ συμπληρώστε τα στοιχεία υποψηφίου που θα βρείτε στο δελτίο εξεταζομένου")




