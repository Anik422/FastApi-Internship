from fastapi.requests import Request

def log(tag="My App", message="", request:Request=None):
    with open("log.txt", "a+") as f:
        f.write(f"{tag} : {message}\n")
        f.write(f"\t{request.url}\n")