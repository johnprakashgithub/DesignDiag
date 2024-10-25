import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create a figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Add a title
ax.set_title('Remap Purge Plugin in Apache Traffic Server (ATS)', fontsize=16)

# Hide axes
ax.axis('off')

# Define the boxes and arrows with better alignment
boxes = [
    {"xy": (0.1, 0.7), "width": 0.1, "height": 0.1, "label": "Client"},
    {"xy": (0.45, 0.7), "width": 0.1, "height": 0.1, "label": "ATS Server"},
    {"xy": (0.8, 0.7), "width": 0.1, "height": 0.1, "label": "Cache"},
    {"xy": (0.45, 0.4), "width": 0.1, "height": 0.05, "label": "Remap Purge Plugin"},
    {"xy": (0.45, 0.1), "width": 0.1, "height": 0.05, "label": "Configuration Files"}
]

arrows = [
    {"start": (0.3, 0.75), "end": (0.4, 0.75), "label": "PURGE Request"},
    {"start": (0.6, 0.75), "end": (0.7, 0.75), "label": ""},
    {"start": (0.5, 0.7), "end": (0.5, 0.5), "label": ""},
    {"start": (0.5, 0.35), "end": (0.5, 0.2), "label": ""}
]

# Add boxes to the plot
for box in boxes:
    rect = patches.FancyBboxPatch(box["xy"], box["width"], box["height"], boxstyle="round,pad=0.1", edgecolor="black", facecolor="lightblue")
    ax.add_patch(rect)
    bbox = rect.get_bbox()
    cx = bbox.x0 + bbox.width / 2
    cy = bbox.y0 + bbox.height / 2
    ax.annotate(box["label"], (cx, cy), color='black', weight='bold', fontsize=12, ha='center', va='center')

# Add arrows to the plot
for arrow in arrows:
    ax.annotate("", xy=arrow["end"], xytext=arrow["start"], arrowprops=dict(arrowstyle="->", lw=2))
    if arrow["label"]:
        ax.annotate(arrow["label"], xy=((arrow["start"][0] + arrow["end"][0]) / 2, (arrow["start"][1] + arrow["end"][1]) / 2),
                    textcoords="offset points", xytext=(5,-5), ha='center', fontsize=10)

# Show the plot
plt.show()

