## How to install
1) Clone the repository
2) Create virtual enviroment
    > python3 -m venv venv
3) Activate virtual enviroment
    >  source venv/bin/activate
4) Install all requirements from file `reuqirements.txt`
    > pip install -r reuqirements.txt
5) Run program
    > python gmail_service.py

The repository consists of two programs

- `gmail_oauth_service.py`
- `gmail_service.py`


## gmail_service.py

Is a program that allows you to send an email using a token and save it as a draft

The program has two functions
 - `gmail_create_draft`
 - `check_email`

`gmail_create_draft`
the function creates an email in draft form
`check_email`
checks mail validation

I decided to create a class called `GmailAPIService` to
1) Separate and isolate this service
2) In the future, you can extend the functionality of this class by adding new features
3) It is very easy and convenient to use this service in different parts of other programs
4) Since this is a separate class in a separate file, it is easy to implement it in existing code

In the class constructor, I decided to add an optional parameter so that you could choose a token file for different users. In the future, when connecting the database, you can replace the file with the token itself.
I also added the object of the service itself to the constructor, because it can be used many times

## gmail_oauth_service.py

This program is needed to get gmail access and refresh tokens. It uses OAuth 2.0 protocol

I created a service on google cloud and added firdosdev@gmail.com as a test email, so only my email can be used. But I will leave the token.json file so you can use my service.
With the following scopes
 - https://mail.google.com/
 - https://www.googleapis.com/auth/gmail.modify
 - https://www.googleapis.com/auth/gmail.compose

