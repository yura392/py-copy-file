def copy_file(command: str) -> None:
    parts = command.strip().split()

    # Expecting format: cp source target
    if len(parts) != 3 or parts[0] != "cp":
        print("Invalid command format. Use: cp <source> <target>")
        return

    _, src, dst = parts

    # Do nothing if source and destination are the same
    if src == dst:
        return

    # Copy file content
    try:
        with open(src, "r", encoding="utf-8") as file_in, open(dst, "w", encoding="utf-8") as file_out:
            for line in file_in:
                file_out.write(line)
    except FileNotFoundError:
        print(f"Source file '{src}' not found.")
    except Exception as e:
        print(f"Error copying file: {e}")
