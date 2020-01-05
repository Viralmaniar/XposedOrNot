# XposedOrNot
XposedOrNot (XoN) tool is to search an aggregated repository of xposed passwords comprising of ~850 million real time passwords. Usage of such compromised passwords is detrimental to individual account security.

# Screenshot
![image](https://user-images.githubusercontent.com/3501170/71776993-1d358980-2f92-11ea-933a-9c8f074ba196.png)

# What is Xposed Passwords?
The main aim of this project is to give a free platform for the general public to check if their password is exposed and compromised.

This massive password collection is an accumulation of real passwords exposed in various data breaches around the world. Passwords are curated from exposed breaches like Collection #1, Yahoo, etc. Adding to that, passwords are also commonly exposed in "pastes" in pastebin.com. We have taken more than 40,000 such exposures and that is again added to this huge list.

The collated passwords are hashed with a highly secure hashing algorithm SHA-3 ( Keccak-512 ), and stored in a one way hash for verification. No passwords are stored in plain text and the process of checking anonymously is explained in detail in our blog post, 850 million passwords for free explaining the technical and operational controls enforced for enhancing the security posture. Feel free to go through the same.

# How to install?
<pre>
git clone https://github.com/Viralmaniar/XposedOrNot.git
cd XposedOrNot
pip install -r requirements.txt
python XposedorNot.py
</pre>

# How to interpret an output?

The output will consist of JSON output for easy reference. Primary reasons for giving an output in JSON instead of a yes/no is to ensure that this can be further used by people to develop and improve on the huge list of real time exposed passwords aggregated here.

Alright, the first element "anon" is added to all password hashes stored in XoN for enabling privacy conscious users to search as well. Second element "char" is a list of characteristics of the password, which can be further used for understanding the strength of the password to know if this will meet the requirements of applications in need. Many websites have policies on the use of selecting passwords based on number of characters, mixture of alphabets, numbers and special characters.

The following table explains a bit more about the characteristics in simple terms :

|Alphabet     | 	Description           |
|------------ | 	--------------------  |
|Digits       | 	Count of numbers      |
|Alphabets    |  Count of alphabets    |
|Special chars| 	Count of special chars|
|Length       | 	Length of the password|

The last one "count" denotes the number of times, this password was observed in the collected xposed data breaches. For a comprehensive list of all xposed websites, please visit Xposed websites-XoN.

Also, one another point to note is the use of Keccak-512 hashing for searching and storing data in XoN. Traditional hashing algorithms like MD5 and SHA1 are currently deprecated and also considering the enormous number of records exposed, I have gone ahead with Keccak-512 hashes.

Yes, Keccak-512 is 128 characters long and it consumes more storage.

Two sample Keccak-512 hashes given for easy reference:
<B>
test - 1e2e9fc2002b002d75198b7503210c05a1baac4560916a3c6d93bcce3a50d7f00fd395bf1647b9abb8d1afcc9c76c289b0c9383ba386a956da4b38934417789e
pass - adf34f3e63a8e0bd2938f3e09ddc161125a031c3c86d06ec59574a5c723e7fdbe04c2c15d9171e05e90a9c822936185f12b9d7384b2bedb02e75c4c5fe89e4d4
</B>
Sample output on not finding the matching password hash:
<pre>
 {
  "Error": "Not found"
}
</pre>

# Collected Passwords timeline - thanks to DevaOnBreaches
![image](https://user-images.githubusercontent.com/3501170/71777306-d8abed00-2f95-11ea-9590-6b3bd1f84406.png)

![image](https://user-images.githubusercontent.com/3501170/71777339-6a1b5f00-2f96-11ea-8bab-1f5b5a22c1b0.png)

![image](https://user-images.githubusercontent.com/3501170/71777347-861f0080-2f96-11ea-8c10-9ed9a3f46179.png)


# Questions?

Twitter: [@ManiarViral](https://twitter.com/maniarviral) <BR>
LinkedIn: https://au.linkedin.com/in/viralmaniar

# Contribution & License

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/80x15.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.</br>
Want to contribute? Please fork it and hit up with a pull request.

Any suggestions or ideas for this tool are welcome - just tweet me on [@ManiarViral](https://twitter.com/maniarviral)

# Credit
XposedOrNot is maintained by DevaOnBreaches. Big thanks for  creating an API for your service. You can connect with him at https://www.devaonbreaches.com/





