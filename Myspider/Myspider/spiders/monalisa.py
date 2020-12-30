import scrapy
from Myspider.items import MyspiderItem

class MonalisaSpider(scrapy.Spider):
    name = 'monalisa'
    allowed_domains = ['www.monalisa.com.cn']
    base_url = 'https://www.monalisa.com.cn/productcenter/list.aspx?page={}'
    page = 0
    start_urls = [base_url.format(page)]

    def parse(self, response):

        if self.page == 45:
            return

        rets = response.xpath("/html/body/div[3]/div[6]/div[1]/ul/li")
        for ret in rets:
            item = MyspiderItem()
            #名称
            item['name'] = ret.xpath("./a/p/text()").extract_first()
            #图片链接1
            item['pic_href1'] = "https://www.monalisa.com.cn/" \
                + ret.xpath("./a/figure[1]/@style").extract_first().split("'")[1]
            #图片链接2
            item['pic_href2'] = "https://www.monalisa.com.cn/" \
                + ret.xpath("./a/figure[2]/@style").extract_first().split("'")[1]
            #详情页链接
            item['info_href'] = "https://www.monalisa.com.cn/" \
                + ret.xpath("./a/@href").extract_first()

            yield scrapy.Request(item['info_href']
                                 ,callback = self.parse_info
                                 ,meta = {"item":item}
                                 )

        self.page += 1
        url = self.base_url.format(self.page)
        yield scrapy.Request(url,callback=self.parse)


    def parse_info(self, response):

        item1 = response.meta["item"]

        #详情
        item1['details'] = response.xpath("normalize-space(/html/body/div[3]/div[1]\
                                          /div/div[2]/p/text())").extract_first()
        #产品类别
        item1['product_class'] = response.xpath("normalize-space(/html/body/div[3]\
                                   /div[1]/div/div[2]/div[1]/text()[2])").extract_first()
        #纹理
        item1['grain'] = response.xpath("normalize-space(/html/body/div[3]\
                                   /div[1]/div/div[2]/div[2]/text()[2])").extract_first()
        #主要规格
        item1['norms'] = response.xpath("normalize-space(/html/body/div[3]\
                                   /div[1]/div/div[2]/div[3]/text()[2])").extract_first()
        #釉面工艺
        item1['glaze'] = response.xpath("normalize-space(/html/body/div[3]\
                                   /div[1]/div/div[2]/div[4]/text()[2])").extract_first()
        #使用场景
        item1['scene'] = response.xpath("normalize-space(/html/body/div[3]\
                                   /div[1]/div/div[2]/div[5]/text()[2])").extract_first()
        #发明专利号
        item1['patent'] = response.xpath("normalize-space(/html/body/div[3]\
                                   /div[1]/div/div[2]/div[6]/text()[2])").extract_first()
        #技术成果鉴定
        item1['identify'] = response.xpath("normalize-space(/html/body/div[3]\
                                   /div[1]/div/div[2]/div[7]/text()[2])").extract_first()
        #产品特性
        item1['features'] = response.xpath("normalize-space(/html/body/div[3]\
                                   /div[1]/div/div[2]/div[8]/text()[2] | /html/body/div[3]\
                                       /div[1]/div/div[2]/div[8]/span[2]/text())").extract_first()
        #空间应用特点
        item1['space'] = response.xpath("normalize-space(/html/body/div[3]\
                                   /div[2]/div[1]/article/text()[1] | /html/body/div[3]\
                                       /div[2]/div[1]/article/p/text())").extract_first()

        yield item1

