---
id: 66
url: https://github.com/ynniv/vagrant-opengenera/blob/master/notes/lispm.txt
title: vagrant-opengenera/notes/lispm.txt at master · ynniv/vagrant-opengenera · GitHub
domain: github.com
source_date: '2025-12-28'
tags:
- github-repo
- lisp
- emulator
summary: 'I don''t have access to browse external URLs or view the specific content
  of that GitHub page. To provide an accurate 2-3 sentence summary, I would need you
  to either:


  1. Copy and paste the main text content from the lispm.txt file

  2. Share the key points you''d like summarized


  Once you provide the actual content, I''ll be happy to create a focused summary
  highlighting the main topic and key takeaways.'
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# vagrant-opengenera/notes/lispm.txt at master · ynniv/vagrant-opengenera · GitHub

[ynniv](/ynniv) 
/
**[vagrant-opengenera](/ynniv/vagrant-opengenera)**
Public

* [Notifications](/login?return_to=%2Fynniv%2Fvagrant-opengenera) You must be signed in to change notification settings
* [Fork
  49](/login?return_to=%2Fynniv%2Fvagrant-opengenera)
* [Star
   299](/login?return_to=%2Fynniv%2Fvagrant-opengenera)

FilesExpand file tree
---------------------

master

/

lispm.txt
=========

Copy path

BlameMore file actions

BlameMore file actions

Latest commit
-------------

History
-------

[History](/ynniv/vagrant-opengenera/commits/master/notes/lispm.txt)

History

336 lines (174 loc) · 11.4 KB

master

/

lispm.txt
=========

Top

File metadata and controls
--------------------------

* Code
* Blame

336 lines (174 loc) · 11.4 KB

[Raw](https://github.com/ynniv/vagrant-opengenera/raw/refs/heads/master/notes/lispm.txt)

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

254

255

256

257

258

259

260

261

262

263

264

265

266

267

268

269

270

271

272

273

274

275

276

277

278

279

280

281

282

283

284

285

286

287

288

289

290

291

292

293

294

295

296

297

298

299

300

301

302

303

304

305

306

307

308

309

310

311

312

313

314

315

316

317

318

319

320

321

322

323

324

325

326

327

328

329

330

331

332

333

334

335

336

[from http://www.cliki.net/VLM\_on\_Linux]

http://labs.aezenix.com/lispm/index.php?title=VLM\_On\_Linux

VLM On Linux

From LispMachinery

Jump to: navigation, search

Contents

\* 1 Running VLM on Linux

o 1.1 What is the VLM?

o 1.2 Using the snap4 Port

o 1.3 inetd

o 1.4 nfs-user-server

o 1.5 File Server authentication using the NIS

o 1.6 Starting Genera and defining your site

o 1.7 Networking the VLM

o 1.8 Getting a Meta Key

o 1.9 Some Painfully Learned Facts

Running VLM on Linux

This file gives some additional hints on running the Symbolics Virtual Lisp Machine (VLM) port to

Linux/x86\_64 by Brad Parker. I am running the VLM on a Ubuntu 6.06.1 host, so whatever I describe

here may not work with other distributions. My background is FreeBSD, so some things I describe may

be obvious to those with a Linux background. The configuration I describe in this file does not try to

provide "security", so by following it, you will potentially expose all files on your Linux host as well as

all passwords you may enter into this configuration to the Internet, and beyond.

What is the VLM?

The VLM is a development by Symbolics that, in a way, represents the last Lisp machine built before

Symbolics went bankrupt. It was originally written for the DEC Alpha processor, which was the first 64

Bit CPU that was commercially available. A software implementation of the Lisp machine required a 64

Bit CPU to attain acceptable performance. The VLM implements the full Lisp machine architecture, so it

is largely software compatible to the "real" Symbolics Lisp machines (36xx, Ivory).

Brad Parker wrote an implementation of the VLM for Linux. It is based on the Symbolics software, and

there is some uncertainty about its legal status as well as the legal status of the rest of Symbolics

intellectual property. This seems to mean that redistribution of the software or using it in a commercial

context is not possible at the moment.

The VLM program is an emulator, it implements the environment for the Lisp machine operating

system, Genera, that looks like real hardware from the Lisp side. It supports a virtual ethernet interface

and a console. The screen is implemented using the X Window System, so you need to have X11

running on your host.

Presently, the ethernet interface is hardwired to use the address 10.0.0.1 for the Linux host and

10.0.0.2 for the VLM. This cannot be changed. See the section on "Networking the VLM" in this file for

some information on how to work with this.

Using the snap4 Port

First of all, you need to get the VLM for Linux tar ball from

http://www.unlambda.com/download/genera/snap4.tar.gz - There may be a newer version, so please

check out the base directory and read this file with extra care if you are using a newer version. Unpack

the snap4 distribution on your Ubuntu host system. Make sure that you have read the README file in

the distribution, at least briefly. This file supplies additional information you'll need.

You also want the OpenGenera 2.0 distribution tarball which includes the system sources as well as

additional software packages and example files. There is no official distribution site for this tar ball, so

you will have to ask around for this. If you have it, unpack it in a directory that you wish to be accessed

by the VLM, for example /vlm.

My starting point is a plain Ubuntu installation from the 6.06.1 boot CD without any special options. A

few packages need to be added in order to make the Linux host system provide the neccessary service

to the VLM. Some of these services are found in auxilary package source which need to be enabled in

/etc/apt/sources.list (I uncommented all commented-out package sources).

$ sudo apt-get update

needs to be run after the sources have been enabled in order to refresh the local cache of package names.

The following packages are required in addition to the base system:

$ sudo apt-get install inetd nfs-common nfs-user-server

If "inetd" doesn't work for you, try "netkit-inetd". If "nfs-user-server" doesn't work for you, you probably didn't uncomment the package sources in /etc/apt/sources.list as described above.

inetd

The Internet superserver is used to provide the VLM with the system date and time during startup. After

installation, the following entries in /etc/inetd.conf need to be added or uncommented:

$ cat /etc/inetd.conf

daytime stream tcp nowait root internal

daytime dgram udp wait root internal

time stream tcp nowait root internal

time dgram udp wait root internal

After the file has been updated, restart inetd with

$ sudo /etc/init.d/inetd restart

nfs-user-server

The NFS file server is used to give the VLM access to a file system. In theory, the kernel mode NFS server

should give better performance, but I had difficulties getting it to run. After installation, /etc/exports

needs to be updated in order to export the host's file system to the VLM by adding a line like:

$ cat /etc/exports

/ 10.0.0.2(rw,no\_root\_squash)

Depending on NFS server flavour, you may want to add also the following options after the no\_root\_squash option to squelch some warnings

sync,subtree\_check

After this has been done, restart the NFS server using

$ sudo /etc/init.d/nfs-user-server restart

Now verify that your file system is properly exported:

$ showmount -e localhost

Note that the VLM now has full access to the hosts' file system and can overwrite or delete any file. You

may restrict access by exporting only part file system, but I have not tried this. Also note that this

example exports the file system to 10.0.0.2, which is the compiled-in address of the VLM. Other

systems in the network have no access to the hosts' file system.

If you access files from the VLM through NFS using "anonymous" access, the uid 4294967294 and gid

4294967294 will be used. These ids are presumably meant to mean "nobody". Add entries to

/etc/passwd and /etc/group for this uid and gid in order to have something better than the numeric uid

be displayed when listing files on the host system.

$ grep lispm /etc/passwd /etc/group

/etc/passwd:lispm:x:4294967294:4294967294::/tmp:/bin/false

/etc/group:lispm:x:4294967294:

You now have a basic setup that will allow you to start Genera. Skip to "Starting Genera and defining your site" if you are impatient.

File Server authentication using the NIS

If you want to set up log ins from the VLM to the NFS server on the host system, the VLM needs to get

access to the mapping from user ids and group ids to user names and vice versa. When Genera was

written, the NIS protocol was commonly used to provide this service within local networks. NIS basically

exports the authentication files in the traditional unix format to a local area network.

To run NIS, you need the nis package:

$ sudo apt-get install nis

You need to decide what your NIS domain name will be. This domain name does not need to

correspond to your DNS domain name. My NIS domain name is the same as my Genera site name

("pharmacy"), but anything else could be used instead. The NIS domain name must be put into the file

/etc/defaultdomain:

$ cat /etc/defaultdomain

pharmacy

You need to set up your system as NIS master in the file /etc/default/nis:

$ grep NISSERVER /etc/default/nis

NISSERVER=master

Your password file needs to use "unix crypt" style passwords instead of the now-common md5

passwords. On Ubuntu with the default installation I use, this is configured in the file

/etc/pam.d/common-password by commenting out the string "md5":

$ grep md5 /etc/pam.d/common-password

password required pam\_unix.so nullok obscure min=4 max=8 # md5

Note that you will now have to re-set all passwords using the "passwd" command so that they appear in the correct format.

The VLM does not support shadow passwords, so you need to convert your password database:

$ sudo pwunconv

$ sudo grpunconv

Once all this is done, you have to initialize your NIS database:

$ cd /var/yp

$ sudo make

This should leave you with a NIS server that can be used for authentication from the Lisp machine.

Starting Genera and defining your site

Once you have set up a suitable host environment, you need to configure the .VLM file in the snap4/

directory. (Note: Make sure you are using the .VLM file and not the dot.VLM file!) As distributed, it

contains two wrong lines:

genera.world: ../symbolics/MIT.vlod

genera.debugger: ../symbolics/VLM\_debugger

These should read

genera.world: MIT.vlod

genera.debugger: VLM\_debugger

Fix the two lines and save the file. Now you are ready to start the VLM by changing your working

directory to the snap4/ directory and type:

$ sudo ./genera

The VLM should start and present you with a welcome screen that asks you to log in. You will then have

to define your site, please see the quickstart.text file in the OpenGenera distribution directory for

information how to do that.

Once you have defined your site, save your world:

Command: Reset Network

Command: Save World :/tmp/my-genera.vlod

Replace by the name of your Linux host, as defined in the Define Site process. The path

you specify needs to be writable from the VLM through NFS. If it is not writeable, the VLM will crash and

you'll loose the site definition.

Networking the VLM

As mentioned, the VLM has a fixed network configuration with a private IP address. In order to be able

to access hosts in the Internet, your Linux host needs to do network address translation. I used the

"firestarter" utility to get a basic configuration running, but this has the drawback that the firewall has

to be manually started after the VLM had come up. firestarter creates interface-dependent firewall rules

and the tun0 interface, which is used by the VLM, exists only while the VLM runs. I am sure that a

better setup can be created by someone who knows more about Linux firewalls, and the best way

would be to use a bridge interface in the VLM so that the Linux network stack would be fully

circumvented. Maybe in the next release.

Getting a Meta Key

Try

$ xmodmap -e "keysym Alt\_L = Meta\_L Alt\_L"

$ xmodmap -e "add mod1 = Meta\_L"

if your left Alt key does not act as a Meta key.

(thanks to ecraven)

Some Painfully Learned Facts

1. The world images that are included in the snap3 and 4 releases won't boot if the system date is after ~2000! y2k thing??

2. set genera.network ip in .VLM to 10.0.0.2 \*

3. when defining world, set the ip address of yourhost to 10.0.0.1 \*

4. xwindow events from the lvm come through on 10.0.0.1, so xhost +10.0.0.1 is usually needed \*

5. genera pretty much has to run as root, ymmv but I was didn't figure out how to get it to work otherwise. \*

6. Recent linux Xwindows implementations leave out some archaic functionality that the VLM requires

only when saving world. If you get everything else set up then find that the VLM hangs during a save

world, you may need to try using an older version of your host operating system (ouch!). \*

7. If running your host OS in a virtual machine and having trouble getting a working meta key,

check that the virtualization software is not munging the keystrokes before they ever get to the X

server. (VMware default key-mappings can be a problem on a Mac keyboard.)

\* But see

Tested/working configurations:

Pentium D system with 2 gig of memory running ubuntu 7.04 64 bit desktop

VMware fusion on Mac Pro running ubuntu 7.04 64bit desktop
