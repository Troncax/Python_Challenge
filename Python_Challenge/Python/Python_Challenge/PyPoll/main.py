import pandas as pd

file_path = r"C:\Users\victo\OneDrive\文档\Python_Challenge\Python\Python_Challenge\PyPoll\Resources\election_data.csv" # This is where I saved my csv

# Load the dataset
data = pd.read_csv(file_path)

# Votes (Total, canditates, counts, and percentages)
total_votes = data.shape[0]
candidates = data['Candidate'].unique()
vote_counts = data['Candidate'].value_counts()
vote_percentages = (vote_counts / total_votes) * 100
winner = vote_counts.idxmax()

# Prepare the analysis output
output = []
output.append("Election Results")
output.append("-------------------------")
output.append(f"Total Votes: {total_votes}")
output.append("-------------------------")
for candidate in vote_counts.index:
    output.append(f"{candidate}: {vote_percentages[candidate]:.3f}% ({vote_counts[candidate]})")
output.append("-------------------------")
output.append(f"Winner: {winner}")
output.append("-------------------------")

# Print the analysis to the terminal
output_text = '\n'.join(output)
print(output_text)

# Export the results to a text file
output_file_path = r"C:\Users\victo\OneDrive\文档\Python_Challenge\Python\Python_Challenge\PyPoll\Analysis\election_results.txt" # This is where my text file is going to be 
with open(output_file_path, 'w') as file:
    file.write(output_text)

print(f"\nAnalysis exported to: {output_file_path}")
