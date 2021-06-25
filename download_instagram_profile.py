
import instaloader

insta = instaloader.Instaloader()

allusers = ['thisisbillgates', 'zuck', 'linustorvalds', 'stevejobsok']

for user in allusers:
    insta.download_profile(user, profile_pic_only=True)


