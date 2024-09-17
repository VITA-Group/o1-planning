import os
for i in range(1,21):
    os.mknod(f"p{i:>02}.pddl.o1-preview")
    os.mknod(f"p{i:>02}.pddl.o1-mini")
    os.mknod(f"p{i:>02}.pddl.gpt4")