# AmazonTitanScrape
The main concept of the job is to fetch data provided by the Titans Chrome Extension, based on the keywords provided on the excel file.
For the project to be done in selenium here are the steps:
1. Gather user requirements (Browser version, Python version, etc)
2. Write the script:
2. Import essential tools in Python.
2. Open a browser tab.
2. Add extension
2. Login on extension 
2. Visit Amazon.com
2. Check for captcha, maximize window then refresh page if encountered. 
2. Open the keyword excel file put into an array.
2. Read the first keyword, then plug in to the amazon search bar.
2. Hit enter, wait until the extension table of data is done loading.
2. Put data in data frame.
2. Loop steps e-h for every keyword, then write into a new excel file when done.
2. Save.
