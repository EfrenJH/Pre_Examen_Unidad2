#Instrituto Tecnológico de San Juan del Río
#Ingeniería en Sistemas Computacionales
#Estructura de Datos
#Unidad 2
#PreExamen.py    LISTAS DOBLEMENTE LIGADAS
#Docente: Domingo Rosales Alvarez
#Efrén Jacobo Hernández
#No. de control: 24590384


class Nodo:
    """
    Clase para representar un nodo individual de la lista doblemente ligada.
    """
    def __init__(self, dato):
        self.dato = dato
        self.prev = None
        self.next = None

class ListaDoble:
    """
    Clase que implementa una lista doblemente ligada para almacenar datos de alumnos.
    """
    def __init__(self):
        self.head = None
        self.tail = None

    # --- Métodos de inserción ---
    def push_back(self, nombre, calificacion):
        """Inserta un alumno al FINAL de la lista."""
        dato = [nombre, calificacion] #Aquí llega el guardado del vector [nombre, calificacion] que se manda a llamar en el main
        n = Nodo(dato)
        n.prev = self.tail # type: ignore
        if self.tail:
            self.tail.next = n # type: ignore
        else:
            self.head = n
        self.tail = n

    def push_front(self, nombre, calificacion):
        """Inserta un alumno al INICIO de la lista."""
        dato = [nombre, calificacion] #Aquí también llega el guardado del vector [nombre, calificacion] que se manda a llamar en el main
        n = Nodo(dato)
        n.next = self.head # type: ignore
        if self.head:
            self.head.prev = n # type: ignore
        else:
            self.tail = n
        self.head = n

    # --- Métodos de recorrido y utilidad ---
    def forward(self):
        """Devuelve una lista con los datos de los alumnos en orden."""
        cur, out = self.head, []
        while cur:
            out.append(cur.dato)
            cur = cur.next
        return out
        
    def __len__(self):
        """Permite usar len(lista) para obtener el número de nodos."""
        cur, c = self.head, 0
        while cur:
            c += 1
            cur = cur.next
        return c

    def remove_node(self, nodo):
        """Método auxiliar para desconectar y eliminar un nodo específico."""
        if not nodo:
            return
        if nodo.prev:
            nodo.prev.next = nodo.next
        else:
            self.head = nodo.next
        if nodo.next:
            nodo.next.prev = nodo.prev
        else:
            self.tail = nodo.prev

    # --- Método original find ---
    def find(self, valor):
        """Busca un valor (un arreglo completo) y devuelve el primer nodo que lo contiene."""
        cur = self.head
        while cur:
            if cur.dato == valor:
                return cur
            cur = cur.next
        return None

    # Estos sigueintes métodos usan la misma estructura que el método find original, pero adaptados a los datos específicos (nombre y calificación).
    # --- Métodos de Búsqueda específicos ---
    def find_por_alumno(self, nombre_buscado):
        resultados = []
        cur = self.head
        while cur:
            if cur.dato[0] == nombre_buscado:
                resultados.append(cur.dato)
            cur = cur.next
        return resultados

    def find_por_calificacion(self, calificacion_buscada):
        """Busca todos los alumnos con una calificación específica."""
        resultados = []
        cur = self.head
        while cur:
            # Se accede por índice, es decir, por cur.dato[1]
            if cur.dato[1] == calificacion_buscada:
                resultados.append(cur.dato)
            cur = cur.next
        return resultados

    def find_calificacion_mas_alta(self):
        """Encuentra al alumno o alumnos con la calificación más alta."""
        if not self.head:
            return []
        mejores_alumnos, calificacion_max = [], -1.0
        cur = self.head
        while cur:
            calif = cur.dato[1] # Se accede por índice
            if calif > calificacion_max:
                calificacion_max = calif
                mejores_alumnos = [cur.dato]
            elif calif == calificacion_max:
                mejores_alumnos.append(cur.dato)
            cur = cur.next
        return mejores_alumnos

    def find_calificacion_mas_baja(self):
        """Encuentra al alumno o alumnos con la calificación más baja."""
        if not self.head:
            return []
        peores_alumnos, calificacion_min = [], 101.0
        cur = self.head 
        while cur:
            calif = cur.dato[1] # Se accede por índice
            if calif < calificacion_min:
                calificacion_min = calif
                peores_alumnos = [cur.dato]
            elif calif == calificacion_min:
                peores_alumnos.append(cur.dato)
            cur = cur.next
        return peores_alumnos

#------------- MAIN ------------------#
lista_alumnos = ListaDoble()

#Agregando varios alumnos con sus calificaciones, en un vector, como anteriormente era un solo dato, ahora es un vector [nombre, calificacion]
lista_alumnos.push_back("Efrén", 9.0)
lista_alumnos.push_back("Hugo", 8.8)
lista_alumnos.push_back("Pablito", 9.8)
lista_alumnos.push_back("José José", 7.0)
lista_alumnos.push_front("Luis Miguel", 9.8)
lista_alumnos.push_back("Juan Gabriel", 6.0)
lista_alumnos.push_front("Domingo", 10) #tqm profe :)
lista_alumnos.push_back("Araceli", 9.9)
lista_alumnos.push_front("Norma", 10)
lista_alumnos.push_back("Hermenegildo", 5.5)
lista_alumnos.push_front("Vicente Guerrero", 6.0)

print("--- Lista completa de alumnos ---")
print(f"Alumnos registrados: {lista_alumnos.forward()}")
print(f"Total de alumnos: {len(lista_alumnos)}\n")

print("--- Búsqueda por nombre 'Maria' ---")
print(f"Resultado: {lista_alumnos.find_por_alumno('Maria')}\n")

print("--- Búsqueda de un registro completo con find(['Ana', 9.5]) ---")
nodo_encontrado = lista_alumnos.find(['Ana', 9.5])
if nodo_encontrado:
    print(f"Nodo encontrado. Dato: {nodo_encontrado.dato}\n")
else:
    print("Nodo no encontrado.\n")

print("--- Alumno(s) con la calificación más alta ---")
print(f"Resultado: {lista_alumnos.find_calificacion_mas_alta()}\n")

print("--- Alumno(s) con la calificación más baja ---")
print(f"Resultado: {lista_alumnos.find_calificacion_mas_baja()}\n")