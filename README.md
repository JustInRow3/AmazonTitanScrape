# AmazonTitanScrape
The main concept of the job is to fetch data provided by the Titans Chrome Extension, based on the keywords provided on the excel file.
For the project to be done in selenium here are the steps:
1. Gather user requirements (Browser version, Python version, etc)
2. Write the script:
a. Import essential tools in Python.
b. Open a browser tab.
c. Add extension and enable extension, then visit amazon.
d. Open the keywork excel file.
e. Read the first keyword, then plug in to the amazon search bar.
f. Hit enter, use seleinum to find table id of the extension.
g. Get XPATH of each section of the header i.e Results
h. Put data in an array or data frame.
i. Loop steps e-h for every keyword, then write into a new excel file when done.
e. Save.
