import HardwareInterface
from MangDang.mini_pupper.Config import ServoParams, PWMParams


angle = 10
servo_params = ServoParams()
axis_index = 1
leg_index = 2

HardwareInterface.angle_to_position(angle, servo_params, axis_index, leg_index)

pwm_params = PWMParams()
joint_angles = [axis_index, leg_index]
HardwareInterface.send_servo_commands(pwm_params, servo_params, joint_angles)