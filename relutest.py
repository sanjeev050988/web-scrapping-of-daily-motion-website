! pip install selenium
! pip install webdriver_manager

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from collections import Counter


options = Options()
options.add_argument('--headless') 
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')


driver = webdriver.Chrome(options=options)


url = input()


driver.get(url)


time.sleep(3)


video_urls = []


count = 0


while count < 500:
    
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  

    
    videos = driver.find_elements(By.XPATH, "//a[contains(@href, '/video/')]")

    
    for video in videos:
        href = video.get_attribute('href')
        if 'video/' in href:
            video_urls.append(href)
            count += 1
            if count >= 500:
                break


driver.quit()




video_ids = [url.split('/video/')[1] for url in video_urls]


all_video_ids = ''.join(video_ids)


character_counts = Counter(all_video_ids)


print("\nCharacter counts:")
for character, count in character_counts.items():
    print(f"Character: {character}, Count: {count}")


most_common_character, most_common_count = min(character_counts.items(), key=lambda x: (-x[1], x[0]))

print(f"\n{most_common_character}:{most_common_count}")