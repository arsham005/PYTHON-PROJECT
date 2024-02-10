import requests
import bs4


#1st PROJECT: Extracting data from Filmnet site

req = requests.get("https://tv.filmnet.ir/")
text = req.text
bs = bs4.BeautifulSoup(text,"html.parser")
find = bs.find_all("h4",attrs={"class":"css-stgv2v eg0dt7k0"})
for i in find:
    print(i.text)

#2nd PROJECT: Extracting the prices of cars from Karnameh website

req2 = requests.get("https://karnameh.com/car-price")
text2 = req2.text
bs2 = bs4.BeautifulSoup(text2,"html.parser")
find2 = bs2.find_all("p",attrs={"class":"MuiTypography-root MuiTypography-body1 muirtl-iy5bpq"})
find22 = bs2.find_all("p",attrs={"class":"MuiTypography-root MuiTypography-body1 muirtl-22intj"})
dict = {}
for i,j in zip(find2,find22):
    dict[j.text] = i.text

print(dict)

#3rd PROJECT: The best Tehran's resturant in takhfifan site

req3 = requests.get("https://takhfifan.com/tehran/restaurants-cafes")
text3 = req3.text
bs3 = bs4.BeautifulSoup(text3,"html.parser")
find3 = bs3.find_all("p",attrs={"class":"vendor-card-box__title-text"})
find33 = bs3.find_all("p",attrs={"class":"rate-badge__rate-value"})
resturant = []
score = []
for i,j in zip(find3,find33):
    resturant.append(i.text)
    score.append(float(j.text))
x = max(score)
print(f"{resturant[score.index(x)]} <{x}>")
