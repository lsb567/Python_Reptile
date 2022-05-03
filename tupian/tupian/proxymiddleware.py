class ProxyMiddleware(object):
    def process_request(self, request, spider):
        # request.meta['proxy'] = 'http://ip:prot'
        # request.meta['proxy'] = 'http://user:password@ip:prot'
        request.meta['proxy'] = 'http://152.136.62.181:9999'
        # request.meta['proxy'] = 'http://398707160:j8inhg2g@139.224.116.10:16816'
