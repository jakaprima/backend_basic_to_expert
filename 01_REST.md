# backend_basic_to_expert
backend_basic_to_expert

REST (Representational State Transfer)
adalah style arsitektur untuk melayani standarisasi antara system komputer di web,
membuat lebih mudah untuk system berkomunikasi antara yang lain.

https://www.codecademy.com/article/what-is-rest

# Memisahkan client dan server
code di client side bisa dirubah tanpa mengganggu operation dari server dan sebaliknya

# Statelessness
system yang mengikuti paradigma REST itu stateless. artinya server tidak perlu tau apapun tentang state si client dan sebaliknya

# Communication antara client dan server

## membuat request
REST membutuhkan client untuk membuat request ke server, untuk menerima atau memodifikasi data
- REQUEST umumnya mengandung:
- HTTP verb: mendefinisikan jenis operation yang dijalankan
- HEADER: dimana client untuk memberikan informasi tentang request
- path ke source:
- opsional message body contain data

HTTP Verb:
GET, POST, PUT, DELETE

Headers and Accept parameters
Contoh:

GET /articles/23
Accept: text/html, application/xhtml

lainnya:
- image — image/png, image/jpeg, image/gif
- audio — audio/wav, audio/mpeg
- video — video/mp4, video/ogg
- application — application/json, application/pdf, application/xml, application/octet-stream

PATH: request harus mengandung path ke source yang akan di eksekusi
GET fashionboutique.com/customers/:id 

CONTENT TYPES
server yang mengirim data payload ke client, server harus mengandung Content-Type di header dari response
headers ini digunakan untuk memberitahu client type data dalam response tersebut.
content types adalah MIME Types
Contoh:

For example, when a client is accessing a resource with id 23 in an articles resource with this GET Request:

GET /articles/23 HTTP/1.1
Accept: text/html, application/xhtml

The server might send back the content with the response header:

HTTP/1.1 200 (OK)
Content-Type: text/html

Response Codes:
server memberitahu client tentang kesuksesan dari operation

Status code	Meaning
200 (OK)	This is the standard response for successful HTTP requests.
201 (CREATED)	This is the standard response for an HTTP request that resulted in an item being successfully created.
204 (NO CONTENT)	This is the standard response for successful HTTP requests, where nothing is being returned in the response body.
400 (BAD REQUEST)	The request cannot be processed because of bad request syntax, excessive size, or another client error.
403 (FORBIDDEN)	The client does not have permission to access this resource.
404 (NOT FOUND)	The resource could not be found at this time. It is possible it was deleted, or does not exist yet.
500 (INTERNAL SERVER ERROR)	The generic answer for an unexpected failure if there is no more specific information available.









# Practice with REST
Let’s imagine we are building a photo-collection site. We want to make an API to keep track of users, venues, and photos of those venues. This site has an index.html and a style.css. Each user has a username and a password. Each photo has a venue and an owner (i.e. the user who took the picture). Each venue has a name and street address. Can you design a REST system that would accommodate:

storing users, photos, and venues
accessing venues and accessing certain photos of a certain venue
Start by writing out:

what kinds of requests we would want to make
what responses the server should return
what the content-type of each response should be
Possible Solution - Models
```
{
  “user”: {
    "id": <Integer>,
    “username”: <String>,
    “password”:  <String>
  }
}
{
  “photo”: {
    "id": <Integer>,
    “venue_id”: <Integer>,
    “author_id”: <Integer>
  }
}
{
  “venue”: {
    "id": <Integer>,
    “name”: <String>,
    “address”: <String>
  }
}
```
Possible Solution - Requests/Responses
```
GET Requests
Request- GET /index.html Accept: text/html Response- 200 (OK) Content-type: text/html

Request- GET /style.css Accept: text/css Response- 200 (OK) Content-type: text/css

Request- GET /venues Accept:application/json Response- 200 (OK) Content-type: application/json

Request- GET /venues/:id Accept: application/json Response- 200 (OK) Content-type: application/json

Request- GET /venues/:id/photos/:id Accept: application/json Response- 200 (OK) Content-type: image/png

POST Requests
Request- POST /users Response- 201 (CREATED) Content-type: application/json

Request- POST /venues Response- 201 (CREATED) Content-type: application/json

Request- POST /venues/:id/photos Response- 201 (CREATED) Content-type: application/json

PUT Requests
Request- PUT /users/:id Response- 200 (OK)

Request- PUT /venues/:id Response- 200 (OK)

Request- PUT /venues/:id/photos/:id Response- 200 (OK)

DELETE Requests
Request- DELETE /venues/:id Response- 204 (NO CONTENT)

Request- DELETE /venues/:id/photos/:id Response- 204 (NO CONTENT)
```


