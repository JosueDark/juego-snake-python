import pygame
import sys
import time
import random

# Inicializar Pygame
pygame.init()

# Definir colores
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Configuración del juego
width, height = 600, 400
snake_size = 20
snake_speed = 15

# Crear la pantalla
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Función principal del juego
def gameLoop():
    game_over = False

    # Inicializar la serpiente
    snake = [(width // 2, height // 2)]
    snake_direction = (1, 0)

    # Inicializar la comida
    food = spawn_food()

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_direction != (0, 1):
                    snake_direction = (0, -1)
                elif event.key == pygame.K_DOWN and snake_direction != (0, -1):
                    snake_direction = (0, 1)
                elif event.key == pygame.K_LEFT and snake_direction != (1, 0):
                    snake_direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and snake_direction != (-1, 0):
                    snake_direction = (1, 0)

        # Mover la serpiente
        snake[0] = (snake[0][0] + snake_direction[0] * snake_size,
                    snake[0][1] + snake_direction[1] * snake_size)

        # Verificar colisiones
        if snake[0] == food:
            food = spawn_food()
            snake.append((-snake_size, -snake_size))  # Agregar una nueva sección a la serpiente

        # Verificar colisiones con los bordes
        if snake[0][0] < 0 or snake[0][0] >= width or snake[0][1] < 0 or snake[0][1] >= height:
            game_over = True

        # Verificar colisiones consigo misma
        if len(snake) > 1 and snake[0] in snake[1:]:
            game_over = True

        # Mover el cuerpo de la serpiente
        snake[1:] = [(x, y) for x, y in snake[:-1]]

        # Dibujar en la pantalla
        screen.fill(black)
        draw_snake(snake)
        draw_food(food)
        pygame.display.flip()

        # Controlar la velocidad del juego
        pygame.time.Clock().tick(snake_speed)

# Función para dibujar la serpiente en la pantalla
def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, white, (segment[0], segment[1], snake_size, snake_size))

# Función para dibujar la comida en la pantalla
def draw_food(food):
    pygame.draw.rect(screen, red, (food[0], food[1], snake_size, snake_size))

# Función para generar una nueva posición para la comida
def spawn_food():
    x = random.randrange(0, width - snake_size, snake_size)
    y = random.randrange(0, height - snake_size, snake_size)
    return x, y

if __name__ == "__main__":
    gameLoop()
    pygame.quit()
    sys.exit()
