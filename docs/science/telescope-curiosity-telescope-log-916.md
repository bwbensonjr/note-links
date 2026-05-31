---
id: 916
url: https://curiosity-telescope.vercel.app/
title: ∫telescope // Curiosity Telescope Log
domain: curiosity-telescope.vercel.app
source_date: '2026-03-08'
tags:
- astronomy
- tutorial
- github-repo
summary: Two enthusiasts in Bengaluru, India built a 6-inch Newtonian reflector telescope
  called "Curiosity" using a combination of 3D-printed components, PVC tubing, and
  commercially available optical parts, documenting their design process, calculations,
  and observations of celestial objects including the moon, Jupiter, and lunar eclipses.
  The project details their engineering approach from initial concept through CAD
  modeling in Fusion 360 to mechanical fabrication, including specific dimensions,
  material choices, and assembly techniques for constructing a functional amateur
  telescope with a Dobsonian mount.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# ∫telescope // Curiosity Telescope Log

Mission CURIOSITY: On a hunt to find the Meaning!

[

Your browser does not support the video tag.
](Telescope/Videos/Moon-2.webm)

MAG: 200x

Observation 30-01-26 // Lunar Descent // Used: 9mm eyepiece with 2x barlow lens // Bengaluru, India

[

Your browser does not support the video tag.
](Telescope/Videos/Moon-1.webm)

MAG: 200x

Observation 30-01-26 // Lunar Descent // Used: 9mm eyepiece with 2x barlow lens // Bengaluru, India

![](Telescope/Fab/IMG_4909.JPG)

10th January, 2026

![](Telescope/Fab/IMG_4966.JPG)

15th January, 2026

![](Telescope/intro/IMG_5050.JPG)

23rd January, 2026

![](Telescope/intro/01.JPG)

25mm eyepiece // 23rd January, 2026

![](Telescope/intro/02.jpg)

9mm eyepiece & 2x barlow // 30th January, 2026

![](Telescope/intro/IMG_5046.JPG)

That's US (Madhav on the left & swarup on the right)! 23rd January, 2026

![](Telescope/intro/04.jpg)

25mm eyepiece & 2x barlow // 27th January, 2026

![](Telescope/intro/03-jupiter.jpg)

9mm eyepiece & 2x barlow // Jupiter // 13th February, 2026

![](Telescope/Fab/IMG_5237.JPG)

Ease of carrying the telescope with bag straps

![](Telescope/March-3-26/phases/wb-1.jpg)

White balance play on a full moon // 03-03-26

![](Telescope/March-3-26/01-Gallery view.png)

Gallery View on the day of Lunar Eclipse // 03-03-26

![](Telescope/March-3-26/phases/IMG_5659.JPG)

Red moon

![](Telescope/March-3-26/phases/03-03-2026.png)

3rd March, 2026 // Lunar Eclipse Phases

Chapter 00 // INTRODUCTION, the Why? Where? How?
------------------------------------------------

Madhav on Computer M & Swarup on Computer S.   
  
Both, looking at their reddit feeds and getting awed by the pictures of Moon, Jupiter, Saturn, Orion Nebulae and what not, clicked by people all around the world.   
Us discussing, HOW MUCH DOES A DECENT TELESCOPE COST?   
  
Well, it does cost a lot (\*a lot is definitely subjective). Living in bengaluru, India where the current period of months(October to March) aids us to stargaze with the most beautiful clear skies. Something had to be done, so we jumped on searching our reddit feeds and cloudy nights to get an understanding on what people have accomplisheed, I came across this book called [“Build Your Own Telescope by Richard Berry (1985)”](Telescope/Rchard Brry - Build your own Telescope (1985)(en).pdf), which communicated in a very interesting way. The initial thought following the book was to build a 4" telescope but eventually we jumped onto a 6" Newtonian Reflector with Dobsonian Mount.   
  
Hence, the name of our telescope "CURIOSITY".

**DESIGN** 6" (150mm) Newtonian Reflector

**FOCAL LENGTH** 900mm

**PRIMARY MIRROR** Ø 150mm

**SECONDARY MIRROR** Ø 28mm - minor axis & Ø 38mm - major axis

**EYEPIECE** 25mm, 9mm & Barlow Lens

02 // DIMENSIONS & CALCULATIONS & DESIGNING

Chapter 01-A // Dimensions & Calculations
-----------------------------------------

The image shown below is the most essential and the easiest calculation that one has to look for while building a newtonian reflector telescope.

![Optical Layout Calculations](Telescope/Design/04-Optical Layout cal.png)

FIG 1.1: Optical Layout and the necessary calculation to make your life easy.  
 Ref: How to build your own telescope by Richard berry

In our case, for the distance between the diagonal mirror and the primary mirror, we did not strictly adhere to the **+1"**, rather we subtracted it i.e., our final equation looked like **F-T-H-1"**.
This was done because of the focuser size. The calculation looks like

* F = Focal Length = 900mm
* T = Tube inner dia = 95mm
* H = Height of focuser = 96mm
* So, F-T-H-25 = 900 - 95 - 96 - 25 = 684mm

**Q.** Why did we go for a 190mm inner diameter of tube?  
**A.** After referring a lot of sources over the internet and also during the assembly process of the telescope, it is advised to maintain an offset of ≥ 20mm from the size of primary mirror i.e., for a 6" or 150mm primary mirror size, 150 + (2\*20) = 190mm should be the minimum inner diameter of your PVC tube.

**>> Our initial procurement of parts looked like**

* PVC Tube dimension: Ø190mm as inner diameter and Ø200mm as outer diameter with a length of 1000mm.
* [6" Newtonian Telescope kit](https://www.tejraj.com/product/6-newtonian-telescope-making-optical-kit) purchased from Tejraj and co. who provide a **6" primary mirror**, **25mm eyepiece**, a **diagonal mirror** as was mentioned in the previous chapter and finally a **Rack-n-pinion focuser**.
* Matte Black Spray paints which we got it from a nearby hardware store.

Chapter 01-B // CAD Modelling & Designing
-----------------------------------------

The following images are snippets of our design from Fusion 360 software which supports student licences, though some limitations, but does fulfill our job.

INITIALIZING 3D RENDER...

Interactive // Curiosity\_6inch\_Telescope.gltf

Use the cursor to move it around and scroll to zoom in and zoom out.

>> **01\_PRIMARY MIRROR ASSEMBLY**

![](Telescope/Design/05-a-Primary Mirror-Full view.png)

Isometric top view

![](Telescope/Design/05-b-Primary Mirror-bottom.png)

Isometric bottom view

![](Telescope/Design/05-c-Primary Mirror-insert.png)

Insert for 3D printed component in blue

Based on the images represented above:

* Back of the mirror is adhered with adhesive velcro hook and the pink component (housing) is adhered with velcro loop.
* The face of the blue components in contact with the mirror is adhered with a 2mm thick rubber padding to hold the mirror in position.
* Excluding the green component which is plywood, all the other components are 3D printed.
* CAD Link: [GRABCAD - Curiosity](https://grabcad.com/library/curiosity-6-newtonian-reflector-dobsonian-telescope-1)

>> **02\_SECONDARY MIRROR with SPIDER VANE ASSEMBLY**

![](Telescope/Design/06-a-Secondary Mirror-Full view.png)

Isometric top view

![](Telescope/Design/06-b-Secondary Mirror-bottom.png)

Isometric bottom view

![](Telescope/Design/06-c-Secondary Mirror-labels.png)

Labelling

Based on the images represented above:

* The green component represents COTS (commercially off the shelf) 0.7mm thick scale/ruler of 30cm length which we got from a stationary store. For spider vane designs, follow the below links for better understanding. To take a note of "Diffraction Spikes"

+ [>>](https://carlin.udjat.nl/spider/spider2.html) Some thoughts about spiders in Newtonian telescopes by Nils Olof Carlin
+ [>>](https://www.cloudynights.com/forums/topic/495707-spider-and-secondary-diffraction-what-to-do-what-to-avoid/) Cloudy Nights: Spider and Secondary Diffraction: what to do, what to avoid
+ [>>](https://www.findlight.net/blog/diffraction-spikes/) Findlight blog: Diffraction Spikes from Telescope Secondary Mirror Spiders

* The secondary mirror is adhered to the top yellow bracket (groove supported for ease of positioning) using standard strong adhesive. To ensure wearing gloves while handling the mirrors.
* Make sure to clean the mirrors using a standard alcohol based wipes.
* CAD Link: [GRABCAD - Curiosity](https://grabcad.com/library/curiosity-6-newtonian-reflector-dobsonian-telescope-1)

>> **03\_OPTICAL TUBE ASSEMBLY (OTA)**

![](Telescope/Design/07-a-OTA-Full view.png)

Isometric Front view

![](Telescope/Design/07-b-OTA-Section View.png)

Section View

![](Telescope/Design/07-c-OTA-only pipe.png)

PVC Optical Tube

Based on the images represented above:

* The OTA is a PVC tube purcahsed from a hardware store of dimensions

+ Height or Length: 1000mm
+ Outer Diameter: 200mm
+ Inner Diameter: 190mm

* The holes positioning were hand drilled based on the calculations that was done above.
* Collimation can be done later, ensure all the brackets are fastened properly and the length of fastener should not exceed the 20mm offset i.e., 20mm space between mirror and the inner diameter of the tube.
* CAD Link: [GRABCAD - Curiosity](https://grabcad.com/library/curiosity-6-newtonian-reflector-dobsonian-telescope-1)

>> **04\_OTA CRADLE**

![](Telescope/Design/08-a-OTA cradle-full view.png)

Isometric view

![](Telescope/Design/08-b-OTA cradle-section view.png)

Section View

![](Telescope/Design/08-c-OTA cradle-sliding bkt assembly.png)

Wooden Insert Guide and Alignment

Based on the images represented above:

* We were heavily inspired by [>>](https://stellafane.org/tm/dob/mount/rockerbox.html) Stellafane's Guide
* Complete OTA Cradle is made with plywood cutout and held together with

+ Firstly with Aluminium profile L brackets.
+ Secondly all the mating surfaces were connected with self tapping screws for wood.
+ To ensure the entire cradle is sturdy with supports.

* CAD Link: [GRABCAD - Curiosity](https://grabcad.com/library/curiosity-6-newtonian-reflector-dobsonian-telescope-1)

>> **05\_ROCKER BOX**

![](Telescope/Design/09-a-Rocker Box-Full view.png)

Isometric view

![](Telescope/Design/09-b-Rocker Box-Teflon.png)

Teflon Spacers

![](Telescope/Design/09-c-Rocker Box-Base.png)

Rocker Box Base view

Based on the images represented above:

* We were heavily inspired by [>>](https://stellafane.org/tm/dob/mount/rockerbox.html) Stellafane's Guide but gave our own touch to the overall design.
* Complete Rocker box is made with plywood cutouts held together with L brackets at multiple locations.
* For smooth rotation, the base body and the upper body can be connected with

+ Compact disk
+ Roller bearings
+ Teflon spacers sliding over each other, but ensure as shown in the second image about a mistake that we did using a very small teflon disc which led to imbalance issues. The red regions have been marked to highlight supports that need to be ensured.
+ Our initial attempt incorporated using a teflon tape which was adhered to both the bodies but we wanted better smoothness in terms of rotation.

* The two bodies should be then clamped with a fastener.
* CAD Link: [GRABCAD - Curiosity](https://grabcad.com/library/curiosity-6-newtonian-reflector-dobsonian-telescope-1)

>> **06-FINAL TELESCOPE ASSEMBLY**

![](Telescope/Design/01-a.png)

![](Telescope/Design/01-b.png)

![](Telescope/Design/03-section view.png)

* CAD Link: [GRABCAD - Curiosity](https://grabcad.com/library/curiosity-6-newtonian-reflector-dobsonian-telescope-1)

03 // MECHANICAL FABRICATION & ASSEMBLY

To get the assembly party started. From design to fabrication!
--------------------------------------------------------------

We were lucky enough to have access to a really big wooden router at our lab's facility. To make our life easier and pace up the process, we decided to utilize the capability of the wooden router for contour cuts of our desired profiles for telescope components.

![](Telescope/Fab/IMG_4781.JPG)

Profile cuts from wooden router

![](Telescope/Fab/IMG_4905.JPG)

Matte Black spray paint job to PVC pipe with drilled holes for focuser and mounting brackets of primary and secondary bracket

![](Telescope/Fab/IMG_4906.JPG)

Matte Black spray paint to be done inside as well

![](Telescope/Fab/IMG_4808.JPG)

Due to excess paint at the inner face of the tube, placing the primary bkt inside required to cut the border to fit inside the tube

![](Telescope/Fab/IMG_4811.JPG)

Adhesive velcro loop pasted to the 3D printed Primary Mirror Bkt

![](Telescope/Fab/IMG_4812.JPG)

Rubber padding adhered to the 3D printed primary bkt clamps

![](Telescope/Fab/IMG_4813.JPG)

Matte black spray paint job to the primary bkt

![](Telescope/Fab/IMG_4814.JPG)

Matte black spray paint job to the clamping bkt. Masking tape pasted to the rubber pads to avoid paint sticking to the rubber padding.

![](Telescope/Fab/IMG_4815.JPG)

3D printed bkt for fastening primary bkt assembly to the PVC tube with an addition of handle

![](Telescope/Fab/IMG_4816.JPG)

Ease of handling of the bracket is ensured by the handle

![](Telescope/Fab/IMG_4817.JPG)

Back view of the previous image

![](Telescope/Fab/IMG_4818.JPG)

Matte Black spray paint job. "I AM BATMAN"

![](Telescope/Fab/IMG_4819.JPG)

Aluminium profile L Brackets highlighting the local protrusions coming out

![](Telescope/Fab/IMG_4820.JPG)

The L brackets were faced using cutting tool and was given a smooth finish to ensure it flushes well with the wooden surface

![](Telescope/Fab/IMG_4821.JPG)

A big shoutout to the assembly table where as you can see we just placed everything. Looked really pretty

![](Telescope/Fab/IMG_4907.JPG)

Scale ruler had drilled holes for the Seondary mirror assembly. This acts as the spider vane

![](Telescope/Fab/IMG_4909.JPG)

Initial assembly of rocker box with the cradle to have a feel how it will look like

![](Telescope/Fab/IMG_4941.JPG)

Assembly of OTA cradle with rubber padding on the clamp brackets

![](Telescope/Fab/IMG_4942.JPG)

Top view of the OTA cradle highlights the rubber padding and L brackets

![](Telescope/Fab/IMG_4955.JPG)

Printouts of stopper bracket pasted on the plywood and then shaped using Electric Drill Saw

![](Telescope/Fab/IMG_4956.JPG)

OTA cradle up & down moving bkt

![](Telescope/Fab/IMG_4957.JPG)

Wooden M8 insert

![](Telescope/Fab/IMG_4962.JPG)

Insert an M8 fastener from the opposite side and using a spanner just start tightening

![](Telescope/Fab/IMG_4963.JPG)

The wooden insert will tighten by itself to the wood

![](Telescope/Fab/IMG_4966.JPG)

Assembled view with the Indian flag

![](Telescope/Fab/IMG_4967.JPG)

Rubber padding adhered with double sided tape

![](Telescope/Fab/IMG_4968.JPG)

Up and down clamping bracket inside the OTA cradle box

![](Telescope/Fab/IMG_4976.JPG)

Ensure to put a center hole on the 3D printed primary bkt while simultaneously making a center mark in the primary mirror back and to match both of them while sticking

![](Telescope/Fab/IMG_4978.JPG)

That's me(left) and Madhav(right) assembling the primary bracket

![](Telescope/Fab/IMG_4983.JPG)

This image was one of the most interesting one's that we captured where we assembled the secondary mirror and primary mirror. We tried to use a laser light to look at the light's path

![](Telescope/Fab/IMG_4993.JPG)

COLLIMATION: Take an exact printout of primary mirror with a center mark and using a red marker, mark a red point to the center of the mirror

![](Telescope/Fab/IMG_4994.JPG)

Spring loaded primary bracket assembly for ease of calibration and collimation

![](Telescope/Fab/IMG_4995.JPG)

Red point at the center of the primary mirror. Ensure to clean the mirror with IPA first

![](Telescope/Fab/IMG_4996.JPG)

Similarly, do the same activity for the secondary mirror but make a green marked point at the center

![](Telescope/Fab/IMG_4997.JPG)

The up & down bracket inside OTA cradle is adhered with a metal plate which will butt against the pushing screw. This was done to avoid any deformation to the wooden surface

![](Telescope/Fab/IMG_5001.JPG)

Rocker box assembly

![](Telescope/Fab/IMG_5002.JPG)

Black spray paint job on the rocker box assembly

![](Telescope/Fab/IMG_5006.JPG)

Madhav cutting circular teflon tooltec for azimuth bearing

![](Telescope/Fab/IMG_5007.JPG)

As can be seen, both the bodies are adhered with teflon tooltec since these bodies are flushing against each other

![](Telescope/Fab/IMG_5236.JPG)

Bag straps were added for ease of handling and movment

![](Telescope/Fab/IMG_5235.JPG)

Madhav observing Jupiter

![](Telescope/Fab/IMG_5237.JPG)

This is how we carry the entire telescope assembly right now

04 // HELP ME UNDERSTAND

What is this? Why is this? How is this?
---------------------------------------

This section highlights all the information that we came across to deepen our understanding pre-during and post assembly of the telescope. The aim is to put up information that will be helpful as and when we get to learn about something new. Happy Learning!

DOCUMENT\_INDEX // CLICK\_TO\_JUMP

### >> How do I learn the sky?

![](https://c02.purpledshub.com/uploads/sites/48/2018/11/planisphere-f7da7ff.jpg?webp=1&w=1200)

A planisphere is an astronomical tool that can help you navigate the night sky

![](https://kehillanw.org/img/articles/item_211_default-stars__q-90.jpg)

Stellarium App - one of the best online free planetarium

![](https://play-lh.googleusercontent.com/zsPc4nNL2XlqX0a8CRh7pmqLdcYuN3GdgZTA2uLvTVrww4AJeuzyG1-5Aqdmk34Mdg=w2560-h1440-rw)

NASA, Spot the station app for IOS and Android

1. Richard Berry in his book suggests, the best way to learn is via [PLANISPHERE](https://www.skyatnightmagazine.com/advice/skills/how-to-use-a-planisphere), wherein you can dial in the date and time and it will show you the sky at that instant.
2. Following is a list of applications for IOS and Android that we came across, which should help you in navigating the skies

* IOS

1. [Stellarium](https://apps.apple.com/us/app/stellarium-mobile-star-map/id1458716890)
2. [SkyGuide](https://apps.apple.com/us/app/sky-guide/id576588894) - notifies you about any transits and also the best objects to look at the sky based on your location
3. [Sky Academy](https://apps.apple.com/us/app/sky-academy-learn-astronomy/id1571488252) - for learning the constellations in the night sky

* Android

1. [Stellarium](https://play.google.com/store/apps/details?id=com.noctuasoftware.stellarium_free&hl=en_IN&pli=1)
2. [Spot the Station](https://play.google.com/store/apps/details?id=gov.nasa.hq.SpotTheStation&hl=en_IN) - notifies you about the ISS transit from your location
3. [Sky Academy](https://play.google.com/store/apps/details?id=digital.dong.skyacademy&hl=en_IN) - for learning the constellations in the night sky
4. [Look4Sat](https://play.google.com/store/apps/details?id=com.rtbishop.look4sat&hl=en_IN) - for tracking the satellites - best for amateur radio astronomers
5. [Heavons-Above](https://play.google.com/store/apps/details?id=com.heavens_above.viewer&hl=en_IN) - for tracking the satellites - best for amateur radio astronomers

### >> What is Light Gathering Power (LGP)?

The property of an optical system that tells you how much brighter things will appera than what the human eye can see.

The Light Gathering Power is defined as: $$LGP = \frac{D^2}{d^2}$$

In our case, our primary mirror has a diameter of 150mm and considering if the average human eye lens has a diameter of 6mm in darkness, how much more light will the mirror gather than the human eye?

Answer: $$LGP = \frac{150^2}{6^2} = 625$$ so 625 times more light. The telescope has much larger aperturer than the eye and allows more light which means even stars too faint to be detected by the eye can easily be brightened by the telescope so that they are easy to detect and study.

1. Bright stars in the sky: FIRST MAGNITUDE
2. Faintest visible to naked eye: SIXTH MAGNITUDE
3. For a 6" telescope having 625 LGP, it reaches stars of magnitude 13.5
4. The "Aperture - Diameter of lens or mirror" of the telescope is the most important factor, larger the aperture, more powerful is the telescope.

![](Telescope/Learning/IMG_5616.JPG)

Working of Newtonian Reflecting Telescope vs Cassegran Reflecting Telescope

![](Telescope/Learning/IMG_5617.JPG)

Short Notes on Refracting Telescope

![](Telescope/Learning/IMG_5615.JPG)

Short Notes on Catadioptric Telescope with a touch on focal ratio

### >> What is Focal Ratio & Magnification of a telescope?

$$FocalRatio = \frac{Focal Length}{Aperture} = \frac{900mm}{150mm} = 6$$

A focal ratio of 6 is an f/6 mirror

$$Magnification = \frac{FocalLengthTelescope}{FocalLengthEyepiece}$$

For a 25mm eyepiece

$$Magnification = \frac{900mm}{25mm} = 36$$

For a 9mm eyepiece

$$Magnification = \frac{900mm}{9mm} = 100$$

* Area of sky visible through an eyepiece = FIELD OF VIEW
* Area of sky covered is = REAL FIELD OF VIEW
* Angle you see when you look into the eyepiece = APPARENT FIELD OF VIEW

### >> What is Diffraction & Airy Disk ?

![](https://avantierinc.com/wp-content/uploads/2024/08/Diffraction-limit-2-768x402.png)

Airy disk is a diffraction pattern

**Diffraction:** Bending of light near the edges of an obstacle similar to how water spreads out into waves when an obstruction is present in front of it. More on diffraction in telescope can be found [>>](http://spiff.rit.edu/classes/phys312/workshops/w10c/telescopes/telescopes.html) Diffraction in Astronomy

**Airy Disk:** A very bright, circular spot of light formed in the center of image which together with the series of concentric rings around is called Airy Pattern.

To deep dive more ...

### >> What is Dobsonian Mount & Equatorial Mount?

**Dobsonian Mount**

The first classic mount for any budding amateur astronomer that only requires screws, glue, plywood and that's it.

The name coming from a renowned amateur astronomer ["John Dobson"](https://en.wikipedia.org/wiki/John_Dobson_(amateur_astronomer)) is best known for promoting awareness regarding astronomy to the common people and thus guiding everyone with low cost & quick mount newtonian reflector telescope.

[>>](https://www.youtube.com/watch?v=snz7JJlSZvw&t=5065s&pp=ygUeam9obiBkb2Jzb24gdGVsZXNjb3BlIGJ1aWxkaW5n) Telescope Building with John Dobson, a must watch video series on building a dobsonian mount.

**Equatorial Mount**

When you don't want to move your telescope manually, you opt for an equatorial mount which is designed to follow the track the movement of the objects in the night sky. Comparing with a dobsonian mount, equatorial mount offers more sturdy and expensive mount.

The motorized tracking of equatorial mount whose axis align with the earth's rotational axis. The electronics involved gives the opportunity to the user to play around with the overall navigation of the deep sky objects.

![](https://www.cloudynights.com/uploads/monthly_08_2012/post-42532-14073910120285_thumb.jpg)

Dobsonian Mount on Cloudy nights

![](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Equatorial_mount.svg/500px-Equatorial_mount.svg.png)

Principle of operation for equatorial mount

![](https://c02.purpledshub.com/uploads/sites/48/2023/01/difference-altaz-equatorial-mount-a32e204.jpg?fit=1024,800&webp=1&w=1200)

Altaz Mount vs Equatorial Mount
