# highschool-exams-results-robot
#### NATIONAL EXAMINATIONS - Ministry of Education, Research and Religious Affairs 
Trying to gather candidate results from https://results.it.minedu.gov.gr to help student limit their axienty about their national exam final results, even if the platform goes down or not accepting new requests 

![alt text](https://github.com/georgetomzaridis/highschool-exams-results-robot/blob/master/resultspage.png "Results Page")

## Features

1. Gather candidate information (code and first letters) and trying to get results from the web application
2. If the site goes down or is busy the programm will wait 30 minutes and retry
3. If the site is out of service(this usually happends when the platform is closed for requests) the programm can wait 30 minutes and retry to access the main page
4. When the page with results show up, the programm will take a screenshot and save it in the same directory
5. It running forever :P (You can stop it any time you want)

## OS Support
Dont worry my friend, we love both windows, linux and mac. If you think to run this programm on different operating system(like linux or mac) you need to get the chrome webdrive version that support your operating system. At the end of the page a provide some links that your can check out and download the appropiate versions that fits your needs

## Screenshots
#### Platform Out of Service (Not accepting requests)
![alt text](https://github.com/georgetomzaridis/highschool-exams-results-robot/blob/master/platform-outofservice.png "Platform out of service")

#### Input candidate info (Before start)
![alt text](https://github.com/georgetomzaridis/highschool-exams-results-robot/blob/master/input-candidate-info.png "Input candidate info")

## Requirements / How does it works?
With the power of python, selenium(browser automation) and chromewebdrive the programm opens a chrome window and take the control for you 

### !WARNING!
The programm can't run if your chrome version doesn't agree with the chrome webdrive version

For example the included chromewebdrive file version is: 75

To allow the programm run smoothly you need to have chrome browser with version 75

Chrome WebDrive Version MUST equal with the Chrome Browser Version

If you dont have the right version, dont worry you can go to the chrome webdrive files, download the right version and replace the old with the new one

## Links
* Selenium: https://www.seleniumhq.org/
* Chrome WebDrive: http://chromedriver.chromium.org/downloads
* National Exams Results Platform: https://results.it.minedu.gov.gr/


## Issues / Questions
If you have questions or issues dont worry i am happy to help you. Just open an issue here in github or email me
* Email: georgetomzaridis@gmail.com

## License
MIT License

Copyright (c) 2019 George Tomzaridis

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


Good luck guys!
