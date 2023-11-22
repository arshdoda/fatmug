<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">Fatmug</h3>

</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#api-endpoints">API Endpoints</a></li>
    <li><a href="#data-creation">Data Creation</a></li>
  </ol>
</details>


<!-- GETTING STARTED -->
## Getting Started

The app is publically availabe on github and is also deployed on aws (http://13.235.81.184/admin/). This doucment focuses on setting up the app on local machine.



### Prerequisites

The app requires python 3.10 or later to run and it can work both on  windows and linux.
* windows
  ```sh
  https://www.python.org/downloads/windows/
  ```
* linux
  ```sh
  sudo apt install python3
  ```

### Installation

Follow the steps to setup the app on local machine.

1. Open the terminal on linux or powershell on windows
2. Clone the repo
   ```sh
   git clone https://github.com/arshdoda/fatmug
   ```
3. Create a virtual env
   ```sh
   cd fatmug
   python3 -m venv .venv
   ```
4. Activate the virtual env
* windows
   ```sh
   .venv/Scripts/activate
   ```
* linux
   ```sh
   source .venv/bin/activate
   ```
4. Install Dependencies
   ```sh
   pip install -r requirements.txt
   ```
5. Run the app
   ```sh
   cd backend
   python3 manage.py runserver
   ```


<!-- USAGE -->
## Usage
This app support Token based authentication and Session based authentication (in local env only).  Use the following credentials to login/get token.

* Online URL: 13.127.83.149
* Local URL: 127.0.0.1:8000
* Username: fatmug
* Password: fatmug@123

<h5>Session Authentication</h5>
The session based authentication provides drf-templates which is very easy to use. To use session based authentication, go to http://13.235.81.184/admin/ and login with above credentials.
You can now use the secured apis.

<h5>Token Authentication</h5>
For token based authentication, go to http://13.235.81.184/api/token/ and login with above credentials.
You will get access token and refresh token.

Then, use curl to call the api's as shown below.
  ```sh
   curl -H "Authorization: JWT {access token}" http://13.235.81.184/api/vendors/
   ```


<!-- Api Endpoints -->
## Api Endpoints

To use the endpoint locally, replace "13.127.83.149" with "127.0.0.1:8000"

<h5>Session Authentication</h5>

http://13.235.81.184/admin/


<h5>Token Authentication</h5>

http://13.235.81.184/api/token/
http://13.235.81.184/api/token/refresh/


* Following apis require a user to be authenticated. You can use both Token and Session base authentication.

<h5>Vendors</h5>

http://13.235.81.184/api/vendors/
http://13.235.81.184/api/vendors/{id}/
http://13.235.81.184/api/vendors/{id}/performance/

<h5>PO</h5>

http://13.235.81.184/api/purchase_orders/
http://13.235.81.184/api/purchase_orders/{id}/
http://13.235.81.184/api/purchase_orders/{id}/performance/

   
<!-- Data Creation -->
## Data Creation

The db.sqlite3 already contains 5 vendors and 100000 PO data. To start from scratch follow the steps  

1. Delete the db.sqlite3 file from backend.
2. Create DB and run migrations
   ```sh
   python3 manage.py migrate
   ```
3. Create superuser
   ```sh
   python3 manage.py createsuperuser
   ```
Now, you can use the above api's to create the data. If you want to generate data in one go then continue with the following steps

4. Modify the dummy_data.py file as required.
5. Run Django shell 
   ```sh
   python3 manage.py shell
   ```
6. Run Data Creation script 
   ```sh
   exec(open('dummy_data.py').read())
   ```
7. Required only if data is generated using script: 
  To calculate the performance matrix for the vendors, authenticate the user with any of the authentication method and then go to the http://127.0.0.1:8000/api/purchase_orders/calculate_matrix



<p align="right">(<a href="#readme-top">back to top</a>)</p>

