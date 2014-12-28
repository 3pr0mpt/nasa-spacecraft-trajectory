# -*- coding: utf8 -*-
#!/usr/bin/python

# README: https://github.com/3pr0mpt/nasa-spacecraft-trajectory/blob/master/README.md
# Packages needed for this script:
# apt-get install python2.7 python-pip libav-tools
# pip2 install progress_bar
# Thanks to Adrienne Kotze for converting video (http://techedemic.com/2014/09/18/creating-a-timelapse-clip-with-avconv/)
# Many thanks to NASA for providing such amazing tool http://space.jpl.nasa.gov/


import time
import sys
import os
import urllib2
import shutil
from progress_bar import InitBar
from datetime import date, datetime, timedelta


def juno(fovmul, rfov, bfov, porbs, showsc, showac):

    #################################
    # Mission JUNO
    # LUNCHED IN SPACE: 05/08/2011
    #################################

    print "While waiting, why don't you take the oportunity to read a little bit more about this mission:"
    print "==> http://en.wikipedia.org/wiki/Juno_(spacecraft)"
    sday = "05"
    smonth = "08"
    syear = "2011"

    tbody = "-61"
    vbody = "1001"

    folder = './NASA_JUNO'
    projectname = "juno"

    mission_to(sday, smonth, syear, fovmul, rfov, bfov, porbs, showsc, showac, tbody, vbody, folder, projectname)


def cassini(fovmul, rfov, bfov, porbs, showsc, showac):

    #################################
    # Mission CASSINI
    # LUNCHED IN SPACE: 15/10/1997
    #################################

    print "While waiting, why don't you take the opportunity to read a little bit more about this mission:"
    print "==> http://en.wikipedia.org/wiki/Cassini%E2%80%93Huygens"
    sday = "15"
    smonth = "10"
    syear = "1997"

    tbody = "-82"
    vbody = "1001"

    folder = './NASA_CASSINI'
    projectname = "cassini"

    mission_to(sday, smonth, syear, fovmul, rfov, bfov, porbs, showsc, showac, tbody, vbody, folder, projectname)


def newhorizons(fovmul, rfov, bfov, porbs, showsc, showac):

    #################################
    # Mission NEW HORIZONS
    # LUNCHED IN SPACE: 19/01/2006
    #################################

    print "While waiting, why don't you take the opportunity to read a little bit more about this mission:"
    print "==> http://en.wikipedia.org/wiki/New_Horizons"
    sday = "19"
    smonth = "01"
    syear = "2006"

    tbody = "-98"
    vbody = "1001"

    folder = './NASA_NEWHORIZONS'
    projectname = "newhorizons"

    mission_to(sday, smonth, syear, fovmul, rfov, bfov, porbs, showsc, showac, tbody, vbody, folder, projectname)


def voyager1(fovmul, rfov, bfov, porbs, showsc, showac):

    #################################
    # Mission VOYAGER I
    # LUNCHED IN SPACE: 05/09/1977
    #################################

    print "While waiting, why don't you take the opportunity to read a little bit more about this mission:"
    print "==> http://en.wikipedia.org/wiki/Voyager_1"
    sday = "05"
    smonth = "09"
    syear = "1977"

    tbody = "-31"
    vbody = "1001"

    folder = './NASA_VOYAGER_I'
    projectname = "voyagerI"

    mission_to(sday, smonth, syear, fovmul, rfov, bfov, porbs, showsc, showac, tbody, vbody, folder, projectname)


def voyager2(fovmul, rfov, bfov, porbs, showsc, showac):

    #################################
    # Mission VOYAGER II
    # LUNCHED IN SPACE: 20/08/1977
    #################################

    print "While waiting, why don't you take the opportunity to read a little bit more about this mission:"
    print "==> http://en.wikipedia.org/wiki/Voyager_2"
    sday = "20"
    smonth = "08"
    syear = "1977"

    tbody = "-32"
    vbody = "1001"

    folder = './NASA_VOYAGER_II'
    projectname = "voyagerII"

    mission_to(sday, smonth, syear, fovmul, rfov, bfov, porbs, showsc, showac, tbody, vbody, folder, projectname)


def mission_to(sday, smonth, syear, fovmul, rfov, bfov, porbs, showsc, showac, tbody, vbody, folder, projectname):
    today = (time.strftime("%d/%m/%Y"))
    print " + Mission started "+sday+"/"+smonth+"/"+syear+""
    print " + Today is", today

    start = date(int(syear), int(smonth), int(sday))
    now = date(int(time.strftime("%Y")), int(time.strftime("%m")), int(time.strftime("%d")))

    delta = now - start
    print "Spacecraft have been in space for "+str(delta.days)+" days\n"

    if (projectname == "voyagerI") or (projectname == "voyagerII"):
        start = date(1980, 01, 02)
        now = date(int(time.strftime("%Y")), int(time.strftime("%m")), int(time.strftime("%d")))
        delta = now - start
        print "----------------------------------------------"
        print "NOTE FOR VOYAGER I/II: NASA Simulator doesn't\n" \
              "include full images range since 1977, only\n" \
              "starting from 01/02/1980"
        print "----------------------------------------------"

    check_folder(folder)
    headers = createheaders()

    alldelta = now - start
    max = str(delta.days)
    pbar = InitBar()

    print "Downloading images...\n"
    time.sleep(1)
    for i in range(alldelta.days + 1):
        date_to_parse = start + timedelta(days=i)
        url = make_url(date_to_parse, tbody, vbody, fovmul, rfov, bfov, porbs, showsc, showac)
        filename = make_filename(folder, projectname, "above", date_to_parse, tbody, vbody)
        current = int((int(i) * 100)/int(max))
        #print i, current, max
        pbar(current)


        # Check if file already exists on system
        if os.path.exists(filename) == False:
            try:
                #print "Downloading image: ", url
                req = urllib2.Request(url, None, headers)
                f = open(filename,'wb')
                f.write(urllib2.urlopen(req).read())
                f.close()
            except:
                print "\nError on downloading the image:"
                print " ==> ", filename
                print " ==> ", url

    del pbar
    print "\n\nAll images are now on filesystem!"
    print "\n✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰"

    movie = raw_input('Do you want me to make a movie from those images: (y/n)')
    if movie == "y":
        print "Let's make a video from the images. This process may take some time depending on your computer..."
        make_video_from_folder(folder, projectname)
    else:
        print "No problem, you can resume this action by running this program again."
        sys.exit()


def make_url(date_to_parse, tbody, vbody, fovmul, rfov, bfov, porbs, showsc, showac):
    url = "http://space.jpl.nasa.gov/cgi-bin/wspace?tbody="+str(tbody)+"&vbody="+str(vbody)+"&month="+str(date_to_parse.strftime("%m"))+"&day="+str(date_to_parse.strftime("%d"))+"&year="+str(date_to_parse.strftime("%Y"))+"&hour=23&minute=59&fovmul="+str(fovmul)+"&rfov="+str(rfov)+"&bfov="+str(bfov)+"&porbs="+str(porbs)+"&showsc="+str(showsc)+"&showac="+str(showac)+""
    return url


def make_filename(folder, spacecraft, view, date_to_parse, tbody, vbody):

    filename = ""+folder+"/"+str(spacecraft)+"_"+str(view)+"_"+str(tbody)+"_"+str(vbody)+"_"+str(date_to_parse.strftime("%Y"))+"_"+str(date_to_parse.strftime("%m"))+"_"+str(date_to_parse.strftime("%d"))+".jpg"
    return filename


def check_folder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)


# Compiling the video directly with Python and module MoviePy isn't the best choice (as per MoviePy documentation)
# Mmplayer and mencoder are now deprecated on Debian and Ubuntu repos, we'll do the compiling stuff with avconv.


def make_video_from_folder(folder, projectname):
    # Copy Files to tmp folder
    if not os.path.exists("./tmp/"):
        os.makedirs("./tmp/")
    cmd = "cp -r "+folder+"/*.jpg ./tmp/"
    os.system(cmd)

    # Rename for avconv "lack of file handling"
    cmd = './rename-images.sh '+projectname+''
    os.system(cmd)

    # Convert video
    cmd = 'avconv -y -r 10 -i ./tmp/'+projectname+'_%4d.jpg -r 10 -vcodec libx264 -q:v 3 -vf crop=800:450,scale=iw:ih '+projectname+'.mp4'
    os.system(cmd)

    # Delete temporary folder
    shutil.rmtree('./tmp')


def getuseragent():
    useragent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1309.0 Safari/537.17"
    return useragent


def createheaders():
    user_agent = getuseragent()
    headers = {"User-Agent": ""+user_agent+"",
               "Proxy-Connection": "keep-alive",
               "Accept": "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
               "Accept-Language": "en-US,en;q=0.5",
               "Connection": "keep-alive",
               "Cache-Control": "max-age=0"
               }

    return headers


print "\n \n \nPython connector for NASA's SOLAR SYSTEM SIMULATOR \n"
print "Please select your mission:\n"
print "1) Juno (2011)\n"\
      "2) Cassini (1997)\n"\
      "3) New Horizons (2006)\n"\
      "4) Voyager I (1977)\n"\
      "5) Voyager II (1977)\n"\


try:
    mission = int(raw_input('Mission number:'))
except ValueError:
    print "Not a number - aborting program"
    sys.exit()

option = {1: "Juno", 2: "Cassini", 3: "New Horizons", 4: "Voyager I", 5: "Voyager II"}


print "\n✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰"
print "Selected Mission: ", option[mission]

# Standard variables:
fovmul = "1"    # Activate rfov or bfov. if 1 then, rfov is activated, if -1, bfov is activated.
rfov = "90"     # field of view values: 0.0005 to 120
bfov = "30"     # body to take up $bfov  percent of the image width, values: 1 to 100
porbs = "1"     # Show other orbiters
showsc = "1"    # Show other spacecrafts.
showac = "1"    # ?

if str(option[mission]) == "Juno":
    juno(fovmul, rfov, bfov, porbs, showsc, showac)
if str(option[mission]) == "Cassini":
    cassini(fovmul, rfov, bfov, porbs, showsc, showac)
if str(option[mission]) == "New Horizons":
    newhorizons(fovmul, rfov, bfov, porbs, showsc, showac)
if str(option[mission]) == "Voyager I":
    voyager1(fovmul, rfov, bfov, porbs, showsc, showac)
if str(option[mission]) == "Voyager II":
    voyager2(fovmul, rfov, bfov, porbs, showsc, showac)







