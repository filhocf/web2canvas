Web2Canvas
=====================

The **Web2Canvas** intended to be a visual map containing preformatted nine blocks of the business model for easy management.
The Business Model Canvas is a strategic management tool, which allows you to develop business models and outline new or existing.

Learn more in [Web2Canvas](https://www-scm.prevnet/desc/web2canvas/ "Web2Canvas")

---------------------------------------

Dependencies
--------------

The Web2Canvas is a web2py application and run it you will need:

- Python 2.7.x
- libsasl2-dev 
- python-dev 
- libldap2-dev 
- libssl-dev
- python-ldap
- Web2Py 2.5.1
- Firefox 20+, Chrome 20+

---------------------------------------

Installation
------------

*1.*  First download [Web2py](https://github.com/web2py/web2py)

*2.*  Clone the repository Web2Canvas inside the folder "applications" of web2py.

    git clone https://www-scm.prevnet/desc/web2canvas.git

*3.*  Copy and edit the application configuration file:

    cd web2canvas/modules
    cp data_config_orig.py data_config.py
    cd ../..

*4.*  Install python-ldap:

    pip install python-ldap

*5.*  Install psycopg2:

    pip install psycopg2

*6.*  Now start web2py.

    python web2py -a 1

*7.*  Access the application by URL.

    http://localhost:8000/web2canvas

*8.*  Edit the file "/modules/data_config.py" and enter the data of your application to connect to ldap and to the mail server.

Changelog
-----------

**v 1.4**:

- Use PostgreSQL instead of sqlite
- Remove facebook authentication
- Remove feedback forms
- Remove share models forms
- Add support for LDAP authentication
- Add instructions to install python-ldap
- Add missing views
- Remove unused view information

**v 1.3**:

- Cards with the possibility of putting colors.
- Profile picture through Facebook or Gravatar.
- Export Canvas in PDF and PNG.
- Add Multilanguage support.

**v 1.2**:

- Delete project.
- Login with Facebook.
- New Project screen.
- Reset user password.
- Contact Us (Feedback).
- Profile picture through Facebook or Gravatar.

**v 1.1**:

- New layout.
- Home Screen.
- Share project with other users.
- Delete cards.
- Cards are automatically saved.
- Improved notifications.

**v 1.0**:

- System login.
- Creation of a new project.
- Issue Model Canvas.

---------------------------------------

TODOLIST
-----------

- Translation all the application to english.
- Realtime on shared projects.
- Removing a User from a project.
- Adjust layout responsive to other devices.
- Send email to new registered users.
- When adding a User in Project emailing him.

---------------------------------------

Developed by:
-------

[**Kolaborativa OpenLab**](https://github.com/kolaborativa)

---------------------------------------

License
---------------------
The Web2Canvas is under MIT license: [http://www.opensource.org/licenses/mit-license.php](http://www.opensource.org/licenses/mit-license.php)
