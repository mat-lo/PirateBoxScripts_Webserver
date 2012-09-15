#!/usr/bin/python

# Modificated ShoutBox Library
#   enables further modifications for the ShoutBox
#   Run without to generate htmlfile
#   Run the following to enter a new line from command line
#     psogen.py input Anonymous default "Text" 

import os, datetime, re 

datafilename = "data.pso"
htmlfilename = "../chat_content.html"


#--------------
#  Generates Shoutbox-HTML-Frame  ... 
#           Imports:
#               content    -   String  containing preformatted data
#--------------
def generate_html(content):
    css = open("style.css", 'r')
    stl =  css.read()
    css.close()

    htmlstring =   "<html><head><meta name='GENERATOR' content='PyShoutOut'><title>Shout-Out Data</title><style type='text/css'>" 
    htmlstring +=  "<style>" + stl   + "</style></head><body>"  
    htmlstring +=  content 
    htmlstring +=  "</body></html>" 
    return htmlstring 

#--------------
#   Generates HTML Data based on given content  and write it to static html file
#          Imports: 
#               content    -   String  containing preformatted data
#--------------
def generate_html_into_file(content):
    css = open("style.css", 'r')
    stl =  css.read()
    css.close()

    htmlstring = generate_html ( content )

    htmlfile = open( htmlfilename , 'w' )
    htmlfile.write( htmlstring )
    htmlfile.close()

#--------------
# Generates HTML Data based on datafilename 's content 
#--------------
def generate_html_from_file():
    old =  read_data_file() 
    generate_html_into_file( old   )

#--------------
# Generates and Displays generated HTML
#--------------
def generate_html_to_display_from_file():    
    old =  read_data_file()
    htmlstring = generate_html ( old )
    print htmlstring 

#--------------
#  Reads Data file from datafilename given name
#--------------
def read_data_file():
    datafile = open(datafilename, 'r')
    old = datafile.read()
    datafile.close()
    return old

#--------------
# Function for saving new Shoubox-Content & Regenerate static HTML file -- usually called by HTML-Form
#--------------
def process_form( name , indata , color ):
    content = save_input(  name , indata , color ) 
    generate_html_into_file ( content )

#--------------
# Acutally Saves SB-Content to datafile
#--------------
def save_input( name , indata , color ):
    old = read_data_file()
    datapass = re.sub("<", "&lt;", indata)
    data = re.sub(">", "&gt;", datapass)
    
    curdate = datetime.datetime.now()

    finalcontent = "<date>" + curdate.strftime("%H:%M:%S") + "</date>&nbsp;&nbsp;<name>" + name + ":</name>&nbsp;&nbsp;&nbsp;<data class='" + color + "'>" + data + "</data><br>\n" + old 
    datafile = open(datafilename, 'r+')
    datafile.write(finalcontent)
    #datafile.truncate(0)
    datafile.close()
    return finalcontent 


#--------------
#  Testing or Generating static HTML File
#--------------
if __name__ == "__main__":
  import sys
  if sys.argv.count("input") >= 1 :
     save_input(  sys.argv[2] ,  sys.argv[3] ,  sys.argv[4] )
     generate_html_to_display_from_file()
     print "Entered Text."
     
  generate_html_from_file ()
  print "Generated HTML-Shoutbox File."

