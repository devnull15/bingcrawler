import scrapy
import time

class DmozSpider(scrapy.Spider):        
        name = "bingcrawler"
        allowed_domains = ["bing.com"]

        # Static URLs, "FORM=" included
        start_urls = [
            "https://www.bing.com/news/search?q=Top%20Stories&FORM=NSBABR",
            "https://www.bing.com/news?q=us+news&FORM=NSBABR",
            "https://www.bing.com/news?q=Northeast+US+News&FORM=NSBABR",
            "https://www.bing.com/news?q=South+US+News&FORM=NSBABR",
            "https://www.bing.com/news?q=Midwest+US+News&FORM=NSBABR",
            "https://www.bing.com/news?q=West+US+News&FORM=NSBABR",
            "https://www.bing.com/news?q=world+news&FORM=NSBABR",
            "https://www.bing.com/news?q=Africa+News&FORM=NSBABR",
            "https://www.bing.com/news?q=Americas+News&FORM=NSBABR",
            "https://www.bing.com/news?q=Asia+Pacific+News&FORM=NSBABR",
            "https://www.bing.com/news?q=Europe+News&FORM=NSBABR",
            "https://www.bing.com/news?q=Middle+East+News&FORM=NSBABR",
            "https://www.bing.com/news?q=local+news&FORM=NSBABR",
            "https://www.bing.com/news?q=entertainment+news&FORM=NSBABR",
            "https://www.bing.com/news?q=Movie+%26+TV+News&FORM=NSBABR",
            "https://www.bing.com/news?q=Music+News&FORM=NSBABR",
            "https://www.bing.com/news/search?q=Sci/Tech&FORM=NSBABR",
            "https://www.bing.com/news?q=Technology+News&FORM=NSBABR",
            "https://www.bing.com/news?q=Science+News&FORM=NSBABR",
            "https://www.bing.com/news?q=business+news&FORM=NSBABR",
            "https://www.bing.com/news?q=political+news&FORM=NSBABR",
            "https://www.bing.com/news?q=sports+news&FORM=NSBABR",
            "https://www.bing.com/news?q=NFL+News&FORM=NSBABR",
            "https://www.bing.com/news?q=CFB+News&FORM=NSBABR",
            "https://www.bing.com/news?q=MLB+News&FORM=NSBABR",
            "https://www.bing.com/news?q=NBA+News&FORM=NSBABR",
            "https://www.bing.com/news?q=NHL+News&FORM=NSBABR",
            "https://www.bing.com/news?q=Soccer+News&FORM=NSBABR",
            "https://www.bing.com/news?q=CBB+News&FORM=NSBABR",
            "https://www.bing.com/news?q=Golf+News&FORM=NSBABR",
            "https://www.bing.com/news?q=Tennis+News&FORM=NSBABR",
            "https://www.bing.com/news?q=health+news&FORM=NSBABR",
        "https://www.bing.com/news?q=products+news&FORM=NSBABR",
                "https://www.bing.com/thiscantberight"
        ]

        
        def parse(self, response):
                ## AUTH ##
                
                        

                ## Custom logging--doesn't work
                #filename = time.strftime("%Y-%m-%d_%H:%M") + ".log"
                #with open('/home/mischief/working/bingcrawler/bingcrawler/logs/bingcrawler.log', 'ab') as f:
                        #f.write('test\n')
