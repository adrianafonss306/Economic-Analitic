import matplotlib.pyplot as plt
from modules import*

"""----------------------------------------------------------------------"""

def Chart_Elder_Population():
    
    years = [1907, 1919, 1931, 1943, 1953, 1970, 1981, 2002, 2012, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
    elder_population = [95084, 138645, 197074, 266304, 402306, 263724, 1054998, 1639262, 2041392, 2140738, 2176657, 2219784, 2251930, 2286948, 2328344, 2386280, 2379887, 2427603, 2452489]
    
    plt.plot(
        years,elder_population,
        color = "darkblue",
        linewidth = 3,
        marker = "*",
        markersize = 10)
    plt.title(
        "Poblacion de adultos mayores en Cuba",
        fontsize = 14)
    plt.xlabel("Años",
        fontsize = 12)
    plt.ylabel("Cantidad de personas (millones)",
        fontsize = 12)
    plt.grid(True)

    plt.show()

        
"""----------------------------------------------------------------------"""
def Chart_Live_Births():
    
    years = [2019, 2020, 2021, 2022, 2023, 2024]
    births = [109716, 105038, 99096, 95403, 90392, 71358]
    
    plt.plot(years, births, 'o-', color='yellow')
    plt.title('Nacidos Vivos (2019-2024)')
    plt.xlabel('Año')
    plt.ylabel('Número de nacidos')
    plt.grid(True)
    for x, y in zip(years, births):
        plt.text(x, y, f'{y:,}', ha='center', va='bottom')
    
    plt.show()
    
"""----------------------------------------------------------------------"""

def Chart_Birth_Rate(): #tasa de natalidad (no)
        
    years = [2019, 2020, 2021, 2022, 2023, 2024]
    rate = [9.8, 9.4, 9.0, 9.0, 8.8, 7.2]
            
    plt.plot(years, rate, 's-', color='red')
    plt.title('Tasa de Natalidad (2019-2024)')
    plt.xlabel('Año')
    plt.ylabel('Tasa (%)')
    plt.grid(True)
    for x, y in zip(years, rate):
        plt.text(x, y, f'{y}%', ha='center', va='bottom')
    plt.show()

"""----------------------------------------------------------------------"""    
    
def Chart_Aging_Rate():
    
    years = [1907, 1919, 1931, 1943, 1953, 1970, 1981, 2002, 2012, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
    aging_rate = [4.6, 4.8, 5.0, 5.6, 6.9, 9.0, 10.8, 14.7, 18.3, 19.0, 19.4, 19.8, 20.1, 20.4, 20.8, 21.3, 21.9, 23.3, 24.4]
    
    plt.plot(
    years,aging_rate,
    color = "darkred",
    linewidth = 3,
    marker = "*",
    markersize = 10)
    plt.title(
        "Grado de Envejecimiento Poblacional",
        fontsize = 14)
    plt.xlabel("Años",
        fontsize = 12)
    plt.ylabel("Tasa de Envejecimiento (%)",
        fontsize = 12)
    plt.grid(True)

    plt.show()
        
"""----------------------------------------------------------------------"""

def Chart_Analiced_Products():
    
    products = list(dict_average_food().keys()) + list(dict_average_bath().keys())
    prices = list(dict_average_food().values()) + list(dict_average_bath().values())

    plt.figure(figsize=(12, 6))
    bars = plt.bar(products, prices)
    plt.bar_label(bars, labels=[f"{p:.0f}" for p in prices], padding=3)
    plt.title("Productos Analizados")
    plt.ylabel("Precio Promedio (CUP)")
    plt.xticks(rotation=40, ha='right')
    plt.grid(axis='y', linestyle='-', alpha=0.5)

    plt.tight_layout()
    plt.show()  
    
    
"""----------------------------------------------------------------------"""

def Chart_Average_VS_Salary():
    
    products = list(dict_average_food().keys()) + list(dict_average_bath().keys())
    prices = list(dict_average_food().values()) + list(dict_average_bath().values())

    salario_minimo = 3056
    salario_medio = 3528
    salario_nuevo_tope = 4000

    plt.figure(figsize=(10, 6))

    plt.barh(products, prices, color='lightcoral')

    plt.axvline(x=salario_minimo, color='red', linestyle='--', label=f'Mínimo: {salario_minimo}')
    plt.axvline(x=salario_medio, color='blue', linestyle='--', label=f'Medio: {salario_medio}')
    plt.axvline(x=salario_nuevo_tope, color='green', linestyle='--', label=f'Máximo: {salario_nuevo_tope}')
    plt.grid(axis="x",alpha = 0.3)

    plt.xlabel('Precio (pesos)')
    plt.title('Precios vs Pensiones')

    plt.legend()
    plt.show()

"""----------------------------------------------------------------------"""

def Chart_Diaper_Availability():
    labels = ['Tienen', 'No tienen']
    counts = [6, 20]  
    total = 30
    percentages = [(x / total) * 100 for x in counts]
    plt.figure(figsize=(6,6))

    plt.pie(percentages, labels=labels,
            colors=["green","red"], autopct='%1.1f%%')

    plt.title('Disponibilidad de pañales de adulto en Mipymes')
    plt.show()

"""----------------------------------------------------------------------"""

def Chart_Max_Salary_VS_Basket():
    price_basic = price_basic_basket()
    price_aditional = price_aditional_basket()

    salario_max_antes = 2650
    salario_max_despues = 4000

    categorias = ["Canasta básica", "Canasta adicional"]
    valores = [price_basic, price_aditional]

    plt.figure(figsize=(8,6))

    plt.bar(categorias, valores, color=["skyblue", "lightgreen"])
    plt.axhline(y=salario_max_antes, color="tomato", linestyle="--", linewidth=2, label="Salario máximo antes")
    plt.axhline(y=salario_max_despues, color="seagreen", linestyle="--", linewidth=2, label="Salario máximo después")

    plt.title("Comparación de canastas vs salario máximo de jubilados")
    plt.ylabel("CUP")
    plt.legend()
    plt.show()

"""----------------------------------------------------------------------"""