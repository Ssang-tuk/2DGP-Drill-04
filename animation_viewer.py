from pico2d import *

open_canvas()

mario = load_image('mario.png')
kirby = load_image('kirby.png')

frame = 0

for x in range(0, 800, 10):
    clear_canvas()
    mario.clip_draw(0, 240, 40, 50, x, 90)
    update_canvas()
    frame = (frame + 1) % 8
    delay(0.02)

close_canvas()
