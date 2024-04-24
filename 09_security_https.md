#HTTPS
https://howhttps.works/why-do-we-need-https/


# OWAS (OPEN WEB APPLICATION SECURITY)
OWASP Security Risks

OWASP or Open Web Application Security Project is an online community that produces freely-available articles, methodologies, documentation, tools, and technologies in the field of web application security.

Visit the following resources to learn more:
https://cheatsheetseries.owasp.org/cheatsheets/AJAX_Security_Cheat_Sheet.html


# Cors (Cross origin resource sharing)
Cross-Origin Resource Sharing (CORS) is an HTTP-header based mechanism that allows a server to indicate any origins (domain, scheme, or port) other than its own from which a browser should permit loading resources.

Visit the following resources to learn more:
https://www.youtube.com/watch?v=4KHiSt0oLJ0

## ANALOGI
Mari kita gunakan analogi untuk memahami keamanan CORS (Cross-Origin Resource Sharing):

Bayangkan Anda memiliki sebuah klub tenis yang hanya memperbolehkan anggotanya untuk menggunakan fasilitasnya. Setiap anggota memiliki kartu keanggotaan yang diberikan saat mereka bergabung. Kartu ini digunakan untuk masuk ke klub dan menikmati fasilitasnya.

Sekarang, bayangkan ada sebuah turnamen tenis besar yang diadakan di klub tetapi dihadiri oleh pemain dari klub-klub lain. Namun, aturan klub Anda tetap berlaku; hanya anggota klub Anda yang boleh masuk ke dalamnya.

Inilah saatnya keamanan CORS bekerja: CORS adalah kebijakan yang memungkinkan atau membatasi akses dari sumber-sumber (domain atau asal) yang berbeda ke sumber daya di sebuah situs web. Ini mirip dengan klub tenis yang mempertimbangkan siapa yang diizinkan masuk ke turnamen tenis besar di dalam klub mereka.


# SSL / TLS
SSL/TLS

Secure Sockets Layer (SSL) and Transport Layer Security (TLS) are cryptographic protocols used to provide security in internet communications. These protocols encrypt the data that is transmitted over the web, so anyone who tries to intercept packets will not be able to interpret the data. One difference that is important to know is that SSL is now deprecated due to security flaws, and most modern web browsers no longer support it. But TLS is still secure and widely supported, so preferably use TLS.

Visit the following resources to learn more:

## ANALOGI
Bayangkan Anda sedang mengirimkan surat rahasia kepada teman Anda. Namun, Anda ingin memastikan bahwa surat tersebut tidak dapat dibaca oleh siapa pun selain teman Anda. Untuk melakukan ini, Anda memutuskan untuk menggunakan sebuah kunci gembok untuk mengunci surat tersebut sebelum mengirimkannya.

SSL/TLS (Secure Socket Layer/Transport Layer Security) mirip dengan kunci gembok ini. Ketika Anda terhubung ke sebuah situs web yang menggunakan SSL/TLS, komputer Anda dan situs web tersebut membuat kunci gembok bersama yang unik. Kunci gembok ini kemudian digunakan untuk mengunci atau mengenkripsi data yang dikirimkan antara kedua pihak. Ini seperti mengunci surat rahasia Anda sebelum mengirimkannya.

Selain itu, SSL/TLS juga memverifikasi identitas situs web yang Anda kunjungi. Ketika Anda terhubung ke situs web yang menggunakan SSL/TLS, komputer Anda meminta sertifikat dari situs web tersebut. Sertifikat ini adalah seperti ID yang dikeluarkan oleh otoritas keamanan online yang terpercaya. Jika sertifikat tersebut valid, Anda dapat yakin bahwa Anda terhubung ke situs web yang sebenarnya dan bukan situs palsu yang mencoba mencuri informasi Anda.

Dengan demikian, SSL/TLS bekerja seperti kunci gembok untuk melindungi informasi Anda saat Anda terhubung ke situs web, serta memastikan bahwa Anda terhubung ke situs web yang sah. Analogi ini memungkinkan kita untuk memahami konsep SSL/TLS dengan lebih mudah.


# CSP
Content Security Policy

Content Security Policy is a computer security standard introduced to prevent cross-site scripting, clickjacking and other code injection attacks resulting from execution of malicious content in the trusted web page context.

Visit the following resources to learn more:
https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP



## ANALOGI
Bayangkan Anda adalah seorang tuan rumah yang mengadakan pesta di rumah Anda. Anda ingin memastikan bahwa tamu Anda berperilaku sesuai dengan aturan yang Anda tetapkan dan tidak melakukan hal-hal yang tidak aman atau merusak.

Dalam hal ini, Anda sebagai tuan rumah adalah situs web Anda, dan tamu yang datang ke pesta adalah berbagai sumber daya yang dimuat di situs web Anda, seperti gambar, skrip, atau frame dari domain eksternal.

Sekarang, untuk memastikan bahwa tamu Anda mengikuti aturan yang telah Anda tetapkan, Anda memberikan setiap tamu sebuah kartu aturan yang harus mereka ikuti selama pesta. Kartu ini mungkin berisi aturan seperti "Tidak ada sepatu di dalam rumah" atau "Harap jaga kebersihan dapur setelah menggunakan."

Dalam keamanan CSP, Anda sebagai pemilik situs web dapat memberikan "kartu aturan" kepada browser pengguna yang menentukan sumber daya apa yang diizinkan untuk dimuat di situs web Anda. Aturan ini dapat melarang atau membatasi jenis sumber daya tertentu, seperti skrip JavaScript dari domain eksternal yang tidak dikenal, atau memerintahkan browser untuk hanya memuat sumber daya dari domain yang telah ditentukan sebelumnya.

Dengan menggunakan keamanan CSP, Anda dapat memastikan bahwa situs web Anda hanya memuat sumber daya yang diperbolehkan, mengurangi risiko serangan seperti XSS (Cross-Site Scripting) dan injeksi skrip lainnya. Analogi ini membantu memahami konsep CSP secara sederhana, di mana situs web bertindak sebagai tuan rumah dan sumber daya situs web bertindak sebagai tamu di pesta


# SERVER SECURITY
Server Security

Learn about the security of your server and how to secure it. Here are some of the topics off the top of my head:

    Use a firewall: One of the most effective ways to secure a server is to use a firewall to block all unnecessary incoming traffic. You can use iptables on Linux systems or a hardware firewall to do this.
    Close unnecessary ports: Make sure to close any ports that are not needed for your server to function properly. This will reduce the attack surface of your server and make it more difficult for attackers to gain access.
    Use strong passwords: Use long, complex passwords for all of your accounts, and consider using a password manager to store them securely.
    Keep your system up to date: Make sure to keep your operating system and software up to date with the latest security patches. This will help to prevent vulnerabilities from being exploited by attackers.
    Use SSL/TLS for communication: Use Secure Sockets Layer (SSL) or Transport Layer Security (TLS) to encrypt communication between your server and client devices. This will help to protect against man-in-the-middle attacks and other types of cyber threats.
    Use a intrusion detection system (IDS): An IDS monitors network traffic and alerts you to any suspicious activity, which can help you to identify and respond to potential threats in a timely manner.
    Enable two-factor authentication: Two-factor authentication adds an extra layer of security to your accounts by requiring a second form of authentication, such as a code sent to your phone, in addition to your password.

Also learn about OpenSSL and creating your own PKI as well as managing certs, renewals, and mutual client auth with x509 certs


## ANALOGI
Bayangkan Anda memiliki sebuah gudang di mana Anda menyimpan barang berharga. Anda ingin memastikan bahwa gudang tersebut aman dari pencuri dan hanya orang-orang yang sah yang diizinkan masuk.

Dalam analogi ini, gudang Anda adalah server Anda, di mana Anda menyimpan data sensitif atau aplikasi penting. Anda ingin memastikan bahwa server tersebut dilindungi dari serangan dan hanya pengguna yang sah yang memiliki akses ke dalamnya.

Untuk melindungi gudang Anda, Anda mungkin melakukan beberapa langkah seperti:

    Pengamanan Pintu Masuk: Anda memasang kunci dan mungkin bahkan sistem keamanan tambahan seperti kamera pengawas atau penjaga keamanan. Ini mencegah orang yang tidak diizinkan dari masuk ke gudang Anda. Dalam server, langkah serupa termasuk penggunaan firewall dan pengaturan akses yang ketat.

    Pemantauan Aktivitas: Anda mungkin memiliki sistem untuk memantau siapa yang masuk dan keluar dari gudang, serta apa yang mereka lakukan di dalamnya. Ini membantu Anda mendeteksi perilaku mencurigakan. Di server, Anda dapat menggunakan alat pemantauan seperti sistem pemantauan log untuk melacak aktivitas yang mencurigakan.

    Pembaruan Keamanan: Seperti mengganti kunci gembok yang usang, Anda perlu memastikan bahwa sistem keamanan Anda tetap mutakhir dengan memperbarui perangkat lunak dan sistem operasi secara berkala. Ini membantu mencegah serangan yang memanfaatkan kerentanan yang telah diketahui.

    Backup dan Pemulihan: Seperti membuat salinan cadangan barang berharga Anda, Anda perlu memiliki salinan cadangan dari data yang disimpan di server Anda, sehingga Anda dapat memulihkan data jika terjadi kejadian yang tidak terduga seperti kehilangan data atau serangan ransomware.


