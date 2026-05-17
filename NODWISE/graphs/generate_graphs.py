import matplotlib.pyplot as plt

components = [
    "Pose",
    "Neck",
    "Temporal",
    "Decision",
    "Threshold",
    "Static",
    "Alert"
]

accuracy = [96.5, 94.2, 92.8, 95.6, 93.7, 94.9, 95.1]
precision = [0.95, 0.93, 0.91, 0.94, 0.92, 0.94, 0.94]
recall = [0.96, 0.94, 0.92, 0.95, 0.93, 0.94, 0.95]
f1 = [0.95, 0.93, 0.91, 0.94, 0.92, 0.94, 0.94]

fps_systems = [
    "Proposed",
    "Deep Learning",
    "Mobile",
    "Wearable",
    "Smart Chair",
    "Hybrid"
]

fps_values = [25, 25, 20, 18, 12, 22]

before_after = [18.5, 10.2]

# Accuracy Graph
plt.figure(figsize=(10, 5))
plt.bar(components, accuracy)
plt.title("Accuracy Analysis")
plt.xlabel("Components")
plt.ylabel("Accuracy (%)")
plt.savefig("graphs/accuracy_graph.png")
plt.show()

# Precision Graph
plt.figure(figsize=(10, 5))
plt.plot(components, precision, marker='o')
plt.title("Precision Analysis")
plt.xlabel("Components")
plt.ylabel("Precision")
plt.savefig("graphs/precision_graph.png")
plt.show()

# Recall Graph
plt.figure(figsize=(10, 5))
plt.plot(components, recall, marker='o')
plt.title("Recall Analysis")
plt.xlabel("Components")
plt.ylabel("Recall")
plt.savefig("graphs/recall_graph.png")
plt.show()

# F1 Score Graph
plt.figure(figsize=(10, 5))
plt.plot(components, f1, marker='o')
plt.title("F1 Score Analysis")
plt.xlabel("Components")
plt.ylabel("F1 Score")
plt.savefig("graphs/f1_graph.png")
plt.show()

# FPS Graph
plt.figure(figsize=(10, 5))
plt.bar(fps_systems, fps_values)
plt.title("FPS Performance")
plt.xlabel("Systems")
plt.ylabel("Frames Per Second")
plt.savefig("graphs/fps_graph.png")
plt.show()

# User Improvement Graph
plt.figure(figsize=(6, 5))
plt.bar(["Before", "After"], before_after)
plt.title("Average Static Duration Improvement")
plt.ylabel("Minutes")
plt.savefig("graphs/user_improvement.png")
plt.show()