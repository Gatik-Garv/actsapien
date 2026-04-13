from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
import uvicorn
import os

app = FastAPI()

# ── OpenEnv reset endpoint Scaler checker requires ───────────────────────────
@app.post("/reset")
async def reset():
    return JSONResponse({"status": "ok", "message": "Environment reset successfully"})

@app.get("/health")
async def health():
    return JSONResponse({"status": "healthy", "app": "ActSapien"})

# ── Serve static frontend ─────────────────────────────────────────────────────
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return FileResponse("static/index.html")

@app.get("/{full_path:path}")
async def catch_all(full_path: str):
    file_path = f"static/{full_path}"
    if os.path.exists(file_path):
        return FileResponse(file_path)
    return FileResponse("static/index.html")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7860)
