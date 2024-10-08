To run correctly the code related to the first part of the project, please follow the following instructions:

1. Download the entire folder Part_1 and put the 'Google-Playstore.csv' file in Public folder of your pc

Due to time consuption and due to google policy, we decided to split the chosen app categories in order to obtain different databases
specific for each category. Only at the end we merged all the databases into a final one, leaving out possible duplicates.
Below are reported the needed steps to obtain one particular database (the only script that changes to obtain category specific database is the one called skim_nameofcategory).

As example, let's consider the steps for the creation of the database related to category 'Music'. 
After having downloaded the csv file:
1. Run 'main_new.py' --> this is the main function.
	Outputs: database specific for the selected category
		 text file with apps not found
2. Run 'main_new_search.py' --> this is the function which adds to the previous database the not found apps
3. (Optional) Run 'readFromJson.py' if you want to know the number of documents which are contained in the created database and if you want to spy it

These three steps were done for all the selected categories.

4. Download the 'Search' folder and run 'Main_search.py'
	Outputs: database specific for the search() function made with keywords
		 text file with apps not found

Lastly, after having collected all the databases each related to a specific category, in order to create the final database, run 'creation_database_tot.py' (this .py file is contained in the 'database creation' folder)

(download the folder 'database creation' where all the small databases are stored)


The final database is called db_TOT.json	