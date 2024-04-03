import csv

#create filepath
election_file_path = "PyPoll\Resources\election_data.csv"

#set variables
total_votes = 0
candidates = []
candidate_votes = []

# open the file
with open(election_file_path) as election_file:
    csv_file = csv.reader(election_file)
    next(csv_file)
    
    
        
        

