import xlrd
from selenium import webdriver

wb = xlrd.open_workbook("官网tdk3.xlsx")
table_name = '官网【会计学院】旗下主要栏目页的TDK'

sh = wb.sheet_by_name(table_name)#打开表格
urls = sh.col_values(5, 1, None)#读取表格第五列

print(urls)
print(type(urls))

for i in urls:#用一个for循环遍历所有的链接，用webdriver打开
    print(i)
    driver = webdriver.Chrome()
    driver.get(i)
    title = driver.title
    keyword = driver.find_elements_by_xpath("/html/head/meta[5]")
    print(keyword.__getattribute__("content"))