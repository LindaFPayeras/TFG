import subprocess
import time
import webbrowser

def runBackend():
    subprocess.Popen(
        'start cmd /k "uvicorn backend.main:app --host 0.0.0.0 --port 1350"',
        shell=True
    )

def runFrontend():
    subprocess.Popen(
        'start cmd /k "streamlit run front_service/streamlit.py"',
        shell=True
    )

if __name__ == "__main__":
    runBackend()

    time.sleep(2)

    runFrontend()

    time.sleep(3)

    webbrowser.open("http://localhost:8501")