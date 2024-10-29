from fastapi import FastAPI, WebSocket
from starlette.websockets import WebSocketDisconnect

app = FastAPI()

@app.websocket_route("/ws/process-complex-query")
async def process_complex_query(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            # Process the received data (query and state)
            response = process_data(data)
            await websocket.send_text(response)
    except WebSocketDisconnect:
        # Handle WebSocket disconnection
        pass

def process_data(data):
    # Implement logic to process the received data
    # and return the response
    return "Processed data: " + data

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
