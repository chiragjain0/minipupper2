import numpy as np

from MangDang.mini_pupper.HardwareInterface import HardwareInterface

hardware_interface = HardwareInterface()

joint_positions = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0]*1

lf1_position = joint_positions[0]
lf2_position = joint_positions[1]
lf3_position = joint_positions[2]
rf1_position = joint_positions[3]
rf2_position = joint_positions[4]
rf3_position = joint_positions[5]
lb1_position = joint_positions[6]
lb2_position = joint_positions[7]
lb3_position = joint_positions[8]
rb1_position = joint_positions[9]
rb2_position = joint_positions[10]
rb3_position = joint_positions[11]

joint_angles = np.array([
            [rf1_position, lf1_position, rb1_position, lb1_position],
            [rf2_position, lf2_position, rb2_position, lb2_position],
            [rf2_position + rf3_position, lf2_position + lf3_position,
             rb2_position + rb3_position, lb2_position + lb3_position]
        ])

hardware_interface.set_actuator_postions(joint_angles)

