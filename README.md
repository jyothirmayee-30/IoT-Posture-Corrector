# 🧘 IoT Posture Corrector

A smart health wearable designed to improve spinal ergonomics. It monitors the user's back angle and provides immediate feedback to encourage better posture habits.

## 🚀 Features
- **Real-time Tilt Sensing:** Detects deviations from the calibrated "neutral" spine position.
- **Haptic Feedback:** Triggers a vibration motor when slouching is detected for more than 5 seconds.
- **Slouch Duration Analytics:** Logs total "Poor Posture Time" vs "Good Posture Time."
- **Desktop Dashboard:** Visualizes daily progress and spinal health trends.

## ⚙️ Engineering Logic
- **Hardware:** M5Stack Atom Lite interfaces with an MPU6050 6-axis IMU.
- **Software:** Python calculates the Pitch angle ($\theta$) of the spine and tracks how long the user stays outside the $\pm 15^\circ$ safe zone.
