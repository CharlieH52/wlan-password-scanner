import subprocess
import os

def build():
    # CONFIGURATION VARIABLES
    output_name = "WLAN_SCANNER"
    main_script = "src/main.py"

    command_sequence = [
        "pyinstaller",
        "--windowed",
        "--onefile",
        "--clean",
        f"--name={output_name}",
        main_script
    ]

    subprocess.run(command_sequence)

def clean():
    for folder in ["build", "__pycache__"]:
        if os.path.exists(folder):
            print(f"Eliminando carpeta: {folder}")
            subprocess.run(["rm", "-rf", folder], shell=True)

    if os.path.exists("main.spec"):
        print("Eliminando archivo: main.spec")
        os.remove("main.spec")

if __name__ == "__main__":
    clean()
    build()