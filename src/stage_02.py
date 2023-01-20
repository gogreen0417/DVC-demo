STAGE="Two"

with open("output/output.txt","r") as f:
    content=f.read()

print(f"cotent read in {STAGE}: {content}")

with open("output/output2.txt","w+") as f:
    f.write(f"stage {STAGE} started succesfully..")