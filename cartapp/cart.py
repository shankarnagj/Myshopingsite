from decimal import Decimal
from typing_extensions import Required
from django.conf import settings
from myshop.models import Product

class Cart(object):
    def __init__(self):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart :
            cart = self.session[settings.CART_SESSION_ID] = {}
        
        self.cart = cart
        