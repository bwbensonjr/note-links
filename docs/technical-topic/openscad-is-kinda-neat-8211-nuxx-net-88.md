---
id: 88
url: https://nuxx.net/blog/2025/12/20/openscad-is-kinda-neat/
title: OpenSCAD Is Kinda Neat &#8211; nuxx.net
domain: nuxx.net
source_date: '2025-12-20'
tags:
- cli-tool
- tutorial
summary: OpenSCAD is a code-based CAD tool that the author found surprisingly effective
  for designing simple 3D-printable objects. By reimplementing a parameterized battery
  holder originally created in Fusion 360, the author discovered that OpenSCAD can
  produce equivalent results without requiring expensive software, making it ideal
  for straightforward geometric designs like spacers and organizers. The approach
  uses simple variables and loops to generate customizable models that can be directly
  sent to a 3D printer.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# OpenSCAD Is Kinda Neat &#8211; nuxx.net

OpenSCAD Is Kinda Neat Published December 20, 2025 Designing a simple battery holder in OpenSCAD. Earlier this year I designed a very basic box/organizer for AA and AAA batteries in Autodesk Fusion , making it parameterized so that by changing a few variables one could adjust the battery type/size, rows/columns, etc. This worked well, and after uploading it to Printables earlier today I realized that reimplementing it would probably be a good way to learn the basics of OpenSCAD . OpenSCAD is a rather different type of CAD tool, one in which you write code to generate objects. Because my battery holder is very simple (just a box with a pattern of cutouts) and uses input parameters, I figured it’d be a good intro to a new language / tool. And in the future might even be better than firing up Fusion for such simple designs. After going through part of the tutorial and an hour or so of poking, here’s the result: battery_holder_generator.scad Slicer showing the Fusion model on top and OpenSCAD on bottom. By changing just a few variables — numRows and numColumns and batteryType — one can render a customized battery holder which can then be plopped into a slicer and printed. No heavy/expensive CAD software needed and the output is effectively the same. Without comments or informative output, this is the meat of the code: AA = 15; AAA = 11; heightCompartment = 19; thicknessWall = 1; numRows = 4; numColumns = 10; batteryType = AA; widthBox = (numRows * batteryType) + ((numRows + 1) * thicknessWall); lengthBox = (numColumns * batteryType) + ((numColumns + 1) * thicknessWall); depthBox = heightCompartment + thicknessWall; difference() { cube([lengthBox, widthBox, depthBox]); for (c = [ 1 : numColumns ]) for (r = [ 1 : numRows ]) let ( startColumn = ((c * thicknessWall) + ((c - 1) * batteryType)), startRow = ((r * thicknessWall) + ((r - 1) * batteryType)) ) { translate([startColumn, startRow, thicknessWall]) cube([batteryType, batteryType, heightCompartment + 1]); } }; Simply, it draws a box and cuts out the holes. (The first cube() draws the main box, then difference() subtracts the battery holes via the second cube() as their quantity and location (via translate() ) is iterated. That’s it. Pretty neat, eh? (One part that confused me is how I needed to use let() to define startColumn and startRow inside the loop. I don’t understand this…) While this probably won’t be very helpful for more complicated designs, I can see this being super useful for bearing drifts, spacers, and other similar simple (yet incredibly useful in real life) geometric shapes. Published in computers and making things
