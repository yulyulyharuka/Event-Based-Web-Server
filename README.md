# Event-Based-Web-Server
Event based web server using low level library and high level library.

## Web-Server Benchmarking Tool
Tool used:
* [JMeter](https://jmeter.apache.org/)

### Requirement
* Java 8+

### Step
1. Download [JMeter](http://jmeter.apache.org/download_jmeter.cgi)
2. Extract downloaded file
3. open apache-jmeter-\<version\>/bin/jmeter.bat or
   ```
   sh apache-jmeter-<version>/bin/jmeter.sh
   ```
4. open test from resource folder (ConccurentTest.jmx) <br>
![](images/open.png)
5. run the test <br>
![](images/run.png)
6. JMeter will create file result.csv

### Test result
#### Nginx
* 500 Byte file
  * Average Latency: 2595.5 ms (3.174 Success Request/ 10.000 concurent request)
  * Memory Usage: 2.7 MB
* 20 KB file
  * Average Latency: 2447.5 ms (3.657 Success Request / 10.000 concurent request)
  * Memory Usage: 2.7 MB

#### Apache
* 500 Byte file
  * Average Latency: 2211 ms (4.700 Success Request/ 10.000 concurent request)
  * Memory Usage: ~8 MB
* 20 KB file
  * Average Latency: 2200.5 ms (3.659 Success Request/ 10.000 concurent request)
  * Memory Usage: ~8 MB

## Petunjuk Instalasi / Building dan Cara Menjalankan Program 
- Program low level library dengan pyuv
1. Install python3 pada perangkat anda 
2. Lakukan instalasi library yang digunakan
    ```pip3 install pyuv```
3. Jalankan web server dengan membuka command prompt dan ketik perintah berikut :
    ```python3 src/main_libuv.py <port_number> <path_file>```

- Program high level library dengan tornado
1. Install python3 pada perangkat anda 
2. Lakukan instalasi library yang digunakan
    ```pip3 install tornado```
3. Jalankan web server dengan membuka command prompt dan ketik perintah berikut :
    ```python3 src/main_tornado.py <port_number> <path_file>```

## Hasil Pengujian untuk Web Server dengan Low Level dan High Level Library