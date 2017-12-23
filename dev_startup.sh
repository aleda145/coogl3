#!/bin/bash

# Trap sigint (CTRL-C) and cleanup the development environment.
trap "cleanup" INT
trap "echo tstp" TSTP

echo "Putting this in background with CTRL-Z is not allowed because then you need to cleanup
yourself. If you feel confident in doing that, you don't need this startup script! :P
Stop and cleanup with CTRL-C"

prevent() {
	echo "Oopsie! Not allowed! Kill with CTRL-C"
}

cleanup() {
	trap "" INT TERM
	echo "**** Shutting down... ****"
    docker-compose down
	kill -TERM 0
	wait
	echo "Done with cleanup"
}

# Try to make sure that we're in the correct folder for running the script, then start the
# development environment.
docker-compose up &

cd Product/Frontend
npm install
npm start &

# Wait for sigint
cat
