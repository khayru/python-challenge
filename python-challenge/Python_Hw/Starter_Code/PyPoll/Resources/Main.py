 
#import 
import csv 
import os
from sqlite3 import Row
import collections
#import Counter
  
#Declare file
pyPoll =os.path.join('..','Resources','election_data.csv')
# print(pyPoll)


# open the csv file to read
with open(pyPoll,'r')as file:
    csvreader = csv.reader(file)
    #read skip header  
    next(csvreader)
       
#find The total number of votes cast
   
#A complete list of candidates who received votes
    candidate_votes = {}
    candilist_List =[]
    votes_per_candidate =[]
    total_votes =0
    winner = ""
    winner_vote = 0
    for row in csvreader:
        candidate = row[2]
        if candidate not in candilist_List: 
                candilist_List.append(candidate)
                candidate_votes[candidate] = 0
        candidate_votes[candidate] = candidate_votes[candidate]+1
        total_votes = total_votes +1
    # print(candidate_votes)
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        percnetage_votes = votes/ total_votes*100 
        print(f"{candidate} {votes} {round(percnetage_votes,2)}")
        # print(f"Winer: {votes},{candidate}")
        if votes > winner_vote:
            winner_vote = votes
            winner = candidate
    
# print the oput put in txt file         
output_file = os.path.join('..','output',"PyPoll_result.txt")
with open(output_file,"w") as output_file:
     output_file.write("Election Result pyPol" + "\n")
     output_file.write("----------------------------\n")
    
     output_file.write(f'Candidate: {candidate}\n')
     output_file.write(f'Votes  : {votes}\n')
     output_file.write(f'percentage_votes:{percnetage_votes}\n')
     output_file.write(f'Winer Vote: {winner_vote}\n')
     output_file.write(f'Winer: {winner}')
# # # Show the output in terminal
print("Election Result pyPol")
print("----------------------------")
print(f' Candidate: {candidate}')
print(f'Votes : {votes}')
print(f'Percentage Votes:{percnetage_votes}')
print(f"Winer: {winner},{winner_vote}")



