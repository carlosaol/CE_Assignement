This is a public repositoy created  for the Curriculum Engineer Assignment
in this repo an excersise on how to build and train your first Neural Network is presented
in order to run the example clone this repo to your PC
the excersise is located in "Notebooks\First_Neural_Network.ipynb"
you can run this if you have jupyter and the dependencies listed in the "requirements.txt" file
also a Docker image is provided for easy execution.

- open a terminal in the repository base folder, and use the following comands to build the Docker image:

    docker build --tag jupyter-docker .
    
- once the image is builded use the following comand to run launch the container

    docker run -it --rm -p 8888:8888 -v ${pwd}/Notebooks:/home/jovyan/work jupyter-docker start-notebook.py --ServerApp.root_dir=/home/jovyan/work

- open the Jupyter Notebbok, once you run the docker file you should see the links to the server in your terminal, just click or copy to to your browser

  ![image](https://github.com/user-attachments/assets/729e438d-d4a1-4581-854a-d52fd4b3878b)

- Open the Notebook First_Neural_Network and follow the instructions

  ![image](https://github.com/user-attachments/assets/fe4761ec-bc66-4261-8f10-8ab0fb2059f7)

  


