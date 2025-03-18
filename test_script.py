import os

OUTPUT_DIR = "output_files"

def output_dir():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    return print(f"✅ Directory '{OUTPUT_DIR}' exists or has been created.")


if __name__=="__main__":
    output_dir()