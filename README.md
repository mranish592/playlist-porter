#### 1. Clone the repository:

```bash
git clone [https://github.com/mranish592/playlist-porter.git](https://github.com/mranish592/playlist-porter.git)
cd playlist-porter
```

#### 2. Create and activate a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

#### 3. Install dependencies:

```bash
pip install -r requirements.txt
```

#### 4. Setup Google oAuth:

[https://ytmusicapi.readthedocs.io/en/stable/setup/oauth.html](https://ytmusicapi.readthedocs.io/en/stable/setup/oauth.html)

1. Search for youtube data api and enable it in the cconsole.
2. Create a consent screen and add the scope for all youtube api.
3. Create credential as TV device.
4. run commande in terminal:

```bash
ytmusicapi oauth
```

#### 5. Run the python script:

Replace .env.example with .env

```bash
venv/bin/python app.py
```
