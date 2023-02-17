def on_received_number(receivedNumber):
    pins.servo_write_pin(AnalogPin.P0, receivedNumber)
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    global channel
    channel += 10
    radio.set_group(channel)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global channel
    channel += 1
    radio.set_group(channel)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    radio.set_group(0)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

channel = 0
channel = 0
radio.set_group(channel)

def on_forever():
    basic.show_string("C")
    basic.show_number(channel)
basic.forever(on_forever)
