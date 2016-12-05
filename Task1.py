import subprocess
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

subprocess.call("php D:/script.php")

driver = webdriver.Chrome()
driver.implicitly_wait(10)
path = "https://tengrinews.kz/"
driver.get(path)

news = [i.text for i in driver.find_elements_by_xpath('//div[@id="main_news"]/div[@class="news clearAfer pl mb"]/div[@class="stats"]//span[@class="sc-icon showed"]')]
news_link = [j.get_attribute("href") for j in driver.find_elements_by_xpath('//div[@id="main_news"]/div[@class="news clearAfer pl mb"]/a')]

comments_count=1
for i in range(0, len(news)):
	driver.get(news_link[i])
	driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

	title = driver.find_elements_by_tag_name('h1')
	authors = driver.find_elements_by_xpath('//div[@class="comment"]/div[@class="user"]/span')
	content = driver.find_elements_by_xpath('//div[@class="content"]')
    
    for j in range(len(comments)):
    	<?php
		$servername = "localhost";
		$username = "Adil";
		$password = "qwerty";
		$dbname = "myDB";

		$conn = new mysqli($servername, $username, $password, $dbname);
		if ($conn->connect_error) {
		    die("Connection failed: " . $conn->connect_error);
		} 

		$sql = "INSERT INTO data (title, content, authors) VALUES (title, content, authors)";

		if ($conn->query($sql) === TRUE) {
		    echo "New record created successfully";
		} else {
		    echo "Error: " . $sql . "<br>" . $conn->error;
		}

		$conn->close();
		?>
        comments_count+=1
