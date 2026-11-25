from TikTokApi import TikTokApi
import asyncio

async def main():
    # Inicializamos la API
    api = TikTokApi()
    
    # Buscamos videos con la etiqueta 'viral'
    # count=5 significa que solo traiga 5 resultados para probar
    videos = api.by_hashtag('viral', count=5)
    
    print("--- Resultados de Búsqueda ---")
    for video in videos:
        # Accedemos al título del video
        print(f"Título: {video.title}")
        # Si quieres ver el enlace, descomenta la siguiente línea:
        # print(f"URL: https://www.tiktok.com/@{video.author.unique_id}/video/{video.id}")
        
    print("--- Bot finalizado correctamente ---")

# Ejecutamos la función principal
if __name__ == "__main__":
    asyncio.run(main())
