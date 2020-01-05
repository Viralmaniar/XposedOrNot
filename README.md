# XposedOrNot
XposedOrNot (XoN) tool is to search an aggregated repository of xposed passwords comprising of ~850 million real time passwords. Usage of such compromised passwords is detrimental to individual account security.

# Screenshot
![image](https://user-images.githubusercontent.com/3501170/71776993-1d358980-2f92-11ea-933a-9c8f074ba196.png)

# What is Xposed Passwords?
The main aim of this project is to give a free platform for the general public to check if their password is exposed and compromised.

This massive password collection is an accumulation of real passwords exposed in various data breaches around the world. Passwords are curated from exposed breaches like Collection #1, Yahoo, etc. Adding to that, passwords are also commonly exposed in "pastes" in pastebin.com. We have taken more than 40,000 such exposures and that is again added to this huge list.

The collated passwords are hashed with a highly secure hashing algorithm SHA-3 ( Keccak-512 ), and stored in a one way hash for verification. No passwords are stored in plain text and the process of checking anonymously is explained in detail in our blog post, 850 million passwords for free explaining the technical and operational controls enforced for enhancing the security posture. Feel free to go through the same.

# How to install?
'''
git clone https://github.com/Viralmaniar/Passhunt.git
cd Passhunt
pip3 install -r requirements.txt
python3 Passhunt.py
'''
# Credit
XposedOrNot is maintained by DevaOnBreaches. Big thanks for  creating an API for your service. You can connect with him at https://www.devaonbreaches.com/





