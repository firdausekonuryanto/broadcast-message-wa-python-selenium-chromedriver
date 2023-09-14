import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def kirim(phone, pesan):
    try:
        driver = webdriver.Chrome()
        driver.get("https://web.whatsapp.com/")
        
        time.sleep(30)
        
        for number in phone:
            element_xpath = '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p'
            element = driver.find_element("xpath", element_xpath)
            text_to_type = number
            element.send_keys(text_to_type)
            element.send_keys(Keys.RETURN)

            element_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'
            element = driver.find_element("xpath", element_xpath)
            text_to_type = pesan
            element.send_keys(text_to_type)
            element.send_keys(Keys.RETURN)
            
            time.sleep(5)
    except Exception as e:
        print(f"Terjadi kesalahan: {str(e)}")
    finally:
        input("Tekan Enter untuk menutup WebDriver...")
        driver.quit()

if __name__ == "__main__":
    phone = ["+6285733796196", "+6285338321400"]
    pesan = "halo selamat datang di akatech ..."

    kirim(phone, pesan)
