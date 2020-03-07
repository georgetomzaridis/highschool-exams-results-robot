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
print('[!!!] ΠΡΟΣΟΧΗ: Το πρόγραμμα εκτελείται συνέχεια μέχρι να καταφέρει να εξαγάγει τους βαθμούς σας απο την σελίδα του υπουργείου. Αν τα καταφέρει αποθηκεύει μια εικόνα των αποτελεσμάτων σας (screenshot) και τερματίζει την λειτουργία του')
print('[#] Αν αντιμετωπίζεται προβλήματα με την εκτέλεση του προγράμματος παρακαλώ αναφέρεται τα εδώ https://github.com/georgetomzaridis/highschool-exams-results-robot/issues')
print('------------------------------------------------------------------')
student_code = input('Κωδικός Υποψηφίου: ')
student_begins = input('Αρχικά Υποψηφίου: ')

results_snapped = 0

if student_code != '' and student_begins != '' or student_code != '' or student_begins != '':
    page_url = 'https://results.it.minedu.gov.gr/'
    while results_snapped == 0:
        options_browser = webdriver.ChromeOptions()
        options_browser.add_argument("--window-size=1920,1080")
        options_browser.add_argument("--headless")
        options_browser.add_argument("--no-sandbox")
        options_browser.add_argument("--disable-dev-shm-usage")
        options_browser.add_argument("--disable-gpu")
        options_browser.add_argument("--incognito")
        options_browser.add_experimental_option("excludeSwitches", ["enable-automation"])
        options_browser.add_experimental_option('useAutomationExtension', False)
        driver = webdriver.Chrome(chrome_options=options_browser)
        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
            Object.defineProperty(navigator, 'webdriver', {
              get: () => undefined
            })
          """
        })
        driver.execute_cdp_cmd("Network.enable", {})
        driver.execute_cdp_cmd("Network.setExtraHTTPHeaders", {"headers": {"User-Agent": "browser1"}})
        print('[' + str(datetime.now())[11:-10] + ']', '  [OK]  ', "Άνοιγμα Σελίδας " + page_url)
        driver.start_client()
        driver.get(str(page_url))
        time.sleep(3)
        try:
            pagetitle = driver.title
            print('[' + str(datetime.now())[11:-10] + ']', '  [OK]  ', "Τίτλος σελίδας: " + str(driver.title))
            if "Εκτός Λειτουργίας" in str(driver.title) and ("Πανελλαδικών" not in str(driver.title)) :
                print('[' + str(datetime.now())[11:-10] + ']', '  [***]  ',
                      "Σελίδα εκτός λειτουργίας δοκιμάζω ξανά σε 30 λεπτά")
                time.sleep(1800)
                print('[' + str(datetime.now())[11:-10] + ']', '  [***]  ', "Ανανέωση σελίδας")
            else:
                try:
                    panelel_title = element = WebDriverWait(driver, 2).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="mineduLogo"]')))
                    if "Αποτελέσματα Πανελλαδικών Εξετάσεων" in str(driver.title):
                        print('[' + str(datetime.now())[11:-10] + ']', '  [OK]  ',
                              "Η σελίδα φορτώθηκε και είναι προσβάσιμη")
                        time.sleep(2)
                        kodikos = driver.find_element_by_xpath('//*[@id="searchform-code"]')
                        arxika = driver.find_element_by_xpath('//*[@id="searchform-initials"]')
                        print('[' + str(datetime.now())[11:-10] + ']', '  [@]  ', "Εισαγωγή στοιχείων υποψηφίου")
                        kodikos.send_keys(student_code)
                        print('[' + str(datetime.now())[11:-10] + ']', '  [>>]  ',
                              "Κωδικός Υποψηφίου: " + str(student_code))
                        time.sleep(2)
                        arxika.send_keys(student_begins)
                        print('[' + str(datetime.now())[11:-10] + ']', '  [>>]  ',
                              "Αρχικά Υποψηφίου: " + str(student_begins))
                        time.sleep(2)
                        send_btn = driver.find_element_by_xpath('//*[@id="login-form"]/div[3]/button')
                        print('[' + str(datetime.now())[11:-10] + ']', '  [!!!!!]  ', "Αναζήτηση Αποτελεσμάτων Υποψηφίου")
                        send_btn.click()
                        time.sleep(8)
                        try:
                            panelel_title = element = WebDriverWait(driver, 2).until(
                                EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[1]/div[2]/div/div/div[1]/h3')))
                            driver.save_screenshot("APOTELESMATA-" + str(student_code) + ".png")
                            print('[' + str(datetime.now())[11:-10] + ']', '  [!!!!!]  ', "SCREENSHOT :)")
                            time.sleep(1.5)
                            driver.quit()
                            print('[' + str(datetime.now())[11:-10] + ']', '  [RESULTS]  ',
                                  "Tα αποτελεσματα βγηκαν φωτογραφια και αποθηκεύτηκαν με ονομα APOTELESMATA-" + str(
                                      student_code) + "")
                            results_snapped = 1
                            time.sleep(2)
                            driver.quit()


                        except:
                            print('[' + str(datetime.now())[11:-10] + ']', '  [ERROR]  ',
                                  "Η σελίδα έχει πρόβλημα μαλλον (4), προσπαθώ ξανά σε 1 λεπτο")
                            print('[' + str(datetime.now())[11:-10] + ']',
                                  ' Σημείωση: Ενδέχετε τα στοιχεία που δώσατε στην αρχή να είναι εσφαλμένα, παρακαλώ ελέγξτε τα και αν χρειαστεί ξανατρέξτε το πρόγραμμα για την εισαγωγή νέων στοιχείων υποψηφίου.')
                            time.sleep(60)
                            driver.quit()
                    else:
                        print('[' + str(datetime.now())[11:-10] + ']', '  [ERROR]  ',
                              "Η σελίδα έχει πρόβλημα μαλλον (1), προσπαθώ ξανά σε 1 λεπτο")
                        print('[' + str(datetime.now())[11:-10] + ']',
                              ' Σημείωση: Ενδέχετε τα στοιχεία που δώσατε στην αρχή να είναι εσφαλμένα, παρακαλώ ελέγξτε τα και αν χρειαστεί ξανατρέξτε το πρόγραμμα για την εισαγωγή νέων στοιχείων υποψηφίου.')
                        time.sleep(60)
                        driver.quit()
                except:
                    print('[' + str(datetime.now())[11:-10] + ']', '  [ERROR]  ',
                          "Η σελίδα έχει πρόβλημα μαλλον (2), προσπαθώ ξανά σε 1 λεπτο")
                    print('[' + str(datetime.now())[11:-10] + ']', ' Σημείωση: Ενδέχετε τα στοιχεία που δώσατε στην αρχή να είναι εσφαλμένα, παρακαλώ ελέγξτε τα και αν χρειαστεί ξανατρέξτε το πρόγραμμα για την εισαγωγή νέων στοιχείων υποψηφίου.')
                    time.sleep(60)
                    driver.quit()
        except:
            print('[' + str(datetime.now())[11:-10] + ']', '  [ERROR]  ',
                  "Η σελίδα έχει πρόβλημα μαλλον (3), προσπαθώ ξανά σε 1 λεπτο")
            print('[' + str(datetime.now())[11:-10] + ']',
                  ' Σημείωση: Ενδέχετε τα στοιχεία που δώσατε στην αρχή να είναι εσφαλμένα, παρακαλώ ελέγξτε τα και αν χρειαστεί ξανατρέξτε το πρόγραμμα για την εισαγωγή νέων στοιχείων υποψηφίου.')
            time.sleep(60)
            driver.quit()
else:
    print("[!!!] Παρακαλώ συμπληρώστε τα στοιχεία υποψηφίου που θα βρείτε στο δελτίο εξεταζομένου")




