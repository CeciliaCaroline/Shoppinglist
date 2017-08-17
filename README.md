# Shopping List Application
[![Coverage Status](https://coveralls.io/repos/github/CeciliaCaroline/Shoppinglist/badge.svg?branch=master)](https://coveralls.io/github/CeciliaCaroline/Shoppinglist?branch=master)
[![Coverage Status](https://coveralls.io/repos/github/CeciliaCaroline/Shoppinglist/badge.svg)](https://coveralls.io/github/CeciliaCaroline/Shoppinglist)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/06515178c94249f092860523e08360c1)](https://www.codacy.com/app/CeciliaCaroline/Shoppinglist?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=CeciliaCaroline/Shoppinglist&amp;utm_campaign=Badge_Grade)
[![Build Status](https://travis-ci.org/CeciliaCaroline/Shoppinglist.svg?branch=master)](https://travis-ci.org/CeciliaCaroline/Shoppinglist)

The bucketlist app is an application that allows users to record, track and share things they want to buy/purchase in order to meet their desires.
This version of the application only contains designs for the User Interface that is no core functionality.

## Features
The application has a couple of features as listed below:-
 * A user is able to `Register` and get an account in the app
 * A user is able to `Login` into the app using their credentials already supplied
 * A user is able to create, edit, update and delete `Shopping Lists`
 * A user is also able to create, edit, update and delete `List Items`
 
 ## Setup
 
 Create the virtual environment and activate it
 
 ```
 virtualenv env
 source env/bin/activate
```

Then install all the required dependencies

```
pip install -r requirements.txt
```

Then run the application

```
python run.py
```

To now view the application head over to
```
http://localhost:5000
```