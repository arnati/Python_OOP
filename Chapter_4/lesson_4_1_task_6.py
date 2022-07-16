class GenericView:
    def __init__(self, methods=('GET',)):
        self.methods = methods

    def get(self, request):
        return ""

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass


class DetailView(GenericView):
    def __init__(self, methods=('GET',)):
        super().__init__(methods)

    def render_request(self, request, method):
        self.check_request(method)
        link_method = getattr(self, method.lower())
        return link_method(request)

    def check_request(self, method):
        if method not in self.methods:
            raise TypeError('данный запрос не может быть выполнен')

    def get(self, request):
        if not isinstance(request, dict):
            raise TypeError('request не является словарем')
        else:
            if 'url' not in request.keys():
                raise TypeError('request не содержит обязательного ключа url')

        return f"url: {request['url']}"


dv = DetailView()
html = dv.render_request({'url': 'https://site.ru/home'}, 'GET')  # url: https://site.ru/home
print(html)