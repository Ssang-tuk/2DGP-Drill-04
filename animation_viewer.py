from pico2d import *

open_canvas()

mario = load_image('mario.png')
kirby = load_image('kirby.png')

frame = 0

while True:
    for x in range(10, 241, 33):
        clear_canvas()
        kirby.clip_draw(x, 1120, 30, 30, 400, 300, 100, 100)
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.2)

close_canvas()
