Integration testing, unit testing, dan functional testing adalah tiga jenis pengujian perangkat lunak yang berbeda, masing-masing dengan tujuan dan cakupan yang berbeda. Berikut adalah perbedaan antara ketiganya beserta contoh penggunaannya dalam Python:

    Unit Testing:
        Tujuan: Unit testing dilakukan untuk menguji setiap unit kode secara terisolasi. Unit biasanya merupakan bagian terkecil dari kode yang dapat diuji secara terpisah, seperti fungsi atau metode.
        Cakupan: Fokus pada tingkat kode yang sangat rendah dan memastikan setiap unit berperilaku sesuai yang diharapkan.
        Contoh dalam Python: Menggunakan modul unittest atau pytest untuk menulis dan menjalankan tes pada fungsi atau metode individu. Contoh:

```python

import unittest

def add(a, b):
    return a + b

class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(3, 5), 8)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-3, -5), -8)

if __name__ == '__main__':
    unittest.main()
```

Integration Testing:

    Tujuan: Integration testing dilakukan untuk memastikan bahwa komponen-komponen yang berbeda dari sistem dapat berinteraksi satu sama lain dengan benar.
    Cakupan: Melibatkan pengujian integrasi antara dua atau lebih unit yang bekerja bersama untuk memastikan bahwa mereka berfungsi dengan baik ketika digabungkan.
    Contoh dalam Python: Menggunakan pustaka seperti unittest atau pytest untuk menguji interaksi antara beberapa modul atau komponen dalam sebuah aplikasi. Contoh:

``` python

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def add_and_multiply(a, b, c):
    return multiply(add(a, b), c)

def test_add_and_multiply():
    result = add_and_multiply(2, 3, 4)
    assert result == 20

if __name__ == '__main__':
    test_add_and_multiply()
```

Functional Testing:

    Tujuan: Functional testing bertujuan untuk memastikan bahwa sistem berperilaku sesuai dengan spesifikasi fungsional yang ditentukan.
    Cakupan: Melibatkan pengujian sistem secara keseluruhan dari perspektif fungsional, seringkali melalui simulasi dari tindakan pengguna.
    Contoh dalam Python: Menggunakan kerangka kerja pengujian fungsional seperti Selenium atau PyTest. Contoh:

``` python

    from selenium import webdriver

    def test_login_functionality():
        driver = webdriver.Chrome()
        driver.get("https://example.com")
        # Simulate user login
        username_input = driver.find_element_by_id("username")
        password_input = driver.find_element_by_id("password")
        login_button = driver.find_element_by_id("login_button")

        username_input.send_keys("user")
        password_input.send_keys("password")
        login_button.click()

        # Assert login success
        assert "Welcome" in driver.page_source

        driver.quit()

    if __name__ == '__main__':
        test_login_functionality()
```

Dengan contoh-contoh di atas, Anda dapat melihat perbedaan penggunaan dan cakupan dari ketiga jenis pengujian tersebut dalam lingkungan Python.