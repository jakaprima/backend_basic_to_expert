
A producer is a user application that sends messages.
A queue is a buffer that stores messages.
A consumer is a user application that receives messages.
exchange : analoginya seperti papan pengumuman
pesan di terima di departement area yang di tunjung (antrian)
tipe pengumuman (exchange):
    Direct Exchange (Satu-ke-Satu): Ini seperti memiliki karyawan tertentu yang bertanggung jawab untuk setiap departemen. Pembuat pesan (pengirim) mengalamatkan pesan secara langsung ke antrian departemen tertentu (routing key). Hanya antrian yang ditunjuk yang menerima pesan.
    Topic Exchange (Pencocokan Fleksibel): Ini mirip dengan papan buletin dengan bagian berkategori (topik) seperti "Penjualan," "Pemasaran," atau "Layanan Pelanggan." Pembuat pesan menyertakan topik dalam pesan. Setiap antrian departemen berlangganan ke topik tertentu. Pesan dikirim ke antrian yang topik berlangganannya cocok dengan topik pesan (routing key dengan wildcard yang diizinkan).
    Headers Exchange (Perutean Berdasarkan Konten): Ini seperti memiliki papan pesan tempat pesan diklasifikasikan berdasarkan kriteria tertentu (header) seperti urgensi, departemen, atau prioritas. Pembuat pesan menyertakan header dalam pesan. Setiap antrian departemen menetapkan aturan berdasarkan header ini. Pesan dikirim ke antrian yang aturannya cocok dengan header pesan.
    Fanout Exchange (Siaran): Ini seperti memiliki sistem pengumuman seluruh perusahaan di mana semua orang menerima pesan yang sama. Semua antrian yang terikat pada exchange fanout menerima salinan pesan, terlepas dari kriteria perutean tertentu.






22_3
sudo rabbitmqctl list_bindings
# => Listing bindings ...
# => logs    exchange        amq.gen-JzTY20BRgKO-HjmUJj0wLg  queue           []
# => logs    exchange        amq.gen-vso0PVvyiRIL2WoV3i48Yg  queue           []
# => ...done.


22_4 demo test
run worker to listen
```sh
python 22_4_receive_log_direct.py warning error > log_from_rabbit.log
```
lalu masukan pesan
```sh
python 22_4_routing_emit_log.py error "isi pesan log error."
```
maka pesan error akan di transmisikan ke log_from_rabbit.log






22_5 topic
To receive all the logs run:
```sh
python receive_logs_topic.py "#"
```

To receive all logs from the facility "kern":
```sh
python receive_logs_topic.py "kern.*"
```

Or if you want to hear only about "critical" logs:
```sh
python receive_logs_topic.py "*.critical"
```

You can create multiple bindings:
```sh
python receive_logs_topic.py "kern.*" "*.critical"
```

And to emit a log with a routing key "kern.critical" type:
```sh
python emit_log_topic.py "kern.critical" "A critical kernel error"
```


more topics usage
https://www.rabbitmq.com/docs
