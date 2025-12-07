import os

directory_path = r'C:\Users\Rudra Patel\OneDrive\Desktop\AI-Production-Engineer-Roadmap\Phase-1-Foundations\Week-1-Python\Python-Basics\dir'

# If directory does not exists
os.makedirs(directory_path,exist_ok=True)

for i in range(10):
    file_path = os.path.join(directory_path,f'file{i}.txt')
    with open(file_path,'w') as f :
        f.write(f"Hello this is file number {i}")

print("Successfully created all files")