from django.shortcuts import render
from django.http import HttpResponse
from . import pycode
# Create your views here.


def index(request):
    x = pycode.main()
    html = """<!DOCTYPE html>
<html lang="en">
  <head>
    <style>
    html {
  min-height: 100%;
}

body {
  font-family: "IBM Plex Serif"; font-size: 16px;
  margin: 2em;
  background-image: linear-gradient(to bottom, #07BFEA 0%, #FFF 100%);
  background-repeat: no-repeat;
  min-height: 100%;
}


p.big {
  font-family: "Times New Roman", Times, serif;
  font-size: 40px;
  font-weight: bold;
}

 .button {
  background-color: black;
  color: white;
  margin: 20px;
  padding: 20px;
}

a:link, a:visited {
  background-color: MediumBlue;
  color: white;
  padding: 10px 20px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
}

a:hover, a:active {
  background-color: DarkBlue;
}

#header {
    font-family: "Bungee Shade";font-size: 40px;
}

    </style>
    <link href="https://fonts.googleapis.com/css?family=Bungee Shade" rel="stylesheet">
      <link href="https://fonts.googleapis.com/css?family=IBM Plex Serif" rel="stylesheet">
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    
  </head>

  <body>
    <h1 align="center" id="header"><strong>Welcome to Pupper Supper!</strong></h1>
    <br>""" + x + """
    <img src="https://cdn.glitch.com/a1349faa-4c88-4763-a928-1d699be7ce17%2FDoggo.png?1549098926102" width="200" height="200" style = "margin-left:45%">
    
    <p align="center" class="big">
      Slo Hacks 2019
    </p>

    <div class="button">
<h2>What is Pupper Supper?</h2>
<p>Humans spend a lot of time trying to improve their health. There are even dedicated apps to help them in their journey to achieve physical wellbeing... but what about for man's best friend?
Our project, PupperSupper is dedicated to helping animals live a healthy life through checking food labels and ensuring that the ingredients in these foods are healthy for dogs to consume.</p>
  <a href="./about" class="bowl">
    <p>
      About us
    </p>
  </a>
</div> 
    
     <div class="button">
<h2>How to get started</h2>
<p>The first thing you will need, of course, is your dog! Our goal is to add support for all pets including cats, horses, pigs, goats, and many more. 
 You need an active Internet connection (which you are probably using to read this right now) to run the Food Safety tool.</p>
</div> 
  
    
    <div class="button">
<h2>Food Safety Tool</h2>
<p>The pet food safety tool is an application that quickly tells you whether a particular human food is unhealthy or even deadly for your dog.</p>
      <a href="./foodsafety" class="bowl">
    <p>
      How did we build it?
    </p>
  </a>
</div> 
    
<h3>
  <br>
  
  <a href="./" class="bowl" style = "margin-left:30%">
    <p>
  <img src="https://cdn.glitch.com/a1349faa-4c88-4763-a928-1d699be7ce17%2Fbowl1.png?1549134065090">
      Click to scan Item
    </p>
  </a>
    </h3>
    
    
  </body>
</html>
"""
    return HttpResponse(html)


def foodsafety(request):
    html = """<!DOCTYPE html>
<html lang="en">
  <head>
    <style> 
      html {
  min-height: 100%;
}

body {
  font-family: "IBM Plex Serif"; font-size: 16px;
  margin: 2em;
  background-image: linear-gradient(to bottom, #07BFEA 0%, #FFF 100%);
  background-repeat: no-repeat;
  min-height: 100%;
}


p.big {
  font-family: "Times New Roman", Times, serif;
  font-size: 40px;
  font-weight: bold;
  
}


 .button {
  background-color: black;
  color: white;
  margin: 20px;
  padding: 20px;
}

a:link, a:visited {
  background-color: MediumBlue;
  color: white;
  padding: 10px 20px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
}

a:hover, a:active {
  background-color: DarkBlue;
}

#header {
    font-family: "Bungee Shade";font-size: 40px;
}
</style>
  <link href="https://fonts.googleapis.com/css?family=Sofia" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=IBM Plex Serif" rel="stylesheet">
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  
     
    <title>Food Safety</title>
    </head>
  
  <body>
    <h1 align="center"><strong>The Pet Food Safety App</strong></h1>
   <p align="center" class="big">
     Powered by Google Vision API
    </p>
    
    <div class="button">
<h2>How it was made</h2>
<p>We programmed an app using Google Vision to scan the ingredients listed on the back of food items to see if the food is safe for your dog to eat or not.
  The app will display the side effects of unhealthy and deadly ingredients. This app was written in Python and is powered by Django. </p>
</div> 
    
  </body>

</html>"""

    return HttpResponse(html)

def about(request):
    html = """<!DOCTYPE html>
<html lang="en">
  <head>
    <style>
      html {
  min-height: 100%;
}

body {
  font-family: "IBM Plex Serif"; font-size: 16px;
  margin: 2em;
  background-image: linear-gradient(to bottom, #07BFEA 0%, #FFF 100%);
  background-repeat: no-repeat;
  min-height: 100%;
}


p.big {
  font-family: "Times New Roman", Times, serif;
  font-size: 40px;
  font-weight: bold;
}


 .button {
  background-color: black;
  color: white;
  margin: 20px;
  padding: 20px;
}

a:link, a:visited {
  background-color: MediumBlue;
  color: white;
  padding: 10px 20px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
}

a:hover, a:active {
  background-color: DarkBlue;
}

#header {
    font-family: "Bungee Shade";font-size: 40px;
}
</style>
  <link href="https://fonts.googleapis.com/css?family=Sofia" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=IBM Plex Serif" rel="stylesheet">
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>About us</title>
    </head>
  <body>
    
    <h1 align="center"><strong>Pupper Supper Heroes</strong></h1>
    
    <div class="button">
<h2>Abraham</h2>
<p><img src="https://cdn.glitch.com/a1349faa-4c88-4763-a928-1d699be7ce17%2Fbowl2.png?1549134070905" alt="idontgetthis" style="float:left;width:42px;height:42px;">
  Programmed the food safety app using Python 3</p>
</div> 
    
    <div class="button">
<h2>Andrew</h2>
<p><img src="https://cdn.glitch.com/a1349faa-4c88-4763-a928-1d699be7ce17%2Fbowl2.png?1549134070905" alt="idontgetthis" style="float:left;width:42px;height:42px;">
  Programmed part of the Python logic and built the Django backend for the web app.</p>
</div> 
    
    <div class="button">
<h2>Eric</h2>
<p><img src="https://cdn.glitch.com/a1349faa-4c88-4763-a928-1d699be7ce17%2Fbowl2.png?1549134070905" alt="idontgetthis" style="float:left;width:42px;height:42px;">
  Developed the frontend of the website using HTML5 and CSS3</p>
</div> 
    
    <div class="button">
<h2>Zubair</h2>
<p><img src="https://cdn.glitch.com/a1349faa-4c88-4763-a928-1d699be7ce17%2Fbowl2.png?1549134070905" alt="idontgetthis" style="float:left;width:42px;height:42px;">
Worked on many parts of the project including web deployment. Acquired and set up our app's future URL, PupperSupper.com</p>
</div> 
    
  </body>
</html>"""
    return HttpResponse(html)