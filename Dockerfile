FROM python:3.9

ADD scrambled_strings.py .

RUN pip install numpy
COPY ./demo_files ./demo_files

CMD ["python", "./scrambled_strings.py", "-d", "./demo_files/dictionary_valid.txt", "-i", "./demo_files/input.txt"]