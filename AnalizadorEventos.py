from typing import List, Dict, Any


class AnalizadorEventos:
    def __init__(self, nombre_evento: str):
        self.nombre_evento = nombre_evento

    def procesar_eventos(self) -> Dict[str, Any]:
        eventos_totales = 0
        eventos_por_tipo = {}
        eventos_por_servidor = {}

        with open(self.nombre_evento) as evento:
            for linea in evento:
                if linea.startswith("Fecha"):
                    eventos_totales += 1
                    _, fecha = linea.split(": ")
                elif linea.startswith("Hora"):
                    _, hora = linea.split(": ")
                elif linea.startswith("Servidor"):
                    _, servidor = linea.split(": ")
                elif linea.startswith("Tipo de evento"):
                    _, tipo_evento = linea.split(": ")
                    if tipo_evento in eventos_por_tipo:
                        eventos_por_tipo[tipo_evento] += 1
                    else:
                        eventos_por_tipo[tipo_evento] = 1
                    if servidor in eventos_por_servidor:
                        eventos_por_servidor[servidor] += 1
                    else:
                        eventos_por_servidor[servidor] = 1
                elif linea.startswith("Descripción"):
                    _, descripcion_evento = linea.split(": ")

        calculo = {
            "Número total de eventos registrados": eventos_totales,
            "Número de eventos por tipo": eventos_por_tipo,
            "Número de eventos por servidor": eventos_por_servidor
        }

        print(calculo)


eventos = AnalizadorEventos("evento.txt")

eventos.procesar_eventos()