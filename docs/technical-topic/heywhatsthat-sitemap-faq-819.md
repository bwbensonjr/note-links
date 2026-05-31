---
id: 819
url: https://www.heywhatsthat.com/faq.html
title: HeyWhatsThat Sitemap/FAQ
domain: www.heywhatsthat.com
source_date: '2026-02-12'
tags:
- web-dev
- astronomy
summary: HeyWhatsThat is a web tool that identifies mountains and landscape features
  visible from any location on Earth by generating 360° panoramic sketches labeled
  with peak names. The site offers additional features including visibility maps (viewsheds)
  showing all areas visible from a location, elevation profiles, and astronomy tools
  for eclipse simulations and night sky viewing. Users can generate their own panoramas
  by selecting a location on the map or entering coordinates, and explore various
  visualizations like contour lines and sight lines to distant peaks.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# HeyWhatsThat Sitemap/FAQ

|  |
| --- |
||  |
| --- |
| [Home](http://www.heywhatsthat.com) [Technical FAQ](techfaq.html) [Mobile FAQ](mobilefaq.html) [Sign up](javascript:signup() "Sign up for HeyWhatsThat email updates") |

![](/images/hwt-logo-293-58.jpg)  

Looking for Sea Level Rise or other mapplets?  
Visit our new [Sea Level](/sealevel.html), [Contours](/layers.html),
and [Profiler](/profiler.html) pages.

WHAT'S HEYWHATSTHAT?

You hike to the top of a mountain or pull off at a scenic overlook. You see mountains in the distance. Which mountains are they? HeyWhatsThat will tell you, providing a 360° panoramic sketch labeled with the names of the peaks you're looking at.
From almost anywhere in the world.

Our current offerings:  

![](images/wtshot.png)

The **[main site](/)**
computes the horizon and mountain names and other related visualizations, including
the surface of the Earth visible from where you're standing (the *visibility cloak* or *viewshed*)
and the line of sight profile between you and the distant peaks.
  
You can view panoramas that someone else has requested and generate your own.
([FAQ](faq.html#main))

![](images/profilershot.png)

The **[Path Profiler](profiler.html)**
allows you to create a path and generate its elevation profile. ([FAQ](faq.html#profiler))

![](images/hwt-jin-50.gif)
We're running on several models of mobile phone ([FAQ](mobilefaq.html)).  
For the **iPhone** and **Android**, use your mobile browser to visit **[m.heywt.com](http://m.heywt.com)**.  

(We're developing [an Android application](/android/heywt-web-1.apk)
that takes advantage of the built-in compass, but it hasn't been tested on much hardware ...)

**Turning to astronomy**,
our **[Eclipse](eclipses.html)** site
uses the Google Earth plug-in (currently only available for Windows and Mac OSX)
to simulate solar and lunar eclipses.

![](/images/eclipses.gif)

![](images/planisphereshot.png)

Our **[Planisphere](planisphere.html)**
enhances the night sky feature of Google Earth by providing overlays of your horizon,
an azimuth/altitude grid, and the positions of the Sun, Moon and planets. ([FAQ](planispherefaq.html))

![](images/cosmicshot.png)
And the **[Cosmic Visibility](cosmic.html)** page
does the same inside your web browser, giving you new insight
into the Moon's phases and the Earth's seasons and what you can
see on Mars.
([FAQ](cosmicfaq.html))

![](images/phasesshot.png)

At **[HeyWhatsThat -- Russia?](/alaska.html)** we tell you where in Alaska you can see Russia.
[![](images/alaskashot.png)](/alaska.html)

![](images/mappletsshot.png)

And we've written *Mapplets* for
[elevation contours](http://maps.google.com/maps/mpl?moduleurl=http://www.heywhatsthat.com/mapplets/contours.xml),
[path profiles](http://maps.google.com/maps/mpl?moduleurl=http://www.heywhatsthat.com/mapplets/profiler.xml), and
[sea level rise](http://maps.google.com/maps/mpl?moduleurl=http://www.heywhatsthat.com/mapplets/sealevel.xml).
([FAQ](mappletfaq.html))

Our **[Reviews](reviews.html)** page
will show you what other people are saying about us, and the **[Technical FAQ](techfaq.html)**
explores issues like the visibility cloak, the elevation profile, and public APIs to our services.

Why isn't it working with my browser?

We develop and debug this site with [Firefox](http://www.mozilla.com/firefox), so
the layout might be incorrect and some features may not work if you're using a different browser.

How do I get more information?

In addition to the general FAQ you're reading right now, we've got a
[technical FAQ](techfaq.html)

and a [planisphere FAQ](planispherefaq.html).
See what other people are saying on our [reviews](reviews.html) page.
We gave a Google Tech Talk [Hey, What's That? A Map Hack](https://www.youtube.com/watch?v=g8_2biEttds).
Sign up for our occasional email announcements or follow [@heywhatsthat](http://twitter.com/heywhatsthat) on Twitter. And please contact us at

MAIN SITE

How do I choose a panorama to view?

Click the tab labelled
*All panoramas*
to see all the panoramas currently available to you.
These include queries you have made (![](images/google_mm_20_red.png)),
queries that other folks have made and set *public* (![](images/google_mm_20_blue.png)).
and queries that you've made and set public (![](images/mm_20_red_blue.png)).

To view a panorama, click on a map marker or a name on the panorama list and hit *View*.
Or select a panorama from the dropdown in the *View* tab.

I'm looking at a panorama. What do I see?

When you view a panorama (e.g.
[the view from Mount Battie in Camden, Maine](http://www.heywhatsthat.com/?view=battie)),
you'll see three panes: a panorama image, a Google Map, and a list of peaks.
The peaks are marked on the image and the map with red triangles (![](images/summit.png)),
and the viewer location on the map is marked with ![](images/orchid-x.png).
You can click on the panorama image, on the Google map, or on the list of peaks and
the other panes will react.
When you click on the map or panorama image, if you click right on a peak, it will be highlighted; if
you miss a peak, you'll get a sight line on the map and the panorama showing you where you're looking.

You can toggle between bearings relative to true or magnetic north.

You're not telling me the name of the mountain I'm looking at.

For a peak to be detected by the system, it must appear against the horizon,
it must be an elevation maximum with enough slope on either side to be visible to the naked
eye (a few arcminutes is what we look for), and it must be listed in the database of features we're using.
If you're curious about a peak that's missing from the list,
clicking on the panorama
and following the resulting line on the Google map should get you to its name, or at least its latitude and longitude.

Yeah, but I'm sure I see Mount Jellyfish when I'm on Mount Squid.

If you're actively looking for a particular peak -- i.e. it's not that
you see something and want to know what it is, but that you
know something is there and keep looking until you find it --
then you'll probably need less of it to be visible than our algorithm requires.

And it could be that there are special atmospheric conditions working in your favor.
We discuss refraction a bit below and in more detail in the [technical FAQ](techfaq.html#refraction),
and acknowledge that our computations don't cover all possible circumstances. On the other
hand, meteorologists have told us that refraction can really only do so much. There are
other possible phenomena: we particularly like the section *How far can you see?*
at [Distance to the Horizon](http://mintaka.sdsu.edu/GF/explain/atmos_refr/horizon.html) and the technical discussion at
[Mirages](http://www.du.edu/~jcalvert/astro/mirage.htm).

We're constantly refining our approach, and welcome your comments and suggestions at

Okay, I can click around and see the peaks. What else can I do?

While viewing a panorama, hit the *Visibility cloak* button on the map.
We overlay the map with red pixels indicating all the ground area that
can be seen from the viewer's location. For example, we predict that from the top of Mount Washington
the farthest you can see is Saddleback Mountain, 137 miles away in Maine at
45.51°N 69.135°W. (This is not the Saddleback Mountain ski resort in Rangeley at 44.946°N 70.526°W,
though much of that is also covered by the visibility cloak.)

Outside of HeyWhatsThat.com the visibility cloak is known as the *viewshed*.
Among its many uses: it can give you an idea of where your proposed building will
be visible from, and it will show the area covered by line of sight communications
(be sure to set your tower height when you make your query).

Next?

Hit the *Contours* button. As you
move around the map you'll see contour lines (lines of constant elevation).
Hover over the button to see the interval between contour lines.
(Finer control over contours -- setting your own intervals and color --
is available in the *Elevation Contours* mapplet; see the [mapplet FAQ.](mappletfaq.html))

And?

The next thing to try is the *Show profile* button on the upper right. This opens
a new pane displaying the elevation of the path you'd walk travelling
from the viewer location to any spot you click on.
(You can draw arbitrary paths and draw their elevation profiles with the [*Path Profiler*](profiler.html)
and the [*Path Profiler mapplet*](mappletfaq.html).)

Wait a minute. I was looking at the Mount Washington panorama and hit *Show Profile*.
Then I zoomed out on the map and clicked on a spot in Rocky Mountain National Park in Colorado.
The profile showed a continuous line between the two spots. Does this mean I can see
Colorado from Mount Washington?

No. Note the 'flat earth' checkbox just under the profile. If it's checked, the profile window
is simply an elevation graph and doesn't
include the effects of the curvature of the Earth; if not checked, you'll see that
the Earth gets in the way. (Note that the computations for the visibility cloak and the list of visible peaks
include the Earth's curvature, and the refraction of light as well.)

How do I generate my own panorama?

Open the request form by clicking on the
*New panorama*
tab.

Set the desired viewer location by clicking on the map,
by entering the latitude and longitude,
or by looking up an address. If you're manually entering latitude and longitude, use
decimal degrees *44.0538*,
degrees with decimal minutes *44 3.23*,
or degrees minutes seconds *44 03 14*.
(Spaces are optional, but if you don't use spaces, be sure to include leading zeroes,
e.g. for 44° 3.23' use *4403.23*, not *443.23*.)
Check that you have the signs correct; in the continental US, longitudes should be negative numbers and latitudes positive.

Use the default elevation of six feet above ground level,
or explicitly set the elevation on the form.

If you want to be sure you're running the calculation on a peak,
use the *Move* button and dropdown to move to the highest nearby point.
For example, suppose careful map reading tells you the peak of Bald Mountain
is at 44.232°, -69.136°. According to the elevation data we use, that
point is actually north
of the summit, and the resulting panorama would have the southern view
blocked. Use *Move* to make sure your request matches where our elevation data puts the peak,
44.22972°, -69.13667° in this case.

Hit the *Submit request* button when you're done. While the request
is being processed you can view other results and enter other queries; a window
will pop up when the computation is finished.

Can I share this query with others?

You can email someone a link that will open a particular panorama;
click on *Email this panorama* while viewing a panorama.

You can also make your queries visible to everyone who visits the site.
*All panoramas*
will show you all the panoramas that you have generated (along
with those that other users have made public).
Click on a map marker or a name in the list
to delete or to change the public/private status of your own queries.

By email? How do I do this by email?

Email to
.
You can send either your latitude and longitude or an address.
In either case we ignore the subject line, but
the request comprises the entire body of the message,
so *don't send HTML formatted messages or any extra text.*

For latitude and longitude, send just the latitude and longitude.
Follow the coordinates with a ***p*** if you want the
system to run the computations from where it thinks the peak is (but no more than 100 feet away).
Latitude and longitude can be entered exactly as described above;
be sure to use negative values for west longitudes and south latitudes.
For example, the email message body  

```
  442107 -693201 p
```

asks for latitude 44°21'7" north longitude 69°32'1" west, adjusted
to the highest spot within 100 feet, and  

```
  44.2107 -69.3201
```

asks for 44.2107°N 69.3201°W, no adjustment.

For addresses, send just the address in the same format
used on this page. These seem to work:

```
  1600 pennsylvania ave, washington dc
  main & elm, 04843
```

How do I export the list of peaks to GPS software?

Check out [GMapToGPX](http://www.elsewhere.org/journal/gmaptogpx).
It's a nifty utility that exports data from a few selected sites
-- heywhatsthat.com's peaks and maps.google.com's directions, for example --
into GPX format.

And Google Earth?

After you've installed [Google Earth,](http://earth.google.com)
click on *View in Google Earth by day* in the top right-hand corner of the page
while viewing a panorama.
Google Earth will open and zip over to the origin of the panorama.
Enable the *Horizon* overlay to see the panorama we generate
and compare it with their visualizations.
(We call it *Horizon* here
because *Panorama* generally refers to wide angle photos in Google Earth.)

Be sure to enable the *Visibility cloak* as well, which will show
both the overall extent visible from the viewer's location (*Entire
visible area*) and the specific regions that are visible (*Pixel by pixel*).

Clicking on *View all in Google Earth* while viewing
the *All panoramas* tab will send a list of all your panoramas
and all the public panoramas to Google Earth.

Google Earth by night?

This is our interface to Google Sky. 
Click on the *at night* button under the *View in Google Earth by day* button.
Google Earth will start up
and overlay the celestial sphere with your horizon and peaks, an azimuth-altitude grid,
and the positions of the Sun, Moon and planets (and Pluto too),
reflecting the state of the sky at that instant.

You may find you have to manually switch to sky view (under the *View* menu hit *Switch to Sky*),
and if you don't see the overlays -- blue horizon line, red summit markers, and green grid lines --
you'll have to
refresh the Network Link you just loaded: look in Google Earth
for an entry on the left under *Temporary Places*
labeled something like *Planisphere for XXXX (current)*, right-click
on it, and select *refresh*. Note that you can refresh it
any time and the horizon and everything else will be updated.

You can do more by visiting our [Planisphere](planisphere.html) page
and its [FAQ](planispherefaq.html),
including determining the horizon for any specified time and for any arbitrary
latitude/longitude, even locations above 60° north
latitude and below 54° south where we don't have elevation
data.

What data do you use?

We use two sets of data to generate these results.
First, we use a *digital elevation model*, which
is the height of the surface of the Earth above sea level
at a network of points. In this case we're using the SRTM data generated
by the February 2000 Space Shuttle mission. It comprises elevations
determined roughly every 100 feet north-south and east-west
for the US and every 300 feet elsewhere, covering
latitude 60°N to 54°S. For more information, see the
[NASA Jet Propulsion Laboratory](http://www2.jpl.nasa.gov/srtm)
and [USGS](http://srtm.usgs.gov) Shuttle Radar Topography Mission pages.

The second data set is a list of summits, comprising
their latitudes, longitudes and names. For the
US names we use data from [U.S. Geological Survey, 19810501, U.S. Geographic Names Information System (GNIS): U.S. Geological Survey, Reston, VA.](http://geonames.usgs.gov) For the
rest of the world we use data compiled by
[Geonames.org](http://www.geonames.org),
licensed under the [Creative Commons 2.5 Attribution License.](http://creativecommons.org/licenses/by/2.5/)

The data used to generate the planisphere is described in the [Planisphere FAQ](planispherefaq.html#data).

How do you compute magnetic North (the *declination*)?

We use code and data from
[NOAA's National Geophysical Data Center](http://www.ngdc.noaa.gov/geomag/models.shtml)
. Specifically, we use GEOMAG Version 7.0 with the
International Geomagnetic Reference Field model, using
the current date and mean sea level, and rounding to the nearest integer.

Note that they also provide some web services for obtaining
this (currently listed in the second paragraph, under *Revised on-line calculators*).

Can I see all the names?

Go to [the main site](/) and
hit the button labelled *All summits* at the top right-hand
corner of the map. You'll see a bunch of markers; mouseover for the names and elevations. Move
the map and click the bookmark again to see more summits.

What datum do you use?

We use the WGS 84 reference ellipsoid in our calculations.

Do you correct for refraction?

We model refraction by adding roughly 3.6 arc seconds to the altitude of an object for every
mile away from the viewer, which comes from the surveying rule of thumb of adding 14% of
the drop in altitude due to curvature of the earth. See the [technical FAQ](techfaq.html#refraction).

What's the *(shown at ...)* business all about?

The elevation data and the summit name data is fairly well synchronized, but can't match exactly.
When we calculate the position of a peak it is usually close to, but not exactly on top of,
the location of the summit in the names database. If we only showed the location from the
names database you'd ask *How come a summit is listed at latitude 44.1111 on your map but you display
it at 44.1112?* and if we just showed the location from the computation you'd say
*I looked up Mount Squid in the latest US GNIS and it's supposed to be at 44.1111 but you
say it's at 44.1112* so we figured we'd give you all the data. Of course, we could just round ...

PATH PROFILER

What's the *Path Profiler?*

The [Path Profiler](profiler.html)
generates an elevation profile for an
arbitrary path.

Build a path, hit *calculate profile*, and you'll
get the elevation profile (the hills and valleys
you'd traverse as you travel that path). You can
add points to the path by clicking on the map
or by entering addresses and hitting *Find*. If you
hit *get route* the system (actually, Google's
system) will find a smooth driving route between
the last two points on the path.

The UI is unapologetically anachronistic; how
often do you see a button labelled *backspace* in
a web app?

The *Path Profiler* doesn't quite do what I want. Do you know of any similar sites?

There are several other web sites with similar functionality, some tailored
to particular applications like walking, running or biking.
(Peter, a cyclist and friend of HeyWhatsThat, has tried a few of them out and
sent us [these images](peter-profiles.html).)
Here's our current list:  

* [Gmaps Pedometer](http://www.gmap-pedometer.com/) (also tells you the calories you've burned)
* [veloroutes.org](http://veloroutes.org/)
* [Map My Ride](http://mapmyride.com) (see [Map My Fitness](http://mapmyfitness.com) for
  the rest of their suite: Map My Run, Walk, ...)
* [Topocoding](http://topocoding.com/) (they also provide the [Altitude Resolving Tool](http://maps.google.com/ig/add?moduleurl=http://www.topocoding.com/demo/topocoding.xml&pid=mpl&synd=mpl) mapplet)

* [USGS: The National Map](https://viewer.nationalmap.gov/advanced-viewer/) (not quite as easy to use as the others, but in addition to profiles, provides access to raw data from multiple USGS datasets)
* [bikemap.net](http://www.bikemap.net)
* [Google Maps Mania: Cycling Directions on Google Maps](http://googlemapsmania.blogspot.com/2009/08/cycling-directions-on-google-maps.html) A roundup of more similar sites
* [Where is the path?](http://wheresthepath.googlepages.com/wheresthepath.htm) is a beautiful site that lets you draw paths and export to KML and GPX (among lots of other things). Also see [Libraries and Web Services for Outdoor Pursuits Mashups](http://www.bdcc.co.uk/Gmaps/Services.htm); scroll to *A UK Gradient Server and a UKOS Grid for Google Maps* about a third of the way down the page. (Latter piece is UK only; also describes an API.)
* [Calcul d'itineraire](http://calculitineraire.free.fr) (jogging, footing, course a pied, velo...)


[Google Earth](earth.google.com) has added the ability to draw profiles, and they have pretty good elevation data. You draw a path
then click "show elevation profile" in the Edit menu.

If you're looking for raw elevation data, see our [Technical FAQ](/techfaq.html#get_elevation_data).

The Profiler is no longer redrawing the profile when I add new points,
or the profile isn't changing

The Profiler should redraw every time you hit the *draw profile*
button, and the Profiler mapplet should redraw whenever you add a point.
If you don't see any changes in the image, maybe you've got too
many points in the path (see next question).

Is there a limit to the number of points in the path?

Yes.

Our server currently limits incoming URLs to 8190 bytes,
which limits profiles to about 200 points. And while
Firefox apparently has no length limit for outgoing URLs,
Internet Explorer limits them to 2083 bytes, which corresponds very
roughly to 50 points.

If you're using *follow driving route* it's
easy to hit these limits, so the profiler tries to interpolate fewer points in smoothed routes when it reaches
these URL limits.

Can I save a path in the profiler?

We don't have accounts for saving paths, but you can hit the button labelled *Checkpoint*
and, in your browser's address bar, you'll get the full URL you'll need to return to the profiler
with the current path. So, when you have the path you want, hit *Checkpoint* and bookmark the page.

You can also
save the URL of the image. In Firefox, for example, right click on the
image, select *copy image location* and paste it into a document.
(Using the API description in the [technical faq](http://www.heywhatsthat.com/techfaq.html#profiler_api)
you can even edit it.)

ACKNOWLEDGMENTS

Data courtesy of the [U.S. Geological Survey,](http://www.usgs.gov) [NASA](http://www.nasa.gov),
[Geonames.org,](http://www.geonames.org) and the [U.S. Naval Observatory.](http://aa.usno.navy.mil/)
Colocation graciously provided by [Midcoast Internet Solutions](http://www.midcoast.com).
None of those organizations endorse this site.  

How do I contact you?

12/2016
