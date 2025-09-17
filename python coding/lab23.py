# Step 1: Define employee skill sets
LP = {"Raunak", "Asad"}         # Python
LJ = {"Raunak", "Kushal" ,"abhi"}       # Java
LN = {"Kushal", "Abhayraj"}     # .NET

# Step 2: Assign employees to specific skill-based projects (only skilled in one)
python_project = LP - LJ - LN
java_project = LJ - LP - LN
dotnet_project = LN - LP - LJ

# Step 3: Identify multi-skilled employees (skilled in 2 or more)
multi_skilled = (LP & LJ) | (LP & LN) | (LJ & LN)

# Step 4: Print the results
print("Python-only project:", python_project)
print("Java-only project:", java_project)
print("DotNet-only project:", dotnet_project)
print("Multi-skilled employees:", multi_skilled)
