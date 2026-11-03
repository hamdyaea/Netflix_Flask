This is the source code of : https://hamdyaea.pythonanywhere.com/     
    
    
    
Developer : Hamdy Abou El Anein     
hamdy.aea@protonmail.com    


## Safe snapshot workflow

Install `requirements.txt` in a virtual environment. `flask --app main run` renders `instance/movies.json` (override with `NETFLIX_SNAPSHOT`). To refresh explicitly, set `UNOGS_RAPIDAPI_KEY` and run `python3 downloader.py --output instance/movies.json`. The API subscription and endpoint must be checked before deployment; tests mock all HTTP. There is no automatic PythonAnywhere reload.

Legacy HTML text files remain untouched but are no longer rendered: the new JSON snapshot uses normal Jinja escaping to prevent catalogue HTML injection. Missing/invalid data returns 503. `python3 -m unittest -v` runs five offline tests with temporary files. No deployment or live API request performed.
