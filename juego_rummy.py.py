import random

# Valores de cartas y palos validos
v_validos = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
p_validos = ("C", "D", "E", "T")
orden_valores = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

# Función para crear una baraja completa
def crear_baraja():
    return [(v, p) for v in v_validos for p in p_validos]

# Función para ordenar la mano del usuario por palo y luego por valor
def ordenar_mano(mano):
    orden_palos = {palo: i for i, palo in enumerate(p_validos)}
    reglas_orden = lambda x: (orden_palos[x[1]], orden_valores.index(x[0]))
    return sorted(mano, key=reglas_orden)

# Función para buscar escaleras dentro de la mano del usuario
def buscar_escaleras(mano):
    escaleras = []
    for palo in p_validos:
        cartas_palo = sorted([carta for carta in mano if carta[1] == palo], key=lambda x: orden_valores.index(x[0]))
        for i in range(len(cartas_palo) - 2):
            escalera = [cartas_palo[i]]
            for j in range(i + 1, len(cartas_palo)):
                valor_anterior = orden_valores.index(escalera[-1][0])
                valor_actual = orden_valores.index(cartas_palo[j][0])
                if valor_actual == valor_anterior + 1:
                    escalera.append(cartas_palo[j])
                    if len(escalera) >= 3:
                        escaleras.append(tuple(escalera[:])) # Usar tuplas para inmutabilidad
                else:
                    break
    return list(set(escaleras)) # Eliminar duplicados convirtiendo a set y luego a lista

# Función para identificar jugadas (ternas y cuarternas)
def identificar_grupos(mano):
    ternas, cuaternas = [], []
    for valor in v_validos:
        cartas = [carta for carta in mano if carta[0] == valor]
        if len(cartas) == 4:
            cuaternas.append(tuple(cartas))
        elif len(cartas) == 3:
            ternas.append(tuple(cartas))
    return list(set(ternas)), list(set(cuaternas)) # Eliminar duplicados

# Función para mostrar la mano del jugador (ordenada)
def mostrar_mano(mano):
    mano_ordenada = ordenar_mano(mano)
    print("Tu mano:", ", ".join([f"{carta[0]}{carta[1]}" for carta in mano_ordenada]))

# Función para mostrar las posibles jugadas en la mano
def mostrar_posibles_jugadas(mano):
    ternas, cuaternas = identificar_grupos(mano)
    escaleras = buscar_escaleras(mano)

    print("\n=== POSIBLES JUGADAS EN TU MANO ===")
    if ternas:
        print(f"Ternas ({len(ternas)}): {[', '.join([f'{c[0]}{c[1]}' for c in t]) for t in ternas]}")
    if cuaternas:
        print(f"Cuaternas ({len(cuaternas)}): {[', '.join([f'{c[0]}{c[1]}' for c in c]) for c in cuaternas]}")
    if escaleras:
        print(f"Escaleras ({len(escaleras)}): {[', '.join([f'{c[0]}{c[1]}' for c in e]) for e in escaleras]}")
    if not ternas and not cuaternas and not escaleras:
        print("No tienes jugadas posibles en tu mano por ahora.")

# Función para que el jugador "coma" una carta de la baraja
def comer_carta(baraja, mano):
    if not baraja:
        print("La baraja está vacía.")
        return None
    carta_comida = baraja.pop(random.randrange(len(baraja)))
    mano.append(carta_comida)
    print(f"Comiste la carta: {carta_comida[0]}{carta_comida[1]}")
    return carta_comida

# Función para que el jugador descarte una carta
def descartar_carta(mano):
    mostrar_mano(mano)
    while True:
        carta_descartar_str = input("Ingrese la carta que desea descartar (ej: 7C): ").upper()
        if len(carta_descartar_str) >= 2 and carta_descartar_str[:-1] in v_validos and carta_descartar_str[-1] in p_validos:
            carta_descartar = (carta_descartar_str[:-1], carta_descartar_str[-1])
            if carta_descartar in mano:
                mano.remove(carta_descartar)
                print(f"Descartaste: {carta_descartar[0]}{carta_descartar[1]}")
                return carta_descartar
            else:
                print("Esa carta no está en tu mano. Intenta nuevamente.")
        else:
            print("Formato de carta inválido. Intenta nuevamente (ej: 7C).")

# Función para mostrar las jugadas en la mesa
def mostrar_mesa(mesa):
    if mesa["escaleras"] or mesa["grupos"]:
        print("\n=== JUGADAS EN LA MESA ===")
        if mesa["escaleras"]:
            print("Escaleras:", [", ".join([f"{c[0]}{c[1]}" for c in escalera]) for escalera in mesa["escaleras"]])
        if mesa["grupos"]:
            print("Grupos:", [", ".join([f"{c[0]}{c[1]}" for c in grupo]) for grupo in mesa["grupos"]])
    else:
        print("\nNo hay jugadas en la mesa.")

# Función para que el jugador coloque una jugada en la mesa
def colocar_jugada(mano, mesa):
    while True:
        print("\n¿Qué desea colocar?")
        print("1. Escala")
        print("2. Grupo (terna o cuaterna)")
        print("3. No colocar nada por ahora")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            escaleras_posibles = buscar_escaleras(mano)
            if not escaleras_posibles:
                print("No tienes escaleras válidas para colocar.")
                continue
            print("Escaleras posibles:")
            for i, escalera in enumerate(escaleras_posibles):
                print(f"{i+1}. {', '.join([f'{c[0]}{c[1]}' for c in escalera])}")
            while True:
                seleccion = input(f"Seleccione el número de la escalera a colocar (o 'n' para cancelar): ")
                if seleccion.lower() == 'n':
                    break
                try:
                    indice = int(seleccion) - 1
                    if 0 <= indice < len(escaleras_posibles):
                        escalera_seleccionada = list(escaleras_posibles[indice])
                        es_valida = True
                        for carta in escalera_seleccionada:
                            if carta not in mano:
                                es_valida = False
                                break
                        if es_valida:
                            mesa["escaleras"].append(tuple(escalera_seleccionada))
                            for carta in escalera_seleccionada:
                                mano.remove(carta)
                            print("Escalera colocada en la mesa.")
                            return True
                        else:
                            print("Alguna de las cartas de la escalera no está en tu mano.")
                    else:
                        print("Selección inválida.")
                except ValueError:
                    print("Ingrese un número válido.")
        elif opcion == "2":
            ternas_posibles, cuaternas_posibles = identificar_grupos(mano)
            grupos_posibles = [(g, "terna") for g in ternas_posibles] + [(g, "cuaterna") for g in cuaternas_posibles]
            if not grupos_posibles:
                print("No tienes grupos válidos para colocar.")
                continue
            print("Grupos posibles:")
            for i, (grupo, tipo) in enumerate(grupos_posibles):
                print(f"{i+1}. {', '.join([f'{c[0]}{c[1]}' for c in grupo])} ({tipo})")
            while True:
                seleccion = input(f"Seleccione el número del grupo a colocar (o 'n' para cancelar): ")
                if seleccion.lower() == 'n':
                    break
                try:
                    indice = int(seleccion) - 1
                    if 0 <= indice < len(grupos_posibles):
                        grupo_seleccionado, _ = grupos_posibles[indice]
                        grupo_seleccionado_lista = list(grupo_seleccionado)
                        es_valida = True
                        for carta in grupo_seleccionado_lista:
                            if carta not in mano:
                                es_valida = False
                                break
                        if es_valida:
                            mesa["grupos"].append(tuple(grupo_seleccionado_lista))
                            for carta in grupo_seleccionado_lista:
                                mano.remove(carta)
                            print("Grupo colocado en la mesa.")
                            return True
                        else:
                            print("Alguna de las cartas del grupo no está en tu mano.")
                    else:
                        print("Selección inválida.")
                except ValueError:
                    print("Ingrese un número válido.")
        elif opcion == "3":
            return False
        else:
            print("Opción inválida.")

# Función para que el jugador agregue una carta a una jugada existente en la mesa
def agregar_carta_a_jugada(mano, mesa):
    if not mesa["escaleras"] and not mesa["grupos"]:
        print("No hay jugadas en la mesa para agregar cartas.")
        return False

    while True:
        print("\n¿A qué jugada desea agregar una carta?")
        if mesa["escaleras"]:
            print("Escaleras:")
            for i, escalera in enumerate(mesa["escaleras"]):
                print(f"E{i+1}. {', '.join([f'{c[0]}{c[1]}' for c in escalera])}")
        if mesa["grupos"]:
            print("Grupos:")
            for i, grupo in enumerate(mesa["grupos"]):
                print(f"G{i+1}. {', '.join([f'{c[0]}{c[1]}' for c in grupo])}")
        print("N. No agregar nada")
        seleccion_jugada = input("Seleccione la jugada (ej: E1, G2, N): ").upper()

        if seleccion_jugada == "N":
            return False

        tipo_jugada = seleccion_jugada[0]
        try:
            indice_jugada = int(seleccion_jugada[1:]) - 1
        except ValueError:
            print("Formato inválido.")
            continue

        if tipo_jugada == "E" and mesa["escaleras"] and 0 <= indice_jugada < len(mesa["escaleras"]):
            escalera_objetivo = list(mesa["escaleras"][indice_jugada])
            mostrar_mano(mano)
            carta_agregar_str = input("Ingrese la carta que desea agregar (ej: 7C, o 'n' para cancelar): ").upper()
            if carta_agregar_str == 'N':
                continue
            if len(carta_agregar_str) >= 2 and carta_agregar_str[:-1] in v_validos and carta_agregar_str[-1] in p_validos:
                carta_agregar = (carta_agregar_str[:-1], carta_agregar_str[-1])
                if carta_agregar in mano and carta_agregar[1] == escalera_objetivo[0][1]: # Mismo palo
                    valores_escalera = [orden_valores.index(c[0]) for c in escalera_objetivo]
                    valor_agregar = orden_valores.index(carta_agregar[0])
                    if valor_agregar == min(valores_escalera) - 1 or valor_agregar == max(valores_escalera) + 1:
                        mesa["escaleras"][indice_jugada] = tuple(sorted(escalera_objetivo + [carta_agregar], key=lambda x: orden_valores.index(x[0])))
                        mano.remove(carta_agregar)
                        print(f"Se agregó {carta_agregar_str} a la escalera.")
                        return True
                    else:
                        print("La carta no sigue la secuencia de la escalera.")
                else:
                    print("La carta no está en tu mano o no es del mismo palo.")
            else:
                print("Formato de carta inválido.")

        elif tipo_jugada == "G" and mesa["grupos"] and 0 <= indice_jugada < len(mesa["grupos"]):
            grupo_objetivo = list(mesa["grupos"][indice_jugada])
            valor_grupo = grupo_objetivo[0][0]
            mostrar_mano(mano)
            carta_agregar_str = input("Ingrese la carta que desea agregar (ej: 7C, o 'n' para cancelar): ").upper()
            if carta_agregar_str == 'N':
                continue
            if len(carta_agregar_str) >= 2 and carta_agregar_str[:-1] in v_validos and carta_agregar_str[-1] in p_validos:
                carta_agregar = (carta_agregar_str[:-1], carta_agregar_str[-1])
                if carta_agregar in mano and carta_agregar[0] == valor_grupo and carta_agregar[1] not in [c[1] for c in grupo_objetivo]:
                    if len(grupo_objetivo) < 4:
                        mesa["grupos"][indice_jugada] = tuple(grupo_objetivo + [carta_agregar])
                        mano.remove(carta_agregar)
                        print(f"Se agregó {carta_agregar_str} al grupo.")
                        return True
                    else:
                        print("El grupo ya tiene 4 cartas.")
                else:
                    print("La carta no está en tu mano, no tiene el mismo valor o el palo ya existe en el grupo.")
            else:
                print("Formato de carta inválido.")
        else:
            print("Selección de jugada inválida.")

# Función principal del juego
def juego_rummy():
    baraja = crear_baraja()
    random.shuffle(baraja)
    mano_jugador = []
    mesa = {"escaleras": [], "grupos": []}
    turnos = 0

    # Inicializar mano del jugador
    for _ in range(10):
        mano_jugador.append(baraja.pop())

    while mano_jugador:
        turnos += 1
        print(f"\n=== TURNO {turnos} ===")
        mostrar_mano(mano_jugador) # La mano se ordena al mostrarla
        mostrar_posibles_jugadas(mano_jugador) # Mostrar las posibles jugadas
        mostrar_mesa(mesa)

        # Fase de comer carta
        comer_carta(baraja, mano_jugador)

        # Fase de colocar jugada o agregar a la mesa
        if mano_jugador:
            while True:
                print("\n¿Qué desea hacer?")
                print("1. Colocar una jugada en la mesa")
                print("2. Agregar una carta a una jugada existente")
                print("3. No hacer nada")
                accion = input("Seleccione una opción: ")
                if accion == "1":
                    colocar_jugada(mano_jugador, mesa)
                elif accion == "2":
                    agregar_carta_a_jugada(mano_jugador, mesa)
                elif accion == "3":
                    break
                else:
                    print("Opción inválida.")

            # Fase de descartar carta
            if len(mano_jugador) > 0:
                descartar_carta(mano_jugador)
            else:
                print(f"\n¡GANASTE en {turnos} turnos! Te quedaste sin cartas.")
                break

    if not mano_jugador:
        print("¡Juego terminado!")
    else:
        print("Se acabaron las cartas de la baraja. Juego terminado.")

# Ejecutar el juego
if __name__ == "__main__":
    juego_rummy()