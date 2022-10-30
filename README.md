# AirBnB Clone

## Description

clone of AirBnB platform with limited features.

## Usage

### How Start it

    ./console.py

### How to display help

    (hbnb) help

    Documented commands (type help <topic>):
    ========================================
    EOF  all  count  create  destroy  help  quit  show  update

    (hbnb)

### How to display help for quit command

    (hbnb) help quit
    Quit command to exit the program

    (hbnb)

### How to exit the console

    (hbnb) quit
    $

### How to create a User

    (hbnb) create User
    320098c5-ab99-4134-b205-5911dec9c9fa
    (hbnb)

### How to create a State

    (hbnb) create State
    d7fb1ba3-5c46-4197-aca1-36094cf22ee9
    (hbnb)

### How to create a City

    (hbnb) create City
    3e647f03-7954-48da-89fd-6504c68dfb09
    (hbnb)

### How to create a user

    (hbnb) create Amenity
    f81e070f-52b6-4a5d-b13b-6c6c33838b4b
    (hbnb)

### How to create a Place

    (hbnb) create Place
    25690873-52e4-4be3-8bcb-029249c91a32
    (hbnb)

### How to create a Review

    (hbnb) create Review
    e76e9aaa-9871-4db2-85dc-f5765cc85a71
    (hbnb)

### How to display a User

    (hbnb) show User 320098c5-ab99-4134-b205-5911dec9c9fa
    [User] (320098c5-ab99-4134-b205-5911dec9c9fa) {'id': '320098c5-ab99-4134-b205-5911dec9c9fa', 'created_at': datetime.datetime(2022, 10, 30, 14, 22, 59, 416038), 'updated_at': datetime.datetime(2022, 10, 30, 14, 22, 59, 416059)}
    (hbnb)

### How to display a State

    (hbnb) show State d7fb1ba3-5c46-4197-aca1-36094cf22ee9
    [State] (d7fb1ba3-5c46-4197-aca1-36094cf22ee9) {'id': 'd7fb1ba3-5c46-4197-aca1-36094cf22ee9', 'created_at': datetime.datetime(2022, 10, 30, 14, 23, 34, 516438), 'updated_at': datetime.datetime(2022, 10, 30, 14, 23, 34, 516491)}
    (hbnb)

### How to display a City

    (hbnb) show City 3e647f03-7954-48da-89fd-6504c68dfb09
    [City] (3e647f03-7954-48da-89fd-6504c68dfb09) {'id': '3e647f03-7954-48da-89fd-6504c68dfb09', 'created_at': datetime.datetime(2022, 10, 30, 14, 23, 54, 140492), 'updated_at': datetime.datetime(2022, 10, 30, 14, 23, 54, 140522)}
    (hbnb)

### How to display a Amenity

    (hbnb) show Amenity f81e070f-52b6-4a5d-b13b-6c6c33838b4b
    [Amenity] (f81e070f-52b6-4a5d-b13b-6c6c33838b4b) {'id': 'f81e070f-52b6-4a5d-b13b-6c6c33838b4b', 'created_at': datetime.datetime(2022, 10, 30, 14, 24, 11, 584531), 'updated_at': datetime.datetime(2022, 10, 30, 14, 24, 11, 584564)}
    (hbnb)

### How to display a Place

    (hbnb) show Place 25690873-52e4-4be3-8bcb-029249c91a32
    [Place] (25690873-52e4-4be3-8bcb-029249c91a32) {'id': '25690873-52e4-4be3-8bcb-029249c91a32', 'created_at': datetime.datetime(2022, 10, 30, 14, 24, 40, 116241), 'updated_at': datetime.datetime(2022, 10, 30, 14, 24, 40, 116287)}
    (hbnb)

### How to display a Review

    (hbnb) show Review e76e9aaa-9871-4db2-85dc-f5765cc85a71
    [Review] (e76e9aaa-9871-4db2-85dc-f5765cc85a71) {'id': 'e76e9aaa-9871-4db2-85dc-f5765cc85a71', 'created_at': datetime.datetime(2022, 10, 30, 14, 24, 49, 88134), 'updated_at': datetime.datetime(2022, 10, 30, 14, 24, 49, 88189)}
    (hbnb)

### How to delete a User

    (hbnb) destroy User 320098c5-ab99-4134-b205-5911dec9c9fa
    (hbnb)

### How to delete a State

    (hbnb) destroy State d7fb1ba3-5c46-4197-aca1-36094cf22ee9
    (hbnb)

### How to delete a City

    (hbnb) destroy City 3e647f03-7954-48da-89fd-6504c68dfb09
    (hbnb)

### How to delete a Amenity

    (hbnb) destroy Amenity f81e070f-52b6-4a5d-b13b-6c6c33838b4b
    (hbnb)

### How to delete a Place

    (hbnb) destroy Place 25690873-52e4-4be3-8bcb-029249c91a32
    (hbnb)

### How to delete a Review

    (hbnb) destroy Review e76e9aaa-9871-4db2-85dc-f5765cc85a71
    (hbnb)

### How to Display all the data

    (hbnb) all
    ["[User] (320098c5-ab99-4134-b205-5911dec9c9fa) {'id': '320098c5-ab99-4134-b205-5911dec9c9fa', 'created_at': datetime.datetime(2022, 10, 30, 14, 22, 59, 416038), 'updated_at': datetime.datetime(2022, 10, 30, 14, 22, 59, 416059)}", "[State] (d7fb1ba3-5c46-4197-aca1-36094cf22ee9) {'id': 'd7fb1ba3-5c46-4197-aca1-36094cf22ee9', 'created_at': datetime.datetime(2022, 10, 30, 14, 23, 34, 516438), 'updated_at': datetime.datetime(2022, 10, 30, 14, 23, 34, 516491)}", "[City] (3e647f03-7954-48da-89fd-6504c68dfb09) {'id': '3e647f03-7954-48da-89fd-6504c68dfb09', 'created_at': datetime.datetime(2022, 10, 30, 14, 23, 54, 140492), 'updated_at': datetime.datetime(2022, 10, 30, 14, 23, 54, 140522)}", "[Amenity] (f81e070f-52b6-4a5d-b13b-6c6c33838b4b) {'id': 'f81e070f-52b6-4a5d-b13b-6c6c33838b4b', 'created_at': datetime.datetime(2022, 10, 30, 14, 24, 11, 584531), 'updated_at': datetime.datetime(2022, 10, 30, 14, 24, 11, 584564)}", "[Place] (25690873-52e4-4be3-8bcb-029249c91a32) {'id': '25690873-52e4-4be3-8bcb-029249c91a32', 'created_at': datetime.datetime(2022, 10, 30, 14, 24, 40, 116241), 'updated_at': datetime.datetime(2022, 10, 30, 14, 24, 40, 116287)}", "[Review] (e76e9aaa-9871-4db2-85dc-f5765cc85a71) {'id': 'e76e9aaa-9871-4db2-85dc-f5765cc85a71', 'created_at': datetime.datetime(2022, 10, 30, 14, 24, 49, 88134), 'updated_at': datetime.datetime(2022, 10, 30, 14, 24, 49, 88189)}"]
    (hbnb)

### How to update a user

    (hbnb) update User 320098c5-ab99-4134-b205-5911dec9c9fa name School
    (hbnb)

### How to count number users

    (hbnb) count User
    1
    (hbnb)
