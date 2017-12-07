"""Roy and Trending Topics"""
""" Roy is trying to develop a widget that shows Trending Topics (similar to Facebook) on the home page of HackerEarth Academy. 
He has gathered a list of N Topics (their IDs) and their popularity score (say z-score) from the database. Now z-score change everyday according to the following rules:

When a topic is mentioned in a 'Post', its z-score is increased by 50.
A 'Like' on such a Post, increases the z-score by 5.
A 'Comment' increases z-score by 10.
A 'Share' causes an increment of 20.
Now the Trending Topics are decided according to the change in z-score. One with the highest increment comes on top and list follows.
Roy seeks your help to write an algorithm to find the top 5 Trending Topics.
If change in z-score for any two topics is same, then rank them according to their ID (one with higher ID gets priority). It is guaranteed that IDs will be unique.

Input format:
First line contains integer N
N lines follow
Each contains 6 space separated numbers representing Topic ID, current z-score - Z, Posts - P, Likes - L, Comments - C, Shares - S

Output format:
Print top 5 Topics each in a new line.
Each line should contain two space separated integers, Topic ID and new z-score of the topic"""

# First line Input that contains integer N
no_sample_input = int(input())
sample_test = {} 
# 6 space separated numbers representing Topic ID, current z-score - Z, Posts - P, Likes - L, Comments - C, Shares - S
for i in range(no_sample_input):
	user_input =  input()
	record = user_input.split()
	sample_test[record[0]] = record[1:]
	user_input = ''

# Taking input from a file.
# file_object = open("sample_input.txt", "r")
# for line in file_object:
# 	record = line.split()
# 	sample_test[record[0]] = record[1:]

# Calculating new score and change in score
for i, j in sample_test.items():
	new_score = 50 * int(j[1]) + 5 * int(j[2]) + 10 * int(j[3]) + 20 * int(j[4])
	sample_test[i].append(new_score)
	sample_test[i].append(new_score - int(j[0]))

# Tag ids with their new change in score
result_set = {}
for i, j in sample_test.items():
	result_set[int(i)] = j[-1]

# Now sort them according to the change in z-score and ID (one with the higher ID gets priority).
result_set = sorted(result_set.items(), key=lambda x: (x[-1], x[0]), reverse=True)
# Print top 5 trending topics 
for i in result_set[0:5]:
	print(i[0], sample_test[str(i[0])][-2])