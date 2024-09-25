from experta import *

class ProjectFact(Fact):
    """Información sobre el estado del proyecto"""
    pass

class KanbanEngine(KnowledgeEngine):
    @Rule(ProjectFact(tasks_in_progress=P(lambda x: x > 5)))
    def too_many_tasks(self):
        print("Demasiadas tareas en progreso, reducir el WIP.")

    @Rule(ProjectFact(task_time_exceeded=True))
    def task_blocked(self):
        print("Tarea bloqueada, revisar cuellos de botella.")

# Ejecutar el motor de inferencia
engine = KanbanEngine()
engine.reset()

# Declarar hechos sobre el proyecto
engine.declare(ProjectFact(tasks_in_progress=6, task_time_exceeded=True))

# Ejecutar las reglas
engine.run()
