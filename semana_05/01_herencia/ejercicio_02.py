"""
    Ejercicio 02
    Programación Orientada a Objetos (POO)
    Participación

Requerimientos:

- Crear una clase `Alumno`.
- Crear el atributo de clase `nacionalidad` con el valor `"Peruano"`.
- Cada alumno deberá tener un nombre, distrito de residencia y tres calificaciones
correspondientes a los siguientes cursos: Cálculo II, Matemática Discreta, Redes Neuronales
- Las calificaciones deberán estar comprendidas entre 0 y 20. Su valor por defecto será 0 y
podrán proporcionarse como parámetros al instanciar la clase.
- Implementar un método que calcule y muestre el promedio de las tres calificaciones.
- Implementar un método que identifique y muestre el curso con la calificación más alta.
Si existen cursos con la misma calificación máxima, deberán mostrarse todos.
- Implementar un método que determine si el alumno está ""aprobado o desaprobado"",
considera un promedio mínimo aprobatorio de 13.
- Implementar un método que permita mostrar el nombre y distrito de residencia del alumno.
- Crea al menos dos instancias de la clase `Alumno`, utilizando datos y calificaciones distintas.
- Ejecutar los métodos implementados para cada alumno y mostrar sus respectivos resultados.

Consideraciones:
- Se permite utilizar diccionarios para organizar las calificaciones.
- Los resultados deberán mostrarse de forma clara y ordenada.
- No se requiere solicitar información mediante `input()`.

"""

class alumno:
    """atributos"""
    nacionalidad = "Peruano"
    def __init__(self,nombre, distrito, calculoii = 0, mat_discreta = 0, rd_neuro=0):
        self.nombre = nombre #input("Ingrese su nombre: ")
        self.distrito = distrito #input("Ingrese su distrito: ")
        self.calculoii = calculoii #input("Ingrese nota Cálculo II: ")
        self.mat_discreta = mat_discreta #input("Ingrese nota Matemática Discreta: ")
        self.rd_neuro = rd_neuro #input("Ingrese nota Redes Neuronales: ")

    """Métodos: Son las funciones de las clases"""
    def promedio(self):
        prom_notas = (self.calculoii +self.mat_discreta + self.rd_neuro)/3
        return prom_notas

    def curso_best_score(self):
        dic_notas_cursos = {
            "Cálculo II": self.calculoii,
            "Matemática Discreta": self.mat_discreta,
            "Redes Neuronales": self.rd_neuro
        }
        nota_maxima = max(dic_notas_cursos.values())
        cursos = []
        for curso, nota in dic_notas_cursos.items():
            if nota == nota_maxima:
                cursos.append(curso)

        if len(cursos) == 1:
            print(f"  La mejor calificación es: {nota_maxima:.2f} en el curso: {cursos[0]}")
        else:
            print(f"  La mejor calificación es: {nota_maxima:.2f} en los cursos: {cursos}")

    def aprobado(self):

        prom = self.promedio()
        print(f"  El promedio de sus calificaciones es: {prom:.2f}")
        if prom >=13:
            print("  El alumno est aprobado")
        else:
            print("  El alumno esta desaprobado")


    def mostrar(self):
        print(f"\n  El alumno: {self.nombre} vive en el distrito de: {self.distrito}")


print ("\n Alumno 1")

alumno1 = alumno("Juan Pérez", "Los Olivos", calculoii=18, mat_discreta=14, rd_neuro=12)
alumno1.mostrar()
alumno1.promedio()
alumno1.curso_best_score()
alumno1.aprobado()

print ("\n Alumno 2")

alumno2 = alumno("María Flores", "San Miguel", calculoii=10, mat_discreta=11, rd_neuro=11)
alumno2.mostrar()
alumno2.promedio()
alumno2.curso_best_score()
alumno2.aprobado()