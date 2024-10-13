from collections import defaultdict

file_data = defaultdict(list)
with open('input.txt', 'r') as file:
    for line in file:
        filename, size, unit = line.strip().split()
        size = int(size)
        if unit == 'B':
            size /= 1024
            unit = 'KB'
        if unit == 'MB':
            size *= 1024
            unit = 'KB'
        file_data[filename.split('.')[1]].append((filename, size))

extension_summary = {}
for extension, files in file_data.items():
    total_size = sum(size for _, size in files)
    extension_summary[extension] = total_size

with open('output.txt', 'w') as output_file:
    for extension, total_size in sorted(extension_summary.items()):
        output_file.write(f"{extension}\n")
        for filename, size in sorted(file_data[extension]):
            output_file.write(f"{filename}\n")
        output_file.write(f"----------\nSummary: {int(total_size)} KB\n\n")
