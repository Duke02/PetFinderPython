import requests as req
import json
from flags import *


def request( subsystem, method, args={ } ):
	url = "http://api.petfinder.com/" + subsystem + "." + method
	if len( args ) != 0:
		url += "?"
		index = 0
		for key, val in args.items( ):
			if index < len( args ):
				url += "&"
			index += 1
			url += key + "=" + val
	return req.get( url )


def getRandomPet( publicKey, animal="", breed="", size="", sex="", location="", shelterID="", output="id",
                  format="xml" ):
	args = { "key": publicKey, "output": output, "format": format }
	if len( animal ) > 0:
		args[ "animal" ] = animal
	if len( breed ) > 0:
		args[ "breed" ] = breed
	if len( size ) > 0:
		args[ "size" ] = size
	if len( sex ) == 1:
		args[ "sex" ] = sex
	if len( location ) > 0:
		args[ "location" ] = location
	if len( shelterID ) > 0:
		args[ "shelterid" ] = shelterID
	return request( "pet", "getRandom", args )


def getBreedList( publicKey, animal, format="xml" ):
	return request( "breed", "list", { "key": publicKey, "animal": animal, "format": format } )


def getPet( publicKey, petID, format="xml" ):
	return request( "pet", "get", { "key": publicKey, "id": petID, "format": format } );


def findPets( publicKey, location, animal="", breed="", size="", sex="", age="", offset="", count=25, output="basic",
              format="xml" ):
	args = { "key": publicKey, "location": location, "output": output, "count": count, "format": format }
	if len( animal ) > 0:
		args[ "animal" ] = animal
	if len( breed ) > 0:
		args[ "breed" ] = breed
	if len( size ) > 0:
		args[ "size" ] = size
	if len( sex ) == 1:
		args[ "sex" ] = sex
	if len( age ) > 0:
		args[ "age" ] = age
	if len( offset ) > 0:
		args[ "offset" ] = offset
	return request( "pet", "find", args )


def findShelters( publicKey, location, name="", offset=0, count=25, format="xml" ):
	args = { "key": publicKey, "location": location, "offset": offset, "count": count, "format": format }
	if len( name ) > 0:
		args[ "name" ] = name
	return request( "shelter", "find", args )


def getAShelter( publicKey, shelterID, format="xml" ):
	return request( "shelter", "get", { "key": publicKey, "id": shelterID, "format": format } )


def getPetsFromShelter( publicKey, shelterID, status="A", offset=0, count=25, output="basic", format="xml" ):
	return request( "shelter", "getPets",
	                { "key": publicKey, "id": shelterID, "status": status, "format": format, "offset": offset,
	                  "count": count, "output": output } )


def getPetsWithBreedFromShelter( publicKey, animal, breed, offset=0, count=25, format="xml" ):
	return request( "shelter", "listByBreed",
	                { "key": publicKey, "animal": animal, "breed": breed, "offset": offset, "count": count,
	                  "format": format } )
