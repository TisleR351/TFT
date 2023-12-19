Hi everyone, and welcome to my new FitTracker project!
We're actually December 19th and I'm really happy to start this project whose main goal is to improve my skills in both FrontEND and BackEND, and which could, why not, result in an iOS or Android application.
I created this project because I often do sports sessions during which I have to write down myself in the notes on my iPhone the exercises I do, at what intensity, etc... 
I said to myself that It would certainly be more practical to create an application that could handle all of this without actually making a short break in my sport session, while still working on my technical skills as a web developer. 
We kill two birds with one stone
To clone this project with SSH, simply run: 
```console
git clone git@github.com:TisleR351/TFT.git
cd TFT
```
To turn on the Django Rest API, make sure you've installed Python 3.12.1 and just run these commands:
(make sure you're at the project's root @/TFT)
```console
cd tft
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
 python manage.py runserver
```

If you want to run the frontEND application, make sure you've installed Node 21.5.0 and simply run:
(make sure you're at the project's root @/TFT)
```console
cd tisfittracker
npm i
npm run dev
```

If you need further informations, don't hesitate to take a look at the README file in tisfittracker.
You can also visit Django Rest Framework's & NextJS' documentations.
