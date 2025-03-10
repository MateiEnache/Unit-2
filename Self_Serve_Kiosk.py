"""
Name:Matei Enache
Date: 3/10/2025
Description: cash_register.py
"""

class CashRegister:
    """Models a cash register
    """
    def __init__(self, item_name:str, item_price:float,items:dict):
        """creates an item

        Args:
            item_name (str): names the item
            item_price (float): gives the item a price
        """
        self.item_name = item_name
        self.item_price = item_price
        
    
    def getTotal(self, transaction_total:float, total_items:int):
        """findsthe total amunt to pay and how many items there are

        Args:
            transaction_total (float): how much money is owed
            total_items (int): how many items the person wants
        """
        
        total_items = 0