"""This file should have our order classes in it."""



class AbstractMelonOrder(object):
    """ We assume a domestic order unless specified """

    def __init__(self, species, qty, tax, order_type, country_code):
        """ Creation of a initialization method that sets parameters to attributes """
        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax
        self.country_code = country_code

    def get_total(self, surge_multiplier = 1, shipping_flat_fee = 0):
        """Calculate price."""

        base_price = 5 
        price = base_price * holiday_multiplier
        total = (1 + self.tax) * self.qty * price + shipping_flat_fee
        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True


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

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def get_total(self):
        return super(InternationalMelonOrder, self).get_total(shipping_flat_fee = 3)


class GovernmentMelonOrder(DomesticMelonOrder):
    
    tax = 0

    def __init__(self, species, qty):
        self.passed_inspection = False
        super(GovernmentMelonOrder, self).__init__(species, qty, tax = self.tax )

    def mark_inspection(self, passed):
        self.passed_inspection = True
