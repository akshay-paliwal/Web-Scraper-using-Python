from flask import Flask, render_template, url_for, request, redirect
import requests
#from flask_sqlalchemy import SQLAlchemy
#from datetime import datetime
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
import pymongo

app = Flask(__name__)




@app.route('/',methods=['POST','GET'])
def index():
    if request.method == 'POST':
        searchString = request.form['content']
        try:
            dbConn = pymongo.MongoClient("mongodb://localhost:27017/")  # opening a connection to Mongo
            db = dbConn['myDB']
            reviews = db[searchString].find({})
            if reviews.count() > 0:
                return render_template('results.html',reviews=reviews)
            else:
                linkedin_url = "https://www.linkedin.com/jobs/search/?geoId=102713980&keywords={}&location=India".format(searchString)

                uClient = uReq(linkedin_url)
                linkedinPage = uClient.read()
                uClient.close()
                linkedin_html = bs(linkedinPage, "html.parser")

                all_reviews = linkedin_html.find_all("li", {
                    "class": "result-card job-result-card result-card--with-hover-state"})
                reviews = []
                table = db[searchString]
                for review in all_reviews:
                    # Finding the job name
                    job = review.find_all('span', {'class': 'screen-reader-text'})
                    job_name = [e.get_text() for e in job]
                    j = job_name[0]
                    # Finding the job location
                    location = review.find_all('span', {'class': 'job-result-card__location'})
                    location_name = [e.get_text() for e in location]
                    l = location_name[0]
                    # Finding the Company name
                    company = review.find_all('a',
                                              {'class': 'result-card__subtitle-link job-result-card__subtitle-link'})
                    company_name = [e.get_text() for e in company]
                    try:
                        c = company_name[0]
                    except:
                        c = "No company name given."
                    # Finding job URL
                    url = review.find_all('a', {'class': 'result-card__full-card-link'})
                    link = [e.get("href") for e in url]
                    u = link[0]
                    # Creating a dictionary
                    mydict = {"Job Name": j, "Company": c, "Location": l, "URL": u}
                    x = table.insert_one(mydict)
                    reviews.append(mydict)
                return render_template('results.html', reviews=reviews)
        except:
            return 'something is wrong'
            #return render_template('results.html')
    else:
        return render_template('index.html')
if __name__ == "__main__":
    app.run(debug=True)
