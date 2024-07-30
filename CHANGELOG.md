# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Template]
### Backend [VERSION]
#### Added

#### Changed

#### Deprecated

#### Removed

#### Fixed

#### Security

### Frontend [VERSION]
#### Added

#### Changed

#### Deprecated

#### Removed

#### Fixed

#### Security

## APP VERSION [0.3.3] (Frontend [0.1.0] / Backend [0.2.3]

## Backend [0.2.3] - 7/29/2023
### Added
- Added github workflow test runners into the code to check for typechecking with mypy and PEP8 adherence with flake8 when pushed to github. I set it up to use the strictest settings 

### Changed
- Reformatted some code again to adhere to the newly implemented, more strict flake8 settings 

## Backend [0.2.2] - 7/29/2023
### Changed 
- Added typechecking via mypy to the code
- Reformatted some code to better adhere to PEP8 guidelines 

## Backend [0.2.1] - 7/29/2023
### Changed 
- Refactored file structure for better organization and practices
  - Created modules for app, database, and queries and moved related files into there
  - Also had to refactor some code to properly import files where needed 

## Backend [0.2.0] - 7/29/2023
### Added 
- Created tables in database to store animal information
- Established new endpoints to interact with database
  - Endpoint to add animals to database
  - Endpoint to retrieve animal from database in JSON format
    - Animal(s) can be requested by their common name, class name, order name, or family name 
  - Endpoints have an API key requirement. API keys will later be generated somehow 
- Wrote scripts to call the endpoints for database interaction

### Changed
- Index endpoint now has a more detailed message to give some details about the API
- Refactored original code to use OOP principles which is what we will do going forward

## Frontend [0.1.0] - 7/22/2023
### Added
- Created Flutter project 

## Backend [0.1.0] - 7/22/2023
### Added
- Established Heroku Postgre database
- Wrote starter API with Flask to connect to database and created some test endpoints 


