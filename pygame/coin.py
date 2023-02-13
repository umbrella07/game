WIDTH = 400
HEIGHT = 400
score = 0
game_over = False
Character1 = Actor("Character1")
Character1 pos = 100, 100
water-droplet = Actor("water-droplet")
water-droplet pos = 200, 200

def draw():
    screen.fill("green")
    Character1.draw()
    water-droplet.draw()
    screen.draw.test("Score: " + str(score). color="black". topleft+(10,!0))
