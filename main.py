from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver

url = "https://www.mdpi.com/journal/entropy/editors"

c = {
        'computer'.upper(),
        'Computational'.upper(),
        'Entropy'.upper(),
        'Algorithm'.upper(),
        'Information theory'.upper(),
        'Robotic'.upper(),
        'Machine'.upper(),
        'Machine learning'.upper(),
        'Artificial inteligence'.upper(),
        'Computational inteligence'.upper(),
        'Probability'.upper(),
        'Solomonoff'.upper(),
        'Kolmogorov'.upper(),
        'Landau'.upper(),
        'computer Physics'.upper(),
        'Computational Physics'.upper(),
}

def get_revisor(driver, min_len):
    return len(driver.find_elements_by_xpath("//div[@class='generic-item editor-div img-exists']")) > min_len


options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')

driver = webdriver.Chrome(chrome_options=options)
driver.get(url)
revisors = []

while len(revisors) < 200:
    print("len:", len(revisors))
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    WebDriverWait(driver, 10).until(lambda driver: get_revisor(driver, len(revisors)))
    revisors += driver.find_elements_by_xpath("//div[@class='generic-item editor-div img-exists']")

for revisor in revisors:
    name = revisor.text.split('\n')[0]
    interests = set(revisor
        .text
        .split('Interests: ')[1]
        .upper()
        .replace('\n', ' ')
        .split('; ')
    )
    if c.intersection(interests) != set():
        print({"name": name})