def reset():
    msg = {
        "ly": 0,
        "lx": 0,
        "rx": 0,
        "ry": 0,
        "L2": 0,
        "R2": 0,
        "R1": 0,
        "L1": 0,
        "dpady": 0,
        "dpadx": 0,
        "x": 0,
        "square": 0,
        "circle": 0,
        "triangle": 0,
        "message_rate": MESSAGE_RATE,
    }
    return msg

def movement_L1():
        msg = {
            "ly": 0,
            "lx": 0,
            "rx": 0,
            "ry": 0,
            "L2": 0,
            "R2": 0,
            "R1": 0,
            "L1": 1,
            "dpady": 0,
            "dpadx": 0,
            "x": 0,
            "square": 0,
            "circle": 0,
            "triangle": 0,
            "message_rate": MESSAGE_RATE,
        }
        return msg

def movement_dpapx():
    msg = {
        "ly": 0,
        "lx": 0,
        "rx": 0,
        "ry": 0,
        "L2": 0,
        "R2": 0,
        "R1": 0,
        "L1": 0,
        "dpady": 0,
        "dpadx": -1,
        "x": 0,
        "square": 0,
        "circle": 0,
        "triangle": 0,
        "message_rate": MESSAGE_RATE,
    }
    return msg

def movement_dpapy():
    msg = {
        "ly": 0,
        "lx": 0,
        "rx": 0,#counter
        "ry": 0,#clockwise
        "L2": 0,
        "R2": 0,
        "R1": 0,
        "L1": 0,
        "dpady": 1,
        "dpadx": 0,
        "x": 0,
        "square": 0,
        "circle": 0,
        "triangle": 0,
        "message_rate": MESSAGE_RATE,
    }
def movement_rx():  
    msg = {
        "ly": 0,
        "lx": 0,
        "rx": 0.3,#counter
        "ry": 0,#clockwise
        "L2": 0,
        "R2": 0,
        "R1": 0,
        "L1": 0,
        "dpady": 0,
        "dpadx": 0,
        "x": 0,
        "square": 0,
        "circle": 0,
        "triangle": 0,
        "message_rate": MESSAGE_RATE,
    }
    return msg

def movement_ry():
    msg = {
        "ly": 0,
        "lx": 0,
        "rx": 0,#counter
        "ry": 0.3,#clockwise
        "L2": 0,
        "R2": 0,
        "R1": 0,
        "L1": 0,
        "dpady": 0,
        "dpadx": 0,
        "x": 0,
        "square": 0,
        "circle": 0,
        "triangle": 0,
        "message_rate": MESSAGE_RATE,
    }
    return msg