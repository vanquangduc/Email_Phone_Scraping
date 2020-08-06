# Need to copy document first
import re
import pyperclip

# Create a regex for the phone numbers
phoneRegex = re.compile(r''' 
# 415-555-10000, 555-10000, (415) 555 10000, 555-0000 ext12345
(
((\d\d\d)|(\(\d\d\d\)))?   #area code
(\s|-)                    #firt separator
\d\d\d                    #firts digits
-                         #separator
\d\d\d\d                  #last 4 digits
(((ext(\.)?\s)|x) 
(\d{2,5}))?               #ext
)            
''', re.VERBOSE)

#Create a regex for email address
emailRegex = re.compile(r'''
[a-zA-z0-9_.+]+#name part
@ #@ symbol
[a-zA-z0-9_.+]+#domain
''',re.VERBOSE)

#Get the text off the clipboard
text = pyperclip.paste()

#Extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumber = []
for phoneNumber in extractedPhone:
    allPhoneNumber.append(phoneNumber[0])

#Copy the extracted email/phone to the clipboard
phoneResults = '\n'.join(allPhoneNumber) 
emailResults = '\n'.join(extractedEmail)

with open('Email.txt','w') as emailf:
    emailf.write(emailResults)

with open('Phone.txt','w') as phonef:
    phonef.write(phoneResults)
