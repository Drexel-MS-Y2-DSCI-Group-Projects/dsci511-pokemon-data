import subprocess
import os
import asyncio
from timeit import default_timer as timer
from datetime import timedelta

import merge

async def main():
    # convert ipynb to python for inline execution
    jupyter_exec = 'jupyter.exe' if os.name == 'nt' else 'jupyter'
    subprocess.call([jupyter_exec, 'nbconvert', '--to', 'script', './pokemondb/pokemondb_fetch.ipynb'], shell=True)
    subprocess.call([jupyter_exec, 'nbconvert', '--to', 'script', './bulbapedia/bulbapedia.ipynb'], shell=True)
    subprocess.call([jupyter_exec, 'nbconvert', '--to', 'script', './pokeAPI/pokeAPI.ipynb'], shell=True)

    start = timer()
    init = start
    print('Running pokeAPI scrape')
    os.environ['poke-prefix'] = './pokeAPI/'
    from pokeAPI import pokeAPI
    end = timer()
    print(f'Finished pokeapi in {timedelta(seconds=end-start)}')

    start = timer()
    print('Running bulbapedia scrape')
    os.environ['poke-prefix'] = './bulbapedia/'
    from bulbapedia import bulbapedia
    end = timer()
    print(f'Finished bulbapedia in {timedelta(seconds=end-start)}')

    start = timer()
    print('Running pokemondb scrape')
    os.environ['poke-prefix'] = './pokemondb/'
    from pokemondb import pokemondb_fetch
    end = timer()
    print(f'Finished pokemondb in {timedelta(seconds=end-start)}')

    start = timer()
    print('Extracting color data')
    os.environ['poke-prefix'] = './pokemondb/'
    os.environ['poke-img-prefix'] = './img'
    from colorAnalysis import pokeColorFinder
    end = timer()
    print(f'Finished color analysis in {timedelta(seconds=end-start)}')

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
