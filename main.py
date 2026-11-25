from TikTokApi import TikTokApi
import asyncio
import os
import requests

async def main():
    # Inicializamos la API
    api = TikTokApi()
    
    # Buscamos videos con la etiqueta 'viral'
    videos = api.by_hashtag('viral', count=5)
    
    print("--- Iniciando descarga de videos ---")
    
    # Creamos una carpeta para guardar los videos si no existe
    if not os.path.exists("videos_descargados"):
        os.makedirs("videos_descargados")

    for i, video in enumerate(videos):
        try:
            # Obtenemos la URL del video
            video_url = video.video_url
            
            if video_url:
                # Descargamos el video
                response = requests.get(video_url, stream=True)
                
                # Nombre del archivo: viral_video_0.mp4, viral_video_1.mp4, etc.
                filename = f"videos_descargados/viral_video_{i}.mp4"
                
                with open(filename, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                
                print(f"✅ Descargado: {filename}")
            else:
                print(f"⚠️ Video {i}: No se encontró URL directa.")
                
        except Exception as e:
            print(f"❌ Error con el video {i}: {e}")

    print("--- Bot finalizado correctamente ---")

# Ejecutamos la función principal
if __name__ == "__main__":
    asyncio.run(main())
