"""This file should have our order classes in it."""
from random import randint 

class TooManyMelons(ValueError):
    ''' '''

    def __init__(self):
        super(TooManyMelons,self).__init__()

    def __str__(self):
        return "Too many melons!"

class AbstractMelonOrder(object):
    """ We assume a domestic order unless specified """

    def __init__(self, species, qty, tax, order_type, country_code):
        """ Creation of a initialization method that sets parameters to attributes """
        self.species = species
        try:
            if qty <100:
                self.qty = qty
            else:
                raise TooManyMelons()
        except TooManyMelons as e:
            print e

        self.shipped = False
        self.order_type = order_type
        self.tax = tax
        self.country_code = country_code
        self.base_price = 0

    def get_total(self, holiday_multiplier = 1, shipping_flat_fee = 0):
        """Calculate price."""

        self.get_base_price()
        price = self.base_price * holiday_multiplier
        total = (1 + self.tax) * self.qty * price + shipping_flat_fee
        return total


    def get_country_code(self):
        """Return the country code."""

        return self.country_code


    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True

    def get_base_price(self):
        """ Checks to see if base price has been set.
            If not, base price is a random val n/w 5-9 (splurge pricing) """
        if self.base_price == 0:
            # self.base_value instance attribute 
            # (initialized in __init__) is rebound.
            self.base_price = randint(5,9)


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    def __init__(self, species, qty, tax = 0.08):

        super(DomesticMelonOrder, self).__init__(species, qty, tax, "domestic", "USA" )

    def get_total(self):
        return super(DomesticMelonOrder, self).get_total(holiday_multiplier = 1.5)



class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    tax = 0.17

    def __init__(self, species, qty, country_code):
        super(InternationalMelonOrder, self).__init__(species, qty, self.tax, "international", country_code)


    def get_total(self):
        shipping_fee = 0
        if self.qty < 10 :
            shipping_fee = 3
        return super(InternationalMelonOrder, self).get_total(
            shipping_flat_fee = shipping_fee)


class GovernmentMelonOrder(DomesticMelonOrder):
    """A domestic (in the US) melon order for the government."""
    
    tax = 0

    def __init__(self, species, qty):
        self.passed_inspection = False
        super(GovernmentMelonOrder, self).__init__(species, qty, tax = self.tax )

    def mark_inspection(self, passed):
        """ updates the status of the melon's passed_inspection
            passing status. passed is a boolean """
        self.passed_inspection = passed
