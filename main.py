import json

# Load data from JSON files
with open('followers.json', 'r') as f:
    follower_data = json.load(f)

with open('following.json', 'r') as f:
    followee_data = json.load(f)

# Extract follower usernames
follower_usernames = [follower["string_list_data"][0]["value"] for follower in follower_data["relationships_followers"]]

# Identify users followed but not followed back
users_not_following_back = [followee["string_list_data"][0]["value"] for followee in followee_data["relationships_following"] if followee["string_list_data"][0]["value"] not in follower_usernames]

# Print users not following back
for user in users_not_following_back:
    print(user)
