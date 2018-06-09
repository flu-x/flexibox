# Browserium

![Browserium logo](https://farm2.staticflickr.com/1742/41852028144_642310d9b6_m.jpg)

**Browserium** is the a selenium wrapper for all **browsers** and **browser configurations**. This module is a single end point to access all the browser drivers and as well as the webdriver object for all the respective browsers along with the installation of your **selenium** module.

## Problem Statement
With the very fast pace of development, it has now become very important to have regular release cycle and with it it should be also kept in mind that we do a quality release. For this reason we have to have our tests automated as well so that we can have a centralised reports for regressions and other flaws in the system at the end of each build.

Now, for a stable build we have to check that our application is compatible with different browsers and platforms. When we start implementing a framework based out of Selenium WebDriver, for the code to get executed in different browsers we have to configure each of the browsers separately and make a call to the browser based on the requirement. Phewww !! That is some good amount of code written.

## The Idea
The problem statement that has been defined above was the reason I took out time to ease this entire process of setting up the browser drivers and the respective configurations for each browser. What if this process can be reduced down into few steps of execution? That is how I ended up with the idea and the implementation of **Browserium**.

## What does 'Browserium' provide you?
* One step to **download** the required browser drivers.
* One step to **update** the required browser drivers.
* Create a **single instance** for your required browser object. No more code required to configure your browsers separately.
* A set of browser related **generic functions** that can be utilised for debugging as well as for achieving the required functionalities. So, we are reducing quite an effort over here as well !!
* You can run browsers **Chrome** and **Firefox** using the **headless** option as well so that it is comfortable running your framework on the server as well.

## Browserium by functionality
![functionality screenshot](https://farm2.staticflickr.com/1750/41853754714_971a727962.jpg)

There are two ways in which you can use Browserium.

* Download the required browser driver, create instance for the specific browser driver class.
* Download the required browser driver, create instance for the specific browser driver class, create instance for the browser controller class and use the generic functions to get started with your framework.

You can refer to the above diagram for reference.

## Installing and Updating driver packages

### Install Browserium module
* To install Browserium using PiP run the command:

	`pip install browserium`
	
* To install Browserium from GitHub run the command:


	`pip install git+git://github.com/browserium/Browserium.git`
	
### Modules installed with browserium
* **requests**

* **selenium**

* **wget**

Make sure you have **ssh** configured in GitHub. You can also use **https** as well to install the module. But preferrable would be if you have **ssh** configured in GitHub.

To install Browserium from GitHub using HTTPS run the command:

	pip install git+https://github.com/browserium/Browserium.git	

* To download chromedriver run the command

	```browserium download --driver=chromedriver```

* To download geckodriver run the command

	```browserium download --driver=geckodriver```

* To download operadriver run the command

	```browserium download --driver=operadriver```

* To download phantomjsdriver run the command

	```browserium download --driver=phantomjsdriver```

### Update Drivers
* To update chromedriver run the command

	```browserium update --driver=chromedriver```

* To update geckodriver run the command

	```browserium update --driver=geckodriver```

* To update operadriver run the command

	```browserium update --driver=operadriver```

* To update phantomjsdriver run the command

	```browserium update --driver=phantomjsdriver```

## Get started with Browserium
### Browser Controller class by functionality
The `Browser Controller` class provides you with some eccentric methods that can be utilised to achieve the required functions. 

* **get_url(driver, url)**: request the required url entered. Pass the required driver object and the 'url' as parameters.

* **implicit_wait_time(driver, time)**: Apply implicit wait before the dom loads. Pass the required driver object and the time as parameters.

* **set_window_size(driver, height, width)**: Set the window size for the current running browser. Pass the required driver object, height and the width of the window.

* **get_current_url(driver)**: Get the current url. Pass the required driver object as parameter.

* **get_network_requests(driver)**: Get all the network requests for the current page. Pass the required driver object as parameter.

* **performance_metrics(driver)**: Get required page performance data. Pass the required driver object as parameter.

* **check_console_logs(driver)**: Get all console logs. Pass the required driver object as parameter.

* **get_page_source(driver)**: Get the current page source. Pass the required driver object as parameter.

* **get_site_cookies(driver)**: Get all the site cookies. Pass the required driver object as parameter.

### Create instance for Chrome
* Create instance for the `ChromeDriverObject` class
* Use the instance for `ChromeDriverObject` class to call the `set_chromedriver_object` method.
* Create instance for the `Browser_controller` class to use the generic methods.

```python
chromedriver = ChromeDriverObject()
controller = Browser_controller()
driver = chromedriver.set_chromedriver_object()
controller.get_url(driver, "https://www.google.co.in")
controller.implicit_wait_time(driver, 4)
current_url = controller.get_current_url(driver)
print current_url
```
* To run chromedriver using the `headless` feature you have to pass the argument '--headless' in the `set_chromedriver_object()` method

```python
chromedriver = ChromeDriverObject()
controller = Browser_controller()
driver = chromedriver.set_chromedriver_object('--headless')
controller.get_url(driver, "https://www.google.co.in")
controller.implicit_wait_time(driver, 4)
current_url = controller.get_current_url(driver)
print current_url
```

### Create instance for Firefox
* Create instance for the `GeckoDriverObject` class
* Use the instance for `GeckoDriverObject` class to call the `set_geckodriver_object` method.
* Create instance for the `Browser_controller` class to use the generic methods.

```python
geckodriver = GeckoDriverObject()
controller = Browser_controller()
driver = geckodriver.set_geckodriver_object()
controller.implicit_wait_time(driver, 4)
controller.get_url(driver, "https://www.google.co.in")
current_url = controller.get_current_url(driver)
print current_url
print driver.title
```
* To run chromedriver using the `headless` feature you have to pass the argument '--headless' in the `set_geckodriver_object()` method

```python
geckodriver = GeckoDriverObject()
controller = Browser_controller()
driver = geckodriver.set_geckodriver_object('--headless')
controller.implicit_wait_time(driver, 4)
controller.get_url(driver, "https://www.google.co.in")
current_url = controller.get_current_url(driver)
print current_url
print driver.title
```

### Create instance for Opera
* Create instance for the `OperaDriverObject` class
* Use the instance for `OperaDriverObject` class to call the `set_operadriver_object` method
* Create instance for the `Browser_controller` class to use the generic methods.

```python
operadriver = OperaDriverObject()
controller = Browser_controller()
driver = operadriver.set_operadriver_object()
controller.implicit_wait_time(driver, 4)
controller.get_url(driver, "https://www.google.co.in")
current_url = controller.get_current_url(driver)
print current_url
print driver.title
```

### Create instance for PhantomJS
* Create instance for the `PhantomDriverObject` class
* Use the instance for `PhantomDriverObject` class to call the `set_phantomdriver_object` method
* Create instance for the `Browser_controller` class to use the generic methods.

```python
phantomdriver = PhantomDriverObject()
controller = Browser_controller()
driver = phantomdriver.set_phantomdriver_object()
print driver
controller.implicit_wait_time(driver, 4)
controller.get_url(driver, "https://www.google.co.in")
current_url = controller.get_current_url(driver)
print current_url
```
P.S: It would be wise not to use PhantomJS as Selenium would not support PhantomJS in its later versions. To run your tests in headless you can use the headless feature provided by `Chromedriver` or `Firefoxdriver`

### Create instance for Safari
* Create instance for the `SafariDriverObject` class
* Use the instance for `SafariDriverObject` class to call the `set_safaridriver_object` method
* Create instance for the `Browser_controller` class to use the generic methods.

```python
safaridriver = SafariDriverObject()
controller = Browser_controller()
driver = safaridriver.set_safaridriver_object()
controller.get_url(driver, "https://www.google.co.in")
controller.implicit_wait_time(driver, 4)
current_url = controller.get_current_url(driver)
print current_url
print driver.title
driver.quit()
```
P.S: Safaridriver comes shipped with the Safari browser by default. You have to enable the `Allow Remote Automation` option from the `Develop` menu. Please check this screenshot.
![Safari](https://farm2.staticflickr.com/1738/28757957868_38fff165d4.jpg)

Keep in mind that your safari version has to be more than 10. If it is not 10 or more than 10 then please update your Safari version.

### Deleting all browser driver
To delete all browser drivers from /usr/local/bin run the command:

	browserium delete --driver=all
