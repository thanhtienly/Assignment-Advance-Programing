- Clone the repository: 
    ````
    git clone https://github.com/thanhtienly/Assignment-Advance-Programing.git
    
    ````
- Go to current project directory: 
    ````
    cd Assignment-Advance-Programing
    
    ````
- Create virtualenv: 
    ````
    python -m venv .venv
    
    ````
    or 
    ````
    python3 -m venv .venv
    
    ````
- Active virtualenv:
  (Windows)
    ````
    source .venv/Scripts/activate
    
    ````
    or (Linux + MacOS)
    ````
    source .venv/bin/activate
    
    ````
- Install all requirement packages: 
    ````
    pip install -r requirements.txt
    
    ````
- Create a new transactions file sort by credit & index file
    ````
    python migrate.py
    
    ````
- Run the app: 
    ````
    fastapi dev main.py
    
    ````
    or
    ````
    fastapi run
    
    ````
- Go to the URL below for the result:
    ````
    http://localhost:8000/query?amount=10000&message=yagi&page=1
    
    ````

