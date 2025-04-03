def on_microbit_id_io_p8_pin_evt_rise():
    global STEPR
    STEPR += 1
control.on_event(EventBusSource.MICROBIT_ID_IO_P8,
    EventBusValue.MICROBIT_PIN_EVT_RISE,
    on_microbit_id_io_p8_pin_evt_rise)

def GO(list2: List[any]):
    global index
    while index <= len(list2):
        if text_list[index] == "FWD":
            MOVE(SR, -1 * SL, 0, 2085)
            MOVE(-255, 255, 30, 0)
        elif text_list[index] == "BWD":
            MOVE(-1 * SR, SL, 0, 2085)
            MOVE(SR, -255, 30, 0)
        elif text_list[index] == "LEFT":
            MOVE(-1 * SR, -1 * SL, 0, 500)
            MOVE(SR, -1 * SL, 30, 0)
        elif text_list[index] == "RIGHT":
            MOVE(SR, SL, 0, 500)
            MOVE(-1 * SR, SL, 30, 0)
        elif text_list[index] == "P":
            MOVE(0, 0, 1000, 0)
        music.ring_tone(784)
        basic.pause(100)
        music.stop_all_sounds()
        index += 1
    index = 0
    music.play(music.string_playable("E D G F B A C5 B ", 120),
        music.PlaybackMode.UNTIL_DONE)
    basic.show_number(STEPR - STEPL)
    basic.show_icon(IconNames.HAPPY)

def on_microbit_id_io_p8_pin_evt_fall():
    global STEPR
    STEPR += 1
control.on_event(EventBusSource.MICROBIT_ID_IO_P8,
    EventBusValue.MICROBIT_PIN_EVT_FALL,
    on_microbit_id_io_p8_pin_evt_fall)

def on_button_pressed_ab():
    global STEPR, SR
    STEPR = 100
    while abs(STEPR - STEPL) > 10:
        MOVE(SR, -1 * SL, 1000, 0)
        motorbit.motor_run_dual(motorbit.Motors.M1, -1 * SR, motorbit.Motors.M2, SL)
        basic.pause(30)
        motorbit.motor_stop_all()
        if STEPR - STEPL < -20:
            SR += -3
        elif STEPR - STEPL > 20:
            SR += 3
        else:
            break
    basic.show_number(SR)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_touch_touched():
    global text_list
    music.ring_tone(247)
    basic.pause(100)
    music.stop_all_sounds()
    if makerbit.is_touched(makerbit.touch_sensor_index(TouchSensor.T7)):
        basic.show_arrow(ArrowNames.EAST)
        text_list.append("LEFT")
    elif makerbit.is_touched(makerbit.touch_sensor_index(TouchSensor.T8)):
        basic.show_string("P")
        text_list.append("P")
    elif makerbit.is_touched(makerbit.touch_sensor_index(TouchSensor.T9)):
        basic.show_icon(IconNames.SMALL_HEART)
    elif makerbit.is_touched(makerbit.touch_sensor_index(TouchSensor.T10)):
        basic.show_arrow(ArrowNames.NORTH)
        text_list.append("FWD")
    elif makerbit.is_touched(makerbit.touch_sensor_index(TouchSensor.T11)):
        basic.show_icon(IconNames.YES)
        GO(text_list)
    elif makerbit.is_touched(makerbit.touch_sensor_index(TouchSensor.T12)):
        basic.show_arrow(ArrowNames.SOUTH)
        text_list.append("BWD")
    elif makerbit.is_touched(makerbit.touch_sensor_index(TouchSensor.T15)):
        basic.show_arrow(ArrowNames.WEST)
        text_list.append("RIGHT")
    elif makerbit.is_touched(makerbit.touch_sensor_index(TouchSensor.T16)):
        basic.show_icon(IconNames.NO)
        text_list = []
        motorbit.motor_stop_all()
    elif makerbit.is_touched(makerbit.touch_sensor_index(TouchSensor.T5)):
        basic.show_string("C")
    elif makerbit.is_touched(makerbit.touch_sensor_index(TouchSensor.T13)):
        basic.show_string("H")
    elif makerbit.is_touched(makerbit.touch_sensor_index(TouchSensor.T14)):
        basic.show_string("L")
    elif makerbit.is_touched(makerbit.touch_sensor_index(TouchSensor.T6)):
        basic.show_string("O")
makerbit.on_touch(TouchSensor.ANY, TouchAction.TOUCHED, on_touch_touched)

def MOVE(M1: number, M2: number, T: number, STP: number):
    global STEPR, STEPL
    STEPR = 0
    STEPL = 0
    motorbit.motor_run_dual(motorbit.Motors.M1, M1, motorbit.Motors.M2, M2)
    while STEPR < STP:
        basic.pause(0)
    basic.pause(T)
    motorbit.motor_stop_all()

def on_microbit_id_io_p12_pin_evt_fall():
    global STEPL
    STEPL += 1
control.on_event(EventBusSource.MICROBIT_ID_IO_P12,
    EventBusValue.MICROBIT_PIN_EVT_FALL,
    on_microbit_id_io_p12_pin_evt_fall)

def on_microbit_id_io_p12_pin_evt_rise():
    global STEPL
    STEPL += 1
control.on_event(EventBusSource.MICROBIT_ID_IO_P12,
    EventBusValue.MICROBIT_PIN_EVT_RISE,
    on_microbit_id_io_p12_pin_evt_rise)

index = 0
text_list: List[str] = []
SL = 0
SR = 0
STEPL = 0
STEPR = 0
basic.show_icon(IconNames.HAPPY)
STEPR = 0
STEPL = 0
SR = 240
SL = 255
text_list = []
pins.set_events(DigitalPin.P8, PinEventType.EDGE)
pins.set_events(DigitalPin.P12, PinEventType.EDGE)