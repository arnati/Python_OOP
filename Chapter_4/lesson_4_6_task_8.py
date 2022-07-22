class RetriveMixin:
    def get(self, request):
        return "GET: " + request.get('url')


class CreateMixin:
    def post(self, request):
        return "POST: " + request.get('url')


class UpdateMixin:
    def put(self, request):
        return "PUT: " + request.get('url')


class GeneralView:
    allowed_methods = ('GET', 'POST', 'PUT', 'DELETE')

    def render_request(self, request):
        self.check_value(request)
        method_request = getattr(self, request.get('method').lower())
        return method_request(request)

    @classmethod
    def check_value(cls, request):
        if "url" not in request or "method" not in request or request["method"] not in cls.allowed_methods:
            raise TypeError(f"Метод {request.get('method')} не разрешен.")


class DetailView(RetriveMixin, UpdateMixin, GeneralView):
    allowed_methods = ('GET', 'POST',)


view = DetailView()
# html = view.render_request({'url': 'https://stepik.org/course/116336/', 'method': 'GET'})
html = view.render_request({'url': 'https://stepik.org/course/116336/', 'method': 'POST'})
print(html)  # GET: https://stepik.org/course/116336/
