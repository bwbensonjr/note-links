---
id: 1030
url: https://github.com/simonw/tools/blob/main/python/openai_image.py
title: tools/python/openai_image.py at main · simonw/tools · GitHub
domain: github.com
source_date: '2026-04-21'
tags:
- python
- cli-tool
- github-repo
- ai
summary: This is a Python CLI tool for generating images using OpenAI's image generation
  API, created by Simon Willison. The script uses Click to build a command-line interface
  that accepts a prompt and optional parameters like model, size, and output format,
  automatically deriving command options by introspecting the OpenAI SDK's type hints.
  It generates images, saves them to a specified file (or a random location in /tmp),
  and outputs timing and metadata information to stderr.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# tools/python/openai_image.py at main · simonw/tools · GitHub

[simonw](/simonw) 
/
**[tools](/simonw/tools)**
Public

* [Notifications](/login?return_to=%2Fsimonw%2Ftools) You must be signed in to change notification settings
* [Fork
  176](/login?return_to=%2Fsimonw%2Ftools)
* [Star
   1.7k](/login?return_to=%2Fsimonw%2Ftools)

FilesExpand file tree
---------------------

main

/

openai\_image.py
================

Copy path

BlameMore file actions

BlameMore file actions

Latest commit
-------------

History
-------

[History](/simonw/tools/commits/main/python/openai_image.py)

History

253 lines (206 loc) · 7.59 KB

main

/

openai\_image.py
================

Top

File metadata and controls
--------------------------

* Code
* Blame

253 lines (206 loc) · 7.59 KB

[Raw](https://github.com/simonw/tools/raw/refs/heads/main/python/openai_image.py)

Copy raw file

Download raw file

Open symbols panel

Edit and raw actions

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

31

32

33

34

35

36

37

38

39

40

41

42

43

44

45

46

47

48

49

50

51

52

53

54

55

56

57

58

59

60

61

62

63

64

65

66

67

68

69

70

71

72

73

74

75

76

77

78

79

80

81

82

83

84

85

86

87

88

89

90

91

92

93

94

95

96

97

98

99

100

101

102

103

104

105

106

107

108

109

110

111

112

113

114

115

116

117

118

119

120

121

122

123

124

125

126

127

128

129

130

131

132

133

134

135

136

137

138

139

140

141

142

143

144

145

146

147

148

149

150

151

152

153

154

155

156

157

158

159

160

161

162

163

164

165

166

167

168

169

170

171

172

173

174

175

176

177

178

179

180

181

182

183

184

185

186

187

188

189

190

191

192

193

194

195

196

197

198

199

200

201

202

203

204

205

206

207

208

209

210

211

212

213

214

215

216

217

218

219

220

221

222

223

224

225

226

227

228

229

230

231

232

233

234

235

236

237

238

239

240

241

242

243

244

245

246

247

248

249

250

251

252

253

#!/usr/bin/env -S uv run

# /// script

# requires-python = ">=3.10"

# dependencies = ["openai>=2.2.0", "typing-extensions", "click"]

# ///

"""

Generate an image with OpenAI’s image models (Click CLI).

- PROMPT is required.

- OUTFILE is optional; defaults to /tmp/image-<6-hex>.png.

- Flags are auto-derived by introspecting `OpenAI().images.generate` using

typing.get\_type\_hints(include\_extras=True), so Literal[...] choices appear

in --help.

- -m/--model defaults to gpt-image-1-mini (not restricted).

- Prints the JSON (without "data") to stderr in yellow; saves image to OUTFILE.

- Adds "generation\_time\_in\_s" to the printed JSON, measuring the API call duration.

"""

import json

import os

import secrets

import sys

import time

import typing as t

import types as pytypes

import typing\_extensions as tx

from base64 import b64decode

from pathlib import Path

from inspect import signature

from typing import get\_args, get\_origin, get\_type\_hints

import click

from openai import OpenAI

from openai.resources.images import Images

# Some OpenAI SDKs use sentinel / helper types; we’ll try to import them to filter unions cleanly.

try:

from openai.\_types import NotGiven, NotGivenType # type: ignore

except Exception: # pragma: no cover

NotGiven = object # type: ignore

class NotGivenType: ... # type: ignore

# ----------------------------- Introspection helpers -----------------------------

def \_is\_literal(ann) -> bool:

return get\_origin(ann) in (t.Literal, tx.Literal)

def \_is\_union(ann) -> bool:

return get\_origin(ann) in (t.Union, pytypes.UnionType)

def \_is\_optional(ann) -> bool:

return \_is\_union(ann) and type(None) in get\_args(ann)

def \_skip\_ann(ann) -> bool:

# Skip NotGiven / sentinel types in unions.

try:

if ann is NotGiven or isinstance(ann, NotGivenType):

return True

except Exception:

pass

name = getattr(ann, "\_\_name\_\_", "") or str(ann)

return "NotGiven" in name or "Omit" in name

def \_unwrap\_optional(ann):

if \_is\_optional(ann):

return tuple(a for a in get\_args(ann) if a is not type(None)) # noqa: E721

return (ann,)

def literal\_choices(annotation) -> list[str]:

"""Extract all Literal[...] strings from (possibly nested) union/optional types."""

out: list[str] = []

seen: set[str] = set()

def walk(ann):

if isinstance(ann, str):

return

if \_is\_literal(ann):

for a in get\_args(ann):

s = str(a)

if s not in seen:

seen.add(s)

out.append(s)

return

if \_is\_union(ann):

for sub in get\_args(ann):

if \_skip\_ann(sub):

continue

walk(sub)

return

origin = get\_origin(ann)

if origin is not None:

for sub in get\_args(ann):

walk(sub)

for part in \_unwrap\_optional(annotation):

if not \_skip\_ann(part):

walk(part)

return out

# ----------------------------- CLI construction -----------------------------

PARAMS = ["background", "moderation", "output\_format", "quality"]

def build\_command() -> click.Command:

# Resolve annotations properly (handles forward refs & \_\_future\_\_ annotations)

images\_mod\_globals = sys.modules[Images.\_\_module\_\_].\_\_dict\_\_

hints = get\_type\_hints(

Images.generate, globalns=images\_mod\_globals, include\_extras=True

)

# model choices are “known” but we don’t enforce them; we just show in help

model\_choices = literal\_choices(hints.get("model", str))

size\_choices = literal\_choices(hints.get("size", str))

params: list[click.Parameter] = []

# PROMPT (positional, required)

params.append(click.Argument(["prompt"], metavar="PROMPT"))

# OUTFILE (positional, optional)

params.append(

click.Argument(

["outfile"],

required=False,

type=click.Path(dir\_okay=False, writable=True, path\_type=Path),

metavar="OUTFILE",

)

)

# -m/--model (not restricted, but show known values)

model\_help = "Model to use"

if model\_choices:

model\_help += f" (known: {', '.join(model\_choices)})"

params.append(

click.Option(

["-m", "--model"],

default="gpt-image-1-mini",

show\_default=True,

help=model\_help,

)

)

# --size (not restricted, but show known values)

size\_help = "size"

if size\_choices:

size\_help += f" (known: {', '.join(size\_choices)})"

params.append(click.Option(["--size"], help=size\_help))

# Derive options (background/moderation/output\_format/quality) with choices from Literal

for name in PARAMS:

ann = hints.get(name)

label = name.replace("\_", " ")

if ann is None:

params.append(

click.Option([f"--{name.replace('\_','-')}"], help=f"{label}.")

)

continue

choices = literal\_choices(ann)

if choices:

params.append(

click.Option(

[f"--{name.replace('\_','-')}"],

type=click.Choice(choices, case\_sensitive=True),

help=f"{label}.",

)

)

else:

params.append(

click.Option([f"--{name.replace('\_','-')}"], help=f"{label}.")

)

@click.pass\_context

def callback(ctx: click.Context, \*\*kw):

if not os.getenv("OPENAI\_API\_KEY"):

raise click.UsageError("OPENAI\_API\_KEY is not set")

prompt: str = kw.pop("prompt")

outfile: Path | None = kw.pop("outfile", None)

model: str = kw.pop("model")

size: str | None = kw.pop("size", None)

if outfile is None:

# Default: /tmp/image-<6 hex>.png

outfile = Path(f"/tmp/image-{secrets.token\_hex(3)}.png")

outfile.parent.mkdir(parents=True, exist\_ok=True)

# Prepare kwargs for Images.generate (drop Nones)

gen\_kwargs = {"model": model}

if size is not None:

gen\_kwargs["size"] = size

for p in PARAMS:

v = kw.get(p, None)

if v is not None:

gen\_kwargs[p] = v

client = OpenAI()

# ---- timing just the generation call ----

t0 = time.perf\_counter()

resp = client.images.generate(prompt=prompt, \*\*gen\_kwargs)

t1 = time.perf\_counter()

generation\_time = float(t1 - t0)

# -----------------------------------------

# Pretty-print JSON (minus "data") to stderr in yellow

payload = (

resp.model\_dump()

if hasattr(resp, "model\_dump")

else json.loads(

json.dumps(resp, default=lambda o: getattr(o, "\_\_dict\_\_", str(o)))

)

)

payload.pop("data", None)

payload["generation\_time\_in\_s"] = generation\_time

click.secho(

json.dumps(payload, indent=2, sort\_keys=True), fg="yellow", err=True

)

# Save image bytes

outfile.write\_bytes(b64decode(resp.data[0].b64\_json))

click.echo(f"Saved {outfile.resolve()}")

return click.Command(

name="image",

params=params,

callback=callback,

help=(

"Generate an image with OpenAI image models.\n\n"

"Positional args:\n"

" PROMPT Text prompt describing the image to generate.\n"

" OUTFILE Output file path (default: /tmp/image-XXXXXX.png)\n"

),

context\_settings={"help\_option\_names": ["-h", "--help"]},

)

def main() -> None:

build\_command()()

if \_\_name\_\_ == "\_\_main\_\_":

main()
