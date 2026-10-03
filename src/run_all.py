import subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
subprocess.run([sys.executable,str(ROOT/'src/validate.py')],check=True)
subprocess.run([sys.executable,str(ROOT/'src/analysis_pipeline.py')],check=True)
subprocess.run([sys.executable,str(ROOT/'src/visualize.py')],check=True)
print('ALL ANALYTICS COMPLETED')
