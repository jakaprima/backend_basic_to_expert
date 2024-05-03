# Building for Scale

Speaking in general terms, scalability (kemampuan suatu sistem, jaringan, atau proses untuk menangani penambahan beban yang diberikan) 
is the ability of a system to handle a growing amount of work by adding resources to it.

A software that was conceived with a scalable architecture in mind, is a system that will support higher workloads without any fundamental changes to it, but don’t be fooled, this isn’t magic. You’ll only get so far with smart thinking without adding more sources to it.

For a system to be scalable, there are certain things you must pay attention to, like:
``` text
    Coupling: Bayangkan sebuah bangunan yang terdiri dari banyak balok kayu yang disatukan dengan paku. Semakin banyak paku yang digunakan untuk menyatukan balok, semakin kuat bangunan tersebut, tetapi juga semakin sulit untuk mengganti satu balok tanpa melepaskan paku dan merestrukturkan seluruh bangunan.
        Jenis-jenis coupling:

            Tight coupling: Ketergantungan tinggi antar komponen, sehingga  perubahan pada satu komponen dapat berdampak besar pada komponen lain.
            Loose coupling: Ketergantungan rendah antar komponen, sehingga perubahan pada satu komponen hanya berdampak minimal pada komponen lain.
```
``` text
    Observability: kemampuan memahami dan memantau perilaku sistem secara realtime
    Komponen Observability:

    Logging: Merekam peristiwa dan data sistem.
    Tracing: Melacak aliran permintaan melalui sistem.
    Metrics: Mengumpulkan data tentang kinerja sistem.
    Monitoring: Memvisualisasikan data observability dan mendeteksi anomali.
```
``` text
    Evolvability
```
``` text
    Infrastructure
```

When you think about the infrastructure of a scalable system, you have two main ways of building it: using on-premises resources or leveraging all the tools a cloud provider can give you.
The main difference between on-premises and cloud resources will be FLEXIBILITY, on cloud providers you don’t really need to plan ahead, you can upgrade your infrastructure with a couple of clicks, while with on-premises resources you will need a certain level of planning.
Visit the following resources to learn more:
    Scalable Architecture: A Definition and How-To Guide

# MITIGATION STRATEGIES (rencana mengurangi dampak negative dari suatu potensi masalah)
dalam keamanan siber: Menerapkan strategi mitigasi serangan siber untuk mengurangi risiko data dicuri atau sistem diretas. Ini bisa berupa pembuatan kata sandi yang kuat atau pemasangan firewall.
## GRACEFUL DEGRATION
analoginya ketika lapar dan tempat makan hanya ada di lantai 2, elevator rusak, tetapi tidak membuat kendala karena ada tangga
developers design websites or systems that still work, even if an advanced function cannot be completed
contoh: use external link to stylesheet

## THROLITTING
design pattern used to limit rate, commonly in cloud computing env.
prevent overuse resources
- rate limiting: involves setting maximum number of request within specific period
- resource location: involves allocation fixed amount of resource. and limiting use of those resources if they exceeded
- token bucket: involves "bucket" of tokens to represent the available resources, then allowing certain number of tokens to be consumed by each request
di aws bisa langsung dengan daftarin path endpoint dan di setting burst / rate limitter di api gateway aws
https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/rel_mitigate_interaction_failure_throttle_requests.html

## BACKPRESSURE (tekanan balik)
design pattern yang digunakan untuk manage flow dari data melewati system
analogi: system tidak bisa proses data datang secepat data diterima. backend itu loket layanan data diibaratkan antrian orang yang ingin dilayani
jika data datang terlalu cepat, antrian akan menjadi panjang dan waktu tunggu untuk proses akan semakin lama
solusi pake 
- buffer: data diterima sementara disimpan disuatu tempat sebelum di proses lebih lanjut. tapi jika tempat buffer sudah penuh maka data baru akan di tolak dan dibuang
- work queue: ibarat loker tempat para pekerja ambil tugas, sehingga tugas yang belum terhandle akan di masukan kedalam loker
- scalling: menambah resource cpu, memory
- throttling: mengurangi kecepatan data datang dan membantu mengendalikan beban system
- dropping data: mengorbankan data yang datang agar sistem stabil

## LOAD SHIFTING
design pattern used to manage workload of system by shifting the load to different components or resources at different times
cloud computing env.
analogi: mendistribusikan tugas pemrosesan data ke waktu yang berbeda untuk mengelola beban kerja
bayangkan seperti loket pelayanan public, pada jam sibuk loket tersebut akan dipenuhi antrian orang yang akan dilayani
solusi bagi jam kerja, loket pelayanan, petugas dibagi beberapa shift. pagi untuk menangani antrian pagi, siang untuk siang
menggunakan pekerja lepas: nambah resource cpu, memory temporer saat beban kerja tinggi
mengubah prioritas tugas: petugas loket memprioritaskan pelayanan kepada orang yang membutuhkan pelayanan cepat
several ways implement load shifting:
scheduling, load balancing, auto scaling, 

## CIRCUIT BREAKER
design pattern way to protect system from failures or excessive load by temperarily stopping certain operation if the system is deemed to be in a failed or overloaded state
consist 3 states: closed, open, half-open


# DIFFERENCE + USAGE
Instrumentation, Monitoring, and Telemetry
Instrumentation refers to the measure of a product’s performance, in order to diagnose errors and to write trace information. Instrumentation can be of two types: source instrumentation and binary instrumentation.
Backend monitoring allows the user to view the performance of infrastructure i.e. the components that run a web application. These include the HTTP server, middleware, database, third-party API services, and more.
Telemetry is the process of continuously collecting data from different components of the application. This data helps engineering teams to troubleshoot issues across services and identify the root causes. In other words, telemetry data powers observability for your distributed applications.
Visit the following resources to learn more:
