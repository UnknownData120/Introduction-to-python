def file_navigator():
    filename = input("Enter the filename: ")
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        while True:
            print(f"The file has {len(lines)} lines.")
            line_num = int(input("Enter a line number (0 to quit): "))
            if line_num == 0:
                break
            elif 1 <= line_num <= len(lines):
                print(lines[line_num - 1].strip())
            else:
                print("Invalid line number.")
    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    file_navigator()
