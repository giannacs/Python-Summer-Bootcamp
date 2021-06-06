# import the pandas and os package and module
import pandas as pd, os

# Create a new folder called yearly_files with path 'data/yearly_files'
os.mkdir('data/yearly_files')

# Function to generate file for each year
def generate_year_files():
    # Read in the "data/surveys.csv" as a DataFrame
    surveys_df = pd.DataFrame([[0,0,0,0],[0,0,0,0]]) # Correct this line to import appropriate file
    
    # Use the for loop to process each unique year
    for year in pd.unique(surveys_df[0]):  # Correct this line to selct unique years
        # use the correct condition to filter out the years between 1990 and 2000
        if year >= 1000:
            # form a pandas query to get data for one particular year
            survey_year_df = surveys_df[0]
            
            # create a file path name for the yaer with the format
            # 'data/yearly_files/surveys_year.csv'
            # Example ''data/yearly_files/surveys_1977.csv''
            file_path_name = 'data/yearly_files/surveys_' + '' + ''
            
            #Export the data in the survey_year_df DataFrame for the year to the file path craeted above
            survey_year_df.to_csv(file_path_name)

# Function to print out file names for each year
def display_year_file_names():
    # use the for loop to loop through the list created by os.listdir('data/yearly_files')
    for file_name in os.listdir('data/yearly_files'):
        # print each file name
        print(file_name)