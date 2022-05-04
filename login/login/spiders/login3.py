# 实现不了,理解过程即可
import scrapy
import re


class Login3Spider(scrapy.Spider):
    name = 'login3'
    allowed_domains = ['dun.163.com']
    start_urls = ['http://passport.ganji.com/login.php']

    def parse(self, response):
        hash_code = re.findall(r'', response.text)[0]
        # 验证码的情况
        img_url = response.xpath('查询img的url的xpath').extract_first()
        yield scrapy.Request(img_url, callback=self.parse_info, meta={'hash_code': hash_code})

    def parse_info(self, response):
        hash_code = response.request.meta['hash_code']
        with open('yzm.jpg', 'wb') as f:
            f.write(response.body)

        code = input("请输入验证码：")  # 看一眼下载下来的验证码图片即可
        form_data = {  # 绘制表单  表单里的内容视情况而定
            'username': '13',
            'password': '23r',
            'setcookie': '0',
            'checkCode': code,
            'next': "/",
            'source': 'passport',
            '__hash__': hash_code
        }
        login_url = '登录网址'
        yield scrapy.FormRequest(login_url, callback=self.after_login, formdata=form_data)

    def after_login(self, response):
        print(response.text)
