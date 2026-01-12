
"""----------------------------------------------------------------------"""

def open_json():#abrir json
    import json
    with open ("./proyecto_icd.json","r",encoding="utf-8") as file:
        data=json.load(file)
        
        return data

"""----------------------------------------------------------------------"""

def open_json_canasta():#abrir json
    import json
    with open ("./Canasta_Basica.json","r",encoding="utf-8") as file:
        data=json.load(file)
        
        return data
    
"""----------------------------------------------------------------------"""


def mipyme_name(): #nombre de las mipymes analizadas
    data = open_json()
    
    mipymes = data["mipymes"]
    for mipyme in mipymes:
        print(mipyme["store"]["name"])

"""----------------------------------------------------------------------"""

def mipyme_amount():#cantidad de mipymes analizadas
    data = open_json()
    
    mipymes = data["mipymes"]
    return len(mipymes)

"""----------------------------------------------------------------------"""

def name_products():#nombre de los productos analizados
    data = open_json()
    
    empty = []
    mipymes = data["mipymes"]
    
    for mipyme in range(len(mipymes)):
        products_food=mipymes[mipyme]["store"]["products"][0]["groceries"]         
        
        for j in products_food:
            if j not in empty:
                empty.append(j)
        products_bath=mipymes[mipyme]["store"]["products"][0]["hygiene"]
        
        for k in products_bath:  
            if k not in empty:
                empty.append(k)
    return empty    

"""----------------------------------------------------------------------"""

def name_products_amount(): #cantidadde productos por categoria en cada mipyme
    data = open_json()
        
    mipymes = data["mipymes"]    
    for i in range(len(mipymes)):
        products = mipymes[i]["store"]["products"]
        for j in products:
            prod_food=j["groceries"]
        for k,l in prod_food.items():
            print(k,len(l))
        print("--------") 

"""----------------------------------------------------------------------"""

def category_prices():
    data = open_json()

    list_prices = {}
    count_food=0
    count_bath=0

    mipymes = data["mipymes"]
    for mipyme in range(len(mipymes)):
        
        for i in range(len(mipymes[mipyme]["store"]["products"][0])):
            food =mipymes[mipyme]["store"]["products"][0]["groceries"]
            bath=mipymes[mipyme]["store"]["products"][0]["hygiene"]
        
            for j, items in food.items(): 
                if j not in list_prices:
                    list_prices[j]=[] 
                for k in items:
                    count_food+=1
                    if k["price"] not in ["",None]:
                        list_prices[j].append(k["price"])
                            
            
            for j, items in bath.items(): 
                if j not in list_prices:
                    list_prices[j]=[] 
                for k in items:
                    count_bath+=1
                    if k["price"] not in ["",None]:
                        list_prices[j].append(k["price"])
                    
    return list_prices

"""----------------------------------------------------------------------"""

def process_products_food(): #procesar precios de los productos de comida
    data = open_json()
    prices_food= {}
    count_food=0

    mipymes = data["mipymes"]
    for mipyme in range(len(mipymes)):
        
        for i in range(len(mipymes[mipyme]["store"]["products"][0])):
            food =mipymes[mipyme]["store"]["products"][0]["groceries"]
            
            for j, items in food.items(): 
                if j not in prices_food:
                    prices_food[j]=[] 
                
                for k in items:
                    count_food+=1
                    if k["price"] not in ["",None]:
                        prices_food[j].append(k["price"])
                        
    return prices_food

"""----------------------------------------------------------------------"""

def process_products_bath(): #procesar precios de los productos de aseo
    data = open_json()
    prices_bath= {}
    count_bath=0

    mipymes = data["mipymes"]
    for mipyme in range(len(mipymes)):
        
        for i in range(len(mipymes[mipyme]["store"]["products"][0])):
            bath=mipymes[mipyme]["store"]["products"][0]["hygiene"]
        
            for j, items in bath.items(): 
                if j not in prices_bath:
                    prices_bath[j]=[] 
        
                for k in items:
                    count_bath+=1
                    if k["price"] not in ["",None]:
                        prices_bath[j].append(k["price"])
                        
    return prices_bath

"""----------------------------------------------------------------------"""

def dict_average_food():#precio promedio de productos alimenticios
    data = open_json()
    prices = process_products_food()
    av_prices ={}
    products = name_products()

    for k, val in prices.items():
        av_prices[k]=sum(val)//len(val)
        
    return av_prices 
        
"""----------------------------------------------------------------------"""

def dict_average_bath():#precio promedio de productos de aseo
    data = open_json()
    prices = process_products_bath()
    av_prices ={}
    products = name_products()

    for k, val in prices.items():
        av_prices[k]=sum(val)//len(val)
        
    return av_prices 

"""----------------------------------------------------------------------"""

def dict_average_all():#precio promedio pero de todos los productos
    prices_food = process_products_food()
    prices_bath = process_products_bath()
    
    all_prices = {**prices_food, **prices_bath}

    av_prices = {}
    for k, val in all_prices.items():
        av_prices[k] = sum(val) // len(val)
    return av_prices

"""----------------------------------------------------------------------"""

def average(list):#promedio de una lista
    for element in list:
        result= sum(element)/len(list)
        return result
    
"""----------------------------------------------------------------------"""

def available_diapers():
    data = open_json()
    yes = 0
    no = 0
    mipymes = data["mipymes"]

    for mipyme in mipymes:
        bath = mipyme["store"]["products"][0]["hygiene"]["pañales de adulto"]
        disponible = False
        for item in bath:
            if item["price"] is not None:
                disponible = True
                break
                
        if disponible:
            yes += 1
        else:
            no += 1
    return {"tienen":yes,"no tienen":no}
    
"""----------------------------------------------------------------------"""

def percent(a,b): #convertir en porciento
    p=a*100/b
    return p

"""----------------------------------------------------------------------"""


