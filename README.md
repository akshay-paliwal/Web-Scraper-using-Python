# Project Title
Web Scraper using Python

## Introduction
This is one of my Python projects from [Machine Learning and Deep Learning with Deployment](https://academy.ineuron.ai/machine-learning-masters.php) course, from [iNeuron.ai](https://academy.ineuron.ai/index.php). In this course, code was written to scrapp or collect the required data from any website based on the keyword given by the user. The code needs to generate the web URL based on the given keyword, send a request to web URL to get raw HTML data, parse the obtained data(HTML) to get the required information, store the information to the database, and display the result to the user.

**Web Scraping** (also termed Screen Scraping, Web Data Extraction, Web Harvesting etc.) is a technique employed to extract data from websites whereby the data is extracted and saved to a local file in your computer or to a database. It is a form of copying, in which specific data is gathered and copied from the web, typically into a central local database, for later retrieval or analysis.

## Install
This project requires Python3. Also, some of the python libraries like Flask, pymongo, bs4, request, and urllib.request.
All the liberaries can be installed using the following commands...
```
pip install flask
pip install bs4
pip install requests
pip install pymongo
pip install urllib
```
Also, the project requires a database to store the obtained information. I used the **mongoDb** as the database which can be installed from [here](https://www.mongodb.com/).<br>
Also, the project require some HTML and CSS konwledge to build the web pages for taking Keyword form the user and displaying the result to the user.

## Code
* `Step-1` Start the flask app whic will run the **"index.html"** on the localhost and get the search string given by the user.
* `Step-2` Esatblish the connection with the database using pyongo and search for the required data in the database-
  * `Step-2.1` If the required data is present in the database, return the **"result.html"** with the required data(to be displayed to the user.)
  * `Step-2.2` If the required data is present in the database do the following- <br>
      * `Step-2.2.1` Create the URL based on the string given by the user.
	  * `Step-2.2.2` Using urllib.request and .read() read the raw HTML of the webpage and using .colse() close the request.
	  * `Step-2.2.3` Using "html.parser" from bs4 parse the obtained raw HTML.
	  * `Step-2.2.4` Etract the required data from the parsed html document.
	  * `Step-2.2.5` Save the gathered data into the database and return the **"result.html"** with the extracted data.
	  
## Data
In this project I extracted the job data from Linkedin whic include the Job type, Company name, Location, and URL of the job. <br>
I ran the app on my local device with Search string as and got the following desired result...
![Image](image.jpg)
