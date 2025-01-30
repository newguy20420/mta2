import requests

def fetch_and_process_playlist():
    url = "https://thetvapp-one.vercel.app/thetvapp"
    output_file = "tta2.txt"

    try:
        # Fetch the playlist
        response = requests.get(url)
        response.raise_for_status()
        
        # Process the playlist
        playlist = response.text
        processed_playlist = "\n".join(
            line for line in playlist.splitlines()
            if not line.startswith("#EXTVLCOPT:")
        )

        # Save the processed playlist to file
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(processed_playlist)
        
        print(f"Playlist successfully processed and saved to {output_file}.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    fetch_and_process_playlist()
