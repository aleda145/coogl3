
# **Getting started - Trending**
## About
The trending module is the part of the system that retrieves trending content from social media sources. 
## Obtaining API keys
 To be able to use the trendning module of the system you need to obtain credentials for the APIs that are beeing used (Youtube and Twitter). Please follow the steps below. 

### Youtube API
1. First of all, you will need a Google account to access the [Google Developers Console](https://console.developers.google.com/), where you will request for an API key.
2. Create a project in the Google Developers Console and obtain authorization credentials.
3. When the project is created, make sure the [YouTube Data API v3](https://developers.google.com/youtube/v3/) is one of the services that is registered to use: 
    3. Go to the Developers Console and select the project that you registered.
    3. Open the API Library in the Google Developers Console. Create new project. In the list of APIs, make sure the status is ON for the Youtube Data API v3.
4. Go to the Google Developers Console and select the project that has been created.
5. Click on ENABLE APIS AND SERVICES and find Youtube Data API v3.
6. Click on Manage and then Create Credentials
7. Add credentials to you project.
    7. Select “Youtube Data API v3”
    7. Calling from a “Other application”
    7. Choose “Public data” on the radio buttons
    7. Click on Create
8. You should now have received your credentials for using the Youtube Data API v3.
9. Insert the created Developer Key in the project. Software/TrendManager/YoutubeAPI.py.

```python
DEVELOPER_KEY = "INSERT DEVELOPER KEY HERE";
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
```


> **Note:** The Youtube Data API has a limited amount of requests per day (1 000 000), more information is to be found at [Google API Console](https://console.developers.google.com/apis/.) 
     
### Twitter API
1. First of you will need a [Twitter](https://twitter.com) account. If you do not already have one you will need to create an account.
2. When you have logged in go to [Twitter application management] (https://apps.twitter.com/). 
3. Click on Creat
e new app
4. Fill in the details.
5. When the app has been successfully created choose **Key and Access Tokens** in the navigation bar.
6. Here you can find your Consumer key and your Consumer Secret.
7. You will also need access token, create it by clicking Create access token
8. Now that the credentials are created go to the project and open: Software/TrendManager/TwitterAPI.py and edit the following lines of code with the Credentials.

```python
access_token = "Access Token";
access_token_secret = "Access Token Secret"
consumer_key = "Consumer Key"
consumer_secret = "Consumer Key Secret"
```  

> **Note:** The Twitter API has a limited amount of requests  (180 calls every 15 minutes), more information is to be found at [Twitter API rate limiting] (https://developer.twitter.com/en/docs/basics/rate-limiting)


### To run the trending module
1. Open a terminal 
2. Navigate to Database/DBFillmovies and remove app.db (if exsists)
3. Run DBFillmovies.py
4. Navigate to TrendManager and run RunTrend.py
5. The database are now updated with the latest trendscores. 

