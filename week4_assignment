def modify_content(content: str) -> str:
    #Modifying the file content by adding line numbers and convert the text to uppercase.
    lines = content.splitlines()
    modified_lines = [f"{idx + 1}: {line.upper()}" for idx, line in enumerate(lines)]
    return "\n".join(modified_lines)


def main():
    filename = input("Enter the name of the file to read: ")

    try:
        with open(filename, "r") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"❌ Error: The file '{filename}' was not found.")
        return
    except PermissionError:
        print(f"❌ Error: You don’t have permission to read '{filename}'.")
        return
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return

    modified = modify_content(content)

    new_filename = "modified_" + filename
    try:
        with open(new_filename, "w") as f:
            f.write(modified)
        print(f"✅ Success! Modified file saved as '{new_filename}'")
    except Exception as e:
        print(f"❌ Could not write to file: {e}")


if __name__ == "__main__":
    main()
