from __future__ import division

users = [
    { "id": 0, "name": "Hero" },
    { "id": 1, "name": "Dunn" },
    { "id": 2, "name": "Sue" },
    { "id": 3, "name": "Chi" },
    { "id": 4, "name": "Thor" },
    { "id": 5, "name": "Clive" },
    { "id": 6, "name": "Hicks" },
    { "id": 7, "name": "Devin" },
    { "id": 8, "name": "Kate" },
    { "id": 9, "name": "Klein" }
]

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
(4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

for user in users:
    user["friends"] = []

for i, j in friendships:
    users[i]["friends"].append(users[j])  #add j as a friend of i
    users[j]["friends"].append(users[i])  #add i as a friend of j

def number_of_friends(user):
    return len(user["friends"])

total_connections = sum(number_of_friends(user)
                            for user in users)

num_users = len(users)
avg_connections = total_connections / num_users

num_friends_by_id = [(user["id"], number_of_friends(user))
                    for user in users]

print(sorted(num_friends_by_id, key=lambda pair: pair[1], reverse=True))

#Data Sceintists You may know, suggest friends of friends

def friends_of_friends_ids_bad(user):
    #'foaf' is shortcut for 'friend of a friend'
    return [foaf["id"]
            for friend in user["friends"]
            for foaf in friend["friends"]]

friends_of_friends_ids_bad(users[0])

# no idea what is going on.

print ([friend["id"] for friend in users[0]["friends"]])  # [1, 2]
print ([friend["id"] for friend in users[1]["friends"]])  # [0, 2, 3]
print ([friend["id"] for friend in users[2]["friends"]])  # [0, 1, 3]