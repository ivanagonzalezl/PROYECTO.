import random
import os
import requests
from Clases.Constructor import Constructor
from Clases.Pilot import Pilot
from Clases.Race import Race
from Clases.Circuit import Circuit
from Clases.ClientGeneral import ClientGeneral as General
from Clases.ClientVIP import ClientVIP as Vip
from Clases.Ticket import Ticket
from Clases.Restaurant import Restaurant
from Clases.ProductDrink import ProductDrink as Drink
from Clases.ProductFood import ProductFood as Food

class AppMA:
    """
    En esta parte, hice dos listas para cada db,
    una es para appendear de forma ordena la info a los .txt
    y la otra es para generar los objetos a partir de los .txt con los que voy a seguir trabajando.
    """
    def __init__(self):

        self.constructors=[]
        self.pilots=[]
        self.races=[]
        self.circuits=[]

        self.aux_constructors=[]
        self.aux_pilots=[]
        self.aux_races=[]
        self.aux_circuits=[]
    
    #LISTAS MODULO II
        self.entradas=[]
        self.general=[]
        self.vip=[]

        self.aux_entradas=[]
        
    #LISTAS MODULO IV
        self.restaurants=[]
        self.productos_food=[]
        self.productos_drinks=[]

        self.aux_restaurants=[]

        self.number_Id = 1

    def down_load_data(self):

        """
        Aquí bajo la info de las API
        """

        url_constructores='https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/constructors.json'
        response_c=requests.request("GET", url_constructores)

        url_pilots='https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/drivers.json'
        response_p=requests.request("GET", url_pilots)

        url_races='https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/races.json'
        response_r=requests.request("GET", url_races)

        """
        Appendeo la info de las API a las listas auxiliares.
        """
        directory=  os.getcwd()+"/TXT/Modulo I/"
        file_name_cons="Constructor.txt"
        with open(directory+file_name_cons, "w") as f:
            for c in response_c.json():
                 x=[]
                 for p in response_p.json():
                    if c["id"]==p["team"]:
                        x.append(p["firstName"])
                 f.write(f"{c['name']},{ c['id']},{c['nationality']},{x[0]},{x[1]},\n")
        
        file_name_p="Pilot.txt"
        with open(directory+file_name_p, "w") as f:
            for i in response_p.json():
                f.write(f'{i["firstName"]},{i["lastName"]},{i["dateOfBirth"]},{i["nationality"]},{i["permanentNumber"]},{i["team"]},\n')
        
        filen_name_r="Race.txt"
        with open(directory+filen_name_r,"w") as f:
            for i in response_r.json():      
                f.write(f'{i["name"]},{i["round"]},{i["date"]},{i["circuit"]["name"]},,False,\n')#FALTA PODIUM
        
        file_name_cir="Circuit.txt"
        with open(directory+file_name_cir, "w") as f:
            for i in response_r.json():
                f.write(f'{i["circuit"]["name"]},{i["circuit"]["location"]["country"]},{i["circuit"]["location"]["locality"]},{i["circuit"]["location"]["lat"]},{i["circuit"]["location"]["long"]},\n')
        
        #LISTAS AUXILIARES MODULO II
        self.aux_entradas= []

        directory = os.getcwd()+"/TXT/Modulo II/"
        file_name = "Ticket.txt"
        with open(directory + file_name,"w") as f:
            for carrera in response_r.json():
                f.write(f'{carrera["name"]},{carrera["map"]["general"][0]*carrera["map"]["general"][1]},{carrera["map"]["vip"][0]*carrera["map"]["vip"][1]},\n')
        

    """
    Llevo la info de los .txt a las listas de objetos que seguiré usando.
    """
    def read_files(self):
        directory= os.getcwd()+"/TXT/Modulo I/"
        
        self.constructors= []
        file_name_cons="Constructor.txt"
        with open(directory+file_name_cons) as f:
            for line in f:
                x=[line.split(",")[3],line.split(",")[4]]
                constructor= Constructor(line.split(",")[0],line.split(",")[1],line.split(",")[2],x)
                self.constructors.append(constructor)

        self.pilots= []
        file_name_p="Pilot.txt"
        with open(directory+file_name_p) as f:
            for line in f:
                pilot= Pilot(line.split(",")[0],line.split(",")[1],line.split(",")[2],line.split(",")[3],line.split(",")[4], line.split(",")[5])
                self.pilots.append(pilot)
                

        self.races= []
        file_name_r="Race.txt"
        with open(directory+file_name_r) as f:
            for line in f:
                if line.split(",")[5]=="True":
                    x=True
                else:
                    x=False

                race= Race(line.split(",")[0],line.split(",")[1],line.split(",")[2],line.split(",")[3],line.split(",")[4],x)
                self.races.append(race)
                
        
        self.circuits= []
        file_name='Circuit.txt'
        with open(directory+file_name) as f:
            for line in f:
                circuit= Circuit(line.split(",")[0],line.split(",")[1],line.split(",")[2],line.split(",")[3],line.split(",")[4])
                self.circuits.append(circuit)

        #MODULO II
        directory=os.getcwd()+"/TXT/Modulo II/"

        
        self.entradas= []
        file_name="Ticket.txt"
        with open(directory+file_name) as f:
            for line in f:
                x=int(line.split(",")[1])
                y=int(line.split(",")[2])
                entrada= Ticket(line.split(",")[0],x,y)
                self.entradas.append(entrada)
        
        self.general=[]
        file_name="ClientGeneral.txt"

        with open(directory+file_name) as f:
            for line in f:
                if len(line)!=0:
                    name=line.split(",")[0]
                    dni=int(line.split(",")[1])
                    age=int(line.split(",")[2])
                    race=line.split(",")[3]
                    ondulado=line.split(",")[4]
                    n_ticket=int(line.split(",")[5])
                    validado=line.split(",")[6]
                    validado=True if validado=="True" else False
                    race_id=int(line.split(",")[7])
                    cliente_general= General(name, dni, age, race, ondulado, n_ticket, validado, race_id)
                    self.general.append(cliente_general)
        
        self.vip=[]
        file_name="ClientVIP.txt"

        with open(directory+file_name) as f:
            for line in f:
                if len(line)!=0:

                    name=line.split(",")[0]
                    dni=int(line.split(",")[1])
                    age=int(line.split(",")[2])
                    race=line.split(",")[3]
                    ondulado=line.split(",")[4]
                    n_ticket=int(line.split(",")[5])
                    validado=line.split(",")[6] 
                    validado=True if validado=="True" else False
                    #gasto = int(line.split(",")[7]) 
                    race_id=int(line.split(",")[7])
                    cliente_vip= Vip(name, dni, age, race, ondulado, n_ticket, validado,race_id)
                    self.vip.append(cliente_vip)
        
        self.number_Id=self.get_actual_id()


        """En esta funcion genero la busqueda de constructores por país de origen.
        """
    def finish_race(self):
 
                    for race in self.races:
                        if race.race_end==False:
                            print(f"\nLa siguiente carrera es: {race.race_name}. ¿La deseas terminar?")
                            option=input("1. Finalizar carrera.\n2. Finalizar siguiente carrera.\n3. Volver.\n>>> ")

                            while option!="1" and option!="2" and option!="3":
                                option=input("ERRROR: Ingreso inválido, intente nuevamente: ")

                            if option=="1":
                                race.race_end=True


                                pilots=self.pilots
                                random.shuffle(pilots)
                                podium_=pilots[0:10]

                                puntos = [25,18,15,12,10,8,6,4,2,1]

                                podium=""

                                print("\nGANADORES\n")
                                for i, pilot in enumerate(podium_):
                                    ganador = "(ganador)" if i==0 else ""
                                    posicion_jugador = f"{i+1}. {pilot.pilot_name} {pilot.pilot_last_name} {ganador} {puntos[i]} puntos."
                                    print(posicion_jugador)
                                    podium+=posicion_jugador+"-"

                                race.race_podium=podium

                                directory= os.getcwd()+"/TXT/Modulo I/"
                                file_name="Race.txt"
                                with open(directory+file_name,"w") as f:
                                    for race in self.races:
                                        f.write(f"{race.race_name},{race.race_number},{race.race_date},{race.race_circuit},{race.race_podium},{race.race_end},\n")
                            
                            elif option=="3":
                                break
                                

    def search_constructors_by_country(self):#LISTO
        print("Buscar constructores por país.")
        """Cree una lista para mostrar las nacionalidades de los constructores numeradas.
        """
        countries=[]
        for constructor in self.constructors:
            countries.append(constructor.constructor_nationality)
        """Saque los países que se repetian convirtiendo la lista en un set y luego nuevamente en una lista, y las ordené por orden alfabético.
        """

        countries=list(set(countries))
        countries.sort()
        """Imprimo la lista y pido un input para seleccionar los equipos que se desean visualizar.
        """
        print("")
        print("Selecciona la nacionalidad del constructor que estas buscando:\n")
        for i, country in enumerate(countries):
            print(f'{i+1}. {country} teams.')
        while True:
            try:
                country=int(input(">>> "))
                while not country in range(1, len(countries)+1):
                    raise Exception
                break
            except:
                print("ERROR: Ingreso iválido, intente nuevamene: ")

        """Generé una lista para guardar los equipos del país seleccionado, ya que hay algunos países con más de un equipo.
        """
        teams=[]        
        for constructor in self.constructors:
            if constructor.constructor_nationality==countries[country-1]:
                teams.append(constructor)

        """Pido un input para seleccionar el equipo que se desea visualizar en caso de que en la lista haya más de un equipo.
        """
        if len(teams)>1:
            print("Seleccione el equipo: ")
            for i, team in enumerate(teams):
                print(f'{i+1}. {team.constructor_name}')
            while True:
                try:
                    x=int(input(">>> "))
                    while not x in range(1,len(teams)+1):
                        raise Exception
                    break
                except:
                    print("ERROR: Ingreso inválido intente nuevamente: ")
            teams[x-1].show_attr()
        else:
            teams[0].show_attr()
    
    def search_pilots_by_constructor(self):
        print("Buscar a los pilotos por constructor.")
        
        """MUESTRO DE FORMA NUMERADA EL NOMBRE DE CADA CONSTRUCTOR.
        """
        for i, t in enumerate(self.constructors):
            print(f'{i+1}. {t.constructor_name}.')
        while True:
            try:
                t=int(input(">>> "))
                while not t in range(1, len(self.constructors)+1):
                    raise Exception
                break
            except:
                print("ERROR: Ingreso inválido, intente de nuevo: ")
        
        """MUESTRO LOS ATRIBUTOS DEL PILOTO SELECCIONADO.
        """
        equipo=(self.constructors[t-1].constructor_id)
        print(equipo)

        for pilot in self.pilots:
            if equipo==pilot.pilot_team:
                pilot.show_attr()
        
    def race_by_circuit_country(self): #LISTO
        print("\nBUSQUEDA DE CARRERAS POR PAÍS DEL CIRCUITO")
        countries=[]
        for pais in self.circuits:
            countries.append(pais.circuit_country)

        countries=list(set(countries))
        
        countries.sort()

        print("\nEscoja el pais cuyas carreras desea visualizar: ")
        for i, p in enumerate(countries):
            print(f'{i+1}. {p}.')

        p=input(">>> ")
        while not p.isnumeric() or not int(p) in range(1, len(countries)+1):
            p=input("ERROR: El ingreso ha sido inválido, intente nuevamente:  ")

        pais=countries[int(p)-1]

        circuitos=[]

        for circuit in self.circuits:
            if pais==circuit.circuit_country:
                circuitos.append(circuit.circuit_name)
        
        for i, circuito in enumerate(circuitos):
            for circuit in self.circuits:    
                if circuitos[0]==circuit.circuit_name:
                    circuit.show_attr()
                
        
    def race_by_month(self): #LISTO
        print("Busqueda de carrera por mes: \n")
        while True:
            try:
                mes=input("Ingrese el mes de la carrera que buscar: ")
                while not mes.isnumeric():
                    raise Exception
                while int(mes) not in range(1,13):
                    raise Exception
                while len(mes)!=2:
                    raise Exception
                break
            except:
                print("Error, ingreso inválido.\nEjemplo de ingreso:\nSi el mes es julio el input es 07.\n ")
        
        x=False

        for race in self.races:
            if race.race_date.split("-")[1]== mes:
                x=True
                race.show_attr()

        if x==False:
            print("En este mes no hay carreras.")

    
    def search_race(self):
        while True:
            print("")
            print("BUSQUEDA DE CARRERAS🔍")
            x=input("1. Buscar los constructores por país.\n2. Buscar los pilotos por constructor.\n3. Buscar a las carreras por país del circuito.\n4. Buscar todas las carreras que ocurran en un mes.\n5. Volver.\n>>> ")
            while not x.isnumeric() or not int(x) in range(1,6):
                x=input("Ingreso inválido intente nuevamente: ")
           
            if x=="1":
                self.search_constructors_by_country()
            elif x=="2":
                self.search_pilots_by_constructor()
            elif x=="3":
                self.race_by_circuit_country()
            elif x=="4":
                self.race_by_month()
            elif x=="5":
                break

    def race_team_management(self):
        while True:
            print("\n🏁MÓDULO DE GESTIÓN DE CARRERAS Y EQUIPOS🏁")
            option=input("1. Búsqueda de carreras.\n2. Finalizar carrera.\n3. Volver.\n>>> ")

            while not option.isnumeric() or not int(option) in range(1,4):
                option=input("Ingreso inválido intente nuevamente: ")

            if option=="1":
                self.search_race()
            elif option=="2":
                self.finish_race()
            else:
                break
#MODULO 2
    def regisgter(self):

        """Imprimo la lista de carreras."""
        print("\nSelecciones la carrera a la que desea asistir: ")
        for i, race in enumerate(self.races):
            print(f"{i+1}. {race.race_name}")

        option=input(">>> ")
        while (not option.isnumeric()) or not (int(option) in range(1, len(self.races)+1)):
            option=input("ERROR: Ingreso inválido, intente nuevamente: ")
        
        option=int(option) - 1
        race_=self.races[option]
        print("")
        carrera=self.entradas[option]


        print(carrera.race_name)

        clientes=[]
        """Comparo el nombre de la opcion con la lista de carreras, luego pregunto si la entrada que desea adquirir es general o vip, y pido los datos correspondientes
        para llenar las clases ClienteVIP y ClienteGeneral"""

        for race in self.races:
            if race.race_name==carrera.race_name:
                if race.race_end==True:
                    print("Es carrera ya finalizó, no puede comprar más entradas.")
                else:
                    tipo=input("Ingrese el tipo de entradad que desea (G)eneral o (V)IP: ").capitalize()
                    while tipo!="G" and tipo!="V":
                        tipo=input("Ingreso inválido, escribe la letra G si desea una entrada general o la letra V si desea una entrada VIP: ").capitalize()
                    if tipo=="G":\
                    
                        
                        print(f"El número de entradas disponibles es de: {self.entradas[option].general}")
                        if self.entradas[option].general==0:
                            print("Lo sentimos, no hay entradas generales disponibles.")
                            break
                        else:
                            num_entrada=input("Ingrese el número de entradas que desea: ")
                            while not num_entrada.isnumeric() or not int(num_entrada) in range(1, self.entradas[option].general+1): #####
                                num_entrada=input("El número de entradas se sale del rango de entradas disponibles, intente nuevamente: ")
                            
                            for i in range(int(num_entrada)):
                                nombre=input("Ingrese su nombre: ").capitalize()
                                cedula=input("Ingrese su número de cédula: ")
                                while not cedula.isnumeric():
                                    cedula=input("Ingreso inválido, intente nuevamente: ")
                                #ONDULADO
                                cedula=int(cedula)

                                edad=input("Ingrese su edad: ")
                                while not edad.isnumeric() or int(edad)<0:
                                    edad=input("Ingreso inválido, intente nuevamente: ")

                                if i != int(num_entrada) -1:
                                    print("Ingrese el siguiente usuario: \n")
                                cliente= General(nombre,cedula,edad,carrera.race_name,False,0, False, race_.race_number)
                                clientes.append(cliente)

                    elif tipo=="V":
                        print(f"El número de entradas disponibles es de: {self.entradas[option].vip}")
                        if self.entradas[option].vip==0:
                            print("Lo sentimos, no hay entradas vip disponibles.")
                            break
                        else:
                            num_entrada=input("Ingrese el número de entradas que desea: ")
                            while not num_entrada.isnumeric() or not int(num_entrada) in range(1, self.entradas[option].vip+1):
                                num_entrada=input("El número de entradas se sale del rango de entradas disponibles, intente nuevamente: ")
                            for i in range(int(num_entrada)):
                                nombre=input("Ingrese su nombre: ").capitalize()
                                cedula=input("Ingrese su número de cédula: ")
                                while not cedula.isnumeric():
                                    cedula=input("Ingreso inválido, intente nuevamente: ")

                                #ONDULADO
                                cedula=int(cedula)

                                edad=input("Ingrese su edad: ")
                                while not edad.isnumeric() or int(edad)<0:
                                    edad=input("Ingreso inválido, intente nuevamente: ")
                                
                                if i != int(num_entrada) -1:
                                    print("Ingrese el siguiente usuario: \n")
                                cliente= Vip(nombre,cedula,edad,carrera.race_name,False,0, False, race_.race_number)
                                clientes.append(cliente)

                    """Pido los datos para hacer la factura."""
                            
                    comprador=input("Ingrese a nombre de quien se realiza la factura: ")
                    dni_comprador=input("Ingrese la cedula del comprador: ")

                    while not dni_comprador.isnumeric():
                        dni_comprador=input("Ingrese un valor numérico: ")
                    cedula=int(dni_comprador)
                    ondulado=False
                    if len(str(cedula))<3:
                        ondulado=True
                    elif (len(str(cedula))%2==0):
                        str_id= str(cedula)[0:2]
                        if (cedula%int(str_id))==0:
                            ondulado=True
                    else:
                        str_id=str(cedula)[0:2]
                        new_str_id= str(cedula)+str_id[1]
                        if(int(new_str_id)) % int(str_id)==0:
                            ondulado=True
                    #SUBTOTAL
                    sub_total=int(num_entrada)*340
                    #DESCUENTO
                    if ondulado==True:
                        descuento=sub_total*0.5
                    else:
                        descuento=0
                    #IVA
                    iva=sub_total*0.16
                    #TOTAL
                    total=(sub_total+iva)-descuento
                    #FACTURA
                    print("FACTURA")
                    print(f"""
        Nombre: {comprador}
        Cedula: {dni_comprador}
        Subtotal: ${sub_total}
        Descuento: {descuento}
        IVA: ${iva}
        TOTAL:${total}""")

                    """Valido la compra"""
                    #VALIDAR COMPRA FINAL
                    validar=input("Desea continuar con su compra: (S)í, (N)o: ").capitalize()
                    while validar!="S" and validar!="N":
                        validar=input("Ingreso inválido, escriba N para no y S para sí: ").capitalize()


                    asientos=[]
                    if validar=="S":
                        n_Tickets_Vendidos = len(clientes)


                        if tipo=="V":
                            carrera.vip-=n_Tickets_Vendidos
                            for cliente in clientes:
                                cliente.n_ticket=self.number_Id
                                asientos.append(str(self.number_Id))

                                self.number_Id+=1
                                cliente.race_name=carrera.race_name

                                self.vip.append(cliente)

                        elif tipo=="G":
                            carrera.general-=n_Tickets_Vendidos
                            for cliente in clientes:
                                cliente.n_ticket=self.number_Id
                                asientos.append(str(self.number_Id))

                                self.number_Id+=1
                                cliente.race_name=carrera.race_name

                                self.general.append(cliente)


                        print("COMPRA REALIZADA CON ÉXITO ")
                        print("FACTURA")
                        asientos_string = ", ".join(asientos)
                        print(f"""
    Nombre: {comprador}
    Cedula: {dni_comprador}
    Subtotal: ${sub_total}
    IVA: ${iva}
    Descuento: ${descuento}
    TOTAL:${total}
    Ids de los Asientos Vendidos: {asientos_string}""")
                            

        """Reescribo en los txt para guardar la info adquirida.
        """
        directory= os.getcwd()+"/TXT/Modulo II/"
        file_name="ClientGeneral.txt"
        with open(directory+file_name,"w") as f:
            for cliente_general in self.general:
                f.write(f"{cliente_general.name},{cliente_general.dni},{cliente_general.age},{cliente_general.race},{cliente_general.ondulado},{cliente_general.n_ticket},{cliente_general.validado},{cliente_general.race_dni},\n")
        
        file_name="ClientVIP.txt"
        with open(directory+file_name,"w") as f:
            for cliente_vip in self.vip:
                f.write(f"{cliente_vip.name},{cliente_vip.dni},{cliente_vip.age},{cliente_vip.race},{cliente_vip.ondulado},{cliente_vip.n_ticket},{cliente_vip.validado},{cliente_vip.race_dni},\n")
        
        file_name="Ticket.txt"
        with open(directory+file_name,"w") as f:
            for ticket in self.entradas:
                f.write(f"{ticket.race_name},{ticket.general},{ticket.vip},\n")
        

    def get_actual_id(self):

        """Esta funcion revisa las lista vip y general para obrtener el número del ticket,
        si las listas estan vacias,retorna uno, si una lista esta vacia pero la otra no, revisa el último
        elemento de la que no lo esta y a su número de ticket, le suma uno, y si ninguna lista esta vacía, busca
        el mayor del último de cada lista, y al mayor le suma 1.
        """
        if len(self.general) == 0 and len(self.vip) == 0:
            return 1

        if len(self.general)==0:
            last_vip=self.vip[-1]
            return last_vip.n_ticket+1
        
        if len(self.vip)==0:
            last_general=self.general[-1]
            return last_general.n_ticket+1
        
        last_general=self.general[-1]
        last_vip=self.vip[-1]
        return max(last_general.n_ticket, last_vip.n_ticket) + 1
    

            
#MODULO 3

    """Pido el número del ticket que la persona desea validar, si el ticket no 
    esta en la lista del tipo de clientes que seleccionó, devuelve error."""
    def attendance_ticket(self):
        print("GESTIÓN DE ASISTENCIAS A LAS CARRERAS 🏎️")
        tipo=input("\nIngrese su tipo de boleto, (V)ip o (G)eneral: ").capitalize()
        while tipo!="V" and tipo!="G":
            tipo=input("Ingrese V para vip y G para general: ").capitalize()
        boleto=input("Ingrese su número de boleto: ")
        while not boleto.isnumeric():
            boleto=input("Los tickets solo tienen valores numéricos.\nIntente de nuevo: ")
        
        encontrado = False
        if tipo=="V":
            for entrada in self.vip:
                if int(boleto)==entrada.n_ticket:
                    encontrado = True
                    if entrada.validado==False:
                        print("Su boleto ha sido validado.")
                        entrada.validado=True
                    else:
                        print("Este boleto ya fue usado.")
                    break

            if not encontrado:
                print("No existe ningun cliene vip con ese numero de ticket")

        elif tipo=="G":

            for entrada in self.general:
                if int(boleto)==entrada.n_ticket:
                    encontrado = True
                    if entrada.validado==False:
                        print("Su boleto ha sido validado.")
                        entrada.validado=True
                    else:
                        print("Este boleto ya fue usado.")
                    break

            if not encontrado:
                print("No existe ningun cliene general con ese numero de ticket")
        
        """Una vez encontrado o no el ticket, la función lee las listas de cliente general, cliente vip y ticket y las escribe en sus respectivos txt.
        """
        
        directory= os.getcwd()+"/TXT/Modulo II/"
        file_name="ClientGeneral.txt"
        with open(directory+file_name,"w") as f:
            for cliente_general in self.general:
                f.write(f"{cliente_general.name},{cliente_general.dni},{cliente_general.age},{cliente_general.race},{cliente_general.ondulado},{cliente_general.n_ticket},{cliente_general.validado},{cliente_general.race_dni},\n")
        
        file_name="ClientVIP.txt"
        with open(directory+file_name,"w") as f:
            for cliente_vip in self.vip:
                f.write(f"{cliente_vip.name},{cliente_vip.dni},{cliente_vip.age},{cliente_vip.race},{cliente_vip.ondulado},{cliente_vip.n_ticket},{cliente_vip.validado},{cliente_vip.race_dni},\n")

        
 