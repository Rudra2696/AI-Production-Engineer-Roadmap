import os

directory_path = r'C:\Users\Rudra Patel\OneDrive\Desktop\AI-Production-Engineer-Roadmap\Phase-1-Foundations\Week-1-Python\Python-Basics\dir'

l=os.listdir(directory_path)

for i, file in enumerate(l,start=10):
    os.rename(os.path.join(directory_path,file),os.path.join(directory_path,f'file{i}.txt'))

print("Successfully renamed all files!")