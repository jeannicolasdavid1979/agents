"""
Worker LiveKit Agents minimal (Hermes).
Se connecte au serveur LiveKit et attend des room. Aucun plugin STT/LLM/TTS n est
configure encore : il faut LIVEKIT_URL, LIVEKIT_API_KEY, LIVEKIT_API_SECRET.
"""
import os
from livekit.agents import JobProcess, cli, WorkerOptions

async def entrypoint(ctx):
    ctx.logfn("Agent vocal Hermes connecte a la room " + ctx.room.name)

def prewarm(proc: JobProcess):
    pass

if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint, prewarm_fnc=prewarm))
