from pico2d import *

open_canvas()

mario = load_image('mario.png')
kirby = load_image('kirby.png')

frame = 0

while True:
    # for x in range(10, 241, 33):
    #     clear_canvas()
    #     kirby.clip_draw(x, 1120, 30, 30, 400, 300, 400, 400)
    #     update_canvas()
    #     frame = (frame + 1) % 8
    #     delay(0.2)
    #
    # for x in range(8, 239, 33):
    #     clear_canvas()
    #     kirby.clip_draw(x, 1054, 33, 33, 400, 300, 400, 400)
    #     update_canvas()
    #     frame = (frame + 1) % 8
    #     delay(0.2)
    #
    # for x in range(8, 328, 32):
    #     clear_canvas()
    #     kirby.clip_draw(x, 1019, 32, 32, 400, 300, 400, 400)
    #     update_canvas()
    #     frame = (frame + 1) % 8
    #     delay(0.2)
    #
    # for x in range(7, 347, 34):
    #     clear_canvas()
    #     kirby.clip_draw(x, 980, 34, 34, 400, 300, 400, 400)
    #     update_canvas()
    #     frame = (frame + 1) % 8
    #     delay(0.2)

    t = 31
    k = 31
    inhale_frames = [(11, 630), (42, 631), (74, 632),
                     (105, 633), (133, 634), (160, 635), (187, 630)]

    for x, y in inhale_frames:
        clear_canvas()

        kirby.clip_draw(x, y, 31, t, 400, 300, 400, 400)
        update_canvas()
        delay(0.2)
        if y >= 630:
            t += 1
        elif y == 630:
            t = 0



close_canvas()
