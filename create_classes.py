import os

train_dir = "dataset/train"

classes = sorted(
    [d for d in os.listdir(train_dir) if os.path.isdir(os.path.join(train_dir, d))]
)

with open("classes.txt", "w") as f:
    for cls in classes:
        f.write(cls + "\n")

print("classes.txt created successfully!")
print("Total classes:", len(classes))