import subprocess
import sys
import os

print("================================")
print(" STARK VISION SETUP BASLIYOR ")
print("================================")

# requirements kurulumu
try:
    print("Kutuphaneler yukleniyor...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
except subprocess.CalledProcessError:
    print("Kutuphane kurulumu basarisiz!")
    sys.exit(1)

print("Kutuphaneler kuruldu!")

# start.py çalıştır
print("Program baslatiliyor...\n")

try:
    subprocess.call([sys.executable, "start.py"])
except:
    print("start.py calistirilamadi!")