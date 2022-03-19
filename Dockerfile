FROM python:3.8

WORKDIR /app

RUN apt update
RUN apt install -y libsdl-pango-dev ffmpeg texlive-full

RUN pip install manim

CMD manim -p -ql src/circuit_simulator.py RLC
