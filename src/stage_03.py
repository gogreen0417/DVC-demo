STAGE="Three"

with open("output/output.txt","r") as f:
    content=f.read()

print(f'out: {content}')

print(f"stage {STAGE} started successfully..")