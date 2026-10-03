# CMD

```bash
cd C:\AISE\A2
py -3.13 -m venv venv
.\venv\Scripts\Activate.ps1
```

```bash
python -m pip install requests
python -m pip install uvicorn
python -m pip install fastapi
```

```bash
uvicorn courses:app --reload --port 8080
uvicorn student:app --reload --port 8081
uvicorn recommend:app --reload --port 8082
```
