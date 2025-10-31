import { setupCanvas, handleDrawing } from "./canvas.js";
import { connectWebRTC } from "./webrtc.js";
import { saveCanvasState } from "./api.js";

document.getElementById("joinBtn").onclick = () => {
  const roomId = document.getElementById("roomInput").value;
  connectWebRTC(roomId);
};

document.getElementById("saveBtn").onclick = () => {
  saveCanvasState();
};

setupCanvas();
handleDrawing();