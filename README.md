Magdiel Santos
Sera una adivinanza para los alumnos sobre mejoramiento del pensamiento en adivinar los numeros random como diversion y mejorar la agilidad de nuestro pensamiento logico.

INVESTIGACION

¿Qué es Pygame y para qué se utiliza?
Pygame es una librería de Python para crear videojuegos y aplicaciones multimedia en 2D. Está construida sobre SDL, una biblioteca de bajo nivel que se comunica con la pantalla, el teclado, el mouse y el sonido. Te da herramientas para abrir ventanas, dibujar formas e imágenes, detectar teclas y clics, reproducir sonidos y controlar el tiempo (los fotogramas por segundo). Se usa para aprender programación con proyectos visuales, hacer prototipos y construir juegos sencillos o medianos.

¿Cómo se relaciona con los temas vistos en clase?
Un programa de Pygame es básicamente un conjunto de conceptos básicos de programación trabajando juntos. El código de main.py ya los usa:
• Ciclos: el game loop es un while corriendo: que se repite 60 veces por segundo, y dentro hay un for evento in pygame.event.get(): que recorre los eventos pendientes.
• Condicionales: if evento.type == pygame.QUIT: decide qué hacer según lo que ocurrió.
• Eventos: cerrar la ventana, presionar una tecla (KEYDOWN) o hacer clic (MOUSEBUTTONDOWN) son eventos que el programa detecta y a los que responde.
• Estructuras de datos: las tuplas guardan colores (30, 30, 40) y posiciones (x, y); las listas guardan varios enemigos, balas o plataformas; los diccionarios pueden guardar la configuración o el estado del juego.
• Funciones: conviene separar el código en funciones como dibujar(), actualizar() o manejar_eventos() para que el programa sea legible y reutilizable.
• Variables y operadores: la posición y la velocidad de un personaje son variables que se modifican en cada vuelta del ciclo (x += velocidad).
• Clases y objetos (si ya se vieron): Pygame incluye pygame.sprite.Sprite, pensada para representar personajes y objetos del juego como clases.

¿Qué significa que permite "tomar mucho o poco" de la librería?
Significa que Pygame es modular y flexible: no te obliga a usar todo, sino que eliges qué partes necesitas.
• Tomar poco: puedes usar solo pygame.display para abrir una ventana y dibujar formas, y escribir tú mismo toda la lógica (movimiento, colisiones, puntaje) con tus propias variables, listas y funciones.
• Tomar mucho: puedes apoyarte en módulos que ya resuelven tareas comunes, como pygame.mixer (sonido), pygame.font (texto), pygame.sprite (grupos de objetos y colisiones), pygame.Rect (rectángulos y colisiones) y pygame.time.Clock (control de velocidad).
