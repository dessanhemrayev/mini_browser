# A mini-browser Flet app

An example of a minimal Flet app.

Install Flet

```bash
pip install -r requirements.txt
```

To run the app:

```bash
python main.py
```

Build and distribution
----------------------

Workflow builds a one-file executable with PyInstaller and uploads it as an artifact and a GitHub Release asset.

Running on Windows
------------------

- From source (recommended if a Windows build is not available):

```powershell
# Install Python 3.11 or later, then in project folder:
python -m pip install --upgrade pip
pip install -r requirements.txt
python main.py
```

- If a Windows executable is published in Releases (file `mini_browser.exe`):

1. Download `mini_browser.exe` from the repository Releases page or from Actions artifacts.
2. Open `cmd` or PowerShell and run:

```powershell
# in the folder with the downloaded file
.\\mini_browser.exe
```

- To build a native Windows executable locally (on a Windows machine):

```powershell
pip install pyinstaller
pyinstaller --noconfirm --onefile --name mini_browser main.py
# result will be in dist\mini_browser.exe
```

Notes
-----
- Our CI currently builds on Ubuntu; to produce a Windows `.exe` automatically, the workflow must run on `windows-latest` or include a matrix that builds for Windows. I can update the workflow to add a Windows build if you want.
- If the Release artifact is a Linux binary, you will not be able to run it on Windows — use the source-run instructions or request a Windows build.