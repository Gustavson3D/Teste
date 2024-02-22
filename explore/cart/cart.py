class Cart():
    def __init__ (self, request):
        self.session = request.session

        # pegar a key da sessão casso a sessão exista
        cart = self.session.get('session_key')

        # se o usuário for novo, sem key, crie uma sessão
        if "session_key" not in request.session:
            cart = self.session['session_key'] = {}

        self.cart = cart


    def add(self, product):

        product_id = product.id

        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'Nome': product.nome_local}
        
        self.session.modified = True


    def __len__(self):
        return len(self.cart)