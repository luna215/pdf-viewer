import os
import subprocess
import time

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():

    # Generate Deck
    # os.system('python slimmed-deckbot/deckbot.py')
    # time.sleep(2)

    # Convert using docker
    os.system('docker cp test.pptx libreoffice:/tmp/test.pptx')
    os.system("docker exec -ti libreoffice \\nunocov \\n   --connection 'socker,host=127.0.0.1,port=8100,tcpNoDelay=1;urp;StartOffice.Component' \\n   -f pdf /tmp/test.pptx")
    os.system("docker cp libreoffice:/tmp/test.pdf .")
    os.system('cp test.pdf my-app/public/myPDF.pdf')
    return 'Pptx has been converted!'

if __name__ == "__main__":
    app.run()