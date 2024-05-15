# LIMIT_MONITORING_APPLICATION"

WORKING

The app consist of 3 inbuilt criterias and users are encouraged to add new criterias as they want.

The app is seeking the help of a third  party API called 'OPENWEATHERMAP' to fetch live weather updates

The app uses CELERY to fetch updated weather details through API calls in regular intervals of time(5mins)
	
Once the data is fetched , the app cross checks the data from the response with the criterias stored in the database, if any certain criterias are met, updates are made in the database



STRUCTURE AND FUNCTIONALITES

The project folder is called 'LMA' short for 'LIMIT MONITORING APPLICATION'

One app is used - 'limit_monitoring_application'

4 API'S are provided for the users:

1. AN API FOR CREATING A NEW CRITERIA
2. AN API FOR UPDATING AN EXISTING CRITERIA
3. AN API FOR RETRIEVING EXISTIN CRITERIAS
4. AN API TO DELETE AN EXISTING CRITERIA


MODELS:
1.Criterias
comparison_operator = '<'
Temperature         = 30
status              = False
about               = 'mild temperature'
    
    
A single model has been used, user can add criterias accordingly.

Inside the app 'limit_monitoring_application' there is a file called 'openweatherapi.py' which contains the logic to fetch weather data from a third party API and 
and then it is checked with the criterias in the database and if certain criterias are met , the BOOLEAN FIELD in the database model is updated as TRUE.
This process is scheduled to happen every 5 minutes with the help of CELERY BEAT.


ERD
An image of the database model has been generated with the help of 'django_extensions' and 'pygraphviz' and it has been added in the directory same as this README file in the name 'ERD.PNG'

CELERY
COMMAND TO RUN CELERY PROCESS = celery -A LMA worker --beat --loglevel=info
    
 
