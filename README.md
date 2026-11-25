# Importamos la librería necesaria
from TikTokApi import TikTokApi
import asyncio

async def main():
    # Iniciamos el bot
    api = TikTokApi()
    
    # Buscamos videos virales con una etiqueta específica
    videos = api.by_hashtag('viral', count=5)
    
    print("Videos encontrados:")
    for video in videos:
        print(f"- {video.title}")
        
    # Aquí podrías agregar lógica para descargar o dar like
    print("Bot ejecutado correctamente.")

# Ejecutamos la función
if __name__ == "__main__":
    asyncio.run(main())
