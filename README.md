# Unit 4 Project: Code Sharing Social Media

<img src="Assets/DALLE.jpg" style="zoom:50%;" />[^1]

[^1]: "a japanese person suffering in coding in front of a laptop in the form of an oil painting" by DALL E 2, Open AI, Accessed 9th April 2023

## Criteria A: Planning

## Problem definition(Client identification)

I am a student at a high school in Karuizawa. Me and a half of my grade take Computer Science as a subject in the International Baccalaureate Diploma Programme. We often times have to share code in class and especially outside of class. We used to rely on platforms like Google Chat and Messenger to copy and paste short pieces of code at a time. It was not a very organised and effective solution as it made crediting code hard. Not to mention, sharing code over chat platforms make it very hard to add description to the code without making the chat very long and inlegible for looking back. Everyone posts their code in the community as well which makes it hard for other users to differentiate between good, working code and code that needs fixing. As such, there was a need for an consolidated solution for everyone in my class to share code and the class decided on a social media styled website that could represent code with correct syntax formatting and indentations shown.(See evidence of consultation in Appendix 1)

## Proposed Solution

Considering the client's requirements, an adequate solution would be social-media styled website that can store data inside a database. The most common tools for web development are Javascript, HTML, CSS[^8]but Javascript is a client-side language, which means that code is executed on the user's browser. This can make it vulnerable to attacks like cross-site scripting (XSS). To remedy this, Python would be an adequate programming language for that as it is not a client-side language, open sourced, mature and excells at memory management[^2]. To host the webiste, Flask would be an adequate choice as it is highly scalable, making it fit to the client's need for a school use website without overcomplicating resources[^3].For the database, SQLite would be a good fit as the data we are fitting is not very large in number and SQLite, with its embedded,serverless nature[^4], can reduce the use of computing resources while running the website, not to mention higher speeds. To interface with the SQLAlchemy is the choice to go as it has improved performance and is protected against security attacks[^5]. As for the user interface for the website, Bootstrap 5 is recommended for its dynamic scaling abilites to scale automatically for different devices[^6].To keep the website and their users secure, JSON web tokens are used because they are resistant to security attacks[^7] and can prevent malicious users from modifying the key to access unauthorized content.

[^2]: Python Geeks. “Advantages of Python: Disadvantages of Python.” Python Geeks, 26 June 2021, https://pythongeeks.org/advantages-disadvantages-of-python
[^3]: “6 Reasons Why Flask Is Better Framework for Web Application Development.” *Able*, https://able.bio/hardikshah/6-reasons-why-flask-is-better-framework-for-web-application-development--cd398f73.
[^4]: S, Ravikiran A. “What Is Sqlite? and When to Use It?” *Simplilearn.com*, Simplilearn, 16 Feb.2023, https://www.simplilearn.com/tutorials/sql-tutorial/what-is-sqlite.
[^5]:  Uwase, Ange. “Here Is the Reason Why SQLAlchemy Is so Popular.” Medium, 8 Feb.2021,https://towardsdatascience.com/here-is-the-reason-why-sqlalchemy-is-so-popular-43b489d3fb00#:~:text=SQLAlchemy%20is%20the%20ORM%20of.
[^6]: Pratikasha Shinde. “6 Reasons to Use Bootstrap 5 for Better UI Development – Blog.” *Jade Global*, 6 Oct. 2021, https://www.jadeglobal.com/blog/6-reasons-use-bootstrap-5-better-ui-development.
[^7]: “What Is JWT?: Akana by Perforce.” *Akana*, https://www.akana.com/blog/what-is-jwt#:~:text=Why%20Use%20JWT%3F,was%20signed%20by%20the%20issuer.
[^8]: “11 Most in-Demand Programming Languages in 2023.” *Berkeley Boot Camps*, 5 Jan. 2023, https://bootcamp.berkeley.edu/blog/most-in-demand-programming-languages/. 

### Design statement

I will design a social media platfom on a website built with Flask, Bootstap, HTML and CSS which stores data in an SQLite database for me and my classmates. This website will allow me and my classmates to post code and descriptions of them accordingly, with a like/dislike system to moderate content. Everything is secured under a hashed login system to keep user data secure. It will take approximately 1 month to complete and will be evaluated according to criterias below:

## Success Criteria

1. The website must keep users seperately with an encrypted login system
1. The website must be able to represent code with the correct syntax highlighting for the appropriate language and the correct indentations
1. The website must allow posting of code and description
1. Users should be able to like/dislike certain posts to increase authenticity of posted content
1. The website will be able to sort the posts by user/amount of likes/time posted
1. The website should allow for the changing of passwords per user

# Criteria B: Design

## System Diagram

​	![](Assets/CodeShare_SysD.jpeg)

**Fig.1** *System diagram of the Website*

## Data Storage

<img src="Assets/CodeShare_ER.jpeg" style="zoom: 50%;" />

**Fig.2** *ER diagram of the Website

### Example of Data Entries

![](Assets/CodeShareDB_Post.jpg)

**Fig.3** *Example of data entry in the Post table*

<img src="Assets/CodeShareDB_User.jpg" alt="CodeShareDB_User" style="zoom: 67%;" />

**Fig.4** *Example of data entry in the User table*

## UML Diagram

![](Assets/CodeShare_UML.jpeg)

**Fig.5** *UML Diagram of the website

## Wireframe

<img src="Assets/CodeShare_Wireframe.jpeg" style="zoom: 67%;" />

**Fig.6** *Wireframe of the website*

## Record of Tasks

| Task No | Planned Action                                   | Planned Outcome                                              | Time estimate | Target completion date | Criterion |
| ------- | ------------------------------------------------ | ------------------------------------------------------------ | ------------- | ---------------------- | --------- |
| 1       | Planning: First Meeting with client              | Start collecting the context of the problem and research on current solutions | 3min          | March 28th             | A         |
| 2       | Planning: Defining problem and proposed solution | Start on refining client's requirements and tools needed     | 2 hr          | March 29th             | A         |
| 3       | Initializing codebase                            | To have the base environment of program ready for coding     | 1 hr          | March 29th             | B         |
| 4       | Planning : Second Meeting with client            | Decided success criteria                                     | 5 min         | March 30th             | A         |
| 5       |                                                  |                                                              |               |                        |           |
| 6       |                                                  |                                                              |               |                        |           |
| 7       |                                                  |                                                              |               |                        |           |
| 8       |                                                  |                                                              |               |                        |           |
| 9       |                                                  |                                                              |               |                        |           |
| 10      |                                                  |                                                              |               |                        |           |
| 11      |                                                  |                                                              |               |                        |           |
| 12      |                                                  |                                                              |               |                        |           |
| 13      |                                                  |                                                              |               |                        |           |
| 14      |                                                  |                                                              |               |                        |           |
| 15      |                                                  |                                                              |               |                        |           |
| 16      |                                                  |                                                              |               |                        |           |
| 17      |                                                  |                                                              |               |                        |           |
| 18      |                                                  |                                                              |               |                        |           |
| 19      |                                                  |                                                              |               |                        |           |
| 20      |                                                  |                                                              |               |                        |           |
| 21      |                                                  |                                                              |               |                        |           |
| 22      |                                                  |                                                              |               |                        |           |
| 23      |                                                  |                                                              |               |                        |           |
| 24      |                                                  |                                                              |               |                        |           |
| 25      |                                                  |                                                              |               |                        |           |
| 26      |                                                  |                                                              |               |                        |           |
| 27      |                                                  |                                                              |               |                        |           |
| 28      |                                                  |                                                              |               |                        |           |
| 29      |                                                  |                                                              |               |                        |           |
| 30      |                                                  |                                                              |               |                        |           |

## Flow Diagrams

### Token System

<img src="Assets/CodeShareFlow_Token.jpg" style="zoom: 25%;" />

**Fig.7** *Flow Diagram of the token system* This diagram shows how users can authenticate in my website with JWT with expiry time. This ensures that users' data is kept safe and no unauthorized access would occur.

### Sorting

<img src="Assets/CodeShareFlow_Sort.jpg" style="zoom:25%;" />

**Fig.8** *Flow Diagram of sorting system* This flow diagram demonstrates the ability to sort posts by different metrics.

### Like System

<img src="Assets/CodeShareFlow_Like2.jpg" style="zoom:25%;" /> 

**Fig.9** *Flow diagram for adding and removing likes* This flow diagram demonstrates how the system for adding like/dislike works.

## Test Plan

| Type | Description | Process | Anticipated Outcome |
| ---- | ----------- | ------- | ------------------- |
|      |             |         |                     |

# Criteria C: Development

## Existing Tools

| Software/Development Tools | Coding Structure Tools      | Libraries    |
| -------------------------- | --------------------------- | ------------ |
| PyCharm                    | Object Oriented Programming | Datetime     |
| VS Code                    | SQL requests                | Flask        |
| Python                     | Databases                   | Jinja2       |
| Javascript                 | Encryptions                 | Passlib.hash |
| HTML                       | For Loops                   | dotenv       |
| CSS                        | If-then-else statements     | Jose         |
| SQLite                     | Object Relation Mapping     | Sqlalchemy   |
| SQLAlchemy                 |                             |              |
| JSON Web Tokens            |                             |              |
| Flask                      |                             |              |
| Bootstrap 5                |                             |              |
| ChatGPT                    |                             |              |
| Github Copilot             |                             |              |

## List of Techniques

1. Object Oriented Programming(OOP)
2. Object Relation Mapping(ORM): SQLAlchemy
3. Flask Library
4. Bootstrap Library
5. Javascript/Python inside HTML
6. CSS Styling
7. For loops
8. if statements
9. Password Hashing
10. Token-based authentication
11. Interacting with Databases
12. Arrays and Lists
13. Text Formatting

## Development

### Cards

When researching about social media website designs, I noticed that most websites prefer a card based designed to better guide the user and make the overall interface clearer for reading. Thus, I chose to employ a card-based design for my login screen. Here is the code snippet:

```html
    <div class="card" style="width: 18rem;">
      {# Code of the sign in fields inside the card is omitted for demonstration puposes#}
</div>
```

As you can see above, the whole sign in form is house inside a `<div>` element which inherits from class `card` from the bootstrap library. This automatically houses the elements inside the `<div>` align to the center and automatically creates a border for the sign in form so the user's attention is immediately grabbed towards it

<img src="Assets/CodeShare_LoginShot.jpg" style="zoom: 33%;" />

**Fig.10**  *Screenshot of the login page, as mentioned above this employs a card design in order to reduce clutter on the screen and lead the user to the most important element which is the login fields.*

### Modals

Throughout this program, the input of certain informations is often needed in instances stated in the success criterias like registering new users, changing passwords, and editing posts. If we redirect the user to a new page everytime one of those actions are being executed, the website will become very cluttered and unintuitive. As such, I have chosen to use a modal which is a web page element that displays in front of and deactivates all other page content. To return to the main content, the user must engage with the modal by completing an action or by closing it. Modals are often used to direct users’ attention to an important action or piece of information on a website or application. For example, when the user clicks on the change password button, it triggers a modal with the following code:

```html
<button type="button" class="btn btn-primary w-100" data-bs-toggle="modal" data-bs-target="#changePasswordModal">
```

When the button is defined, it is set to toggle the modal defined below:

```html
<div class="modal fade" id="changePasswordModal" tabindex="-1" aria-labelledby="changePasswordModalLabel" aria-hidden="true">
                            <div class="modal-dialog">
                                {# Code omitted for demonstrative purposes#}
                            </div>
                        </div>
```

The modal is created by inheriting from the `modal` class from the Bootstrap 5 library. Inside the modal, we can house ordinary html elements like forms and text fields.

<img src="Assets/Modal.jpg" style="zoom:33%;" />

**Fig.11**  *Screenshot of the modal pop up.*

As you can see, the content around the modal is darkened and directs the user's attention there. 

### JSON Web Tokens

One of the success criterias was to have a hashed login system. One issue I had after the user logged in which was that I couldn't recognize the user after the inital login process. I wanted to use cookies to store the user ids. I realized soon afterwards that the cookies can be easily modified in flight and makes the hashed passwords useless. Soon I came across session tokens. Session tokens are encrypted token that contain information about the user. They expire after a time designated by the developer and can be used to protect the user as it is hashed using a special secret key that only the developer has control over. Currently, once the user succesfully logs in with the right username and password. The main key function on the flask endpoint executes a `create_token` function from the `token_management.py`. The token is created as follows:

```py
#This functions takes in the username and the how long the token should last in minutes
def create_token(username, token_duration): 
  	#This adjusts the starting time of counting the token expiry to keep constenticy across platforms
    unix_timestamp = (datetime.now() - datetime(1970, 1, 1)).total_seconds()
    #This line sets the expiry time of the token
    ttl = token_duration * 60 + unix_timestamp
    #token format = encoded(username, datetime) token_duration in minutes
    token  = jwt.encode({'username': username, 'datetime': ttl}, token_encryption_key, algorithm='HS256')
    #Token is returned to the main flask function
    return token
```

After the main function receives the token from the `create_token` function, its gives the token back to the client by putting it into the session variable of the browser as follows:

```py
session['token'] = create_token(username, 120)
```

Now, the user holds the token in their browser. When they want to execute an action, the backend tries to get the token from the browser as follows:

```py
@app.route("/new_post", methods=['GET', 'POST'])
def new_post():
    try:
        token = session['token']
    except KeyError:
        return redirect(url_for('login'))
     #Continues function
```

On the code above, I used the `try` statement to handle `KeyError` in the instance that the JWT is not present in the user's browser and redirects them to the login page. If the token is present, the validity of it is checked using a `check_token` function. It decodes the token and checks if the expiry time has exceeded current time as follows:

```py
def check_token(token): #check if token is valid and not expired
    try:
      	#Decodes token using predefined key and algorithm
        decoded_token = jwt.decode(token, token_encryption_key, algorithms=['HS256'])
        current_time = datetime.utcnow().timestamp()
        #Compares expiry time and current time
        if decoded_token['datetime'] < current_time:
            return False
        else:
            return True
    except Exception:
        return False
```

The main function then recieves a boolean value of whether the user is valid in an active session and lets them proceed with the desired action. This system closes the loophole of modifying cookies and completes the hashed authentication system criteria.

### Header and Footer

### Base Template(Pattern Recognition/Generalization/Abstraction)

### Posts Representation

### Code Representation - Syntax Highlighting

### Like/Dislike System

### Sorting System(Algorithms)

### Changing of Passwords(Decomposition)

### Endpoints



### Database Models

### Initializing Database/Inserting Dummy Data







# Criteria D: Functionality

## Demonstration Video

[Click here for the Video]()

# Criteria E: Evaluation

## Evaluation by Client



## Evaluation by Peer

## Recommendations for Improvements



# Appendix

![](Assets/Appendix1.jpeg)

**Fig.?** *Rough notes from first meeting with client, includes basic ideas behind problem with current solution*

