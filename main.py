def on_button_pressed_a():
    input.calibrate_compass()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_forever():
    if input.compass_heading() < 340 and input.compass_heading() >= 180:
        pass
    elif False:
        pass
    else:
        pass
basic.forever(on_forever)
