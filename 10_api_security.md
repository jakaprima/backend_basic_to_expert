
# AUTHENTICATION
- jangan gunain Basic Auth, gunakan JWT
- Berikut beberapa contoh mekanisme autentikasi mapan yang dapat Anda gunakan alih-alih menciptakan kembali roda:

     OAuth: OAuth adalah standar terbuka yang banyak digunakan untuk otorisasi yang memungkinkan pengguna memberikan akses aplikasi pihak ketiga ke sumber daya mereka tanpa membagikan kredensial mereka. Ini biasanya digunakan oleh layanan web dan API untuk memungkinkan pengguna masuk dengan akun media sosial atau akun pihak ketiga lainnya.

     OpenID Connect: OpenID Connect adalah protokol autentikasi yang dibangun di atas OAuth 2.0 yang memungkinkan pengguna mengautentikasi beberapa situs web dan aplikasi menggunakan satu set kredensial. Ini biasanya digunakan untuk sistem masuk tunggal (SSO) di beberapa situs web dan aplikasi.

     SAML: Security Assertion Markup Language (SAML) adalah standar berbasis XML untuk pertukaran data autentikasi dan otorisasi antar pihak. Ini biasanya digunakan untuk SSO di beberapa domain atau organisasi.

     Algoritme hashing kata sandi: Algoritme hashing kata sandi seperti bcrypt dan scrypt banyak digunakan untuk menyimpan dan melindungi kata sandi pengguna dengan aman. Algoritme ini memastikan bahwa meskipun penyerang mendapatkan akses ke database kata sandi, mereka tidak akan dapat memulihkan kata sandi dengan mudah.

     Otentikasi dua faktor (2FA): 2FA adalah mekanisme otentikasi yang mengharuskan pengguna memberikan dua bentuk identifikasi untuk mengakses akun mereka. Hal ini biasanya melibatkan sesuatu yang diketahui pengguna (seperti kata sandi) dan sesuatu yang dimiliki pengguna (seperti perangkat seluler atau kunci keamanan). Banyak layanan dan aplikasi kini menawarkan 2FA sebagai tindakan keamanan tambahan.

- use max retry and jail
Max Retry: The “Max Retry” feature limits the number of login attempts that a user can make within a specified time period. After a certain number of failed login attempts, the user is locked out of their account for a specified period of time, typically several minutes or hours. This helps to prevent brute-force attacks, where an attacker attempts to guess a user’s password by making repeated login attempts. By limiting the number of attempts, the system can slow down or prevent such attacks.

Jail: The “jail” feature involves blocking IP addresses or user accounts that have exceeded the maximum number of failed login attempts within a certain time period. The blocked IP addresses or user accounts are prevented from attempting further logins for a specified period of time, typically several minutes or hours. This helps to prevent brute-force attacks, and also provides a mechanism to prevent malicious users from repeatedly attempting to access an account or system.

- Sensitive Data Encryption
Sensitive Data Encryption

    Encrypting sensitive data is important for protecting it from unauthorized access, theft, and exploitation.

Encryption is a process of converting plain text data into a cipher text that can only be deciphered by someone who has the decryption key. This makes it difficult for attackers to access sensitive data, even if they are able to intercept it or gain unauthorized access to it.

To encrypt sensitive data, you can use encryption algorithms such as AES or RSA, along with a strong key management system to ensure that keys are securely stored and managed. Additionally, you can implement other security measures such as access controls, firewalls, and intrusion detection systems to further protect sensitive data.


# JWT
- check file best practice 11_api_security_jwt.py
- setting shorten token expiry
- avaoid storing sensitive data in jwt payload
- jwt payload size keep small


# access control
- check 11_api_security_limit_request.py
- use https on server side and secure ciphers
- use hSTS headers check 
- turn off directory listing
``` sh
To disable directory listings in a web server, you typically need to configure the server's settings. Below, I'll outline how you can disable directory listings for popular web servers: Apache and Nginx.
Apache

In Apache, you can disable directory listings by modifying the server's configuration file (httpd.conf) or adding a .htaccess file to the directory you want to protect.

To disable directory listings globally (for all directories), you can add the following line to your httpd.conf file:

mathematica

Options -Indexes

Alternatively, if you want to disable directory listings for a specific directory, you can create a .htaccess file in that directory and add the same line:

mathematica

Options -Indexes

After making the changes, restart the Apache server for the changes to take effect.
Nginx

In Nginx, you can disable directory listings by editing the server configuration file (nginx.conf or a specific virtual host configuration file).

To disable directory listings, you can add the following line within the server block:

vbnet

autoindex off;

For example:

nginx

server {
    listen 80;
    server_name example.com;

    location / {
        # Other directives...
        autoindex off;
    }
}

After making the changes, reload or restart the Nginx server for the changes to take effect.

By disabling directory listings, you prevent unauthorized users from accessing the contents of directories on your web server, thereby enhancing the security of your API and preventing potential attacks.
```


# private apis to be only accessiable from safe listed IP
``` sh
To restrict access to a private API to specific IP addresses, you can implement IP whitelisting in your web server or application firewall. Below, I'll outline how you can achieve this using various methods:
Using Nginx

If you're using Nginx as your web server, you can restrict access to your API endpoints by IP address in the server configuration.

nginx

server {
    listen 80;
    server_name example.com;

    location /api {
        allow 192.168.1.1;  # Replace with your safe-listed IP address
        deny all;
        # Your API configuration...
    }
}

In this configuration, only requests coming from the IP address 192.168.1.1 will be allowed access to the /api endpoint. Requests from other IP addresses will be denied.
```


# OAUTH SECURITY
- https://roadmap.sh/best-practices/api-security

# INPUT
- validate content-type on request headers
- validate user input to avoid common vulneraibilities
- use standart Authorization
- avoid client side encryption


