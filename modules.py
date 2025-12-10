def mipyme_name(): #nombre de todas las mipymes
    import json
    with open ("./proyecto_icd.json","r",encoding="utf-8") as file:
        data=json.load(file)
    
        mipymes = data["mipymes"]
        for i in mipymes:
            print(i["store"]["name"])

mipyme_name()

def mipyme_amount(): #cantidad de mipymes
    import json
    with open ("./proyecto_icd.json","r",encoding="utf-8") as file:
        data=json.load(file)
    
        mipymes = data["mipymes"]
        return len(mipymes)
    
print(mipyme_amount())


def name_products(): #nombre de productos analizados 
    import json
    with open ("./proyecto_icd.json","r",encoding="utf-8") as file:
        datos=json.load(file)
    
        empty = []
        mipymes = datos["mipymes"]
        for i in range(len(mipymes)):
            products_food=mipymes[i]["store"]["products"][0]["groceries"]         
            for j in products_food:
                if j not in empty:
                    empty.append(j)
            products_bath=mipymes[i]["store"]["products"][0]["hygiene"]
            for k in products_bath:  
                if k not in empty:
                    empty.append(k)
    print(empty)
    
name_products()

def name_products_amount(): #nombre del producto y cantidad del mismo en una mipyme
    import json
    with open ("./proyecto_icd.json","r",encoding="utf-8") as file:
        data=json.load(file)
        
        mipymes = data["mipymes"]    
        for i in range(len(mipymes)):
            products = mipymes[i]["store"]["products"]
            for j in products:
                prod_food=j["groceries"]
            for k,l in prod_food.items():
                print(k,len(l))
            print("--------") 
            
name_products_amount()