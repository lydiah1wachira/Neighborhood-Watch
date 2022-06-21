# Neighborhood-Watch
This is a web application that allows you to be in the loop about everything happening in your neighborhood. From contact information of different handyman to meeting announcements or even alerts.

## live link
https://nhoodwatch.herokuapp.com/

## User stories
* Sign in with the application to start using.
* Set up a profile about me and a general location and my neighborhood name.
* Find a list of different businesses in my neighborhood.
* Find Contact Information for the health department and Police authorities near my neighborhood.
* Create Posts that will be visible to everyone in my neighborhood.
* Change My neighborhood when I decide to move out.
* Only view details of a single neighborhood.

## BDD
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Admin Authentication | **On demand** | Access Admin dashboard |
| To add an hoods,businesses  | **Admin** | Click on add and save respectively|
| To edit hoods,posts,businesses  | **Admin** | Redirected to the  hoods,posts,businesses form details and editing happens|
| To delete an hoods,posts,businesses  | **Admin** | click on hoods,posts,businesses object and confirm by delete button|
| To search business by name | **Enter text in search bar** | Users can search businesses by Name|
| View posts by neighbours | **Add posts** | Users can add posts to hoods they join|

<br>

## Setup and Installation
Fork and then clone this repository 
cd into the folder 
create a virtual environment
pip install -r requirements.txt
create a database 
Run migrations

## Technologies used
*Django Rest Framework
*Django
*Cloudinary

## By 
Lydiah Wachira

## License 
MIT License

Copyright (c) 2022 lydiah wachira

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
