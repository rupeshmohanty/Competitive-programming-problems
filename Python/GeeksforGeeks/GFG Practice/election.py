n = int(input())
votes = list(map(str,input().split()))
votes.sort()
max_votes = 0
candidate = ""

for i in votes:
    if votes.count(i) > max_votes:
        max_votes = votes.count(i)
        candidate = i

print(candidate,max_votes)