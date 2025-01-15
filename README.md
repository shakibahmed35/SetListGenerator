# Setlist Generator

* This program retrieves a setlist from Setlist.fm and automatically creates a corresponding playlist on Spotify.

## Getting Started

### Dependencies

* All Necessary files are in the environment.yml
* Core Dependencies
    * BeautifulSoup
    * Spotipy

### Installing

* Install all necessary dependencies
* You will need to create a .env file containing you spotipy credentials
    * Enter the spotify developer page and log into your account
    * Open the project and open settings
    * Here you will need your client id, client secret and redirect url
    * store these in a .env file with the corresponding names

### Executing program

* To execute this program run the file playlistGenerator.py
* After find the Set in which you are attending on Setlist.fm and paste that link
* Then just type the artists name in and now there will be a playlist uploaded to spotify with the corresponding songs
* It will then give a list of all the songs in the Setlist and whether it was added to playlist or not found to add


## Help

For major issues reference the spotipy documentation

## Authors

Contributors names and contact info

* Shayaan Ahmed  
[@Shaydoge](https://github.com/Shaydoge)
[@shakibahmed35](https://github.com/shakibahmed35)

## Version History

* 1.0
    * Initial Release

## License

This project is unlicensed - see the license.txt file for details

## Acknowledgments

Inspiration, code snippets, etc.
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [setlist.fm](https://www.setlist.fm/)
* [spotipy](https://spotipy.readthedocs.io/en/2.24.0/index.html#)