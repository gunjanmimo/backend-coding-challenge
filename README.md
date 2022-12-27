# SOLUTION
Thank you for giving this opportunity. Here is my solution.

### **Build the project**
I am using Dockerfile to build the FastAPI app. 

Commands
```
docker build -t be_challenge .
docker run -p 80:80 be_challenge
```
Access API endpoint using url `http://0.0.0.0:80/planner/get_planners` 
### **API Endpoint**

I am using one API endpoint `planner/get_planners` for 
  1. pagination
  2. filtering
  3. sorting


  Payload schema

  ```
  page_no               : int             =  0
  page_limit            : int             =  50
  sort_by               : list            =  ['id']
  sort_order            : str             =  "desc"
  filter_by             : dict            =  {}
  ```
  page_no: current page number. 
  page_limit: Max number of planning data on each page
  sort_by: List of columns names
  sort_order: sort data by ascending or descending order
  filter_by: Data filtering criteria


  **Pagination**

  We have total 10000 plan data. Each page can have `page_limit` records. Page No count starts from `0`. 

  **Sorting**

  API endpoint support multi column sorting. 
  ``sort_by`` payload parameters accepts list of key names. 

  Example payload:
  ```
  {
    "page_no":1,
    "sort_by":["totalHours","endDate"],
    "sort_order":"asc"
  }
  ```


  **Filtering**

  Filtering for following columns takes Columns name and list of values.

    1. originalId
    2. talentId
    3. talentName
    4. talentGrade
    5. bookingGrade
    6. operatingUnit
    7. officeCity
    8. officePostalCode
    9. jobManagerName
    10. jobManagerId
    11. clientName
    12. clientId
    13. industry
    14. isUnassigned
  Example: 

  If you want to filter by `officeCity` names, then payload should be
  
  ```
  {
    "page_no":1,
    "filter_by": {
        "officeCity": ["Hamburg","Neuruppin"]
    }
  }
  ```

  Example of filtering by skill, payload should be 

  ```
  {
    "page_no": 1,
    "filter_by": {
        "skills": [
            {
                "name": "TypeScript",
                "category": "Coding Language"
            },
            {
                "name": "Javascript",
                "category": "Coding Language"
            }
        ]
    }
  }
  ```

  If you want to filter by `startDate/endDate`, payload should be 

  ```
  {
    "page_no":1,
    "filter_by": {
             "startDate":["2022-01-11 00:00 ","2022-02-11 00:00 "]
    }
  }
  ```


  Similarly if you want to filter by `totalHours`, then you have to pass a lower and upper limit of `totalHours`. Example Payload 

  ```
  {
    "page_no":1,
    "filter_by": {
        "totalHours":[5,10]
    }
  }
  ```


We can use combine of all of these.  


# Backend Coding Challenge

At aspaara a squad of superheroes works on giving superpowers to planning teams.
Through our product dashboard, we give insights into data – a true super-vision
superpower. Join forces with us and build a dashboard of the future!

![aspaara superhero](aspaara_superhero.png)

## Goal

Create a simple backend application that provides an API for a dashboard which
allows a planner to get insights into client and planning information.

You will find the corresponding data that needs to be imported into the database
in `planning.json`, which contains around 10k records.

## Requirements

1. Create proper database tables that can fit the data model.
2. Create a script that imports the data into the database (sqlite).
3. Create REST APIs to get the planning data from the database.
    1. The APIs don't need to be complete, just create what you can in the
       available time.
    2. Please include at least one example on how to do each of the following:
        1. pagination
        2. sorting
        3. filtering / searching

## Data Model

* ID: integer (unique, required)
* Original ID: string (unique, required)
* Talent ID: string (optional)
* Talent Name: string (optional)
* Talent Grade: string (optional)
* Booking Grade: string (optional)
* Operating Unit: string (required)
* Office City: string (optional)
* Office Postal Code: string (required)
* Job Manager Name: string (optional)
* Job Manager ID: string (optional)
* Total Hours: float (required)
* Start Date: datetime (required)
* End Date: datetime (required)
* Client Name: string (optional)
* Client ID: string (required)
* Industry: string (optional)
* Required Skills: array of key-value pair (optional)
* Optional Skills: array of key-value pair (optional)
* Is Unassigned: boolean

## Preferred Tech Stack

* Python 3.8+
* FastAPI
* SQLAlchemy

## Submission

* Please fork the project, commit and push your implementation and add
  `sundara.amancharla@aspaara.com` as a contributor.
* Please update the README with any additional details or steps that are
  required to run your implementation.
* We understand that there is a limited amount of time, so it does not have to
  be perfect or 100% finished. Plan to spend no more than 2-3 hours on it.

For any additional questions on the task please feel free to email
`sundara.amancharla@aspaara.com`.
