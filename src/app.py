import argparse
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routers import users, products

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from any origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)


app.include_router(users.router)
app.include_router(products.router)



if __name__ == '__main__':
    argparser = argparse.ArgumentParser(add_help=True)
    argparser.add_argument('--host', dest='host', type=str, default='0.0.0.0', help='The server address')
    argparser.add_argument('--port', dest='port', type=int, default=8080, help='The server port')
    argparser.add_argument('--workers', dest='workers', type=int, default=1, help='The number of workers')
    args = argparser.parse_args()
    uvicorn.run(
        'app:app',
        host=args.host,
        port=args.port,
        workers=args.workers
    )
