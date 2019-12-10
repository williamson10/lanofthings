# This is no longer being developed after finding [HomeAssistant](https://www.home-assistant.io/)
# LOT-Server

This is a POC project for disconnecting IOT devices from the internet and controlling them locally. Currently supports TP-Link smart plugs. As I get devices I will likely add support for them to this project.

## Getting Started

TODO

### Prerequisites

Requires Python and Flask

### Installing

flask run

## Deployment

Docker Image is now available: [LOTServer](https://hub.docker.com/r/williamson10/lot-server)
Data is saved in the same directory as the app. This still needs to be separated out.

## Built With

* [Flask](http://flask.pocoo.org/)
* [SoftsCheck reverse engineering efforts](https://www.softscheck.com/en/reverse-engineering-tp-link-hs110/)
* [Bootstrap](https://getbootstrap.com/) 

## Authors

* **Justin Williamson** - *Initial work* - [LOT-Server](https://github.com/williamson10/lanofthings)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
