from selenium import webdriver
driver=webdriver.Firefox()
path='http://www.imitam.co.il/campus/%D7%A9%D7%99%D7%A2%D7%95%D7%A8-5/'
NPage=116
lec=5

driver.get(path)


#yuliavraham@gmail.com
#a371995


NPage=59
lec=18
for i in range(NPage):
    st='lect'+str(lec)+'_page_'+str(i+1)
    print(st)
    driver.save_screenshot(st+'.png')
    driver.find_element_by_class_name("pdfemb-next").click() # click the NEXT BUTTON





# this code crop images, need to make sure it will not destroy others.
# and interate over each folder and save in a similar folder
from PIL import Image
x=Image.open('C:\\Users\\errorValue\\PycharmProjects\\untitled\\Lect1\\lect1_page_2.png')
x.show()

area=(310,0,1580,930)
new=x.crop(area)
new.show()
new.save('ssss.png')














driver.find_element_by_class_name("ppdfemb-inner-div pdfemb-page2")

driver.find_elements_by_xpath('/html/body/div[1]/div/div/div/section').screenshot("sss.png")




driver.find_element_by_xpath('/html/body/div[1]/div/div/div/section/article/div/div/div/section/div/div/div/div/div/div/div/div/p[1]/div').screenshot_as_png("tmp1.png")


xpath1='/html/body/div[1]/div/div/div/section/article/div/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/p[1]/div/div[2]/div[1]'




driver.find_element_by_class_name("ppdfemb-inner-div pdfemb-page3")
driver.find_element_by_xpath("/html/body/div[1]/div/div/div/section/article/div/div/div/section/div/div/div/div/div/div/div/div/p[1]/div/div[2]/div[2]/canvas").screenshot("sas")

driver.find_element_by_xpath('/html/body/div[1]/div/div/div/section/article/div/div/div/section/div/div/div/div/div/div/div/div/p[1]/div/div[2]/div[2]')

import numpy as np
from selenium import webdriver
keys = webdriver.common.keys.Keys

def open_game():
    driver = webdriver.Firefox()
    driver.get(r'http://www.freeminesweeper.org/minecore.html')
    return driver

def set_to_expert(driver):
    driver.find_element_by_xpath(r'/html/body/table/tbody/tr/td[2]/a').click()
    driver.find_element_by_xpath(r'/html/body/div[1]/table/tbody/tr/td/a[4]').click()

def get_game_grid(driver,xlim=31,ylim=16):
    game_grid =
driver.find_element_by_xpath(r'/html/body/div[5]/table/tbody/tr/td')
    return np.array([a for a in
game_grid.find_elements_by_tag_name('a') if a.get_attribute('onclick')
== '']).reshape(xlim,ylim)

def snap_grid(driver,filename):
    driver.find_element_by_xpath(r'/html/body/div[5]/table/tbody/tr/td').screenshot(filename=filename)

def click_cell(x,y):
    cells = get_game_grid(driver)
    cells[x,y].click()

def mark_cell(x,y,driver):
    driver.execute_script(f'cellClick({x},{y})')

def get_first_click_statistics(driver,n_samples):
    driver.switch_to.active_element.send_keys(keys.F2)
    snap_grid(driver,'screenshot_data/initial.png')

    for i,cell in enumerate(get_game_grid(driver)):
        for sample in range(n_samples):
            cell.click()
            snap_grid(driver,f'screenshot_data/{i}_{sample}.png')
            driver.switch_to.active_element.send_keys(keys.F2)

def main():
    driver = open_game()
    set_to_expert(driver)
    n_samples = 100
    #mark_cell(0,0,driver)
    #get_first_click_statistics(driver,n_samples)

if __name__ == '__main__':
    main()
