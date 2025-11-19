def mipyme_name():
    import json
    with open ("./proyecto_icd.json","r",encoding="utf-8") as file:
        data=json.load(file)
    
        mipymes = data["mipymes"]
        for i in mipymes:
            return i["store"]["name"]  
        
        
def mipyme_amount():
    import json
    with open ("./proyecto_icd.json","r",encoding="utf-8") as file:
        data=json.load(file)
    
        mipymes = data["mipymes"]
        return len(mipymes)
    
    

def name_products():
    import json
    with open ("./proyecto_icd.json","r",encoding="utf-8") as file:
        datos=json.load(file)
    
        empty = []
        mipymes = datos["mipymes"]
        for i in range(len(mipymes)):
            all_products= mipymes[i]["store"]["products"]
            for j in range(len(all_products)):
                if all_products[j]["name"] not in empty:            
                    empty.append(all_products[j]["name"]) 
                    return", ".join(empty) 


def name_products_amount():
    import json
    with open ("./proyecto_icd.json","r",encoding="utf-8") as file:
        data=json.load(file)
    
        mipymes = data["mipymes"]
        for i in mipymes:
            prod_amount = len(i["store"]["products"])
            return i["store"]["name"], prod_amount
        

        
def average_prices():#son todos los productos sin categorizar
    import json
    with open("./proyecto_icd.json","r", encoding = "utf-8") as file:
        data = json.load(file)
    
        list_prices = []
        mipymes = data["mipymes"]
        for i in range(len(mipymes)):
            for j in range(len(mipymes[i]["store"]["products"])):
                if mipymes[i]["store"]["products"][j]["price"] not in list_prices:                
                    list_prices.append(mipymes[i]["store"]["products"][j]["price"])
                    
                average = sum(list_prices)/len(list_prices)
        return average