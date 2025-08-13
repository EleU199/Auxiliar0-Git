class Usuario:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.tareas = []

    def agregarTarea(self, tarea):
        self.tareas.append(tarea)
<<<<<<< HEAD

    def listarTareas(self):
        for tarea in self.tareas:
            if tarea.estaLista():
                print(f"La tarea {tarea.obtenerNombre()} está lista")
                print(f"La tarea {tarea.obtenerNombre()} no está lista")


=======
>>>>>>> e7bfcb6ec5883c1bf4f5c2b770ef2bdffc9c9526
