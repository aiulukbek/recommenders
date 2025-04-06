# conversion rate calculator 
from typing import List 

class VisitorCR: 
    """
        The class is responsible for Conversion rate calculation 
    """
    def __init__(self, visitors : List[int], addtocart : List[int], purchase : List[int]): 
        """ 
            Params: 
                :param visitors - visitors 
                :param addtocart - visitors with add to cart event 
                :param purchase - visitors with purchase events 
        """
        self.visitors = visitors 
        self.addtocart = addtocart 
        self.purchase = purchase 

    def visitors_to_addtocart(self): 
        """
            Intersection between view visitors and addtocart visitors 
            Returns: 
                intersection of visitors with view events and addtocart visitors 
        """
        return len(set(self.visitors) & set(self.addtocart))
    
    def addtocart_to_purchased(self): 
        """
            Intersection between addtocart visitors and purchase visitors 
        """
        return len(set(self.addtocart) & set(self.purchase))
    
    def visitors_only(self): 
        """
            Calculates neveractives 
        """
        return len(set(self.visitors) - set(self.addtocart) - set(self.purchase))
    
    def addtocart_only(self): 
        """
            Calculates cart abondened visitors 
        """
        return len(set(self.addtocart) - set(self.purchase))
    
    def purchased_only(self): 
        """
            Calculates purchase only customers 
        """
        return len(set(self.purchase) - set(self.addtocart))   
    
    def visitors_to_purchase(self): 
        """
            Intersection between visitors and purchase customers 
        """
        return len(set(self.visitors) & set(self.purchase))
    
    def cr_visitors_to_addtocart(self): 
        """
            Conversion rate in terms of addtocart and visitors 
        """
        view_addtocart = self.visitors_to_addtocart() 
        return view_addtocart / len(self.visitors)
    
    def cr_visitors_to_purchase(self): 
        """
            Conversion rate in terms of views and purchase 
        """
        view_purchase = self.visitors_to_purchase() 
        return view_purchase / len(self.visitors)

    def cr_addtocart_to_purchase(self): 
        """
            Conversion rate in terms of addtocart and purchase 
        """
        addtocart_purchase = self.addtocart_to_purchased()
        return addtocart_purchase / len(self.addtocart)
    
