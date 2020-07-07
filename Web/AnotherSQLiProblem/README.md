Difficulty: Easy

### Question

Rob claims that his website is unhackable, and constantly brags about it to Misha. Misha, getting annoyed with this, decides to teach Rob a lesson. He begins looking for security vulnerabilities in Rob's website. Pretty soon, he discovers that the website does not sanitize SQL inputs, which means it is prone to SQL injection attacks.

The website contains a login form. On entering the username + password details, all the user data is visible. The server-side code for getting the user details based on information entered in the login form is the following:


```
user_details = "SELECT * FROM users WHERE username='" + uname + "' AND password='" + passwd + "'"
```

where *uname* is the username entered in the login form, and *passwd* is the corresponding password.

The above is prone to SQL injection attacks, as we can set the *passwd* field to something like:

```password' OR 1=1```

As a result, the database server runs the following SQL query:

```SELECT * FROM users WHERE username='username' AND password='password' OR 1=1'```

Leading to the second part of the AND clause being always evaluated as True, even if the password is wrong, since 1=1 always. This enables us to see the details of any user using this security flaw, without knowing their password.

Using the above login form, what will be the input to the password field form so that Misha can delete Rob's user row entirely? (Hint: Use the SQL [DELETE](https://www.w3schools.com/sql/sql_delete.asp) statement).

### Answer
       
```'; DELETE FROM users WHERE username='Bobby';```
