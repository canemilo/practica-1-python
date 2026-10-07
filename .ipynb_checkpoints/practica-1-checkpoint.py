def main():
  
    lista_personajes_1 = ["Mario", "Wario", "Luigi"]
    
  
    lista_personajes_2 = ["Toad", "Toadette", "Huesitos"]
    
   
    lista_personajes_1.extend(lista_personajes_2)
    
    # 5.5: 
    print("El último elemento de la lista es:", lista_personajes_1[-1])
    
    # 5.6: 
    numeros_tupla = (2, 4, 6)
    
    # 5.7: 
    print("El primer elemento de la tupla es:", numeros_tupla[0])
    
    # 5.8: 
    print("\n--- Configuración del Rango ---")
    inicio = int(input("Introduce el valor de inicio: "))
    fin = int(input("Introduce el valor de fin: "))
    salto = int(input("Introduce el valor del salto: "))
    
    mi_rango = range(inicio, fin, salto)
    
    # 5.9:
    print("El rango generado es:", list(mi_rango))

if __name__ == "__main__":
    main()