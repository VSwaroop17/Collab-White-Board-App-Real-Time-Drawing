# Collab-White-Board-App-Real-Time-Drawing
This project is a web-based collaborative drawing application that allows multiple users to join virtual rooms and draw on a shared canvas in real-time. Built with modern web technologies, it emphasizes low-latency interaction through peer-to-peer communication, making it ideal for creative collaboration, remote brainstorming, or educational tools.


# Collaborative Whiteboard

A ready-to-run collaborative whiteboard app using FastAPI, WebRTC, and MongoDB.

## Features

- Real-time drawing (peer-to-peer WebRTC)
- Multiple users can join a session
- Save/load canvas to MongoDB

## Quick Start

### Backend

1. Install dependencies:
    ```
    cd backend
    pip install -r requirements.txt
    ```
2. Start FastAPI:
    ```
    uvicorn main:app --reload
    ```
   MongoDB must be running locally.

### Frontend

Simply open `frontend/index.html` in your browser.

## Notes

- WebRTC signaling is basic and for demo purposes.
- For production: add authentication, improve signaling logic, host frontend with backend, secure MongoDB, etc.
