### Welcome to locust

The [official](https://locust.io) site is avialable.

Use the **pip install locust** to install the module.

In order to run the framework in WebUI mode use the following command.

``` bash
locust
```

In order to run it in headless run the following command.

``` bash
locust --headless --users 10 --spawn-rate 1 -H http://your-server.com
```

In order to use **master-slave** setup use the following commands.

``` bash
locust -f my_locustfile.py --master
locust -f - --worker --master-host <your master> --processes 4
```


