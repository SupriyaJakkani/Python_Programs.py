import pygame
import time
import random

#Intializing pygame---
pygame.init()

#Colors---
white = (255, 255, 255) # It follows RGB tuples (RED, GREEN, BLUE)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = ( 50, 153, 213)

# Screen Size---
dis_width = 800
dis_height = 600

# Create the game window---
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("Snake Game")

# Clock to control the speed of the snake---
clock = pygame.time.Clock()

# Snake settings
snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)  # We can use other fonts like---
#("arial","timesnewroman","calibri","consolas","comic sans ms","couriernew","georgia","verdana","tahoma") 

# Function to display the Score---
def Your_score(score):
    value = font_style.render("Your Score: " + str(score), True, white)
    dis.blit(value, [0,0])

# Function to draw snake---
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])

# Game loop function---
def gameLoop():
    game_over = False
    game_close = False

    # width,height/2 means snake start from center
    x1 = dis_width / 2
    y1 = dis_height / 2

    # snake movement 0 means not started 
    x1_change = 0 # horizontal
    y1_change = 0 # vertical

    snake_List = [] # store the segments(pieces) of snake
    Length_of_snake = 1 # start with one segment

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            dis.fill(black)
            message = font_style.render("Game Over! Press Q-Quit or C-Play Again")
            dis.blit(message, [dis_width / 6, dis_height / 3])
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_close = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_DOWN:
                    x1_change = snake_block
                    y1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)

        pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block)/ 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()
gameLoop()

                


                        
