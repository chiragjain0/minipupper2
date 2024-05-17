import HardwareInterface
from MangDang.mini_pupper.Config import ServoParams, PWMParams
import numpy as np
from MangDang.mini_pupper.ESP32Interface import ESP32Interface

positions = [0, 512, 512, 512, 0, 512, 512, 512, 512, 512, 512, 512]
esp32 = ESP32Interface()
esp32.servos_set_position(positions)
# joint = np.zeros((3, 4))  # Assuming 3 axes and 4 legs

# angle = 10
# servo_params = ServoParams()
# axis_index = 1
# leg_index = 2

# HardwareInterface.angle_to_position(angle, servo_params, axis_index, leg_index)

# pwm_params = PWMParams()

# joint[axis_index, leg_index] = angle

# joint_angles = joint[axis_index, leg_index]
# HardwareInterface.send_servo_commands(pwm_params, servo_params, joint_angles)