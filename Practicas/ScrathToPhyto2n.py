try:
    import pygame  # type: ignore[import-not-found]
except ModuleNotFoundError as error:
    if error.name == "pygame":
        raise SystemExit(
            "Pygame no está instalado. Ejecuta: python -m pip install pygame"
        ) from error
    raise
import random

# Inicializar Pygame
pygame.init()

# Configuración de pantalla
ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Atrapa la Galleta")

# Colores
BLANCO = (255, 255, 255)
AZUL = (50, 100, 255)
NARANJA = (255, 165, 0)

# Variables del jugador (Bowl)
bowl_x = ANCHO // 2
bowl_y = ALTO - 60
bowl_ancho = 100
bowl_alto = 30
velocidad = 10

# Variables de la galleta
cookie_x = random.randint(0, ANCHO - 40)
cookie_y = 0
cookie_tam = 40
caida = 5

# Variables del juego
score = 0
vidas = 3

fuente = pygame.font.SysFont(None, 36)

ejecutando = True
while ejecutando:

    # Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Movimiento del bowl
    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_RIGHT]:
        bowl_x += velocidad

    if teclas[pygame.K_LEFT]:
        bowl_x -= velocidad

    # Limitar movimiento
    bowl_x = max(0, min(ANCHO - bowl_ancho, bowl_x))

    # Caída de la galleta
    cookie_y += caida

    # Detectar captura
    bowl_rect = pygame.Rect(bowl_x, bowl_y, bowl_ancho, bowl_alto)
    cookie_rect = pygame.Rect(cookie_x, cookie_y, cookie_tam, cookie_tam)

    if bowl_rect.colliderect(cookie_rect):
        score += 1

        cookie_x = random.randint(0, ANCHO - cookie_tam)
        cookie_y = 0

    # Si llega al fondo
    if cookie_y > ALTO:
        vidas -= 1

        cookie_x = random.randint(0, ANCHO - cookie_tam)
        cookie_y = 0

    # Fondo
    if vidas > 0:
        pantalla.fill(AZUL)
    else:
        pantalla.fill((20, 20, 20))

    # Dibujar bowl
    pygame.draw.ellipse(
        pantalla,
        NARANJA,
        (bowl_x, bowl_y, bowl_ancho, bowl_alto)
    )

    # Dibujar galleta
    pygame.draw.circle(
        pantalla,
        (255, 220, 150),
        (cookie_x + cookie_tam // 2,
         cookie_y + cookie_tam // 2),
        cookie_tam // 2
    )

    # Mostrar puntuación y vidas
    texto_score = fuente.render(f"Score: {score}", True, BLANCO)
    texto_vidas = fuente.render(f"Vidas: {vidas}", True, BLANCO)

    pantalla.blit(texto_score, (10, 10))
    pantalla.blit(texto_vidas, (10, 50))

    # Fin del juego
    if vidas <= 0:
        texto_fin = fuente.render("GAME OVER", True, BLANCO)
        pantalla.blit(texto_fin, (ANCHO // 2 - 80, ALTO // 2))

    pygame.display.flip()
    pygame.time.delay(20)

pygame.quit()