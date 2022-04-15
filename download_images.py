import json
import urllib.request

def generate_slug(name: str):
    return name.lower().replace(" ", "-").replace(":", "").replace(".", "").replace("’", "").replace("♀", "-f").replace("♂", "-m").replace("é", "e")

def main():
    base_url = "https://img.pokemondb.net/sprites/home/normal/{:}.png"
    with open("pokedex.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    pokemon = [p for p in data["list"]]
    failed = []
    for p in pokemon:
        name = generate_slug(p["localization"]["en"])
        url = base_url.format(name)
        print("Downloading from {:}...".format(url))
        try:
            opener = urllib.request.URLopener()
            opener.addheader("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39")
            filename, headers = opener.retrieve(url, "{:04d}_{:}.png".format(p["nr"], name))
        except Exception as e:
            print(e)
            failed.append(name)
    print("Finished downloading. Failed: " + str(failed))

if __name__ == "__main__":
    main()