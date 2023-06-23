import re
url = input("Put the URL: ").strip()
#username = url.replace("https://twitter.com/", "")
#re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
#print(f"Username: {username}")
if matches:= re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE):
    print(f"Username:", matches.group(1))



