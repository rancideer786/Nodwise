import cv2
import mediapipe as mp

from core.angle_calculator import calculate_angle
from core.posture_classifier import classify_posture

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

class PostureDetector:

    def __init__(self):
        self.cap = cv2.VideoCapture(0)

    def run(self):

        while True:

            success, frame = self.cap.read()

            if not success:
                break

            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = pose.process(rgb)

            if results.pose_landmarks:

                landmarks = results.pose_landmarks.landmark

                nose = landmarks[0]
                left_shoulder = landmarks[11]
                right_shoulder = landmarks[12]

                h, w, _ = frame.shape

                nose_point = (
                    int(nose.x * w),
                    int(nose.y * h)
                )

                shoulder_mid = (
                    int((left_shoulder.x + right_shoulder.x) * w / 2),
                    int((left_shoulder.y + right_shoulder.y) * h / 2)
                )

                vertical = (
                    shoulder_mid[0],
                    shoulder_mid[1] - 100
                )

                angle = calculate_angle(
                    nose_point,
                    shoulder_mid,
                    vertical
                )

                posture = classify_posture(angle)

                cv2.putText(
                    frame,
                    posture,
                    (30, 50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 0),
                    2
                )

                cv2.putText(
                    frame,
                    f"Angle: {int(angle)}",
                    (30, 100),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (255, 255, 0),
                    2
                )

            cv2.imshow("NODWISE", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()
