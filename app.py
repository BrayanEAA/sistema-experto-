from flask import Flask, render_template, request
from experta import *

app = Flask(__name__)

# Definición del sistema experto
class KanbanExpert(KnowledgeEngine):

    @DefFacts()
    def _initial_action(self):
        yield Fact('inicio')

    @Rule(Fact('inicio'))
    def accion_inicial(self):
        print("Sistema experto para Kanban iniciado.")

    @Rule(Fact('task_state', state='Por Hacer'))
    def task_in_progress(self):
        print("La tarea puede ser movida a 'En Proceso'.")

    @Rule(Fact('task_priority', priority='Alta'))
    def recommend_task_priority(self):
        print("Recomendar trabajar en la tarea prioritaria.")

    @Rule(Fact('team_member', load='Alta'))
    def recommend_assignment(self):
        print("Recomendar asignar esta tarea a un miembro del equipo con baja carga de trabajo.")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/agregar_tarea', methods=['GET', 'POST'])
def agregar_tarea():
    if request.method == 'POST':
        nombre_tarea = request.form['nombre_tarea']
        estado = request.form['estado']
        prioridad = request.form['prioridad']
        
        # Aquí puedes crear un hecho y ejecutar el motor de reglas
        kanban_expert = KanbanExpert()
        kanban_expert.reset()  # Reinicia el motor de reglas
        kanban_expert.declare(Fact('task_name', name=nombre_tarea))
        kanban_expert.declare(Fact('task_state', state=estado))
        kanban_expert.declare(Fact('task_priority', priority=prioridad))
        kanban_expert.run()  # Ejecuta el motor de reglas
        
        return f"Tarea '{nombre_tarea}' agregada con estado '{estado}' y prioridad '{prioridad}'."
    
    return render_template('agregar_tarea.html')

if __name__ == '__main__':
    app.run(debug=True)
