import os
from pathlib import Path

# Pegando o diretório raiz do usuáiro atual
HOME_DIR = os.path.expanduser("~") 
# Criando caminho para onde os vídeos serão baixados
WINDOWS_VIDEO_END_PATH = os.path.join(HOME_DIR, "Videos\\PyTubeDownloads")

# Criando caminho para onde os vídeos serão baixados
LINUX_VIDEO_END_PATH = Path.home() / "Videos/PyTubeDownloads"
