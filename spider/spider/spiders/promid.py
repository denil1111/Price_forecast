import base64
  
# Start your middleware class
class ProxyMiddleware(object):
    # overwrite process request
    def process_request(self, request, spider):
        # Set the location of the proxy
        request.meta['proxy'] = "121.57.232.56:4000"
