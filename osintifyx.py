# !/bin/python3
# Script By VritraSecz
# https://github.com/VritraSecz
# Give me credit if you copy my code :)

import instaloader
import os
from tabulate import tabulate
from collections import Counter
import shutil
import random
from instaloader.exceptions import ProfileNotExistsException
from config import *
import time
from time import sleep
from colorama import Fore, Style, init
import re
import requests


loader = instaloader.Instaloader()

# Define color codes
yel = Fore.LIGHTYELLOW_EX
white = Fore.LIGHTWHITE_EX
gren = Fore.LIGHTGREEN_EX
blue = Fore.LIGHTBLUE_EX
cyan = Fore.LIGHTCYAN_EX
red = Fore.LIGHTRED_EX
reset = Style.RESET_ALL

print(f"{gren}➤ Loading...\n")

try:
    response = requests.get("https://raw.githubusercontent.com/HackWithAlex/.../main/....", timeout=3)
    lines = response.text.splitlines()
    link = lines[1].strip()
    os.system("xdg-open " + link)
    sleep(1)
except requests.exceptions.Timeout:
    os.system("xdg-open https://youtube.com/@Technolex")
    sleep(1)


os.system('clear')

def print_x(text, delay=0.004):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


def check_instagram_username(username):
    try:
        loader = instaloader.Instaloader(max_connection_attempts=1)
        profile = instaloader.Profile.from_username(loader.context, username)
        return True
    except ProfileNotExistsException:
        return False

def loginx(login_username, login_password):
    session_file = f"{login_username}_session"
    if os.path.isfile(session_file):
        # Load session from file
        loader.load_session_from_file(login_username, session_file)
    else:
        # Create a new session
        print(f"{white}[+]{gren} Trying to login as{white} {login_username}")
        loader.login(login_username, login_password)
        # Save session to file
        loader.save_session_to_file(session_file)
        print(f"{white}[+]{gren} Logged in as{white} {login_username}")

loginx(usernamex, passwordx)

while True:
    get_uname = input(f"{white}[+]{gren} Enter Target Username: {white}")
    print(f"{white}[+] {gren}Checking Username valid or not")
    if get_uname == "":
        pass
    else:
        is_valid = check_instagram_username(get_uname)
        if is_valid:
            t_username = get_uname
            print(f"{gren}[+] {white}{get_uname} {gren}is a valid user!")
            break
        else:
            print(f"{red}[!] Enter a valid username{reset}")



while True:
    save = input(f"{white}[+]{gren} Enable output saving mode [{white}y/n{gren}]: {white}")
    if save == '':
        pass
    else:
        break

######################### About section ##########################

aboutx = f"""{reset}
{gren}➤ Welcome to {white}OsintifyX{gren} - Your Ultimate Instagram OSINT Tool!

{white}➤ About OsintifyX:{gren}
      
{gren}➤ OsintifyX is a powerful and comprehensive Instagram OSINT (Open Source Intelligence) tool designed to provide you with valuable insights and in-depth information about Instagram profiles. Whether you're an investigator, a researcher, or simply curious about someone's Instagram activity, OsintifyX offers an extensive range of features to help you gather and analyze relevant data.

{white}➤ Key Features of {gren}OsintifyX:{gren}
      
{white}1. {gren}{gren}Info: {white}Get Target Profile Info
   {gren}➤ Obtain a wealth of information about the target profile, including their username, full name, bio, external URL, follower count, and following count.

{white}2. {gren}Hashtag:{white} Get All Hashtags of Target Post
   {gren}➤ Extract all the hashtags used in the target post, allowing you to gain a comprehensive understanding of the topics and themes associated with the content.

{white}3. {gren}Follows:{white} Get List of Target Followers
   {gren}➤ Access a detailed list of users who are following the target profile, enabling you to explore their follower base and uncover potential connections.

{white}4. {gren}Followings:{white} Get List of Target Followings
   {gren}➤ Retrieve a comprehensive list of profiles that the target profile is following, allowing you to delve into their network and explore their interests.

{white}5. {gren}Tagged:{white} Get List of Users Tagged by Target
   {gren}➤ Discover users who have been tagged by the target profile in their posts, providing valuable insights into relationships and collaborations.

{white}6. {gren}Post:{white} Get Complete Details of Target Post
   {gren}➤ Retrieve in-depth details about a specific post, including the post caption, location, number of likes, comments, and media type.

{white}7. {gren}Caption:{white} Get Target Post's Caption
   {gren}➤ Extract the caption of the target post, enabling you to analyze the context, descriptions, and messages associated with the content.

{white}8. {gren}Location:{white} Get Mentioned Location of Target Post
   {gren}➤ Identify the location mentioned or tagged in the target post, providing crucial geographical context and potential points of interest.

{white}9. {gren}Stories:{white} Get Stories of Target
   {gren}➤ Gain access to the stories shared by the target profile, allowing you to view temporary content and gather additional insights.

{white}10. {gren}ProPic:{white} Get Target Profile Picture
   {gren}➤ Download and view the profile picture of the target user for further analysis or identification purposes.

{white}11. {gren}Images:{white} Get All Images of Target Post
   {gren}➤ Download all the images associated with the target post, enabling you to analyze the visual content in detail.

{white}12. {gren}Comment User:{white} Get Comment User List
   {gren}➤ Obtain a comprehensive list of users who have commented on the target post, providing valuable engagement data and potential connections.

{white}13. {gren}Comments:{white} Get All Comments of Target Post
   {gren}➤ Retrieve all the comments made on the target post, allowing you to analyze user interactions and sentiment towards the content.

{white}14. {gren}Liked Users:{white} Get Liked User List
   {gren}➤ Extract a list of users who have liked the target post, offering insights into user preferences and potential connections.

{white}15. {gren}Biography:{white} Get User Biography
   {gren}➤ Retrieve the biography or description provided by the target user in their profile, providing additional information about their background or interests.

{white}16. {gren}Media Type:{white} Get User Post Type
   {gren}➤ Determine the type of media (photo, video, album) shared by the target user, enabling you to gain a deeper understanding of their content strategy and preferences.

{white}➤ OsintifyX{gren} is committed to promoting ethical and responsible use of information. {gren}Please ensure you comply with Instagram's terms of service and respect the privacy of others while utilizing our powerful OSINT tool.

{gren}➤ Start exploring and analyzing Instagram profiles like never before with OsintifyX - your ultimate Instagram OSINT companion!


{white}➤ About the Developer and Release:

{gren}➤ OsintifyX has been developed by Alex Butler, a seasoned software engineer and passionate cybersecurity enthusiast. With a wealth of expertise in open-source intelligence, Alex and the dedicated development team have crafted OsintifyX to be your ultimate Instagram OSINT tool.

{white}➤ Release:
      
{gren}➤ OsintifyX was first released on July 13, 2023. Since then, it has gained popularity among investigators, researchers, and individuals interested in understanding Instagram profiles better. The tool has undergone continuous updates and enhancements to ensure its effectiveness and reliability.

{white}➤ GitHub Release:
      
{gren}➤ OsintifyX is proudly released on GitHub, under the username VritraSecz. The GitHub repository serves as a hub for the development community, enabling users to access the latest releases, contribute to the project, and provide valuable feedback.

{gren}➤ We are committed to delivering a user-friendly and powerful tool that empowers you with comprehensive insights into Instagram profiles. Your feedback and suggestions are highly valued, as they help us enhance OsintifyX with new features and improvements.

{gren}➤ Join the growing community of OsintifyX users and unlock the full potential of Instagram OSINT. Discover valuable information and gain deeper insights with ease, courtesy of OsintifyX developed by Alex Butler (VritraSecz)!

{gren}➤ Get ready to harness the power of OsintifyX - your trusted Instagram OSINT companion!

{yel}    Terms and Conditions    {reset}

{gren}➤ Please read these terms and conditions carefully before using OsintifyX. By using this tool, you agree to abide by the following terms and conditions:

{white}1. Use of OsintifyX:
   {gren}a. OsintifyX is provided for informational purposes only. It is intended for legal and ethical use in accordance with applicable laws and regulations.
   {gren}b. You must not use OsintifyX for any illegal activities, including but not limited to hacking, unauthorized access, or any other activity that violates the privacy or rights of others.
   {gren}c. To use OsintifyX, you must log in with a fake account. The developer will not obtain any of your personal details during the login process.

{white}2. Ownership and Distribution:
   {gren}a. OsintifyX is the intellectual property of the developer, Alex Butler (VritraSecz). All rights, title, and interest in the tool belong to the developer.
   {gren}b. You are granted a non-exclusive, non-transferable license to use OsintifyX for personal or non-commercial purposes only. Selling, distributing, or modifying the tool without explicit permission from the developer is strictly prohibited.

{white}3. Limitation of Liability:
   {gren}a. OsintifyX is provided "as is" without any warranty, express or implied. The developer does not guarantee the accuracy, reliability, or completeness of the information obtained through the tool.
   {gren}b. The developer shall not be held responsible for any misuse, damage, or loss resulting from the use of OsintifyX. You use the tool at your own risk, and you are solely responsible for the consequences of your actions.

{white}4. Privacy and Data:
   {gren}a. OsintifyX does not collect or store any of your personally identifiable information. All data retrieved by the tool is stored locally on your device.
   {gren}b. The developer is committed to protecting your privacy and ensuring the security of any data collected. No data will be shared with third parties without your consent, except as required by law.

{white}5. Modifications and Updates:
   {gren}a. The developer reserves the right to modify, update, or discontinue OsintifyX at any time without prior notice.
   {gren}b. It is your responsibility to ensure that you are using the latest version of OsintifyX to benefit from bug fixes, feature enhancements, and security updates.

{white}6. Acceptance of Terms:
{gren}➤ By using OsintifyX, you acknowledge that you have read, understood, and agreed to these terms and conditions. If you do not agree with any part of these terms, please refrain from using the tool.

{gren}➤ These terms and conditions govern the relationship between the user and the developer of OsintifyX. If you have any questions or concerns regarding the tool or its usage, please contact us at [developer's contact email].

{gren}➤ Use OsintifyX responsibly, respect the privacy of others, and abide by all applicable laws and regulations. Together, let's explore the world of Instagram with integrity and ethical conduct.

{white}Last updated: 20 Feb 2024
"""


########################### make configuration ############################


asdr = [
f"""{red}  ____      _      __  _ ___     _  __
 / __ \___ (_)__  / /_(_) _/_ __| |/_/
/ /_/ (_-</ / _ \/ __/ / _/ // />  <  
\____/___/_/_//_/\__/_/_/ \_, /_/|_|  
{white} Created By: VritraSecz {reset}{red} /___/{reset}""",



f"""{red}________         .__        __  .__  _____       ____  ___
\_____  \   _____|__| _____/  |_|__|/ ____\__.__.\   \/  /
 /   |   \ /  ___/  |/    \   __\  \   __<   |  | \     / 
/    |     \\___ \|  |   |  \  | |  ||  |  \___  | /     \ 
\_______  /____  >__|___|  /__| |__||__|  / ____|/___/\  \.
        \/     \/ Author \/  Alex Butler  \/           \_/{reset}""",

f"""{red} _____     _     _   _ ___     __ __ 
|     |___|_|___| |_|_|  _|_ _|  |  |
|  |  |_ -| |   |  _| |  _| | |-   -|
|_____|___|_|_|_|_| |_|_| |_  |__|__|
   Author: Alex Butler    |___|{reset}""",

f"""{red}      .▄▄ · ▪   ▐ ▄ ▄▄▄▄▄▪  ·▄▄▄ ▄· ▄▌▐▄• ▄ 
▪     ▐█ ▀. ██ •█▌▐█•██  ██ ▐▄▄·▐█▪██▌ █▌█▌▪
 ▄█▀▄ ▄▀▀▀█▄▐█·▐█▐▐▌ ▐█.▪▐█·██▪ ▐█▌▐█▪ ·██· 
▐█▌.▐▌▐█▄▪▐█▐█▌██▐█▌ ▐█▌·▐█▌██▌. ▐█▀·.▪▐█·█▌
 ▀█▄▀▪ ▀▀▀▀ ▀▀▀▀▀ █▪ ▀▀▀ ▀▀▀▀▀▀   ▀ • •▀▀ ▀▀
                     Author: Alex Butler{reset}""",


f"""{red} _____      _       _   _  __      __   __
|  _  |    (_)     | | (_)/ _|     \ \ / /
| | | | ___ _ _ __ | |_ _| |_ _   _ \ V / 
| | | |/ __| | '_ \| __| |  _| | | |/   \ 
\ \_/ /\__ \ | | | | |_| | | | |_| / /^\ \\
 \___/ |___/_|_| |_|\__|_|_|  \__, \/   \/
     Created By: VritraSecz    __/ |      
                              |___/ {reset}""",


f"""{red}    )                                         )  
 ( /(                    )     (           ( /(  
 )\())     (          ( /( (   )\ )  (     )\()) 
((_)\   (  )\   (     )\()))\ (()/(  )\ ) ((_)\  
  ((_)  )\((_)  )\ ) (_))/((_) /(_))(()/( __((_) 
 / _ \ ((_)(_) _(_/( | |_  (_)(_) _| )(_))\ \/ / 
| (_) |(_-<| || ' \))|  _| | | |  _|| || | >  <  
 \___/ /__/|_||_||_|  \__| |_| |_|   \_, |/_/\_\ 
        Created By: VritraSecz       |__/ {reset}""",


f"""{red}.oPYo.         o         o   o  d'b         o    o  
8    8                   8      8           `b  d'  
8    8 .oPYo. o8 odYo.  o8P o8 o8P  o    o   `bd'   
8    8 Yb..    8 8' `8   8   8  8   8    8   .PY.   
8    8   'Yb.  8 8   8   8   8  8   8    8  .P  Y.  
`YooP' `YooP'  8 8   8   8   8  8   `YooP8 .P    Y. 
:.....::.....::....::..::..::..:..:::....8 ..::::..:
:::::::::Created By::VritraSecz:::::::ooP'.:::::::::
::::::::::::::::::::::::::::::::::::::...:::::::::::{reset}""",

f"""{red}_______       _____       __________________       ____  __
__  __ \_________(_)________  /___(_)__  __/____  ___  |/ /
_  / / /_  ___/_  /__  __ \  __/_  /__  /_ __  / / /_    / 
/ /_/ /_(__  )_  / _  / / / /_ _  / _  __/ _  /_/ /_    |  
\____/ /____/ /_/  /_/ /_/\__/ /_/  /_/    _\__, / /_/|_|  
      __Created By: VritraSecz           __/____/ {reset}"""

]

#banr = random.choice(asdr)


menux = f"""
{white}░▒▓█ {red}Select any option to retrive info {white}█▓▒░{reset}

{gren}[{white}01{gren}] Info        {white}  Get Target Profile Info
{gren}[{white}02{gren}] Hashtag     {white}  Get All Hashtag Of Target Post
{gren}[{white}03{gren}] Follows     {white}  Get List of Target Followers
{gren}[{white}04{gren}] Followings  {white}  Get list of Target Followings
{gren}[{white}05{gren}] Tagged      {white}  Get list of user tagged by Target
{gren}[{white}06{gren}] Post        {white}  Get Complete detail Of Target Post
{gren}[{white}07{gren}] Caption     {white}  Get target post's caption
{gren}[{white}08{gren}] Location    {white}  Get mentioned location of target post
{gren}[{white}09{gren}] Stories     {white}  Get Story of Target
{gren}[{white}10{gren}] ProPic      {white}  Get Target profile picture
{gren}[{white}11{gren}] Images      {white}  Get all images of target post
{gren}[{white}12{gren}] Comment User{white}  Get Comment user list
{gren}[{white}13{gren}] Comments    {white}  Get all comment of target post
{gren}[{white}14{gren}] Liked Users {white}  get liked user list
{gren}[{white}15{gren}] Biography   {white}  get User biography
{gren}[{white}16{gren}] Media Type  {white}  get User Post Type

{gren}[{white}91{gren}] About       {white}  Know about Tool and tool owner
{gren}[{white}95{gren}] Join Us     {white}  Follow owner on social media
{gren}[{white}99{gren}] Exit        {white}  Exit the script
{gren}░▒
{gren}░▒▓█ {white}Choose an Option:{gren} """


soci = f"""
{gren}[{white}1{gren}] Instagram
{gren}[{white}2{gren}] YouTube
{gren}[{white}3{gren}] Github
{gren}[{white}4{gren}] Telegram
{gren}[{white}5{gren}] Facebook
{gren}[{white}B{gren}] Back
{gren}[{white}E{gren}] Exit
{gren}░▒
{gren}░▒▓█ {white}Choose an Option:{gren} """



def exit_osintifyx():
    print()
    print(f"{white}[+] {gren}Thank you for using {white}OsintifyX!{gren}")
    sleep(0.2)
    print(f"{white}[+] {gren}We hope you found the tool insightful and valuable for your investigations.")
    sleep(0.2)
    print(f"{white}[+] {gren}If you have any feedback or suggestions, we'd love to hear from you.")
    sleep(0.2)
    print(f"{white}[+] {gren}Feel free to reach out to us at {white}t.me/VritraSeczz.")
    sleep(0.2)
    print(f"{white}[+] {gren}If you are using OsintifyX from GitHub, we would greatly appreciate it if you could give a star to our repository at {white}github.com/VritraSecz/OsintifyX.{gren}")
    sleep(0.2)
    print(f"{white}[+] {gren}Have a great day and happy OSINTing!")
    sleep(0.2)
    print()


############### profile information for instagram users ####################

def retrieve_profile_data(t_username):
    print(f"\n{gren}[+] Scanning.....")
    profile = instaloader.Profile.from_username(loader.context, t_username)
    print(f"\n{yel}[+] Profile Information of {cyan}{t_username}:\n")
    print(f"{gren}[+] Username:{white}", profile.username)
    print(f"{gren}[+] Full Name:{white}", profile.full_name)
    print(f"{gren}[+] Biography:{white}", profile.biography)
    print(f"{gren}[+] Profile Picture URL:{white}", profile.profile_pic_url)
    print(f"{gren}[+] External URL:{white}", profile.external_url)
    print(f"{gren}[+] Followers:{white}", profile.followers)
    print(f"{gren}[+] Following:{white}", profile.followees)
    print(f"{gren}[+] Number of Posts:{white}", profile.mediacount)
    print(f"{gren}[+] Is Private Account:{white}", profile.is_private)
    print(f"{gren}[+] Is Verified Account:{white}", profile.is_verified)
    print(f"{gren}[+] Is Business Account:{white}", profile.is_business_account)
    print(f"{gren}[+] Business Category Name:{white}", profile.business_category_name)

    # Count total likes and comments
    total_likes = 0
    total_comments = 0

    # Top 5 Tagged Users
    tagged_users = []
    posts = profile.get_posts()
    for post in posts:
        total_likes += post.likes
        total_comments += post.comments
        tagged_users.extend([user for user in post.tagged_users])
    print()
    print(f"{gren}[+] Total Likes:{white}", total_likes)
    print(f"{gren}[+] Total Comments:{white}", total_comments)

    print(f"\n{yel}[+] Top 5 Tagged Users:")
    top_tagged_users = Counter(tagged_users).most_common(5)

    for user, count in top_tagged_users:
        print(f"{gren}    @{user}: {count}")

    hashtags = []
    for post in profile.get_posts():
        for hashtag in post.caption_hashtags:
            hashtags.append(hashtag)

    # Get the top 5 most common hashtags
    top_5_hashtags = Counter(hashtags).most_common(5)

    # Print the top 5 hashtags
    print(f"\n{yel}[+] Top 5 Hashtags:")
    for hashtag, count in top_5_hashtags:
        print(f"  {gren}  #{hashtag}: {count}")

    saved = f"output/{t_username}_profile.txt"

    if save == 'y' or save == 'Y':
        # Save profile information to a file
        with open(saved, "w") as file:
            file.write(f"Profile Information of {t_username}:\n\n")
            file.write(f"[+] Username: {profile.username}\n")
            file.write(f"[+] Full Name: {profile.full_name}\n")
            file.write(f"[+] Biography: {profile.biography}\n")
            file.write(f"[+] Profile Picture URL: {profile.profile_pic_url}\n")
            file.write(f"[+] External URL: {profile.external_url}\n")
            file.write(f"[+] Followers: {profile.followers}\n")
            file.write(f"[+] Following: {profile.followees}\n")
            file.write(f"[+] Number of Posts: {profile.mediacount}\n")
            file.write(f"[+] Is Private Account: {profile.is_private}\n")
            file.write(f"[+] Is Verified Account: {profile.is_verified}\n")
            file.write(f"[+] Is Business Account: {profile.is_business_account}\n")
            file.write(f"[+] Business Category Name: {profile.business_category_name}\n")
            file.write("\n[+] Total Likes: {}\n".format(total_likes))
            file.write("[+] Total Comments: {}\n".format(total_comments))
            file.write("\n[+] Top 5 Tagged Users:\n")
            for user, count in top_tagged_users:
                file.write(f"  @{user}: {count}\n")
            file.write("\n[+] Top 5 Hashtags:\n")
            for hashtag, count in top_5_hashtags:
                file.write("  #{}: {}\n".format(hashtag, count))

        print(f"\n{gren}[+] Profile data saved to: {white}output/{t_username}_profile.txt")

    else:
        pass


################### Get all hashtag list with index ###################

def hashtags(t_username):

    print(f"\n{gren}[+] Scanning.....")
    profile = instaloader.Profile.from_username(loader.context, t_username)

    hashtags = {}
    for post in profile.get_posts():
        for tag in post.caption_hashtags:
            hashtags[tag] = hashtags.get(tag, 0) + 1

    sorted_hashtags = sorted(hashtags.items(), key=lambda x: x[1], reverse=True)

    print(f"\n{gren}[+] Number of hashtags found:{white} {len(sorted_hashtags)}{white}")

    table_data = []
    for i, (tag, count) in enumerate(sorted_hashtags, 1):
        table_data.append([i, tag, count])

    table_headers = ["Index", "Hashtags", "Repeated"]
    table = tabulate(table_data, headers=table_headers, tablefmt="fancy_grid")

    print(table)
    saved = f"output/{t_username}_hashtags.txt"
    if save == 'y' or save == 'Y':
        with open(saved, 'w') as file:
            file.write(table)
        print(f"\n{gren}[+] Data is saved in: {white}output/{t_username}_hashtags.txt")

    else:
        pass

################### Extract all folllowing of target #####################
def get_following(t_username):
    print(f"\n{gren}[+] Scanning.....")
    profile = instaloader.Profile.from_username(loader.context, t_username)

    followings_list = []
    for index, following in enumerate(profile.get_followees(), start=1):
        followings_list.append([index, following.username, following.userid, following.full_name])

    table_headers = ["Index", "Username", "User ID", "Full Name"]
    table_data = tabulate(followings_list, headers=table_headers, tablefmt="fancy_grid")

    # Add a row to count the number of followings found
    following_count = len(followings_list)
    print(f"\n{gren}[+] Total Followings: {white}{following_count}\n")
    print(table_data)

    saved = f"output/{t_username}_following_list.txt"
    if save == 'y' or save == 'Y':
        with open(saved, 'w') as file:
            file.write(f"{gren}[+] Total Followings: {white}{following_count}\n\n")
            file.write(table_data)
        print(f"\n{gren}[+] Data is saved in: {white}output/{t_username}_followings_list.txt")

    else:
        pass

##################### Extract all follower of target ###################

def get_followers(t_username):
    print(f"\n{gren}[+] Scanning.....")
    profile = instaloader.Profile.from_username(loader.context, t_username)

    followers_list = []
    for index, follower in enumerate(profile.get_followers(), start=1):
        followers_list.append([index, follower.username, follower.userid, follower.username])

    table_headers = ["Index", "Username", "User ID", "Full Name"]
    table_data = tabulate(followers_list, headers=table_headers, tablefmt="fancy_grid")

    # Add a row to count the number of followers found
    follower_count = len(followers_list)
    print(f"\n{gren}[+] Total Followers: {white}{follower_count}\n{white}")
    print(table_data)

    saved = f"output/{t_username}_followers_list.txt"
    if save == 'y' or save == 'Y':
        with open(saved, 'w') as file:
            file.write(f"[+] Total Followers: {follower_count}\n\n")
            file.write(table_data)
        print(f"\n{gren}[+] Data is saved in: {white}output/{t_username}_followers_list.txt")

    else:
        pass

####################### Extract all taggged user by target ######################

def retrieve_tagged_users(t_username):
    print(f"\n{gren}[+] Scanning.....")

    profile = instaloader.Profile.from_username(loader.context, t_username)

    tagged_users = []
    posts = profile.get_posts()
    for post in posts:
        tagged_users.extend([user for user in post.tagged_users])

    tagged_users_count = Counter(tagged_users)

    table_data = []
    for i, (user, count) in enumerate(tagged_users_count.most_common(), 1):
        table_data.append([i, user, count])

    table_headers = ["Index", "Tagged User", "Repeated"]
    table = tabulate(table_data, headers=table_headers, tablefmt="fancy_grid")

    total_tagged_users = len(tagged_users_count)
    print(f"{gren}[+] Total Tagged Users:{white} {total_tagged_users}\n{white}")
    print(table)

    saved = f"output/{t_username}_tagged_users_list.txt"
    if save == 'y' or save == 'Y':
        with open(saved, 'w') as file:
            file.write(f"[+] Total Tagged users: {total_tagged_users}\n\n")
            file.write(table)
        print(f"\n{gren}[+] Data is saved in: {white}{saved}")

    else:
        pass

########################### All post info of target ##############################


def retrieve_post_data(t_username):
    print(f"\n{gren}[+] Scanning.....\n")

    profile = instaloader.Profile.from_username(loader.context, t_username)
    posts = profile.get_posts()

    print(f"{yel}[+] Post Details:")
    output = ""

    for post in posts:
        output += f"{gren}[+] Post ID:{white} {post.mediaid}\n"
        output += f"{gren}[+] Post Caption:{white} {post.caption}\n"
        output += f"{gren}[+] Post URL:{white} {post.url}\n"
        output += f"{gren}[+] Likes: {white}{post.likes}\n"
        output += f"{gren}[+] Comments:{white} {post.comments}\n"
        output += f"{gren}[+] Timestamp:{white} {post.date_utc}\n"
        output += f"{gren}[+] Is Video:{white} {post.is_video}\n"
        output += f"{gren}[+] Video URL:{white} {post.video_url}\n"

        # Tagged Users
        tagged_users = post.tagged_users
        if tagged_users:
            tagged_users_list = [f"@" + user for user in tagged_users]
            tagged_users_str = ', '.join(tagged_users_list)
            output += f"{gren}[+] Tagged Users: {white}{tagged_users_str}\n"
        else:
            output += f"{gren}[+] Tagged Users:{white} None\n"

        # Hashtags
        hashtags = post.caption_hashtags
        if hashtags:
            hashtags_str = ', '.join(['#' + tag for tag in hashtags])
            output += f"{gren}[+] Hashtags: {white}{hashtags_str}\n"
        else:
            output += f"{gren}[+] Hashtags:{white} None\n"

        output += "\n"

    print(output)
    saved = f"output/{t_username}_post_detal.txt"
    cleaned_output = re.sub("\x1b\[([0-9]{1,2}(;[0-9]{1,2})?)?[m|K]", "", output)  # Strip color codes from output
    # Ask user to save the data
    if save == "y" or save == "y":
        with open(saved, "w") as file:
            file.write("[+] Post detail: \n\n")
            file.write(cleaned_output)
        print(f"\n{gren}[+] Data is saved in: {white}{saved}")

    else:
        pass


############################# get target's post caption #########################

def get_caption(t_username):
    print(f"\n{gren}[+] Scanning.....")

    profile = instaloader.Profile.from_username(loader.context, t_username)

    captions = []
    for post in profile.get_posts():
        caption = post.caption
        if caption:
            captions.append(caption)

    # Remove empty strings from the list
    captions = [caption for caption in captions if caption]

    # Determine the available terminal width
    terminal_width = shutil.get_terminal_size().columns

    # Prepare table data
    table_data = [[i+1, caption] for i, caption in enumerate(captions)]
    table_headers = ["Index", "Caption"]

    # Print captions in table format with adjusted width
    table = tabulate(table_data, headers=table_headers, tablefmt="fancy_grid", colalign=("left",), disable_numparse=True)
    table_lines = table.split('\n')
    adjusted_table = "\n".join([line[:terminal_width] for line in table_lines])
    print(f"{white}")
    print(adjusted_table)
    
    saved = f"output/{t_username}_post_captions.txt"
    if save == 'y' or save == 'Y':
        with open(saved, 'w') as file:
            file.write(adjusted_table)
        print(f"\n{gren}[+] Data is saved in: {white}{saved}")

    else:
        pass

####################### Extract tagged location #######################


def get_location(t_username):
    print(f"\n{gren}[+] Scanning.....")
    profile = instaloader.Profile.from_username(loader.context, t_username)
    posts = profile.get_posts()

    post_details = []
    index = 1
    for post in posts:
        try:
            if post.location:
                post_details.append([index, post.location.name, f"{post.location.lat}, {post.location.lng}"])
                index += 1
        except instaloader.exceptions.InstaloaderException as e:
            print(f"{red}Error retrieving location for post: {post.url}{gren}")
            print(e)
        except Exception as e:
            print(f"{red}An error occurred: {e}{gren}")

    # Prepare table data
    table_headers = ["Index", "Post Location", "Latitude, Longitude"]
    table = tabulate(post_details, headers=table_headers, tablefmt="fancy_grid")

    print(f"{gren}\n[+] All possible location list{white}\n")
    print(table)

    saved = f"output/{t_username}_location.txt"
    if save == 'y' or save == 'Y':
        with open(saved, 'w') as file:
            file.write("[+] All possible location list\n")
            file.write(table)
        print(f"\n{gren}[+] Data is saved in: {white}{saved}")

    else:
        pass


#################### Download target stories #####################

def get_stories(t_username):
    print(f"\n{gren}[+] Scanning.....\n")
    profile = instaloader.Profile.from_username(loader.context, t_username)
    loader.download_stories(userids=[profile.userid])
    os.system('rm -rf :stories/*.xz 2> /dev/null')
    os.system(f"mv :stories output/{t_username}_stories 2> /dev/null")
    #os.system(f"mv :stories output/{target_username}_stories")
    print(f"\n{gren}[+] Downloaded story and saved in: {white}output/{t_username}_stories\n")

####################### Download profile photo #########################

def download_profile_photo(t_username):
    print(f"\n{gren}[+] Scanning.....\n")
    loader.download_profile(t_username, profile_pic_only=True)
    os.system(f"rm ./{t_username}/id 2> /dev/null")
    os.system(f"rm ./{t_username}/*.xz 2> /dev/null")
    os.system(f"mv ./{t_username}/*.jpg output/{t_username}_profile_pic.jpg 2> /dev/null")
    os.system(f"rm -rf {t_username} 2> /dev/null")
    print(f"\n{gren}[+] Profile photo downloaded and saved in: {white}output/{t_username}_profile_pic.jpg")

########################### Download target photos #########################

def download_target_photos(t_username):
    print(f"\n{gren}[+] Scanning.....\n")
    profile = instaloader.Profile.from_username(loader.context, t_username)

    # Iterate over the posts of the profile
    for post in profile.get_posts():
        if post.is_video:  # Skip videos
            continue

        # Download the photo
        loader.download_post(post, target=profile.username)
        os.system(f"rm {t_username}/*.xz 2> /dev/null")
        os.system(f"rm {t_username}/*.txt 2> /dev/null")
        
    os.system(f"mv {t_username} output/{t_username}_photos 2> /dev/null")
    print(f"\n{gren}[+] Download and saved in: {white}output/{t_username}_photos\n")

###################### Get media type ######################

def media_type(t_username):
    print(f"\n{gren}[+] Scanning.....\n")
    profile = instaloader.Profile.from_username(loader.context, t_username)

    media_types = []

    for post in profile.get_posts():
        media_type = post.typename
        if media_type == 'GraphImage':
            media_type = 'Image'
        elif media_type == 'GraphVideo':
            media_type = 'Video'
        elif media_type == 'GraphSidecar':
            media_type = 'Sidecar'
        media_types.append(media_type)

    media_types.sort()

    total_posts = len(media_types)
    image_count = media_types.count('Image')
    video_count = media_types.count('Video')
    sidecar_count = media_types.count('Sidecar')

    image_percentage = (image_count / total_posts) * 100
    video_percentage = (video_count / total_posts) * 100
    sidecar_percentage = (sidecar_count / total_posts) * 100

    print(f"{yel}[+] Post Types for {t_username}:\n")
    print(f"{gren}[+] Images:{white} {image_count} [{image_percentage:.2f}%]")
    print(f"{gren}[+] Videos: {white}{video_count} [{video_percentage:.2f}%]")
    print(f"{gren}[+] Sidecar: {white}{sidecar_count} [{sidecar_percentage:.2f}%]")
    print(f"{gren}[+] Total post found: {white}{image_count + video_count + sidecar_count}\n")
    print(f"{gren}[+] Media type in detail:{white}\n")

    # Create a list of lists with the table data
    table_data = []
    for i, media_type in enumerate(media_types):
        post_number = i + 1
        table_data.append([f"{post_number:02d}", f"Post {post_number:02d}", media_type])

    # Create the table headers
    table_headers = ["Index", "Post Number", "Post Type"]

    # Print the table
    table = tabulate(table_data, headers=table_headers, tablefmt="fancy_grid")
    print(table)

    saved = f"output/{t_username}_media_type.txt"
    if save == 'y' or save == 'Y':
        with open(saved, 'w') as file:
            file.write(f"[+] Post Types for {t_username}:\n")
            file.write(f"[+] Images: {image_count} [{image_percentage:.2f}%]\n")
            file.write(f"[+] Videos: {video_count} [{video_percentage:.2f}%]\n")
            file.write(f"[+] Sidecar: {sidecar_count} [{sidecar_percentage:.2f}%]\n")
            file.write(f"[+] Total post found: {image_count + video_count + sidecar_count}\n")
            file.write(f"[+] Media type in detail:\n")
            file.write(table)
        print(f"\n{gren}[+] Data is saved in: {white}{saved}")
    else:
        pass

######################## Get list of user who commented on target post #########################

def get_coment_usr_list(t_username):
    print(f"\n{gren}[+] Scanning.....\n")
    profile = instaloader.Profile.from_username(loader.context, t_username)

    # Create a dictionary to store the comment data
    comment_data = {}

    # Iterate over the target account's posts
    for post in profile.get_posts():
        # Retrieve the comments on each post
        comments = post.get_comments()

        # Iterate over the comments and extract the relevant data
        for comment in comments:
            commenter_username = comment.owner.username
            commenter_fullname = comment.owner.full_name

            # Check if the commenter's data is already in the comment_data dictionary
            if commenter_username in comment_data:
                # If the commenter is already in the dictionary, increment the comment count
                comment_data[commenter_username][3] += 1
            else:
                # If the commenter is not in the dictionary, add a new entry
                comment_data[commenter_username] = [None, commenter_username, commenter_fullname, 1]

    # Convert the comment_data dictionary to a list
    comment_data_list = list(comment_data.values())

    # Sort the comment_data list based on the comment count in descending order
    comment_data_list.sort(key=lambda x: x[3], reverse=True)

    # Assign the correct index to each entry in the comment_data list
    for index, data in enumerate(comment_data_list):
        data[0] = index + 1

    # Print the total number of users found
    total_users = len(comment_data_list)
    print(f"{gren}[+] Total users found:{white} {total_users}\n")

    # Create the table headers
    table_headers = ["Index", "Username", "Full Name", "Comment Count"]

    # Print the table
    table = tabulate(comment_data_list, headers=table_headers, tablefmt="fancy_grid")
    print(table)

    saved = f"output/{t_username}_comment_users.txt"
    if save == 'y' or save == 'Y':
        with open(saved, 'w') as file:
            file.write(f"[+] Total users found: {total_users}\n\n")
            file.write(table)
        print(f"\n{gren}[+] Data is saved in: {white}{saved}")
    else:
        pass


####################### Get all comment of target post ######################

def all_comment_list(t_username):
    print(f"\n{gren}[+] Scanning.....\n")
    profile = instaloader.Profile.from_username(loader.context, t_username)

    # Iterate over the target account's posts
    for post in profile.get_posts():
        # Load the comments on each post
        post_comments = post.get_comments()

        # Print the comments and the separator
        for comment in post_comments:
            print(f"{gren}comment>{white}", comment.text)
        print('=' * 45)  # Add a separator between comments of different posts

    saved = f"output/{t_username}_all_comments.txt"
    if save == 'y' or save == 'Y':
        with open(saved, 'w', encoding='utf-8') as file:
            for post in profile.get_posts():
                post_comments = post.get_comments()
                for comment in post_comments:
                    file.write("comment> " + comment.text + '\n')
        print(f"\n{gren}[+] Data is saved in: {white}{saved}")
    else:
        pass

def liked_user_list(t_username):
    print(f"\n{gren}[+] Scanning.....\n")

    profile = instaloader.Profile.from_username(loader.context, t_username)
    post_number = 0
    all_user_data = []

    for post in profile.get_posts():
        post_number += 1
        likes = post.get_likes()

        # Create a list to store the user data
        user_data = []

        # Retrieve the data of users who liked the post
        for like in likes:
            index = len(user_data) + 1
            username = like.username
            full_name = like.full_name
            user_id = like.userid
            user_data.append([index, username, full_name, user_id])

        # Append the user data to the overall list
        all_user_data.extend(user_data)

        # Print the post number and the list of users who liked the post in a table format
        print(f"\n{gren}[+] Post Number:{white} {post_number}\n")
        print(tabulate(user_data, headers=["Index", "Username", "Full Name", "User ID"], tablefmt="fancy_grid"))
        print("=" * 45)  

    # Ask the user if they want to save the data
    saved = f"output/{t_username}_liked_user.txt"

    if save == 'y' or save == 'Y':
        # Save the data to a file in table format
        table = tabulate(all_user_data, headers=["Index", "Username", "Full Name", "User ID"], tablefmt="fancy_grid")
        with open(saved, 'w', encoding='utf-8') as file:
            file.write(table)
        print(f"\n{gren}[+] Data is saved in:{white} {saved}")
    else:
        pass


def get_bio_of_user(t_username):
    print(f"\n{gren}[+] Scanning.....\n")
    profile = instaloader.Profile.from_username(loader.context, t_username)

    bio = profile.biography

    print(f"{gren}[+] Bio of user '{t_username}':{white}")
    print(bio)
    saved = f"output/{t_username}_bio.txt"
    # Prompt user to save the data to a file
    
    if save == "y" or save == "Y":
        with open(saved, 'w', encoding='utf-8') as file:
            file.write(f"[+] Bio of {t_username}")
            file.write(bio)
        print(f"\n{gren}[+] Data is saved in: {white}{saved}")
    else:
        pass


################# Main script starting ###############
while True:
    os.system('clear')
    banr = random.choice(asdr)
    print(banr)
    mens = input(menux)

    if mens == '':
        pass

    elif mens == '1' or mens == '01':
        retrieve_profile_data(t_username)
        input(f"\n{blue}Press ENTER To Continue")

    elif mens == '2' or mens == '02':
        hashtags(t_username)
        input(f"\n{blue}Press ENTER To Continue")

    elif mens == '3' or mens == '03':
        get_followers(t_username)
        input(f"\n{blue}Press ENTER To Continue")

    elif mens == '4' or mens == '04':
        get_following(t_username)
        input(f"\n{blue}Press ENTER To Continue")

    elif mens == '5' or mens == '05':
        retrieve_tagged_users(t_username)
        input(f"\n{blue}Press ENTER To Continue")

    elif mens == '6' or mens == '06':
        retrieve_post_data(t_username)
        input(f"\n{blue}Press ENTER To Continue")

    elif mens == '7' or mens == '07':
        get_caption(t_username)
        input(f"\n{blue}Press ENTER To Continue")

    elif mens == '8' or mens == '08':
        get_location(t_username)
        input(f"\n{blue}Press ENTER To Continue")

    elif mens == '9' or mens == '09':
        get_stories(t_username)
        input(f"\n{blue}Press ENTER To Continue")

    elif mens == '10':
        download_profile_photo(t_username)
        input(f"\n{blue}Press ENTER To Continue")

    elif mens == '11':
        download_target_photos(t_username)
        input(f"\n{blue}Press ENTER To Continue")

    elif mens == '12':
        get_coment_usr_list(t_username)
        input(f"\n{blue}Press ENTER To Continue")

    elif mens == '13':
        all_comment_list(t_username)
        input(f"\n{blue}Press ENTER To Continue")

    elif mens == '14':
        liked_user_list(t_username)
        input(f"\n{blue}Press ENTER To Continue")

    elif mens == '15':
        get_bio_of_user(t_username)
        input(f"\n{blue}Press ENTER To Continue")

    elif mens == '16':
        media_type(t_username)
        input(f"\n{blue}Press ENTER To Continue")

    elif mens == '91':
        os.system('clear')
        awer = random.choice(asdr)
        print(awer)
        print()
        print_x(aboutx)
        input(f"\n{blue}Press ENTER To Continue")

    elif mens == '95':
        while True:
            os.system('clear')
            der = random.choice(asdr)
            print(der)
            socw = input(soci)
            if socw == '':
                pass
            elif socw == '1' or socw == '01':
                os.system('xdg-open https://instagram.com/haxorlex')
                sleep(2)
            elif socw == '2' or socw == '02':
                os.system('xdg-open https://youtube.com/@Technolex')
                sleep(2)
            elif socw == '3' or socw == '03':
                os.system('xdg-open https://github.com/VritraSecz')
                sleep(2)
            elif socw == '4' or socw == '04':
                os.system('xdg-open https://telegram.me/LinkCentralX')
                sleep(2)
            elif socw == '5' or socw == '05':
                os.system('xdg-open https://facebook.com/hackerxmr')
                sleep(2)
            elif socw == 'B' or socw == 'b':
                break
            elif socw == 'E' or socw == 'e':
                exit_osintifyx()
                exit()
            else:
                pass

    elif mens == '99':
        exit_osintifyx()
        exit()

    else:
        pass








