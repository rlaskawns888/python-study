from step1.day6.apiTemplate import get_user, create_post

user = get_user(1)
print(user["name"])

post = create_post("hi", "test", 1)
print(post["id"])