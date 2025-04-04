from typing import List 

class VisitorCR: 
    def __init__(self, visitors : List[int], addtocart : List[int], purchase : List[int]): 
        self.visitors = visitors 
        self.addtocart = addtocart 
        self.purchase = purchase 

    def visitors_to_addtocart(self): 
        return len(set(self.visitors) & set(self.addtocart))
    
    def addtocart_to_purchased(self): 
        return len(set(self.addtocart) & set(self.purchase))
    
    def visitors_only(self): 
        return len(set(self.visitors) - set(self.addtocart) - set(self.purchase))
    
    def addtocart_only(self): 
        return len(set(self.visitors) - set(self.purchase))
    
    def purchased_only(self): 
        return len(set(self.purchase) - set(self.addtocart))   
    
    def visitors_to_purchase(self): 
        return len(set(self.visitors) & set(self.purchase))
    
    def cr_visitors_to_addtocart(self): 
        view_addtocart = self.visitors_to_addtocart() 
        return view_addtocart / len(self.visitors)
    
    def cr_visitors_to_purchase(self): 
        view_purchase = self.visitors_to_purchase() 
        return view_purchase / len(self.visitors)

    def cr_addtocart_to_purchase(self): 
        addtocart_purchase = self.addtocart_to_purchased()
        return addtocart_purchase / len(self.addtocart)
    
