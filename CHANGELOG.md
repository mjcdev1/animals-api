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

## APP VERSION [0.6.0] (Frontend [0.1.0] / Backend [0.5.0])

## Backend [0.5.0] - 8/1/2023
### Added
- Created new 'users' table in database
  - uid (user_id)
  - username
  - email
  - hashed_pw
  - user_stats
- Added new endpoints to be able to add or retrieve users to/ from the users table 
  - Query for inserting into users table
  - Query for selecting from users table
  - DBOps functions for calling these insert/ select statements
  - Endpoints call these functions and handle errors
  - Wrote test scripts to be able to call these endpoints

### Fixed
- Fixed testrunner to also run on the new develop branch, not just on main 

## Backend [0.4.0] - 7/31/2023
### Added
- Added new endpoint to be able to retrieve marker data
  - Added query for selecting a specific marker by mid (marker id) 
  - New function in DBOps to call the query on the database and return the data to the API 
  - Wrote script to call the endpoint and get the desired data for the marker 

## Backend [0.3.0] - 7/31/2023
### Added
- Created new package and script for utility functions
- Created utility function to generate IDs for either markers or users (soon to come) 
- Created new database table to store markers
  - mid (marker id)
  - marker_lat_lon
  - marker_location
  - marker_title
  - marker_date_placed
  - marker_placed_by_uid
  - marker_status
  - marker_animal_details
  - marker_stats
- Added new endpoint to be able to add markers
  - Added query for inserting markers into marker table 
  - New function in DBOps to to call the new marker insert query 
  - Wrote new script to call the endpoint with some temporary fake data 

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


