# Bronnen:
# Chat gpt Algemene controle 2/4/2025
# Cursus [Hoorcollege] Git 2/04/2025
# Cursus [Werkcollege] JSON api 2/04/2025
# https://github.com/microsoft/api-guidelines   2/04/2025
# https://realpython.com/api-integration-in-python/?utm_source=realpython&utm_medium=web&utm_campaign=related-   2/04/2025
# https://en.wikipedia.org/wiki/WTA_rankings  2/04/2025
# https://en.wikipedia.org/wiki/ATP_rankings  2/04/2025
# https://my-json-server.typicode.com/Pepe-max400/Mijn_Project_Tennis  2/04/2025
# https://canvas.kdg.be/courses/49875/pages/hoorcollege-web-apps-in-python?module_item_id=1139846  2/4/2025
# https://stock.adobe.com/be_nl/search/images?k=tennis+logo  2/4/2025

from flask import Flask, render_template
import requests

app = Flask(__name__)
API_URL = "https://my-json-server.typicode.com/Pepe-max400/Mijn_Project_Tennis"

@app.route('/')
def home():
    return render_template('index.html', 
                         title="Tennis API Dashboard",
                         name="Tennisliefhebber")

@app.route('/spelers')
def show_spelers():
    spelers = requests.get(f"{API_URL}/tennisspelers").json()
    return render_template('spelers.html', spelers=spelers)

@app.route('/toernooien')
def show_toernooien():
    toernooien = requests.get(f"{API_URL}/toernooien").json()
    return render_template('toernooien.html', toernooien=toernooien)

@app.route('/stats')
def show_stats():
    spelers = requests.get(f"{API_URL}/tennisspelers").json()
    stats = {
        'total': len(spelers),
        'active': sum(1 for p in spelers if p['actief']),
        'countries': len({p['land'] for p in spelers})
    }
    return render_template('stats.html', stats=stats)

if __name__ == '__main__':
    app.run(debug=True)
    