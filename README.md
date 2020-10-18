# Mole Analyzer
AI course final project directed by [bdubreu](https://github.com/bdubreu)

The aim of this project is to detect skin cancer from a mole picture. 

Demo version hosted [here](https://isen--ai-project.herokuapp.com)

<br>

# Installation
* install git [Large File Storage](https://git-lfs.github.com/)
* clone this project
 ```
$ git clone https://github.com/frieeze/moles-analyzer.git
$ cd moles-analyzer
```
* install dependencies `pip install -r requirements`
    > Note : to run the model on GPU remove : `+cpu` on torch and torchvision dependencies <br>
    > Ex : `torch==1.6.0+cpu` => `torch==1.6.0` and `torchvision==0.7.0+cpu` => `torchvision==0.7.0`

# Run
## Production 
```
$ gunicorn app:app
```
## Development
```
$ python app.py
```