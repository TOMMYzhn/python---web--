import faker


class UserAgentMiddleware(object):
    def __init__(self,settings):
        self.faker = faker.Faker()

    @classmethod
    def from_crawler(cls,crawler):
        return cls(crawler.settings)

    def process_request(self,request,spider):
        request.headers['User-Agent'] = self.faker.user_agent()
