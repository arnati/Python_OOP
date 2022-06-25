class Handler:
    def __init__(self, methods):
        self.methods = methods

    def __call__(self, func):
        def wrapper(request, *args, **kwargs):
            req = request.get('method', 'GET')

            if req == 'GET' and req in self.methods:
                return self.get(func, self.methods)
            elif req == 'POST' and req in self.methods:
                return self.post(func, self.methods)
            else:
                return None

        return wrapper

    def get(self, func, request, *args, **kwargs):
        return f"GET: {func(request)}"

    def post(self, func, request, *args, **kwargs):
        return f"POST: {func(request)}"


@Handler(methods=('GET', "POST"))  # по умолчанию methods = ('GET',)
def contact(request):
    return "Сергей Балакирев"


res = contact({"method": "POST", "url": "contact.html"})

print(res)