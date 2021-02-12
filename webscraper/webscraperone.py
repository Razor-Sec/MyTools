from selenium import webdriver
url = 'https://www.youtube.com/watch?v=CHUxmVVH2AQ&t=268s&ab_channel=KalleHallden'
browser = webdriver.Chrome()
browser.get(url)

browser.find_element_by_xpath('//*[@id="movie_player"]/div[27]/div[2]/div[1]/a[2]').click()
