# Validare_Coding_Assignment


Objective
Fetch data from https://www.crudemonitor.ca/savePHPExcel.php using request module
Filter data based on input 
Python files to be executed as command line utility with the user inputs 
Display data filters based on the input using python packages 

Assumptions
The CSV file is provided by exporting it from the website as a csv file manually instead of programatically fetching data 
Issues
Website https://www.crudemonitor.ca/savePHPExcel.php was not exporting any data
An error message was displayed manually as well as programatically 
While processing your request, an error occurred with the date input you have provided. Please ensure that it was properly formatted (DDMMYYYY).
Format provided was exactly same as mentioned in the error
Approach 
As the data was not fetched programmatically, .csv formatted file was exported from the website
Created a virtual environment for the assignment
Installed pandas as a required package for the assignment
Imported required packages:
Pandas
Argparse
Sys
Datetime
Required arguments were passed with type and default parameters in the main to execute it as command utility.
Help parameter was mentioned to print a message regarding the format of the date
Function’s Workflow
Imported csv 
Generated data frame from csv data
In order to make sure the format of the date is valid Strptime function and isoformat function is being used for both start and end date 
Filter based on date was calculated on column at index value 2
.loc function from pandas library is being used
Conditions are mentioned in the .loc function:
Operation: greater than the user input
& is being used in order to statisfy all the conditions
filtered_data_date is the data in between user input start and end date
crude_acronym provided as user input should match the value at index 1.
