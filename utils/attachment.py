import allure
import json
class Attach:
    """Для прикрепления отладки в формате json"""
    def __init__(self,**kwargs) -> None:
        self.attachment={}
        self.add(**kwargs)    
          
    def add(self,**kwargs)  -> None:
        for arg in kwargs:
            self.attachment[arg]=kwargs[arg]

    def attach(self)-> None:
        allure.attach(json.dumps(self.attachment), 'Attach Json', allure.attachment_type.JSON)