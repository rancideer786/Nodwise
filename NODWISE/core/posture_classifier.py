ANGLE_THRESHOLD = 35

def classify_posture(angle):
    if angle > ANGLE_THRESHOLD:
        return "BAD POSTURE"

    return "GOOD POSTURE"
