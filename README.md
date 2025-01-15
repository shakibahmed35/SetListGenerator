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
    * Use conda to create an environment and use the provided yml
* You will need to create a .env file containing you spotipy credentials
    * Enter the spotify developer page and log into your account
    * Open the project and open settings
    * Here you will need your client id, client secret and redirect url
    * store these in a .env file with the corresponding names

### Executing program

* To execute this program run the file playlistGenerator.py
* The program will prompt you for a setlist link. Find a set list on setlist.fm 
* The program will now prompt for an artists name. Please enter it as it appears on spotify.
* At conclustion, the program will output songs it did not find, and the corresponding spotify account will have a new playlist


## Help

For major issues reference the spotipy documentation

## Authors

Contributors names and contact info

* Shayaan Ahmed  
[@Shaydoge](https://github.com/Shaydoge)
* Shakib Ahmed
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