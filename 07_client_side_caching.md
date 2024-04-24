client side caching
client side caching is the storage of network data to local cache for feture re-use.
after an application fetches network data, it stores that resource in a local cache. once a resource has been cached, the browser uses cache on future request
for that resource to boost performance



BROWSER CACHE
Proxy Server cache
Reverse Proxy Server cache

terminologi
client request source -> 

caching headers:
RESPONSE FROM SERVER
expires: Mon, 15 oct 2020 12:00:00 GMT
pragma: no -cache
content-control: private / public / no-store (tidak boleh di cache) / no-cache (bisa dicache tapi harus di validasi)
Cache-Control: max-age=3600, private (bisa di cached for given number of seconds) / s-max-age=3600 (bisa di cached at public places for given number of seconds) / must-revalidate (never serve the stale content and must validate the content) / proxy-revalidate

Etag entity tags



CLOUDFLARE
https://dash.cloudflare.com/login


