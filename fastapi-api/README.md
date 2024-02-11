# Start the application on port 8081g
```
python -m uvicorn main:app --reload --port 8081 
```

# Try the hello world endpoint
```
curl http://localhost:8081/my-app/hello-world-path
```
