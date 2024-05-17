import HardwareInterface

angle = 10
servo_params = HardwareInterface.ServoParams
axis_index = 1
leg_index = 2

HardwareInterface.angle_to_position(angle, servo_params, axis_index, leg_index)