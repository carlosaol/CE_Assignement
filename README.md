# CE Assignement repository
## Autor: [Carlos Armando Ortiz López](https://github.com/carlosaol)
This public repository was created for the Curriculum Engineer Assignment. It contains an exercise on building and training your first Neural Network. To run the example, clone this repo to your PC.

The exercise is located in "Notebooks\First_Neural_Network.ipynb",  You can run it if you have Jupyter and the dependencies listed in the requirements.txt file. A Docker image is provided for easy execution.

## Instructions 

### 1. Clone the repository into your projects directory:
```
git clone https://github.com/carlosaol/CE_Assignement.git
```

### 2. Build the docker image:
* Open a terminal in the repository base folder and use the following commands to build the Docker image:
    
```
docker build --tag jupyter-docker .
```
        
* Once the image is built, run and launch the container using the following command.
    
```
docker run -it --rm -p 8888:8888 -v ${pwd}/Notebooks:/home/jovyan/work jupyter-docker start-notebook.py --ServerApp.root_dir=/home/jovyan/work
```
### 3. Open the Jupyter Notebook:
* Once you run the dockerfile, you should see the links to the server in your terminal; click or copy to your browser.

![image](https://github.com/user-attachments/assets/729e438d-d4a1-4581-854a-d52fd4b3878b)

* Open the Notebook First_Neural_Network and follow the instructions.

![image](https://github.com/user-attachments/assets/b21c2b7d-9cb1-41fe-8ecb-1f056da7c5a0)


  


