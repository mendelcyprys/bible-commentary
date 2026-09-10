import os

for folder in os.listdir('.'):
    #exclude .git and .vscode folders
    if folder not in ['.git', '.vscode']:
        if os.path.isdir(folder):
            print(f"Folder: {folder}")
            for chapter in os.listdir(folder):
                print(f"  Chapter: {chapter}")
                for file in os.listdir(os.path.join(folder, chapter)):
                    print(f"    File: {file}")
                    # Rename .txt files to .md
                    if file.endswith('.txt'):
                        old_file_path = os.path.join(folder, chapter, file)
                        new_file_path = os.path.join(folder, chapter, file.replace('.txt', '.md'))
                        os.rename(old_file_path, new_file_path)
                        print(f"      Renamed: {file} to {file.replace('.txt', '.md')}")
                        # add a # at the beginning of the first line of the file
                        with open(new_file_path, 'r+') as f:
                            content = f.readlines()
                            content[0] = '# ' + content[0]
                            f.seek(0)
                            f.writelines(content)
                            print(f"      Added '#' to the beginning of the first line of {file.replace('.txt', '.md')}")
                    