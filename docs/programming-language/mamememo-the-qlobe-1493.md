---
id: 1493
url: http://mamememo.blogspot.com/2010/09/qlobe.html
title: 'mamememo: The Qlobe'
domain: mamememo.blogspot.com
source_date: '2026-11-09'
tags:
- ruby
summary: The Qlobe is a self-reproducing Ruby program (a quine) by Yusuke Endoh that
  displays an ASCII art globe. Each copy is rotated, so running it turns the globe
  45 degrees and it completes a full rotation after eight runs. Endoh wrote it for
  RubyConf as a "global" quine rather than one specialized for Japanese.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-5-5
---

# mamememo: The Qlobe

2010-09-05
----------

### The Qlobe

My Quines are sometimes specialized for Japanese. But to attend RubyConf, I should write "global" Quines.

```
v=0000;eval$s=%q~d=%!^Lcf<LK8,                  _@7gj*LJ=c5nM)Tp1g0%Xv.,S[<>YoP
4ZojjV)O>qIH1/n[|2yE[>:ieC       "%.#%  :::##"       97N-A&Kj_K_><wS5rtWk@*a+Y5
yH?b[F^e7C/56j|pmRe+:)B     "##%      ::##########"     O98(Zh)'Iof*nm.,$C5Nyt=
PPu01Avw^<IiQ=5$'D-y?    "##:         ###############"    g6`YT+qLw9k^ch|K'),tc
6ygIL8xI#LNz3v}T=4W    "#            #.   .####:#######"    lL27FZ0ij)7TQCI)P7u
}RT5-iJbbG5P-DHB<.   "              ##### # :############"   R,YvZ_rnv6ky-G+4U'
$*are@b4U351Q-ug5   "              #######################"   00x8RR%`Om7VDp4M5
PFixrPvl&<p[]1IJ   "              ############:####  %#####"   EGgDt8Lm#;bc4zS^
y]0`_PstfUxOC(q   "              .#############:##%   .##  ."   /,}.YOIFj(k&q_V
zcaAi?]^lCVYp!;  " %%            .################.     #.   "  ;s="v=%04o;ev"%
(;v=(v-($*+[45,  ":####:          :##############%       :   "  ])[n=0].to_i;)%
360)+"al$s=%q#{  "%######.              #########            "  ;;"%c"%126+$s<<
126}";d.gsub!(/  "##########.           #######%             "  |\s|".*"/,"");;
require"zlib"||  "###########           :######.             "  ;d=d.unpack"C*"
d.map{|c|n=(n||  ":#########:           .######: .           "  )*90+(c-2)%91};
e=["%x"%n].pack   " :#######%           :###### #:          "   &&"H*";e=Zlib::
Inflate.inflate(   "  ######%           .####% ::          "   &&e).unpack("b*"
)[0];22.times{|y|   "  ####%             %###             "   ;w=(Math.sqrt(1-(
(y*2.0-21)/22)**(;   " .###:             .#%             "   ;2))*23).floor;(w*
2-1).times{|x|u=(e+    " %##                           "    )[y*z=360,z]*2;u=u[
90*x/w+v+90,90/w];s[(    " #.                        "    ;y*80)+120-w+x]=(""<<
32<<".:%#")[4*u.count((     " .                   "     ;"0"))/u.size]}};;puts\
s+";_ The Qlobe#{" "*18+ (       "#  :#######"       ;"Copyright(C).Yusuke End\
oh, 2010")}";exit~;_ The Qlobe                  Copyright(C).Yusuke Endoh, 2010
```

This quine turns 45 degrees when executed; thus, it will come around when executed eight times (see below). You can make it any-degree turn by giving an integer as an command-line argument.

```
v=0416;eval$s=%q~d=%!^Lcf<LK8,                  _@7gj*LJ=c5nM)Tp1g0%Xv.,S[<>YoP
4ZojjV)O>qIH1/n[|2yE[>:ieC       ".#####%.#% "       97N-A&Kj_K_><wS5rtWk@*a+Y5
yH?b[F^e7C/56j|pmRe+:)B     "    .#####%##%      :"     O98(Zh)'Iof*nm.,$C5Nyt=
PPu01Avw^<IiQ=5$'D-y?    "       #####%###:         #"    g6`YT+qLw9k^ch|K'),tc
6ygIL8xI#LNz3v}T=4W    "        %########            #."    lL27FZ0ij)7TQCI)P7u
}RT5-iJbbG5P-DHB<.   "          :#######              ###"   R,YvZ_rnv6ky-G+4U'
$*are@b4U351Q-ug5   "            ###:  :              ####"   00x8RR%`Om7VDp4M5
PFixrPvl&<p[]1IJ   "              %#...               #####"   EGgDt8Lm#;bc4zS^
y]0`_PstfUxOC(q   "                %###               .#####"   /,}.YOIFj(k&q_V
zcaAi?]^lCVYp!;  "                    :. %%            .#####"  ;s="v=%04o;ev"%
(;v=(v-($*+[45,  "                      :####:          :####"  ])[n=0].to_i;)%
360)+"al$s=%q#{  "                      %######.             "  ;;"%c"%126+$s<<
126}";d.gsub!(/  "                      ##########.          "  |\s|".*"/,"");;
require"zlib"||  "                      ###########          "  ;d=d.unpack"C*"
d.map{|c|n=(n||  "                      :#########:          "  )*90+(c-2)%91};
e=["%x"%n].pack   "                      :#######%          "   &&"H*";e=Zlib::
Inflate.inflate(   "                      ######%          "   &&e).unpack("b*"
)[0];22.times{|y|   "                     ####%           "   ;w=(Math.sqrt(1-(
(y*2.0-21)/22)**(;   "                   .###:           "   ;2))*23).floor;(w*
2-1).times{|x|u=(e+    "                 %##           "    )[y*z=360,z]*2;u=u[
90*x/w+v+90,90/w];s[(    "               #.          "    ;y*80)+120-w+x]=(""<<
32<<".:%#")[4*u.count((     "            .        "     ;"0"))/u.size]}};;puts\
s+";_ The Qlobe#{" "*18+ (       " .#####  :#"       ;"Copyright(C).Yusuke End\
oh, 2010")}";exit~;_ The Qlobe                  Copyright(C).Yusuke Endoh, 2010

v=0341;eval$s=%q~d=%!^Lcf<LK8,                  _@7gj*LJ=c5nM)Tp1g0%Xv.,S[<>YoP
4ZojjV)O>qIH1/n[|2yE[>:ieC       "#% .#####%."       97N-A&Kj_K_><wS5rtWk@*a+Y5
yH?b[F^e7C/56j|pmRe+:)B     " :        %#####%##. "     O98(Zh)'Iof*nm.,$C5Nyt=
PPu01Avw^<IiQ=5$'D-y?    "              #####%###:   "    g6`YT+qLw9k^ch|K'),tc
6ygIL8xI#LNz3v}T=4W    "                %########      "    lL27FZ0ij)7TQCI)P7u
}RT5-iJbbG5P-DHB<.   "                   :#######        "   R,YvZ_rnv6ky-G+4U'
$*are@b4U351Q-ug5   "                     :###   :        "   00x8RR%`Om7VDp4M5
PFixrPvl&<p[]1IJ   "                        %#...          "   EGgDt8Lm#;bc4zS^
y]0`_PstfUxOC(q   "                          .###:          "   /,}.YOIFj(k&q_V
zcaAi?]^lCVYp!;  "                               :. %%       "  ;s="v=%04o;ev"%
(;v=(v-($*+[45,  "                                 :####:    "  ])[n=0].to_i;)%
360)+"al$s=%q#{  "                                 %######.  "  ;;"%c"%126+$s<<
126}";d.gsub!(/  "                                 ##########"  |\s|".*"/,"");;
require"zlib"||  "%                                ##########"  ;d=d.unpack"C*"
d.map{|c|n=(n||  "                                 :#########"  )*90+(c-2)%91};
e=["%x"%n].pack   "                                 ########"   &&"H*";e=Zlib::
Inflate.inflate(   "#.                              ######%"   &&e).unpack("b*"
)[0];22.times{|y|   "##                            :####. "   ;w=(Math.sqrt(1-(
(y*2.0-21)/22)**(;   "#.                          .###:  "   ;2))*23).floor;(w*
2-1).times{|x|u=(e+    "%    .                   %##   "    )[y*z=360,z]*2;u=u[
90*x/w+v+90,90/w];s[(    "   .                  #.   "    ;y*80)+120-w+x]=(""<<
32<<".:%#")[4*u.count((     "                 :   "     ;"0"))/u.size]}};;puts\
s+";_ The Qlobe#{" "*18+ (       "#.  .##### "       ;"Copyright(C).Yusuke End\
oh, 2010")}";exit~;_ The Qlobe                  Copyright(C).Yusuke Endoh, 2010

v=0264;eval$s=%q~d=%!^Lcf<LK8,                  _@7gj*LJ=c5nM)Tp1g0%Xv.,S[<>YoP
4ZojjV)O>qIH1/n[|2yE[>:ieC       "####% .####"       97N-A&Kj_K_><wS5rtWk@*a+Y5
yH?b[F^e7C/56j|pmRe+:)B     "#####  :       .#####"     O98(Zh)'Iof*nm.,$C5Nyt=
PPu01Avw^<IiQ=5$'D-y?    "######.              #####%"    g6`YT+qLw9k^ch|K'),tc
6ygIL8xI#LNz3v}T=4W    "####:  .                %######"    lL27FZ0ij)7TQCI)P7u
}RT5-iJbbG5P-DHB<.   "####  .                     :######"   R,YvZ_rnv6ky-G+4U'
$*are@b4U351Q-ug5   "####%                          ###:  "   00x8RR%`Om7VDp4M5
PFixrPvl&<p[]1IJ   "###                               %#..."   EGgDt8Lm#;bc4zS^
y]0`_PstfUxOC(q   "##  ..                               %###"   /,}.YOIFj(k&q_V
zcaAi?]^lCVYp!;  ":#.  .                                    :"  ;s="v=%04o;ev"%
(;v=(v-($*+[45,  ":   : :                                    "  ])[n=0].to_i;)%
360)+"al$s=%q#{  "% %#:                                      "  ;;"%c"%126+$s<<
126}";d.gsub!(/  "#::#.:  %#%                                "  |\s|".*"/,"");;
require"zlib"||  "  :      :#%                               "  ;d=d.unpack"C*"
d.map{|c|n=(n||  "       :% :                                "  )*90+(c-2)%91};
e=["%x"%n].pack   "     %###%%                              "   &&"H*";e=Zlib::
Inflate.inflate(   "   ########.                           "   &&e).unpack("b*"
)[0];22.times{|y|   "   ########.                         "   ;w=(Math.sqrt(1-(
(y*2.0-21)/22)**(;   "   ##:%###.                        "   ;2))*23).floor;(w*
2-1).times{|x|u=(e+    "       %%    .                 "    )[y*z=360,z]*2;u=u[
90*x/w+v+90,90/w];s[(    "          .                "    ;y*80)+120-w+x]=(""<<
32<<".:%#")[4*u.count((     "                     "     ;"0"))/u.size]}};;puts\
s+";_ The Qlobe#{" "*18+ (       "####.  .###"       ;"Copyright(C).Yusuke End\
oh, 2010")}";exit~;_ The Qlobe                  Copyright(C).Yusuke Endoh, 2010

v=0207;eval$s=%q~d=%!^Lcf<LK8,                  _@7gj*LJ=c5nM)Tp1g0%Xv.,S[<>YoP
4ZojjV)O>qIH1/n[|2yE[>:ieC       "#######% .#"       97N-A&Kj_K_><wS5rtWk@*a+Y5
yH?b[F^e7C/56j|pmRe+:)B     "##########: :        "     O98(Zh)'Iof*nm.,$C5Nyt=
PPu01Avw^<IiQ=5$'D-y?    "#############.             "    g6`YT+qLw9k^ch|K'),tc
6ygIL8xI#LNz3v}T=4W    "############:  .               "    lL27FZ0ij)7TQCI)P7u
}RT5-iJbbG5P-DHB<.   "#############  .                   "   R,YvZ_rnv6ky-G+4U'
$*are@b4U351Q-ug5   "##############                       "   00x8RR%`Om7VDp4M5
PFixrPvl&<p[]1IJ   "#  %#########                          "   EGgDt8Lm#;bc4zS^
y]0`_PstfUxOC(q   "    %#:  %##:  :                         "   /,}.YOIFj(k&q_V
zcaAi?]^lCVYp!;  "     #.   .:#.  .                          "  ;s="v=%04o;ev"%
(;v=(v-($*+[45,  "      :    :   : :                         "  ])[n=0].to_i;)%
360)+"al$s=%q#{  "          :% %#:                           "  ;;"%c"%126+$s<<
126}";d.gsub!(/  "           #::#.:  %#%                     "  |\s|".*"/,"");;
require"zlib"||  "             :      :#%                    "  ;d=d.unpack"C*"
d.map{|c|n=(n||  "                  :% :                     "  )*90+(c-2)%91};
e=["%x"%n].pack   "               .###%#                    "   &&"H*";e=Zlib::
Inflate.inflate(   "             ########.                 "   &&e).unpack("b*"
)[0];22.times{|y|   "            :########                "   ;w=(Math.sqrt(1-(
(y*2.0-21)/22)**(;   "            ##:%###.               "   ;2))*23).floor;(w*
2-1).times{|x|u=(e+    "               %%    .         "    )[y*z=360,z]*2;u=u[
90*x/w+v+90,90/w];s[(    "                 .         "    ;y*80)+120-w+x]=(""<<
32<<".:%#")[4*u.count((     "                     "     ;"0"))/u.size]}};;puts\
s+";_ The Qlobe#{" "*18+ (       "#######.  ."       ;"Copyright(C).Yusuke End\
oh, 2010")}";exit~;_ The Qlobe                  Copyright(C).Yusuke Endoh, 2010

v=0132;eval$s=%q~d=%!^Lcf<LK8,                  _@7gj*LJ=c5nM)Tp1g0%Xv.,S[<>YoP
4ZojjV)O>qIH1/n[|2yE[>:ieC       ":::#######%"       97N-A&Kj_K_><wS5rtWk@*a+Y5
yH?b[F^e7C/56j|pmRe+:)B     "################  :  "     O98(Zh)'Iof*nm.,$C5Nyt=
PPu01Avw^<IiQ=5$'D-y?    "####################.      "    g6`YT+qLw9k^ch|K'),tc
6ygIL8xI#LNz3v}T=4W    "  .####:############:  .       "    lL27FZ0ij)7TQCI)P7u
}RT5-iJbbG5P-DHB<.   "# # :#################  .          "   R,YvZ_rnv6ky-G+4U'
$*are@b4U351Q-ug5   "#######################%             "   00x8RR%`Om7VDp4M5
PFixrPvl&<p[]1IJ   "######:####  %#########                "   EGgDt8Lm#;bc4zS^
y]0`_PstfUxOC(q   "#######:##%   .##  .###  ..              "   /,}.YOIFj(k&q_V
zcaAi?]^lCVYp!;  "##########.     #.   .:#.  .               "  ;s="v=%04o;ev"%
(;v=(v-($*+[45,  "#########%       :    :   : :              "  ])[n=0].to_i;)%
360)+"al$s=%q#{  "#########            :% %#:                "  ;;"%c"%126+$s<<
126}";d.gsub!(/  "#######%              #::#.:  %#%          "  |\s|".*"/,"");;
require"zlib"||  ":######.                :      :#%         "  ;d=d.unpack"C*"
d.map{|c|n=(n||  ".######: .                   :% :          "  )*90+(c-2)%91};
e=["%x"%n].pack   ":###### #:                %###%%         "   &&"H*";e=Zlib::
Inflate.inflate(   ".####% ::              ########.       "   &&e).unpack("b*"
)[0];22.times{|y|   " %###                 ########.      "   ;w=(Math.sqrt(1-(
(y*2.0-21)/22)**(;   " .#%                 ##:%###.      "   ;2))*23).floor;(w*
2-1).times{|x|u=(e+    "                       %%    . "    )[y*z=360,z]*2;u=u[
90*x/w+v+90,90/w];s[(    "                        .  "    ;y*80)+120-w+x]=(""<<
32<<".:%#")[4*u.count((     "                     "     ;"0"))/u.size]}};;puts\
s+";_ The Qlobe#{" "*18+ (       "##########."       ;"Copyright(C).Yusuke End\
oh, 2010")}";exit~;_ The Qlobe                  Copyright(C).Yusuke Endoh, 2010

v=0055;eval$s=%q~d=%!^Lcf<LK8,                  _@7gj*LJ=c5nM)Tp1g0%Xv.,S[<>YoP
4ZojjV)O>qIH1/n[|2yE[>:ieC       "%  :::#####"       97N-A&Kj_K_><wS5rtWk@*a+Y5
yH?b[F^e7C/56j|pmRe+:)B     "   .:################"     O98(Zh)'Iof*nm.,$C5Nyt=
PPu01Avw^<IiQ=5$'D-y?    "     ######################"    g6`YT+qLw9k^ch|K'),tc
6ygIL8xI#LNz3v}T=4W    "     #.   .####:############:  "    lL27FZ0ij)7TQCI)P7u
}RT5-iJbbG5P-DHB<.   "     ##### # :#################  . "   R,YvZ_rnv6ky-G+4U'
$*are@b4U351Q-ug5   "    :############################    "   00x8RR%`Om7VDp4M5
PFixrPvl&<p[]1IJ   "    ############:####  %#########      "   EGgDt8Lm#;bc4zS^
y]0`_PstfUxOC(q   "    %############:###    %#:  %##:  :    "   /,}.YOIFj(k&q_V
zcaAi?]^lCVYp!;  "    .################.     #.   .:#.  .    "  ;s="v=%04o;ev"%
(;v=(v-($*+[45,  "     :##############%       :    :   : :   "  ])[n=0].to_i;)%
360)+"al$s=%q#{  "           #########            :% %#:     "  ;;"%c"%126+$s<<
126}";d.gsub!(/  "           #######%              #::#.:  %#"  |\s|".*"/,"");;
require"zlib"||  "           :######.                :      :"  ;d=d.unpack"C*"
d.map{|c|n=(n||  "           .######: .                   :% "  )*90+(c-2)%91};
e=["%x"%n].pack   "           ######%:#                .###%"   &&"H*";e=Zlib::
Inflate.inflate(   "          .####% ::              ######"   &&e).unpack("b*"
)[0];22.times{|y|   "          .###:                :#####"   ;w=(Math.sqrt(1-(
(y*2.0-21)/22)**(;   "          .#%                 ##:%#"   ;2))*23).floor;(w*
2-1).times{|x|u=(e+    "                               "    )[y*z=360,z]*2;u=u[
90*x/w+v+90,90/w];s[(    "                           "    ;y*80)+120-w+x]=(""<<
32<<".:%#")[4*u.count((     "                     "     ;"0"))/u.size]}};;puts\
s+";_ The Qlobe#{" "*18+ (       ":##########"       ;"Copyright(C).Yusuke End\
oh, 2010")}";exit~;_ The Qlobe                  Copyright(C).Yusuke Endoh, 2010

v=0000;eval$s=%q~d=%!^Lcf<LK8,                  _@7gj*LJ=c5nM)Tp1g0%Xv.,S[<>YoP
4ZojjV)O>qIH1/n[|2yE[>:ieC       "%.#%  :::##"       97N-A&Kj_K_><wS5rtWk@*a+Y5
yH?b[F^e7C/56j|pmRe+:)B     "##%      ::##########"     O98(Zh)'Iof*nm.,$C5Nyt=
PPu01Avw^<IiQ=5$'D-y?    "##:         ###############"    g6`YT+qLw9k^ch|K'),tc
6ygIL8xI#LNz3v}T=4W    "#            #.   .####:#######"    lL27FZ0ij)7TQCI)P7u
}RT5-iJbbG5P-DHB<.   "              ##### # :############"   R,YvZ_rnv6ky-G+4U'
$*are@b4U351Q-ug5   "              #######################"   00x8RR%`Om7VDp4M5
PFixrPvl&<p[]1IJ   "              ############:####  %#####"   EGgDt8Lm#;bc4zS^
y]0`_PstfUxOC(q   "              .#############:##%   .##  ."   /,}.YOIFj(k&q_V
zcaAi?]^lCVYp!;  " %%            .################.     #.   "  ;s="v=%04o;ev"%
(;v=(v-($*+[45,  ":####:          :##############%       :   "  ])[n=0].to_i;)%
360)+"al$s=%q#{  "%######.              #########            "  ;;"%c"%126+$s<<
126}";d.gsub!(/  "##########.           #######%             "  |\s|".*"/,"");;
require"zlib"||  "###########           :######.             "  ;d=d.unpack"C*"
d.map{|c|n=(n||  ":#########:           .######: .           "  )*90+(c-2)%91};
e=["%x"%n].pack   " :#######%           :###### #:          "   &&"H*";e=Zlib::
Inflate.inflate(   "  ######%           .####% ::          "   &&e).unpack("b*"
)[0];22.times{|y|   "  ####%             %###             "   ;w=(Math.sqrt(1-(
(y*2.0-21)/22)**(;   " .###:             .#%             "   ;2))*23).floor;(w*
2-1).times{|x|u=(e+    " %##                           "    )[y*z=360,z]*2;u=u[
90*x/w+v+90,90/w];s[(    " #.                        "    ;y*80)+120-w+x]=(""<<
32<<".:%#")[4*u.count((     " .                   "     ;"0"))/u.size]}};;puts\
s+";_ The Qlobe#{" "*18+ (       "#  :#######"       ;"Copyright(C).Yusuke End\
oh, 2010")}";exit~;_ The Qlobe                  Copyright(C).Yusuke Endoh, 2010
```

translated from [mamememo in Japanese (2010-09-05)](http://d.hatena.ne.jp/ku-ma-me/20100905/p1).

posted by

[Yusuke Endoh](https://draft.blogger.com/profile/10746868996593093045 "author profile")






[![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)](https://draft.blogger.com/post-edit.g?blogID=6309946718175890735&postID=6314550434067746526&from=pencil "Edit Post")

label:
[ruby](http://mamememo.blogspot.com/search/label/ruby)

#### 35 comments:

1. ![](//resources.blogblog.com/img/blank.gif)

   Anonymous[07 September, 2010 05:36](http://mamememo.blogspot.com/2010/09/qlobe.html?showComment=1283805379546#c6526162095885858024)

   This is awe-inspiring. Thank you.

   Reply[Delete](https://draft.blogger.com/comment/delete/6309946718175890735/6526162095885858024)

   Replies


   Reply
2. ![](//resources.blogblog.com/img/blank.gif)

   Anonymous[07 September, 2010 08:22](http://mamememo.blogspot.com/2010/09/qlobe.html?showComment=1283815371858#c2907206271893892769)

   You are a mad man. You are completely insane.  
     
   Very, very impressive. Wow.

   Reply[Delete](https://draft.blogger.com/comment/delete/6309946718175890735/2907206271893892769)

   Replies


   Reply
3. ![](//resources.blogblog.com/img/blank.gif)

   Anonymous[07 September, 2010 13:08](http://mamememo.blogspot.com/2010/09/qlobe.html?showComment=1283832480449#c1967098334552783793)

   WOW.

   Reply[Delete](https://draft.blogger.com/comment/delete/6309946718175890735/1967098334552783793)

   Replies


   Reply
4. ![](//resources.blogblog.com/img/blank.gif)

   Anonymous[07 September, 2010 13:19](http://mamememo.blogspot.com/2010/09/qlobe.html?showComment=1283833146742#c6231524519792108302)

   Do you accept worshipers?

   Reply[Delete](https://draft.blogger.com/comment/delete/6309946718175890735/6231524519792108302)

   Replies


   Reply
5. ![](//resources.blogblog.com/img/blank.gif)

   [Baishampayan Ghose](http://freegeek.in)[07 September, 2010 13:55](http://mamememo.blogspot.com/2010/09/qlobe.html?showComment=1283835318551#c4474783650911059795)

   You rock! Never seen a better quine.

   Reply[Delete](https://draft.blogger.com/comment/delete/6309946718175890735/4474783650911059795)

   Replies


   Reply
6. ![](//resources.blogblog.com/img/blank.gif)

   Anonymous[07 September, 2010 16:14](http://mamememo.blogspot.com/2010/09/qlobe.html?showComment=1283843666310#c3307693258842282540)

   WO. AW. WOAW.

   Reply[Delete](https://draft.blogger.com/comment/delete/6309946718175890735/3307693258842282540)

   Replies


   Reply
7. ![](//www.blogger.com/img/blogger_logo_round_35.png)

   [Crane](https://draft.blogger.com/profile/12114589148413458257)[07 September, 2010 19:34](http://mamememo.blogspot.com/2010/09/qlobe.html?showComment=1283855646794#c4618517949337703516)

   I get a syntax error in line 1 about the token ')',i don't have much knowledge of ruby,but i want to experience this amazing program,can someone help me?

   Reply[Delete](https://draft.blogger.com/comment/delete/6309946718175890735/4618517949337703516)

   Replies


   Reply
8. ![](//www.blogger.com/img/blogger_logo_round_35.png)

   [Yusuke Endoh](https://draft.blogger.com/profile/10746868996593093045)[07 September, 2010 21:48](http://mamememo.blogspot.com/2010/09/qlobe.html?showComment=1283863687751#c9155627088886032563)

   Crane: What version of ruby are you using? I tested it with ruby 1.8.7-p72 and 1.9.2-p0.

   Reply[Delete](https://draft.blogger.com/comment/delete/6309946718175890735/9155627088886032563)

   Replies


   Reply
9. ![](//www.blogger.com/img/blogger_logo_round_35.png)

   [Crane](https://draft.blogger.com/profile/12114589148413458257)[08 September, 2010 02:11](http://mamememo.blogspot.com/2010/09/qlobe.html?showComment=1283879493309#c66208146383210139)

   I tried it with ruby 1.9.1p378  
   the total error message is:  
   ./earthrotate.rb: line 1: syntax error near unexpected token `)'  
   ./earthrotate.rb: line 1: `v=0000;eval$s=%q~d=%!^LcfYoP'

   Reply[Delete](https://draft.blogger.com/comment/delete/6309946718175890735/66208146383210139)

   Replies


   Reply
10. ![](//resources.blogblog.com/img/blank.gif)

    [Justin](http://www.jiraffe.net)[08 September, 2010 02:55](http://mamememo.blogspot.com/2010/09/qlobe.html?showComment=1283882137110#c1280791670711189277)

    Crane: I was able to get past this by using ruby to execute the script. So use:  
      
    $ ruby earthrotate.rb  
      
    instead of:  
      
    $ ./earthrotate.rb

    Reply[Delete](https://draft.blogger.com/comment/delete/6309946718175890735/1280791670711189277)

    Replies


    Reply
11. ![](//www.blogger.com/img/blogger_logo_round_35.png)

    [Crane](https://draft.blogger.com/profile/12114589148413458257)[08 September, 2010 10:54](http://mamememo.blogspot.com/2010/09/qlobe.html?showComment=1283910880764#c6891094073282067605)

    @Justin:I tried as what you said:  
    ruby earthrotate.rb  
    and I get this:  
    earthrotate.rb:12:in `eval': (eval):7: syntax error, unexpected $undefined (SyntaxError)  
    zcaAi?]^lCVYp!; " %% .###% " |\s|".\*"/,"");;  
     ^  
    (eval):7: syntax error, unexpected ','  
    zcaAi?]^lCVYp!; " %% .###% " |\s|".\*"/,"");;  
     ^  
     from earthrotate.rb:12:in `main'

    Reply[Delete](https://draft.blogger.com/comment/delete/6309946718175890735/6891094073282067605)

    Replies


    Reply
12. ![](//resources.blogblog.com/img/blank.gif)

    Anonymous[08 September, 2010 12:27](http://mamememo.blogspot.com/2010/09/qlobe.html?showComment=1283916470132#c8164519690998757002)

    1. Copy one of the above programs as a.rb.  
      
    2. Run:  
      
     while true; do clear; ruby a.rb | tee b.rb; sleep 1; mv -f b.rb a.rb; done  
      
    JAWDROP

    Reply[Delete](https://draft.blogger.com/comment/delete/6309946718175890735/8164519690998757002)

    Replies


    Reply
13. ![](//resources.blogblog.com/img/blank.gif)

    Anonymous[08 September, 2010 12:39](http://mamememo.blogspot.com/2010/09/qlobe.html?showComment=1283917143947#c3446398903454247918)

    This has convinced me to write my first blog comment. That is incredible.

    Reply[Delete](https://draft.blogger.com/comment/delete/6309946718175890735/3446398903454247918)

    Replies


    Reply
14. ![](//blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh7jNxewfSdAIKyGym-2TKLRGAaD5X4EiJNXCVp8m2dnIsofaiim_9B1tiNyJqQhBW_koUiBccQI63W8IYFqfU_-D7BCNAjrqpWZRTivj2kWMDeW5QKQPc6PKG0MsuC7A/s45-c/a534cad9b273de6c620b34687979e2a5.png)

    [Robert Massaioli](https://draft.blogger.com/profile/09276670983250867687)[12 September, 2010 11:40](http://mamememo.blogspot.com/2010/09/qlobe.html?showComment=1284259242500#c7812615626273177115)

    When I wrote and thought up my first quine I thought that was pretty impressive, however you have completely blown my mind with this one. That is the single most amazing quine that I have ever seen.

    Reply[Delete](https://draft.blogger.com/comment/delete/6309946718175890735/7812615626273177115)

    Replies


    Reply
15. ![](//blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh7jNxewfSdAIKyGym-2TKLRGAaD5X4EiJNXCVp8m2dnIsofaiim_9B1tiNyJqQhBW_koUiBccQI63W8IYFqfU_-D7BCNAjrqpWZRTivj2kWMDeW5QKQPc6PKG0MsuC7A/s45-c/a534cad9b273de6c620b34687979e2a5.png)

    [Robert Massaioli](https://draft.blogger.com/profile/09276670983250867687)[12 September, 2010 11:48](http://mamememo.blogspot.com/2010/09/qlobe.html?showComment=1284259700053#c210269421134141646)

    Oh, and for those of you that want to see it in action:   
    $ watch -n1 'ruby current.rb | tee next.rb && mv next.rb current.rb'

    Reply[Delete](https://draft.blogger.com/comment/delete/6309946718175890735/210269421134141646)

    Replies


    Reply
16. ![](//resources.blogblog.com/img/blank.gif)

    [Alexander Repty](http://twitter.com/arepty)[12 September, 2010 22:59](http://mamememo.blogspot.com/2010/09/qlobe.html?showComment=1284299998515#c980999535228968194)

    I've made a YouTube video for those who want to see it in action:  
      
    http://www.youtube.com/watch?v=ktq-22iq-Po

    Reply[Delete](https://draft.blogger.com/comment/delete/6309946718175890735/980999535228968194)

    Replies


    Reply
17. ![](//resources.blogblog.com/img/blank.gif)

    Anonymous[16 September, 2010 22:30](http://mamememo.blogspot.com/2010/09/qlobe.html?showComment=1284643810024#c5834029400424298502)

    Crazy!  
    Keep it up!  
      
    Any chance on having a writeup on it's logic?

    Reply[Delete](https://draft.blogger.com/comment/delete/6309946718175890735/5834029400424298502)

    Replies


    Reply
18. ![](//www.blogger.com/img/blogger_logo_round_35.png)

    [Yusuke Endoh](https://draft.blogger.com/profile/10746868996593093045)[16 September, 2010 23:21](http://mamememo.blogspot.com/2010/09/qlobe.html?showComment=1284646915885#c3368906353966426200)

    Please read the source code :-)

    Reply[Delete](https://draft.blogger.com/comment/delete/6309946718175890735/3368906353966426200)

    Replies


    Reply
19. ![](//resources.blogblog.com/img/blank.gif)

    Anonymous[29 October, 2010 15:19](http://mamememo.blogspot.com/2010/09/qlobe.html?showComment=1288333141348#c6349301674988421409)

    dead Anonymous 2 up: quininess is achieved by having most of the program in a string and evaling it. the only exceptions are the v variable and the eval statement itself. v contains the angle of rotation of the globe at a given moment.  
      
    fully half of the program is a compressed map of the earth, which is unpacked, and as each line is printed, the corresponding line of the globe is rotated according to the value in v and distorted to proper shape by a lot of Math™, converted to ascii by a simple map, and printed in the correct area. A lot of tricks are used to make sure said area does not get executed as code or stored as data. Hope this helps in your own parsing of the source.

    Reply[Delete](https://draft.blogger.com/comment/delete/6309946718175890735/6349301674988421409)

    Replies


    Reply
20. ![](//www.blogger.com/img/blogger_logo_round_35.png)

    [Tiger](https://draft.blogger.com/profile/14382175653187845546)[18 December, 2010 02:04](http://mamememo.blogspot.com/2010/09/qlobe.html?showComment=1292605454199#c1593915253955207844)

    qlobe.ruby:24: warning: parenthesize argument(s) for future version  
      
    ruby 1.8.1  
      
    although it does work perfectly... just gives a warning.   
      
    i've never coded in ruby so i have no idea what the heck that warning means.   
      
    that is one AWESOME quine you've built

    Reply[Delete](https://draft.blogger.com/comment/delete/6309946718175890735/1593915253955207844)

    Replies


    Reply
21. ![](//resources.blogblog.com/img/blank.gif)

    Anonymous[21 December, 2010 04:46](http://mamememo.blogspot.com/2010/09/qlobe.html?showComment=1292874381124#c4631810182995475045)

    always had doubts if GOD existed. now i noe He's called Yusuke Endoh.

    Reply[Delete](https://draft.blogger.com/comment/delete/6309946718175890735/4631810182995475045)

    Replies


    Reply
22. ![](//www.blogger.com/img/blogger_logo_round_35.png)

    [Debanjan Chanda](https://draft.blogger.com/profile/05074622623754859617)[22 December, 2010 05:13](http://mamememo.blogspot.com/2010/09/qlobe.html?showComment=1292962419000#c26499281993028213)

    Hi, I don't know Ruby at all,but I am very much interested in enjoying this piece or your work :) I tried your code on http://ideone.com/sNY7M but as you could see it's giving compilation error.

    Reply[Delete](https://draft.blogger.com/comment/delete/6309946718175890735/26499281993028213)

    Replies


    Reply
23. ![](//resources.blogblog.com/img/blank.gif)

    Zubin[24 December, 2010 04:05](http://mamememo.blogspot.com/2010/09/qlobe.html?showComment=1293131154113#c8993078288958164900)

    For those wondering how to view this:  
      
    1. copy contents of textarea to qlobe.rb  
    2. for ((;;)); do for i in {1..45}; do clear; ruby qlobe.rb $i; sleep 0.1; done; done  
      
    Not sure if the "45" is correct...

    Reply[Delete](https://draft.blogger.com/comment/delete/6309946718175890735/8993078288958164900)

    Replies


    Reply
24. ![](//resources.blogblog.com/img/blank.gif)

    [Tim Jones](http://timjones.id.au)[05 January, 2011 06:45](http://mamememo.blogspot.com/2010/09/qlobe.html?showComment=1294177519256#c4963110915113161884)

    It should be 360, not 45. If it's 45 it will only rotate 45° and then start again. So the command should be:  
      
    for ((;;)); do for i in {1..360}; do clear; ruby qlobe.rb $i; sleep 0.1; done; done

    Reply[Delete](https://draft.blogger.com/comment/delete/6309946718175890735/4963110915113161884)

    Replies


    Reply
25. ![](//resources.blogblog.com/img/blank.gif)

    LVB[10 January, 2011 13:44](http://mamememo.blogspot.com/2010/09/qlobe.html?showComment=1294634649312#c3799148188814167568)

    Holy shi..quine.

    Reply[Delete](https://draft.blogger.com/comment/delete/6309946718175890735/3799148188814167568)

    Replies


    Reply
26. ![](//resources.blogblog.com/img/blank.gif)

    [Greg Mefford](http://www.gregmefford.com)[13 January, 2011 11:22](http://mamememo.blogspot.com/2010/09/qlobe.html?showComment=1294885341709#c4264529978402347038)

    for i in {0..360}; do clear; ruby qlobe.rb $i; sleep 0.05; done

    Reply[Delete](https://draft.blogger.com/comment/delete/6309946718175890735/4264529978402347038)

    Replies


    Reply
27. ![](//resources.blogblog.com/img/blank.gif)

    Anonymous[18 January, 2011 05:59](http://mamememo.blogspot.com/2010/09/qlobe.html?showComment=1295297952364#c3180574611543060578)

    @Greg, can you script that to run infinitely? I'm not sure how to wrap your script is an infinite do loop.

    Reply[Delete](https://draft.blogger.com/comment/delete/6309946718175890735/3180574611543060578)

    Replies


    Reply
28. ![](//resources.blogblog.com/img/blank.gif)

    Anonymous[18 January, 2011 06:01](http://mamememo.blogspot.com/2010/09/qlobe.html?showComment=1295298074518#c8139345916277072150)

    got it.   
    Infinite loop:  
      
    being; for i in {0..360}; do clear; ruby qlobe.rb $i; sleep 0.05; done; end while true;

    Reply[Delete](https://draft.blogger.com/comment/delete/6309946718175890735/8139345916277072150)

    Replies


    Reply
29. ![](//resources.blogblog.com/img/blank.gif)

    Anonymous[18 January, 2011 06:07](http://mamememo.blogspot.com/2010/09/qlobe.html?showComment=1295298452710#c975288625361515957)

    scratch that, doesn't work right, lemme know if any of you figure it out.

    Reply[Delete](https://draft.blogger.com/comment/delete/6309946718175890735/975288625361515957)

    Replies


    Reply
30. ![](//resources.blogblog.com/img/blank.gif)

    Anonymous[25 January, 2011 06:06](http://mamememo.blogspot.com/2010/09/qlobe.html?showComment=1295903168740#c6538570825311468709)

    for (( i=0 ; ; i++ )) do clear; ruby qlobe.rb $i%360; sleep 0.05; done

    Reply[Delete](https://draft.blogger.com/comment/delete/6309946718175890735/6538570825311468709)

    Replies


    Reply
31. ![](//blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiF2hIllFYh2kmOHWMfdsS_mI_rmIbuKvnAtz6S-qGE9cyWIjEpyKUV0cZPwm2ik-tIsvOtFTjWfDFQKzjaD2IlnanHokn-vTd0ZC33Bdu6p6PEFTm7mef2XENI-sicyds/s45-c/friends2.gif)

    [Kevin Chen](https://draft.blogger.com/profile/11100406375266020334)[08 March, 2011 20:31](http://mamememo.blogspot.com/2010/09/qlobe.html?showComment=1299583868837#c4617411118160140020)

    This is amazing.

    Reply[Delete](https://draft.blogger.com/comment/delete/6309946718175890735/4617411118160140020)

    Replies


    Reply
32. ![](//resources.blogblog.com/img/blank.gif)

    Anonymous[01 December, 2011 04:42](http://mamememo.blogspot.com/2010/09/qlobe.html?showComment=1322682140970#c5446442952238186838)

    Managed to avoid flickering using the following:  
      
    clear; for ((;;)); do for i in {1..360}; do tput cup 0 0; ruby qlobe.rb $i; sleep 0.1; done; done;

    Reply[Delete](https://draft.blogger.com/comment/delete/6309946718175890735/5446442952238186838)

    Replies


    Reply
33. ![](//resources.blogblog.com/img/blank.gif)

    Anonymous[04 May, 2012 12:50](http://mamememo.blogspot.com/2010/09/qlobe.html?showComment=1336103454926#c353851458289954845)

    Amazing.

    Reply[Delete](https://draft.blogger.com/comment/delete/6309946718175890735/353851458289954845)

    Replies


    Reply
34. ![](//blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg3sjONIN8bNUUzNj_aCJF1fppJ9Q-1H8Jla4kYO_BCswF8yS1B1LdgIfo5Hj-ffRRA3rFV7jgAA-ylVtxqgQ9gAjWyUXUEbuCKgWReD3ZUj4x3Cwp1L-eWXVGQb69O-A/s45-c/*)

    [Vizay Soni](https://draft.blogger.com/profile/15980381147809072537)[11 December, 2015 22:00](http://mamememo.blogspot.com/2010/09/qlobe.html?showComment=1449838844118#c8236982389045934301)

    Awesome...

    Reply[Delete](https://draft.blogger.com/comment/delete/6309946718175890735/8236982389045934301)

    Replies


    Reply
35. ![](//resources.blogblog.com/img/blank.gif)

    [best ed pills](https://besterectiledysfunctionpills.com/)[24 November, 2020 09:21](http://mamememo.blogspot.com/2010/09/qlobe.html?showComment=1606177271819#c8717444720491533377)

    I do not know whether it's just me or if everybody else encountering problems with your site. It looks like some of the written text in your content are running off the screen. Can someone else please provide feedback and let me know if this is happening to them as well? This might be a problem with my internet browser because I've had this happen previously. Many thanks

    Reply[Delete](https://draft.blogger.com/comment/delete/6309946718175890735/8717444720491533377)

    Replies


    Reply

Add comment

Load more...

[Newer Post](http://mamememo.blogspot.com/2010/09/inline-ook-library-that-allows-you-to.html "Newer Post")

[Older Post](http://mamememo.blogspot.com/2010/08/rubykaigi-2010.html "Older Post")
[Home](http://mamememo.blogspot.com/)

Subscribe to:
[Post Comments (Atom)](http://mamememo.blogspot.com/feeds/6314550434067746526/comments/default)
