import deso 
import json 




desoPosts = deso.Posts()
postsByUser = desoPosts.getPostsForPublicKey(username="bitclout_artist")
with open("posts.json", "w") as file:
    json.dump(postsByUser.json(), file)