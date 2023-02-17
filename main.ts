radio.onReceivedNumber(function (receivedNumber) {
    pins.servoWritePin(AnalogPin.P0, receivedNumber)
})
input.onButtonPressed(Button.A, function () {
    channel += 10
    radio.setGroup(channel)
})
input.onButtonPressed(Button.AB, function () {
    basic.showNumber(channel)
    basic.showString("C")
})
input.onButtonPressed(Button.B, function () {
    channel += 1
    radio.setGroup(channel)
})
input.onGesture(Gesture.Shake, function () {
    radio.setGroup(0)
})
let channel = 0
basic.showString("C")
basic.showNumber(channel)
channel = 34
radio.setGroup(channel)
