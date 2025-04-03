control.onEvent(EventBusSource.MICROBIT_ID_IO_P8, EventBusValue.MICROBIT_PIN_EVT_RISE, function () {
    STEPR += 1
})
function GO (list2: any[]) {
    while (index <= list2.length) {
        basic.showNumber(1 + index)
        if (text_list[index] == "FWD") {
            MOVE(SR, -1 * SL, 0, 2085)
            MOVE(-255, 255, 30, 0)
        } else if (text_list[index] == "BWD") {
            MOVE(-1 * SR, SL, 0, 2085)
            MOVE(SR, -255, 30, 0)
        } else if (text_list[index] == "LEFT") {
            MOVE(-1 * SR, -1 * SL, 0, 500)
            MOVE(SR, -1 * SL, 30, 0)
        } else if (text_list[index] == "RIGHT") {
            MOVE(SR, SL, 0, 500)
            MOVE(-1 * SR, SL, 30, 0)
        } else if (text_list[index] == "P") {
            MOVE(0, 0, 1000, 0)
        }
        music.ringTone(784)
        basic.pause(100)
        music.stopAllSounds()
        index += 1
    }
    index = 0
    music.play(music.stringPlayable("E D G F B A C5 B ", 120), music.PlaybackMode.UntilDone)
    basic.showIcon(IconNames.Happy)
}
control.onEvent(EventBusSource.MICROBIT_ID_IO_P8, EventBusValue.MICROBIT_PIN_EVT_FALL, function () {
    STEPR += 1
})
input.onButtonPressed(Button.AB, function () {
    STEPR = 100
    while (Math.abs(STEPR - STEPL) > 10) {
        MOVE(SR, -1 * SL, 500, 0)
        motorbit.MotorRunDual(motorbit.Motors.M1, -1 * SR, motorbit.Motors.M2, SL)
        basic.pause(30)
        motorbit.MotorStopAll()
        if (STEPR - STEPL < -10) {
            if (SL < 255) {
                SL += 2
            } else {
                SR += -2
            }
        } else if (STEPR - STEPL > 10) {
            if (SR < 255) {
                SR += 2
            } else {
                SL += -2
            }
        }
    }
})
makerbit.onTouch(TouchSensor.Any, TouchAction.Touched, function () {
    music.ringTone(247)
    basic.pause(100)
    music.stopAllSounds()
    if (makerbit.isTouched(makerbit.touchSensorIndex(TouchSensor.T7))) {
        basic.showArrow(ArrowNames.East)
        text_list.push("LEFT")
    } else if (makerbit.isTouched(makerbit.touchSensorIndex(TouchSensor.T8))) {
        basic.showString("P")
        text_list.push("P")
    } else if (makerbit.isTouched(makerbit.touchSensorIndex(TouchSensor.T9))) {
        basic.showIcon(IconNames.SmallHeart)
    } else if (makerbit.isTouched(makerbit.touchSensorIndex(TouchSensor.T10))) {
        basic.showArrow(ArrowNames.North)
        text_list.push("FWD")
    } else if (makerbit.isTouched(makerbit.touchSensorIndex(TouchSensor.T11))) {
        basic.showIcon(IconNames.Yes)
        GO(text_list)
    } else if (makerbit.isTouched(makerbit.touchSensorIndex(TouchSensor.T12))) {
        basic.showArrow(ArrowNames.South)
        text_list.push("BWD")
    } else if (makerbit.isTouched(makerbit.touchSensorIndex(TouchSensor.T15))) {
        basic.showArrow(ArrowNames.West)
        text_list.push("RIGHT")
    } else if (makerbit.isTouched(makerbit.touchSensorIndex(TouchSensor.T16))) {
        basic.showIcon(IconNames.No)
        text_list = []
        motorbit.MotorStopAll()
        music.ringTone(554)
        basic.pause(500)
        music.stopAllSounds()
        basic.showIcon(IconNames.Happy)
    } else if (makerbit.isTouched(makerbit.touchSensorIndex(TouchSensor.T5))) {
        basic.showString("C")
    } else if (makerbit.isTouched(makerbit.touchSensorIndex(TouchSensor.T13))) {
        basic.showString("H")
    } else if (makerbit.isTouched(makerbit.touchSensorIndex(TouchSensor.T14))) {
        basic.showString("L")
    } else if (makerbit.isTouched(makerbit.touchSensorIndex(TouchSensor.T6))) {
        basic.showString("O")
    }
})
function MOVE (M1: number, M2: number, T: number, STP: number) {
    STEPR = 0
    STEPL = 0
    motorbit.MotorRunDual(motorbit.Motors.M1, M1, motorbit.Motors.M2, M2)
    while (STEPR < STP) {
        basic.pause(0)
    }
    basic.pause(T)
    motorbit.MotorStopAll()
}
control.onEvent(EventBusSource.MICROBIT_ID_IO_P12, EventBusValue.MICROBIT_PIN_EVT_FALL, function () {
    STEPL += 1
})
control.onEvent(EventBusSource.MICROBIT_ID_IO_P12, EventBusValue.MICROBIT_PIN_EVT_RISE, function () {
    STEPL += 1
})
let index = 0
let text_list: string[] = []
let SL = 0
let SR = 0
let STEPL = 0
let STEPR = 0
basic.showIcon(IconNames.Happy)
motorbit.MotorStopAll()
STEPR = 0
STEPL = 0
SR = 240
SL = 255
text_list = []
pins.setEvents(DigitalPin.P8, PinEventType.Edge)
pins.setEvents(DigitalPin.P12, PinEventType.Edge)
