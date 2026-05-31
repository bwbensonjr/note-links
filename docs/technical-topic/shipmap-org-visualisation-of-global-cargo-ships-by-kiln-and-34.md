---
id: 34
url: https://www.shipmap.org/
title: Shipmap.org | Visualisation of Global Cargo Ships | By Kiln and UCL
domain: www.shipmap.org
source_date: '2026-01-07'
tags:
- web-dev
- academic-paper
summary: Shipmap.org is an interactive animated visualization created by Kiln and
  UCL that displays the global movement of merchant ships throughout 2012, tracking
  cargo types and carbon emissions in real-time. The map allows users to explore five
  categories of vessels (container, dry bulk, tanker, gas bulk, and vehicles), filter
  by ship type, and observe shipping routes overlaid on ocean bathymetry. The visualization
  reveals the environmental impact of global maritime trade by displaying CO2 emissions
  and freight volumes, making complex shipping data accessible and engaging for research,
  education, and public understanding.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Shipmap.org | Visualisation of Global Cargo Ships | By Kiln and UCL

Carbon

CO2

t

Freight

Containers

Dry

kt

Liquids

kt

Gas

m3

Vehicles

kt

Options

Show

Ports

Routes

Ships

Map

Colours

Uniform

Ship type

Filters

Container

Dry bulk

Tanker

Gas bulk

Vehicles

Map: [Kiln](https://www.kiln.digital)  Research: [UCL EI](http://www.bartlett.ucl.ac.uk/energy)

Data: [exactEarth](http://www.exactearth.com) & [Clarksons]( http://www.clarksons.com/services/research/)

Back to map

New! Stunning high-res maps for print
-------------------------------------

Due to popular demand the designers of this map, [Kiln](https://kiln.digital), are now selling stunning high-resolution versions of the world “routes” view. There are two versions available: coloured by ship type over the inky-blue base map; or just the ship in a single colour a transparent background so you can overlay or print onto whatever background colour you like. Contact [[email protected]](/cdn-cgi/l/email-protection#fb939e979794bb90929795d59f929c928f9a97) for pricing and further information.

![](images/colored_preview.jpg)
![](images/transparent_preview.jpg)

Can I embed this map?
---------------------

Yes. You are welcome to embed this map. Please include a link back to [Kiln](https://www.kiln.digital) somewhere in the text of your article. Use the following embed code for a fully responsive embed that will adjust to the width of your website. Feel free to change the height and/or give it a fixed width if you prefer.

What can I see?
---------------

You can see movements of the global merchant fleet over the course of 2012, overlaid on a bathymetric map. You can also see a few statistics such as a counter for emitted CO2 (in thousand tonnes) and maximum freight carried by represented vessels (varying units).

What can I do?
--------------

You can pan and zoom in the usual ways, and skip back and forward in time using the timeline at the bottom of the screen. The controls at the top right let you show and hide different map layers: port names, the background map, routes (a plot of all recorded vessel positions), and the animated ships view. There are also controls for filtering and colouring by vessel type.

What the are types of ships shown?
----------------------------------

The merchant fleet is divided into five categories, each of which has a filter and a CO2 and freight counter for the hour shown on the clock. The ship types and units are as follows:

* Container (e.g. manufactured goods): number of container slots equivalent to 20 feet (i.e. a 40-foot container takes two slots)
* Dry bulk (e.g. coal, aggregates): combined weight of cargo, fuel, water, provisions, passengers and crew a vessel can carry, measured in thousand tonnes
* Tanker (e.g. oil, chemicals): same as dry bulk
* Gas bulk (e.g. liquified natural gas): capacity for gases, measured in cubic metres
* Vehicles (e.g. cars): same as dry bulk

Why do ships sometimes appear to move across land?
--------------------------------------------------

In some cases this is because there are ships navigating via canals or rivers that aren’t visible on the map. Generally, though, this effect is an artefact of animating a ship between two recorded positions with missing data between, especially when the positions are separated by a narrow strip of land. We may develop the map to remove this effect in the future.

Why are there fewer ships visible in the first part of the year?
----------------------------------------------------------------

Unfortunately the data we are using for the map is incomplete for the first few months of the year: roughly January to April.

Who created this map?
---------------------

The map was created by [Kiln](https://www.kiln.digital) based on data from the [UCL Energy Institute](http://www.bartlett.ucl.ac.uk/energy) (UCL EI)

Website: Duncan Clark & Robin Houston from Kiln

Data: Julia Schaumeier & Tristan Smith from the UCL EI

Music: Bach Goldberg Variations played by [Kimiko Ishizaka](http://www.opengoldbergvariations.org)

How was the map created?
------------------------

UCL EI took data showing location and speed of ships and cross-checked it with another database to get the vessel characteristics, such as engine type and hull measurements. With this information they were able to compute the CO2 emissions for each observed hour, following the approach laid out in the Third IMO Greenhouse Gas Study 2014. Kiln took the resulting dataset and visualized it with WebGL on top of a specially created base map, which shows bathymetry (ocean depth), based on the [GEBCO\_2014 Grid](http://www.gebco.net) (version 20150318), as well as continents and major rivers from [Natural Earth](http://www.naturalearthdata.com/).

Where did you get the data and who paid?
----------------------------------------

Our data sources for shipping positions are [exactEarth](http://www.exactearth.com) for AIS data (location/speed) and [Clarksons Research UK World Fleet Register]( http://www.clarksons.com/services/research/) (static vessel information). We are very grateful to our funders, the [European Climate Foundation](http://europeanclimate.org/).

I want one too!
---------------

If you want to have an installation in your foyer, museum, living room, you can contact us at [[email protected]](/cdn-cgi/l/email-protection#94fcf1f8f8fbd4fffdf8fabafde0). We’d be happy to work on a bespoke version.

[![](images/iiba.png)](http://www.informationisbeautifulawards.com/showcase/1580-shipmap-org)

Back to map
