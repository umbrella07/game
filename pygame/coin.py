WIDTH = 400
HEIGHT = 400
score = 0
game_over = False
Character1 = Actor("character1")
Character1.pos = 100, 100
water_droplet = Actor("water-droplet")
water_droplet.pos = 200, 200

def draw():
    screen.fill("green")
    Character1.draw()
    water_droplet.draw()
    screen.draw.text("Score: " + str(score), color="black", topleft=(10,10))

