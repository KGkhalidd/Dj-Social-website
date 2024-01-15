# Dj-Social-website
**Project Description:**
Developed a dynamic social web application using Python and Django, seamlessly connecting users for enhanced social networking. This comprehensive platform facilitates image sharing and incorporates key features to boost user engagement.

**Key Features:**
- **User Authentication:** Implemented a secure authentication system, encompassing login, logout, change password, and password reset functionalities.
- **User Registration and Profiles:** Enabled user registration with extended profiles featuring photos and birthdates.
- **Social Integration:** Integrated social authentication options, allowing users to sign in via Facebook, Twitter, or Google accounts.
- **Image Bookmarking:** Users can bookmark and share images from diverse sources, curating personalized collections.
- **Content Importing:** Facilitated seamless content importing from other websites, simplifying content sharing across the web.
- **User Interactions:** Implemented 'like/unlike' functionality for images shared by others, promoting user engagement.
- **User Tracking System:** Established a comprehensive tracking system for users to follow each other and receive real-time updates on activities, utilizing a generic activity stream application.
- **Query Optimization:** Utilized select_related and prefetch_related techniques to enhance database query performance.
- **Debugging Tools:** Integrated Django Debug Toolbar for efficient debugging during development.
- **Redis Integration:** Leveraged Redis, a high-performance key-value store, for counting image views and managing rankings efficiently.

**Technologies Used:**
- Python
- Django
- Messages Framework
- Python Social Authentication
- HTML
- CSS
- Pillow
- Extensions
- Requests
- JavaScript
- Easy-Thumbnails
- Redis

### Installation

1. Clone the Repo

```sh
git clone https://github.com/KGkhalidd/Dj-Social-website.git
```

2. Create Python Enviornment

```sh
python -m venv ENV
```

3. Install Requirements Libs

```sh
pip install -r requirements.txt
```
### Running Server 

1. Migrate the Database 
```sh
python manage.py migrate
```

2. Run Server 
```sh
python manage.py runserver
```
