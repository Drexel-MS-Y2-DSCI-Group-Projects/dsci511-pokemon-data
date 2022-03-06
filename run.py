import subprocess
import os
import asyncio
from timeit import default_timer as timer
from datetime import timedelta

import merge

async def main():
    # convert ipynb to python for inline execution
    # TODO: remove windows dependency on jupyter
    subprocess.call(['jupyter.exe', 'nbconvert', '--to', 'script', './pokemondb/pokemondb_fetch.ipynb'], shell=True)
    subprocess.call(['jupyter.exe', 'nbconvert', '--to', 'script', './bulbapedia/bulbapedia.ipynb'], shell=True)
    subprocess.call(['jupyter.exe', 'nbconvert', '--to', 'script', './pokeAPI/pokeAPI.ipynb'], shell=True)

    start = timer()
    init = start
    print('Running pokeAPI scrape')
    from pokeAPI import pokeAPI
    end = timer()
    print(f'Finished pokeapi in {timedelta(seconds=end-start)}')

    start = timer()
    print('Running bulbapedia scrape')
    from bulbapedia import bulbapedia
    end = timer()
    print(f'Finished bulbapedia in {timedelta(seconds=end-start)}')

    start = timer()
    print('Running pokemondb scrape')
    from pokemondb import pokemondb_fetch
    end = timer()
    print(f'Finished pokemondb in {timedelta(seconds=end-start)}')

    # cleanup
    for py_file in ['./pokemondb/pokemondb_fetch.py', './bulbapedia/bulbapedia.py', './pokeAPI/pokeAPI.py']:
        if os.path.exists(py_file):
            print(f'removing {py_file}')
            os.remove(py_file)

    print('Merging')
    merge.run()
    print(f'Done in {timedelta(seconds=end-init)}')

if __name__ == '__main__':
    asyncio.run(main())
