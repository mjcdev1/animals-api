# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added

### Changed

### Deprecated

### Removed

### Fixed

### Security

## [0.1.0] - 7/29/2023
### Added
#### Frontend 
- Created welcome screen with placeholder logo, app name and some features, and a button to continue to the main UI
- Created starting UI with 5 main pages
- Added bottom AppBar with 5 icon buttons each leading to a main page, and a top AppBar stating the page name
- Main UI home page features subpages for app information and other stuff (button for donating to charity etc)
- Main UI features a placeholder quick searchbar
- Implemented Google Maps API into the maps page, currently just goes to a random lat/ lon on the map 
#### Backend
- Setup database and tables to store animal information
- Established endpoints to interact with database
  - Endpoint to add animals to database
  - Endpoint to retrieve animal from database in JSON format
  - Endpoints have an API key requirement that will later be implemented
- Wrote scripts to call the endpoints for database interaction

