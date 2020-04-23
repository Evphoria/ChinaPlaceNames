import requests
s = requests.session()
# s.proxies = {"https": "https://171.35.169.104:9999", "http": "http://171.12.113.232:9999", }
s.keep_alive = False # 关闭多余连接


from urllib import request
from bs4 import BeautifulSoup
import time

hw=open("1600017460_StatData.txt","w")


url = "http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2019/index.html"
web = s.get(url)
web.encoding = 'gb2312'
soup = BeautifulSoup(web.text, 'html.parser')
soup



provincels = []
for pv in soup.find_all("a")[:-1]:
    pvline = []
    pvline.append(pv.get_text())
    pvline.append(pv.attrs['href'])
    provincels.append(pvline)


# first loop
for province in provincels[6:]:
    url1= "http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2019/" + province[1]
    print(province[1][:2]+'0000000000'+province[0],file=hw)
    success = False
    attempts = 0
    while attempts<10 and not success:
        try:
            time.sleep(0.001)
            web = s.get(url1,timeout=1)
            web.encoding = 'gb2312'
            soup = BeautifulSoup(web.text, 'html.parser')
            success = True
            # get city list
            cityls = []
            for ct in soup.find_all("a")[:-1]:
                ctline = []
                ctline.append(ct.get_text())
                href = ct.attrs['href']
                ctline.append(href)
                cityls.append(ctline)
            ctnum = int(len(cityls)/2)

            # second loop
            for ct in range(ctnum):
                print('\t'+cityls[ct*2][0]+cityls[ct*2+1][0],file=hw)
                url2= "http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2019/"+cityls[ct*2][1]
                success2 = False
                attempts2 = 0
                while attempts2<10 and not success2:
                    try:
                        time.sleep(0.001)
                        web = s.get(url2,timeout=1)
                        web.encoding = 'gb2312'
                        soup = BeautifulSoup(web.text, 'html.parser')
                        success2 = True
                        # get county list
                        countyls = []
                        for cy in soup.find_all("a")[:-1]:
                            cyline = []
                            cyline.append(cy.get_text())
                            href = cy.attrs['href']
                            cyline.append(href)
                            countyls.append(cyline)
                        cynum = int(len(countyls)/2)

                        # third loop
                        for cy in range(cynum):
                            print('\t\t'+countyls[cy*2][0]+countyls[cy*2+1][0],file=hw)
                            url3 = "http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2019/"+province[1][:2]+'/'+countyls[cy*2][1]

                            success3 = False
                            attempts3 = 0
                            while attempts3<10 and not success3:
                                try:
                                    time.sleep(0.001)
                                    web = s.get(url3,timeout=1)
                                    web.encoding = 'gb2312'
                                    soup = BeautifulSoup(web.text, 'html.parser')
                                    success3 = True

                                    # get town list
                                    townlist = []
                                    for tn in soup.find_all("a")[:-1]:
                                        tnline = []
                                        tnline.append(tn.get_text())
                                        href = tn.attrs['href']
                                        tnline.append(href)
                                        townlist.append(tnline)
                                    tnnum = int(len(townlist)/2)

                                    # forth loop
                                    for tn in range(tnnum):
                                        print('\t\t\t'+townlist[tn*2][0]+townlist[tn*2+1][0],file=hw)
                                        url4 = "http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2019/"+province[1][:2]+'/'+countyls[cy*2][1][:2]+'/'+townlist[tn*2][1]

                                        success4 = False
                                        attempts4 = 0
                                        while attempts4<10 and not success4:
                                            try:
                                                time.sleep(0.001)
                                                web = s.get(url4,timeout=1)
                                                web.encoding = 'gb2312'
                                                soup = BeautifulSoup(web.text, 'html.parser')
                                                success4 = True


                                                # get village list
                                                vlgls = []
                                                vlgnum = int(len(soup.select('tr[class="villagetr"] > td'))/3)
                                                for i in range(vlgnum):
                                                    vlgno = soup.select('tr[class="villagetr"] > td')[3*i].get_text()
                                                    vlgattr = soup.select('tr[class="villagetr"] > td')[3*i+1].get_text()
                                                    vlgname = soup.select('tr[class="villagetr"] > td')[3*i+2].get_text()
                                                    vlgline = [vlgno,vlgname,vlgattr]
                                                    vlgls.append(vlgline)


                                                for vlg in vlgls:
                                                    print('\t\t\t\t'+vlg[0]+vlg[1]+vlg[2],file=hw)
                                            except:
                                                attempts4 =+1
                                except:
                                    attempts3 =+3
                    except:
                        attempts2 += 1
        except:
            attempts =+ 1


hw.close()
