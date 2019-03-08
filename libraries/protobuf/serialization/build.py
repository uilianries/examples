#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess
import os
import platform

if __name__ == "__main__":
    subprocess.run("pip install protobuf", shell=True, check=True)
    subprocess.run("mkdir build", shell=True, check=True)
    os.chdir("build")

    if platform.system() == "Windows":
        print("Windows build")

        cmake_generator = os.getenv("CMAKE_GENERATOR", "Visual Studio 14 2015 Win64")
        subprocess.run("conan install ..", shell=True, check=True)
        subprocess.run('cmake .. -G "%s"' % cmake_generator, shell=True, check=True)
        subprocess.run("cmake --build . --config Release", shell=True, check=True)
        subprocess.run("bin/sensor.exe", shell=True, check=True)
        open("__init__.py", 'a').close()
        os.chdir("..")
        subprocess.run("python main.py", shell=True, check=True)
    else:
        print("Unix build")
        subprocess.run("conan install ..", shell=True, check=True)
        subprocess.run("cmake .. -DCMAKE_BUILD_TYPE=Release", shell=True, check=True)
        subprocess.run("cmake --build .", shell=True, check=True)
        subprocess.run("bin/sensor", shell=True, check=True)
        open("__init__.py", 'a').close()
        os.chdir("..")
        subprocess.run("python main.py", shell=True, check=True)