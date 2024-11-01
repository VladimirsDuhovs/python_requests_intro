
## Python packages

https://pypi.org/project/pip/

## Install Python on Ubuntu

```bash
sudo apt install python3
```

## Install pip

```bash
sudo apt install python3-pip
```

## Setup virtual environment

1. Install python3-venv

```bash
sudo apt install python3-venv
```

2. Create a new virtual environment

```bash
python3 -m venv python310
```

3. Activate the virtual environment

```bash
source python310/bin/activate
```

** To deactivate run this command

```bash
deactivate
```

## To download packages from requirements.txt

```bash
pip install -r requirements.txt
```