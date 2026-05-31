---
id: 358
url: https://github.com/openvenues/libpostal
title: 'GitHub - openvenues/libpostal: A C library for parsing/normalizing street
  addresses around the world. Powered by statistical NLP and open geo data.'
domain: github.com
source_date: '2025-07-09'
tags:
- github-repo
- c
- python
summary: '**libpostal** is a C library that parses and normalizes street addresses
  worldwide using statistical NLP and open data, supporting 100+ languages across
  230+ countries. It converts messy, human-entered addresses into clean, standardized
  formats suitable for machine comparison and indexing, making it ideal as a preprocessing
  tool for geocoding and location-based applications. The library offers language
  bindings for Python, Ruby, Go, Java, PHP, and NodeJS, and is trained on over 1 billion
  addresses using machine learning techniques.'
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# GitHub - openvenues/libpostal: A C library for parsing/normalizing street addresses around the world. Powered by statistical NLP and open geo data.

libpostal: international street address NLP
===========================================

[![Build Status](https://github.com/openvenues/libpostal/actions/workflows/test.yml/badge.svg)](https://github.com/openvenues/libpostal/actions)
[![Build Status](https://camo.githubusercontent.com/fdb54bcc4fe87ddf1cf63611a74061c8902c1a638a76a12f8aa2d7c5e08c03c2/68747470733a2f2f63692e6170707665796f722e636f6d2f6170692f70726f6a656374732f7374617475732f6769746875622f6f70656e76656e7565732f6c6962706f7374616c3f6272616e63683d6d6173746572267376673d74727565)](https://ci.appveyor.com/project/albarrentine/libpostal/branch/master)
[![License](https://camo.githubusercontent.com/50ef8df3f5ac87fb90f4812ce86858015771f822e7e456a371477062fcfda16f/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f6f70656e76656e7565732f6c6962706f7374616c2e737667)](https://github.com/openvenues/libpostal/blob/master/LICENSE)
[![OpenCollective Sponsors](https://camo.githubusercontent.com/c788161b3443fe3313a5363501c12cde02503761a4a437e46b7cc19446bbb795/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f6c6962706f7374616c2f73706f6e736f72732f62616467652e737667)](#sponsors)
[![OpenCollective Backers](https://camo.githubusercontent.com/a0c2f065f8cda145a9671ab670f50a6d0dd4081babe62c6c3fe0449219651b63/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f6c6962706f7374616c2f6261636b6572732f62616467652e737667)](#backers)

libpostal is a C library for parsing/normalizing street addresses around the world using statistical NLP and open data. The goal of this project is to understand location-based strings in every language, everywhere. For a more comprehensive overview of the research behind libpostal, be sure to check out the (lengthy) introductory blog posts:

* **Original post**: [Statistical NLP on OpenStreetMap](https://medium.com/@albarrentine/statistical-nlp-on-openstreetmap-b9d573e6cc86)
* **Follow-up for 1.0 release**: [Statistical NLP on OpenStreetMap: Part 2](https://medium.com/@albarrentine/statistical-nlp-on-openstreetmap-part-2-80405b988718)

🇧🇷 🇫🇮 🇳🇬 🇯🇵 🇽🇰  🇧🇩  🇵🇱  🇻🇳  🇧🇪  🇲🇦  🇺🇦  🇯🇲  🇷🇺 🇮🇳  🇱🇻  🇧🇴  🇩🇪 🇸🇳  🇦🇲  🇰🇷 🇳🇴  🇲🇽  🇨🇿  🇹🇷  🇪🇸 🇸🇸  🇪🇪  🇧🇭  🇳🇱  🇨🇳 🇵🇹  🇵🇷  🇬🇧 🇵🇸

Addresses and the locations they represent are essential for any application dealing with maps (place search, transportation, on-demand/delivery services, check-ins, reviews). Yet even the simplest addresses are packed with local conventions, abbreviations and context, making them difficult to index/query effectively with traditional full-text search engines. This library helps convert the free-form addresses that humans use into clean normalized forms suitable for machine comparison and full-text indexing. Though libpostal is not itself a full geocoder, it can be used as a preprocessing step to make any geocoding application smarter, simpler, and more consistent internationally.

🇷🇴  🇬🇭  🇦🇺  🇲🇾  🇭🇷  🇭🇹  🇺🇸 🇿🇦  🇷🇸  🇨🇱  🇮🇹 🇰🇪 🇨🇭  🇨🇺  🇸🇰  🇦🇴  🇩🇰  🇹🇿  🇦🇱  🇨🇴  🇮🇱  🇬🇹  🇫🇷 🇵🇭  🇦🇹  🇱🇨  🇮🇸 🇮🇩   🇦🇪   🇸🇰  🇹🇳  🇰🇭  🇦🇷  🇭🇰

The core library is written in pure C. Language bindings for [Python](https://github.com/openvenues/pypostal), [Ruby](https://github.com/openvenues/ruby_postal), [Go](https://github.com/openvenues/gopostal), [Java](https://github.com/openvenues/jpostal), [PHP](https://github.com/openvenues/php-postal), and [NodeJS](https://github.com/openvenues/node-postal) are officially supported and it's easy to write bindings in other languages.

Sponsors
--------

If your company is using libpostal, consider asking your organization to sponsor the project. Interpreting what humans mean when they refer to locations is far from a solved problem, and sponsorships help us pursue new frontiers in geospatial NLP. As a sponsor, your company logo will appear prominently on the Github repo page along with a link to your site. [Sponsorship info](https://opencollective.com/libpostal#sponsor)

[![](https://camo.githubusercontent.com/723f64f9d676e03993a27e68f2f991b09788541389d002d9042cb358513a054e/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f6c6962706f7374616c2f73706f6e736f722f302f6176617461722e737667)](https://opencollective.com/libpostal/sponsor/0/website)
[![](https://camo.githubusercontent.com/a94d40d589766a33839a30850a297b08923ad38cb84ab71c29f5e259a4128f80/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f6c6962706f7374616c2f73706f6e736f722f312f6176617461722e737667)](https://opencollective.com/libpostal/sponsor/1/website)
[![](https://camo.githubusercontent.com/e64965e1b5d0fc3b44b97185537c455514ffd4b2ddbfb86a4bab19f74e57f4d6/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f6c6962706f7374616c2f73706f6e736f722f322f6176617461722e737667)](https://opencollective.com/libpostal/sponsor/2/website)
[![](https://camo.githubusercontent.com/0099703894ba4ea8641073e23f482697144dacd15dc73f6aee3bcde70e6fd14b/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f6c6962706f7374616c2f73706f6e736f722f332f6176617461722e737667)](https://opencollective.com/libpostal/sponsor/3/website)
[![](https://camo.githubusercontent.com/6d32b40ff2339660ad8865ebb8bfc1a490a8cfd3c3e97085198cfd9c6d65ce44/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f6c6962706f7374616c2f73706f6e736f722f342f6176617461722e737667)](https://opencollective.com/libpostal/sponsor/4/website)
[![](https://camo.githubusercontent.com/ab33fc8ebf44f717b40326ad2bcffde2df458ded9c11de8f56220acf1e1a46c2/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f6c6962706f7374616c2f73706f6e736f722f352f6176617461722e737667)](https://opencollective.com/libpostal/sponsor/5/website)
[![](https://camo.githubusercontent.com/87b7acdbb7f60eec8555c926b27b85861ebd993892e806d2b8b13603184d4f2f/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f6c6962706f7374616c2f73706f6e736f722f362f6176617461722e737667)](https://opencollective.com/libpostal/sponsor/6/website)
[![](https://camo.githubusercontent.com/a008cd2113f17d67da754a64cebfd1ddaee49f39e9a74d9a7a1c6eb48b2caa70/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f6c6962706f7374616c2f73706f6e736f722f372f6176617461722e737667)](https://opencollective.com/libpostal/sponsor/7/website)
[![](https://camo.githubusercontent.com/6f848e7428d76054048f505a1d3b60587a3a9d1f8b350f6d5e2d7a6fd60c58d0/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f6c6962706f7374616c2f73706f6e736f722f382f6176617461722e737667)](https://opencollective.com/libpostal/sponsor/8/website)
[![](https://camo.githubusercontent.com/375efd3ec1899cede0e106a9b350da049eb8ce54a417574759007118351fad9d/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f6c6962706f7374616c2f73706f6e736f722f392f6176617461722e737667)](https://opencollective.com/libpostal/sponsor/9/website)
[![](https://camo.githubusercontent.com/16c183bf5166a409bc30ffcbc2f2c2ffca07cf584565ae936e8928c13339e6ac/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f6c6962706f7374616c2f73706f6e736f722f31302f6176617461722e737667)](https://opencollective.com/libpostal/sponsor/10/website)
[![](https://camo.githubusercontent.com/27e729ed2a295c80ff3533a3028380d57d181513cfb59645fab255423c3b2f1d/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f6c6962706f7374616c2f73706f6e736f722f31312f6176617461722e737667)](https://opencollective.com/libpostal/sponsor/11/website)
[![](https://camo.githubusercontent.com/73b4fa18efa033015f149c892a8e8da1716f466b3cf5d7992b17ddeca54c50b4/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f6c6962706f7374616c2f73706f6e736f722f31322f6176617461722e737667)](https://opencollective.com/libpostal/sponsor/12/website)
[![](https://camo.githubusercontent.com/094630fd23424315ed5e941319a55ff8c0134f21553dad0a82a1df41d36809dc/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f6c6962706f7374616c2f73706f6e736f722f31332f6176617461722e737667)](https://opencollective.com/libpostal/sponsor/13/website)
[![](https://camo.githubusercontent.com/36dbaffc95d6f358b909dcd97a4d86d4a7649f20dc475d6877d68c2da970c985/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f6c6962706f7374616c2f73706f6e736f722f31342f6176617461722e737667)](https://opencollective.com/libpostal/sponsor/14/website)
[![](https://camo.githubusercontent.com/f925e948f1f81d7dff9a444275a170f64dea7a6969c9af47e5c5b19169bf199e/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f6c6962706f7374616c2f73706f6e736f722f31352f6176617461722e737667)](https://opencollective.com/libpostal/sponsor/15/website)
[![](https://camo.githubusercontent.com/ff814935bee568873e7bf80f2c9cb3112a9d8952ffa3fd8d92c4319f9d925fa8/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f6c6962706f7374616c2f73706f6e736f722f31362f6176617461722e737667)](https://opencollective.com/libpostal/sponsor/16/website)
[![](https://camo.githubusercontent.com/14fa6d1ff84306ae77efedecd2237f48040a1c96f16c794498af8bb83b00b507/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f6c6962706f7374616c2f73706f6e736f722f31372f6176617461722e737667)](https://opencollective.com/libpostal/sponsor/17/website)
[![](https://camo.githubusercontent.com/0dd5708692ece01229ec40c853e9f8ff4639926ab77d56f32a1af6b57a97a7a5/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f6c6962706f7374616c2f73706f6e736f722f31382f6176617461722e737667)](https://opencollective.com/libpostal/sponsor/18/website)
[![](https://camo.githubusercontent.com/61611e87655fcf477790757da23e8fc4922b11f13a32f9a9cdc2a1acf88550ff/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f6c6962706f7374616c2f73706f6e736f722f31392f6176617461722e737667)](https://opencollective.com/libpostal/sponsor/19/website)
[![](https://camo.githubusercontent.com/e1d447691f196913f641afcf2da2f9bd514f78fd130cfbabcd1b8a99a9757a9c/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f6c6962706f7374616c2f73706f6e736f722f32302f6176617461722e737667)](https://opencollective.com/libpostal/sponsor/20/website)
[![](https://camo.githubusercontent.com/fbcf5b1b588539cc1f11bd744fe651f49f9dba66d89aaf348e9cdbbc1bff2353/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f6c6962706f7374616c2f73706f6e736f722f32312f6176617461722e737667)](https://opencollective.com/libpostal/sponsor/21/website)
[![](https://camo.githubusercontent.com/397540e4f35ff176a03abad7d1b65f5a514208318fe22e86bf5f3b5610ebddec/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f6c6962706f7374616c2f73706f6e736f722f32322f6176617461722e737667)](https://opencollective.com/libpostal/sponsor/22/website)
[![](https://camo.githubusercontent.com/b4e3236107e7b1facbd3b75b15292a8ba0cd06dd3d9161658310a478ced67a90/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f6c6962706f7374616c2f73706f6e736f722f32332f6176617461722e737667)](https://opencollective.com/libpostal/sponsor/23/website)
[![](https://camo.githubusercontent.com/ded2aa0ad0cd51cbec3f4989cbb09d3f8f35450fe5a5eda390547366f8b20cf6/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f6c6962706f7374616c2f73706f6e736f722f32342f6176617461722e737667)](https://opencollective.com/libpostal/sponsor/24/website)
[![](https://camo.githubusercontent.com/7bac96d311a6f233beee303c2bd28a6dc359c0769de2a3ce2912c74aedf16cc3/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f6c6962706f7374616c2f73706f6e736f722f32352f6176617461722e737667)](https://opencollective.com/libpostal/sponsor/25/website)
[![](https://camo.githubusercontent.com/fceb20ae7e776eedc00fda798bee3cfedbf81f52a3e9142f8d0e2a70da938a57/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f6c6962706f7374616c2f73706f6e736f722f32362f6176617461722e737667)](https://opencollective.com/libpostal/sponsor/26/website)
[![](https://camo.githubusercontent.com/bbbd3ef3f4e2e628c85015de7387b2623549a86ead8ab81366757b90447a7d10/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f6c6962706f7374616c2f73706f6e736f722f32372f6176617461722e737667)](https://opencollective.com/libpostal/sponsor/27/website)
[![](https://camo.githubusercontent.com/83f3081680335e2d9f33b78b39cc9113ae12d306fce77f35ac502ec7721d7a43/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f6c6962706f7374616c2f73706f6e736f722f32382f6176617461722e737667)](https://opencollective.com/libpostal/sponsor/28/website)
[![](https://camo.githubusercontent.com/805d772936003b55e72e4a7e285cdc5e423e0ac0fedb92d447905954bc025ae6/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f6c6962706f7374616c2f73706f6e736f722f32392f6176617461722e737667)](https://opencollective.com/libpostal/sponsor/29/website)

Backers
-------

Individual users can also help support open geo NLP research by making a monthly donation:

[![](https://camo.githubusercontent.com/3ca8d903e8344f42c5760ed713825042dadde8317bf7bb8ac4203fcbd564562a/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f6c6962706f7374616c2f6261636b65722f302f6176617461722e737667)](https://opencollective.com/libpostal/backer/0/website)
[![](https://camo.githubusercontent.com/b86468166a242a8a2be0cfe44ea2a2a60dbbea7c8232bb2a981697109a9492f7/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f6c6962706f7374616c2f6261636b65722f312f6176617461722e737667)](https://opencollective.com/libpostal/backer/1/website)
[![](https://camo.githubusercontent.com/dd3c8850f1837db744851abf46f1f7c9b988e74b0d7232991c14bef5d16d3841/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f6c6962706f7374616c2f6261636b65722f322f6176617461722e737667)](https://opencollective.com/libpostal/backer/2/website)
[![](https://camo.githubusercontent.com/4946d80892a0cc4dd3aa98a428e0008553289b0a31487256cffd93d971a3e865/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f6c6962706f7374616c2f6261636b65722f332f6176617461722e737667)](https://opencollective.com/libpostal/backer/3/website)
[![](https://camo.githubusercontent.com/89830bf2e52f177ccf83af87a8b2e37fb7680a7e86ae9491234f7d0c2446d56c/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f6c6962706f7374616c2f6261636b65722f342f6176617461722e737667)](https://opencollective.com/libpostal/backer/4/website)
[![](https://camo.githubusercontent.com/0ebb5d8897947105b420c65753b4fff2e193914c929bea23540b91eab1618ce1/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f6c6962706f7374616c2f6261636b65722f352f6176617461722e737667)](https://opencollective.com/libpostal/backer/5/website)
[![](https://camo.githubusercontent.com/3d963f81c8570a9e14c312050c7e4fc3a0cb6f90308bb638f9051cdafc06e6dd/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f6c6962706f7374616c2f6261636b65722f362f6176617461722e737667)](https://opencollective.com/libpostal/backer/6/website)
[![](https://camo.githubusercontent.com/4aed429cb5509b26488f82f890305d230e45699d168c7fcc1b8b97cf16609f9b/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f6c6962706f7374616c2f6261636b65722f372f6176617461722e737667)](https://opencollective.com/libpostal/backer/7/website)
[![](https://camo.githubusercontent.com/f946fb8708aa509e60d7aa38c2f632cb4be8d4c018679710d42185b3b6248cac/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f6c6962706f7374616c2f6261636b65722f382f6176617461722e737667)](https://opencollective.com/libpostal/backer/8/website)
[![](https://camo.githubusercontent.com/df09fe4b0453c97ed014e2746a5bc5aed65d42d2a7b1c3246edf936676a8223e/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f6c6962706f7374616c2f6261636b65722f392f6176617461722e737667)](https://opencollective.com/libpostal/backer/9/website)
[![](https://camo.githubusercontent.com/fdafbccd0057ddf2541d4b556f5a6ffe2a3e08e69944d6ef9f6dd6bd31e8e682/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f6c6962706f7374616c2f6261636b65722f31302f6176617461722e737667)](https://opencollective.com/libpostal/backer/10/website)
[![](https://camo.githubusercontent.com/0377782c406a9b2adb7584436b916a97c83fa3779a95b74acc363fb44a420bb0/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f6c6962706f7374616c2f6261636b65722f31312f6176617461722e737667)](https://opencollective.com/libpostal/backer/11/website)
[![](https://camo.githubusercontent.com/f794be76d986a140fafecd5d660667c087ef67730de3b6409d72289233d5fbf6/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f6c6962706f7374616c2f6261636b65722f31322f6176617461722e737667)](https://opencollective.com/libpostal/backer/12/website)
[![](https://camo.githubusercontent.com/327e29ae586c47d5a89648b97577755ccc65b037e6daa8cc783ab322c2783a99/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f6c6962706f7374616c2f6261636b65722f31332f6176617461722e737667)](https://opencollective.com/libpostal/backer/13/website)
[![](https://camo.githubusercontent.com/bb6fcfd4f6bae17d94579f93bbcfb99258b4ba4f728f56263973c57e1984f0aa/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f6c6962706f7374616c2f6261636b65722f31342f6176617461722e737667)](https://opencollective.com/libpostal/backer/14/website)
[![](https://camo.githubusercontent.com/3485391d97209e20bc7e25f1ab17d2016212dffb08621d6c158ea91cfc882154/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f6c6962706f7374616c2f6261636b65722f31352f6176617461722e737667)](https://opencollective.com/libpostal/backer/15/website)
[![](https://camo.githubusercontent.com/5135859f1f042c3fe955ad14c2daf80211d31eafb59fff6f2a53fb4326b379fb/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f6c6962706f7374616c2f6261636b65722f31362f6176617461722e737667)](https://opencollective.com/libpostal/backer/16/website)
[![](https://camo.githubusercontent.com/3971d7abac0f7315c8124f5496c1a5d1d3dea0cc2b072b298d2fad12f35f2f29/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f6c6962706f7374616c2f6261636b65722f31372f6176617461722e737667)](https://opencollective.com/libpostal/backer/17/website)
[![](https://camo.githubusercontent.com/53fdc0ff0a4935aa73df7fc67843e6fe47f2cbbd043f3aaa524110c0c9da922d/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f6c6962706f7374616c2f6261636b65722f31382f6176617461722e737667)](https://opencollective.com/libpostal/backer/18/website)
[![](https://camo.githubusercontent.com/c7068360fbc674247f9a946a64bcd5cec39cd756b0a78083ea92f8fd7d4194e0/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f6c6962706f7374616c2f6261636b65722f31392f6176617461722e737667)](https://opencollective.com/libpostal/backer/19/website)
[![](https://camo.githubusercontent.com/065a4317c996068e0629ca46c2655faacfb766d16813cf2f30101a7d03f3e025/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f6c6962706f7374616c2f6261636b65722f32302f6176617461722e737667)](https://opencollective.com/libpostal/backer/20/website)
[![](https://camo.githubusercontent.com/9d8636b5e8fe641b0bdccfc4ca75179e0d292e0c3fb06a7907855aabffd45543/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f6c6962706f7374616c2f6261636b65722f32312f6176617461722e737667)](https://opencollective.com/libpostal/backer/21/website)
[![](https://camo.githubusercontent.com/0f0c4d1de278a056ec44d71b087aaaf0e2ea509fd01aeabe9703122128276d69/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f6c6962706f7374616c2f6261636b65722f32322f6176617461722e737667)](https://opencollective.com/libpostal/backer/22/website)
[![](https://camo.githubusercontent.com/69af2add6df75bf971290e49f77b636ff070c632b77f83679e430a484f15f8d4/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f6c6962706f7374616c2f6261636b65722f32332f6176617461722e737667)](https://opencollective.com/libpostal/backer/23/website)
[![](https://camo.githubusercontent.com/8078d464ecb21f2f82a9eeb1ec13dd2d3e9b0ba2a1183587f9e60593a97bce49/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f6c6962706f7374616c2f6261636b65722f32342f6176617461722e737667)](https://opencollective.com/libpostal/backer/24/website)
[![](https://camo.githubusercontent.com/9ec7f05188e3e312a64c2a33b4d884dce6c5a2d05d859f537eba6b5a2e11421c/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f6c6962706f7374616c2f6261636b65722f32352f6176617461722e737667)](https://opencollective.com/libpostal/backer/25/website)
[![](https://camo.githubusercontent.com/8437fec43995297fd2951f9364d11e2c20f347869cb9d1cf3c501acf5f3d993c/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f6c6962706f7374616c2f6261636b65722f32362f6176617461722e737667)](https://opencollective.com/libpostal/backer/26/website)
[![](https://camo.githubusercontent.com/3505e3bef5580f3397a320a926db4d2ed2b0a847edd865144eb19dde420a6599/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f6c6962706f7374616c2f6261636b65722f32372f6176617461722e737667)](https://opencollective.com/libpostal/backer/27/website)
[![](https://camo.githubusercontent.com/0494b9412e7a2c36f3e13e81018e866ee6390e361460f47a6da4583eee333dfe/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f6c6962706f7374616c2f6261636b65722f32382f6176617461722e737667)](https://opencollective.com/libpostal/backer/28/website)
[![](https://camo.githubusercontent.com/a431fd10bb7d66c6c3ee4e617274b2bc814b43adbf9afce421bff9829c16e019/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f6c6962706f7374616c2f6261636b65722f32392f6176617461722e737667)](https://opencollective.com/libpostal/backer/29/website)

Installation (Mac/Linux)
------------------------

Before you install, make sure you have the following prerequisites:

**On Ubuntu/Debian**

```
sudo apt-get install -y curl build-essential autoconf automake libtool pkg-config
```

**On CentOS/RHEL**

```
sudo yum install curl autoconf automake libtool pkgconfig
```

**On macOS**

Install with one command via [MacPorts](https://www.macports.org/):

```
port install libpostal
```

Or with [Homebrew](https://brew.sh/):

```
brew install libpostal
```

To compile the C library from source:

If you're using an M1 Mac, add `--disable-sse2` to the `./configure` command. This will result in poorer performance but the build will succeed.

```
git clone https://github.com/openvenues/libpostal
cd libpostal

# skip if installing for the first time
make distclean

./bootstrap.sh

# omit --datadir flag to install data in current directory
./configure --datadir=[...some dir with a few GB of space where a "libpostal" directory exists or can be created/modified...]
make -j4

# For Intel/AMD processors and the default model
./configure --datadir=[...some dir with a few GB of space where a "libpostal" directory exists or can be created/modified...]

# For Apple / ARM cpus and the default model
./configure --datadir=[...some dir with a few GB of space where a "libpostal" directory exists or can be created/modified...] --disable-sse2

# For the improved Senzing model:
./configure --datadir=[...some dir with a few GB of space where a "libpostal" directory exists or can be created/modified...] MODEL=senzing

make -j8
sudo make install

# On Linux it's probably a good idea to run
sudo ldconfig
```

libpostal has support for pkg-config, so you can use the pkg-config to print the flags needed to link your program against it:

```
pkg-config --cflags libpostal         # print compiler flags
pkg-config --libs libpostal           # print linker flags
pkg-config --cflags --libs libpostal  # print both
```

For example, if you write a program called app.c, you can compile it like this:

```
gcc app.c `pkg-config --cflags --libs libpostal`
```

Installation (Windows)
----------------------

**MSys2/MinGW**

For Windows the build procedure currently requires MSys2 and MinGW. This can be downloaded from <http://msys2.org>. Please follow the instructions on the MSys2 website for installation.

Please ensure Msys2 is up-to-date by running:

```
pacman -Syu
```

Install the following prerequisites:

```
pacman -S autoconf automake curl git make libtool gcc mingw-w64-x86_64-gcc
```

Then to build the C library:

```
git clone https://github.com/openvenues/libpostal
cd libpostal
cp -rf windows/* ./
./bootstrap.sh
./configure --datadir=[...some dir with a few GB of space...]
make -j4
make install
```

Notes: When setting the datadir, the `C:` drive would be entered as `/c`. The libpostal build script automatically add `libpostal` on the end of the path, so '/c' would become `C:\libpostal\` on Windows.

The compiled .dll will be in the `src/.libs/` directory and should be called `libpostal-1.dll`.

If you require a .lib import library to link this to your application. You can generate one using the Visual Studio `lib.exe` tool and the `libpostal.def` definition file:

```
lib.exe /def:libpostal.def /out:libpostal.lib /machine:x64
```

Installation with an alternative data model
-------------------------------------------

An alternative data model is available for libpostal. It is created by Senzing Inc. for improved parsing on US, UK and Singapore addresses and improved US rural route address handling.
To enable this add `MODEL=senzing` to the configure line during installation:

```
./configure --datadir=[...some dir with a few GB of space...] MODEL=senzing
```

The data for this model is gotten from [OpenAddress](https://openaddresses.io/), [OpenStreetMap](https://www.openstreetmap.org/) and data generated by Senzing based on customer feedback (a few hundred records), a total of about 1.2 billion records of data from over 230 countries, in 100+ languages. The data from OpenStreetMap and OpenAddress is good but not perfect so the data set was modified by filtering out badly formed addresses, correcting misclassified address tokens and removing tokens that didn't belong in the addresses, whenever these conditions were encountered.

Senzing created a data set of 12950 addresses from 89 countries that it uses to test and verify the quality of its models. The data set was generated using random addresses from OSM, minimally 50 per country. Hard-to-parse addresses were gotten from Senzing support team and customers and from the libpostal github page and added to this set. The Senzing model got 4.3% better parsing results than the default model, using this test set.

The size of this model is about 2.2GB compared to 1.8GB for the default model so keep that in mind if storages space is important.

Further information about this data model can be found at: <https://github.com/Senzing/libpostal-data>
If you run into any issues with this model, whether they have to do with parses, installation or any other problems, then please report them at <https://github.com/Senzing/libpostal-data>

Examples of parsing
-------------------

libpostal's international address parser uses machine learning (Conditional Random Fields) and is trained on over 1 billion addresses in every inhabited country on Earth. We use [OpenStreetMap](https://openstreetmap.org) and [OpenAddresses](https://openaddresses.io) as sources of structured addresses, and the OpenCage address format templates at: <https://github.com/OpenCageData/address-formatting> to construct the training data, supplementing with containing polygons, and generating sub-building components like apartment/floor numbers and PO boxes. We also add abbreviations, drop out components at random, etc. to make the parser as robust as possible to messy real-world input.

These example parse results are taken from the interactive address\_parser program
that builds with libpostal when you run `make`. Note that the parser can handle
commas vs. no commas as well as various casings and permutations of components (if the input
is e.g. just city or just city/postcode).

[![parser](https://cloud.githubusercontent.com/assets/238455/24703087/acbe35d8-19cf-11e7-8850-77fb1c3446a7.gif)](https://cloud.githubusercontent.com/assets/238455/24703087/acbe35d8-19cf-11e7-8850-77fb1c3446a7.gif)

The parser achieves very high accuracy on held-out data, currently 99.45%
correct full parses (meaning a 1 in the numerator for getting *every* token
in the address correct).

Usage (parser)
--------------

Here's an example of the parser API using the Python bindings:

```
from postal.parser import parse_address
parse_address('The Book Club 100-106 Leonard St Shoreditch London EC2A 4RH, United Kingdom')
```

And an example with the C API:

```
#include <stdio.h>
#include <stdlib.h>
#include <libpostal/libpostal.h>

int main(int argc, char **argv) {
    // Setup (only called once at the beginning of your program)
    if (!libpostal_setup() || !libpostal_setup_parser()) {
        exit(EXIT_FAILURE);
    }

    libpostal_address_parser_options_t options = libpostal_get_address_parser_default_options();
    libpostal_address_parser_response_t *parsed = libpostal_parse_address("781 Franklin Ave Crown Heights Brooklyn NYC NY 11216 USA", options);

    for (size_t i = 0; i < parsed->num_components; i++) {
        printf("%s: %s\n", parsed->labels[i], parsed->components[i]);
    }

    // Free parse result
    libpostal_address_parser_response_destroy(parsed);

    // Teardown (only called once at the end of your program)
    libpostal_teardown();
    libpostal_teardown_parser();
}
```

Parser labels
-------------

The address parser can technically use any string labels that are defined in the training data, but these are the ones currently defined, based on the fields defined in [OpenCage's address-formatting library](https://github.com/OpenCageData/address-formatting), as well as a few added by libpostal to handle specific patterns:

* **house**: venue name e.g. "Brooklyn Academy of Music", and building names e.g. "Empire State Building"
* **category**: for category queries like "restaurants", etc.
* **near**: phrases like "in", "near", etc. used after a category phrase to help with parsing queries like "restaurants in Brooklyn"
* **house\_number**: usually refers to the external (street-facing) building number. In some countries this may be a compount, hyphenated number which also includes an apartment number, or a block number (a la Japan), but libpostal will just call it the house\_number for simplicity.
* **road**: street name(s)
* **unit**: an apartment, unit, office, lot, or other secondary unit designator
* **level**: expressions indicating a floor number e.g. "3rd Floor", "Ground Floor", etc.
* **staircase**: numbered/lettered staircase
* **entrance**: numbered/lettered entrance
* **po\_box**: post office box: typically found in non-physical (mail-only) addresses
* **postcode**: postal codes used for mail sorting
* **suburb**: usually an unofficial neighborhood name like "Harlem", "South Bronx", or "Crown Heights"
* **city\_district**: these are usually boroughs or districts within a city that serve some official purpose e.g. "Brooklyn" or "Hackney" or "Bratislava IV"
* **city**: any human settlement including cities, towns, villages, hamlets, localities, etc.
* **island**: named islands e.g. "Maui"
* **state\_district**: usually a second-level administrative division or county.
* **state**: a first-level administrative division. Scotland, Northern Ireland, Wales, and England in the UK are mapped to "state" as well (convention used in OSM, GeoPlanet, etc.)
* **country\_region**: informal subdivision of a country without any political status
* **country**: sovereign nations and their dependent territories, anything with an [ISO-3166 code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).
* **world\_region**: currently only used for appending “West Indies” after the country name, a pattern frequently used in the English-speaking Caribbean e.g. “Jamaica, West Indies”

Examples of normalization
-------------------------

The expand\_address API converts messy real-world addresses into normalized
equivalents suitable for search indexing, hashing, etc.

Here's an interactive example using the Python binding:

[![expand](https://cloud.githubusercontent.com/assets/238455/14115012/52990d14-f5a7-11e5-9797-159dacdf8c5f.gif)](https://cloud.githubusercontent.com/assets/238455/14115012/52990d14-f5a7-11e5-9797-159dacdf8c5f.gif)

libpostal contains an OSM-trained language classifier to detect which language(s) are used in a given
address so it can apply the appropriate normalizations. The only input needed is the raw address string.
Here's a short list of some less straightforward normalizations in various languages.

| Input | Output (may be multiple in libpostal) |
| --- | --- |
| One-hundred twenty E 96th St | 120 east 96th street |
| C/ Ocho, P.I. 4 | calle 8 polígono industrial 4 |
| V XX Settembre, 20 | via 20 settembre 20 |
| Quatre vingt douze R. de l'Église | 92 rue de l eglise |
| ул Каретный Ряд, д 4, строение 7 | улица каретныи ряд дом 4 строение 7 |
| ул Каретный Ряд, д 4, строение 7 | ulitsa karetnyy ryad dom 4 stroyeniye 7 |
| Marktstraße 14 | markt strasse 14 |

libpostal currently supports these types of normalizations in *60+ languages*,
and you can [add more](https://github.com/openvenues/libpostal/tree/master/resources/dictionaries) (without having to write any C).

For further reading and some bizarre address edge-cases, see:
[Falsehoods Programmers Believe About Addresses](https://www.mjt.me.uk/posts/falsehoods-programmers-believe-about-addresses/).

Usage (normalization)
---------------------

Here's an example using the Python bindings for succinctness (most of the higher-level language bindings are similar):

```
from postal.expand import expand_address
expansions = expand_address('Quatre-vingt-douze Ave des Champs-Élysées')

assert '92 avenue des champs-elysees' in set(expansions)
```

The C API equivalent is a few more lines, but still fairly simple:

```
#include <stdio.h>
#include <stdlib.h>
#include <libpostal/libpostal.h>

int main(int argc, char **argv) {
    // Setup (only called once at the beginning of your program)
    if (!libpostal_setup() || !libpostal_setup_language_classifier()) {
        exit(EXIT_FAILURE);
    }

    size_t num_expansions;
    libpostal_normalize_options_t options = libpostal_get_default_options();
    char **expansions = libpostal_expand_address("Quatre-vingt-douze Ave des Champs-Élysées", options, &num_expansions);

    for (size_t i = 0; i < num_expansions; i++) {
        printf("%s\n", expansions[i]);
    }

    // Free expansions
    libpostal_expansion_array_destroy(expansions, num_expansions);

    // Teardown (only called once at the end of your program)
    libpostal_teardown();
    libpostal_teardown_language_classifier();
}
```

Command-line usage (expand)
---------------------------

After building libpostal:

```
cd src/

./libpostal "Quatre vingt douze Ave des Champs-Élysées"
```

If you have a text file or stream with one address per line, the command-line interface also accepts input from stdin:

```
cat some_file | ./libpostal --json
```

Command-line usage (parser)
---------------------------

After building libpostal:

```
cd src/

./address_parser
```

address\_parser is an interactive shell. Just type addresses and libpostal will
parse them and print the result.

Bindings
--------

Libpostal is designed to be used by higher-level languages. If you don't see your language of choice, or if you're writing a language binding, please let us know!

**Officially supported language bindings**

* Python: [pypostal](https://github.com/openvenues/pypostal)
* Ruby: [ruby\_postal](https://github.com/openvenues/ruby_postal)
* Go: [gopostal](https://github.com/openvenues/gopostal)
* Java/JVM: [jpostal](https://github.com/openvenues/jpostal)
* PHP: [php-postal](https://github.com/openvenues/php-postal)
* NodeJS: [node-postal](https://github.com/openvenues/node-postal)
* R: [poster](https://github.com/ironholds/poster)

**Unofficial language bindings**

* Java: [javacpp-presets-libpostal](https://github.com/bytedeco/javacpp-presets/tree/master/libpostal)
* LuaJIT: [lua-resty-postal](https://github.com/bungle/lua-resty-postal)
* Perl: [Geo::libpostal](https://metacpan.org/pod/Geo::libpostal)
* Elixir: [Expostal](https://github.com/SweetIQ/expostal)
* Haskell: [haskell-postal](http://github.com/netom/haskell-postal)
* Rust: [rust-postal](https://github.com/pnordahl/rust-postal)
* Rust: [rustpostal](https://crates.io/crates/rustpostal)

**Unofficial database extensions**

* PostgreSQL: [pgsql-postal](https://github.com/pramsey/pgsql-postal)

**Unofficial servers**

* Libpostal REST GO Server (need ~4Gb memory) with basic security: [postal\_server](https://github.com/le0pard/postal_server)
* Libpostal REST Go Docker: [libpostal-rest-docker](https://github.com/johnlonganecker/libpostal-rest-docker)
* Libpostal REST FastAPI Docker: [libpostal-fastapi](https://github.com/alpha-affinity/libpostal-fastapi)
* Libpostal ZeroMQ Docker: [libpostal-zeromq](https://github.com/pasupulaphani/libpostal-docker)

Tests
-----

libpostal uses [greatest](https://github.com/silentbicycle/greatest) for automated testing. To run the tests, use:

```
make check
```

Adding [test cases](https://github.com/openvenues/libpostal/tree/master/test) is easy, even if your C is rusty/non-existent, and we'd love contributions. We use mostly functional tests checking string input against string output.

libpostal also gets periodically battle-tested on millions of addresses from OSM (clean) as well as anonymized queries from a production geocoder (not so clean). During this process we use valgrind to check for memory leaks and other errors.

Data files
----------

libpostal needs to download some data files from S3. The basic files are on-disk
representations of the data structures necessary to perform expansion. For address
parsing, since model training takes a few days, we publish the fully trained model
to S3 and will update it automatically as new addresses get added to OSM, OpenAddresses, etc. Same goes for the language classifier model.

Data files are automatically downloaded when you run make. To check for and download
any new data files, you can either run `make`, or run:

```
libpostal_data download all $YOUR_DATA_DIR/libpostal
```

And replace $YOUR\_DATA\_DIR with whatever you passed to configure during install.

Language dictionaries
---------------------

libpostal contains a number of per-language dictionaries that influence expansion, the language classifier, and the parser. To explore the dictionaries or contribute abbreviations/phrases in your language, see [resources/dictionaries](https://github.com/openvenues/libpostal/tree/master/resources/dictionaries).

Training data
-------------

In machine learning, large amounts of training data are often essential for getting good results. Many open-source machine learning projects either release only the model code (results reproducible if and only if you're Google), or a pre-baked model where the training conditions are unknown.

Libpostal is a bit different because it's trained on open data that's available to everyone, so we've released the entire training pipeline (the [geodata](https://github.com/openvenues/libpostal/tree/master/scripts/geodata) package in this repo), as well as the resulting training data itself on the Internet Archive. It's over 100GB unzipped.

Training data are stored on archive.org by the date they were created. There's also a file stored in the main directory of this repo called `current_parser_training_set` which stores the date of the most recently created training set. To always point to the latest data, try something like: `latest=$(cat current_parser_training_set)` and use that variable in place of the date.

### Parser training sets

All files can be found at <https://archive.org/download/libpostal-parser-training-data-YYYYMMDD/$FILE> as gzip'd tab-separated values (TSV) files formatted like:`language\tcountry\taddress`.

* **formatted\_addresses\_tagged.random.tsv.gz** (ODBL): OSM addresses. Apartments, PO boxes, categories, etc. are added primarily to these examples
* **formatted\_places\_tagged.random.tsv.gz** (ODBL): every toponym in OSM (even cities represented as points, etc.), reverse-geocoded to its parent admins, possibly including postal codes if they're listed on the point/polygon. Every place gets a base level of representation and places with higher populations get proportionally more.
* **formatted\_ways\_tagged.random.tsv.gz** (ODBL): every street in OSM (ways with highway=\*, with a few conditions), reverse-geocoded to its admins
* **geoplanet\_formatted\_addresses\_tagged.random.tsv.gz** (CC-BY): every postal code in Yahoo GeoPlanet (includes almost every postcode in the UK, Canada, etc.) and their parent admins. The GeoPlanet admins have been cleaned up and mapped to libpostal's tagset
* **openaddresses\_formatted\_addresses\_tagged.random.tsv.gz** (various licenses, mostly CC-BY): most of the address data sets from [OpenAddresses](https://openaddresses.io/), which in turn come directly from government sources
* **uk\_openaddresses\_formatted\_addresses\_tagged.random.tsv.gz** (CC-BY): addresses from [OpenAddresses UK](https://alpha.openaddressesuk.org/)

If the parser doesn't perform as well as you'd hoped on a particular type of address, the best recourse is to use grep/awk to look through the training data and try to determine if there's some pattern/style of address that's not being captured.

Features
--------

* **Abbreviation expansion**: e.g. expanding "rd" => "road" but for almost any
  language. libpostal supports > 50 languages and it's easy to add new languages
  or expand the current dictionaries. Ideographic languages (not separated by
  whitespace e.g. Chinese) are supported, as are Germanic languages where
  thoroughfare types are concatenated onto the end of the string, and may
  optionally be separated so Rosenstraße and Rosen Straße are equivalent.
* **International address parsing**: [Conditional Random Field](https://web.archive.org/web/20240104172655/http://blog.echen.me/2012/01/03/introduction-to-conditional-random-fields/) which parses
  "123 Main Street New York New York" into {"house\_number": 123, "road":
  "Main Street", "city": "New York", "state": "New York"}. The parser works
  for a wide variety of countries and languages, not just US/English.
  The model is trained on over 1 billion addresses and address-like strings, using the
  templates in the [OpenCage address formatting repo](https://github.com/OpenCageData/address-formatting) to construct formatted,
  tagged training examples for every inhabited country in the world. Many types of [normalizations](https://github.com/openvenues/libpostal/blob/master/scripts/geodata/addresses/components.py)
  are performed to make the training data resemble real messy geocoder input as closely as possible.
* **Language classification**: multinomial logistic regression
  trained (using the [FTRL-Proximal](https://research.google.com/pubs/archive/41159.pdf) method to induce sparsity) on all of OpenStreetMap ways, addr:\* tags, toponyms and formatted
  addresses. Labels are derived using point-in-polygon tests for both OSM countries
  and official/regional languages for countries and admin 1 boundaries
  respectively. So, for example, Spanish is the default language in Spain but
  in different regions e.g. Catalunya, Galicia, the Basque region, the respective
  regional languages are the default. Dictionary-based disambiguation is employed in
  cases where the regional language is non-default e.g. Welsh, Breton, Occitan.
  The dictionaries are also used to abbreviate canonical phrases like "Calle" => "C/"
  (performed on both the language classifier and the address parser training sets)
* **Numeric expression parsing** ("twenty first" => 21st,
  "quatre-vingt-douze" => 92, again using data provided in CLDR), supports > 30
  languages. Handles languages with concatenated expressions e.g.
  milleottocento => 1800. Optionally normalizes Roman numerals regardless of the
  language (IX => 9) which occur in the names of many monarchs, popes, etc.
* **Fast, accurate tokenization/lexing**: clocked at > 1M tokens / sec,
  implements the TR-29 spec for UTF8 word segmentation, tokenizes East Asian
  languages character by character instead of on whitespace.
* **UTF8 normalization**: optionally decompose UTF8 to NFD normalization form,
  strips accent marks e.g. à => a and/or applies Latin-ASCII transliteration.
* **Transliteration**: e.g. улица => ulica or ulitsa. Uses all
  [CLDR transforms](http://www.unicode.org/repos/cldr/trunk/common/transforms/), the exact same source data as used by [ICU](http://site.icu-project.org/),
  though libpostal doesn't require pulling in all of ICU (might conflict
  with your system's version). Note: some languages, particularly Hebrew, Arabic
  and Thai may not include vowels and thus will not often match a transliteration
  done by a human. It may be possible to implement statistical transliterators
  for some of these languages.
* **Script detection**: Detects which script a given string uses (can be
  multiple e.g. a free-form Hong Kong or Macau address may use both Han and
  Latin scripts in the same address). In transliteration we can use all
  applicable transliterators for a given Unicode script (Greek can for instance
  be transliterated with Greek-Latin, Greek-Latin-BGN and Greek-Latin-UNGEGN).

Non-goals
---------

* Verifying that a location is a valid address
* Actually geocoding addresses to a lat/lon (that requires a database/search index)
* Extracting addresses from free text

Raison d'être
-------------

libpostal was originally created as part of the [OpenVenues](https://github.com/openvenues/openvenues) project to solve the problem of venue deduping. In OpenVenues, we have a data set of millions of
places derived from terabytes of web pages from the [Common Crawl](http://commoncrawl.org/).
The Common Crawl is published monthly, and so even merging the results of
two crawls produces significant duplicates.

Deduping is a relatively well-studied field, and for text documents
like web pages, academic papers, etc. there exist pretty decent approximate
similarity methods such as [MinHash](https://en.wikipedia.org/wiki/MinHash).

However, for physical addresses, the frequent use of conventional abbreviations
such as Road == Rd, California == CA, or New York City == NYC complicates
matters a bit. Even using a technique like MinHash, which is well suited for
approximate matches and is equivalent to the Jaccard similarity of two sets, we
have to work with very short texts and it's often the case that two equivalent
addresses, one abbreviated and one fully specified, will not match very closely
in terms of n-gram set overlap. In non-Latin scripts, say a Russian address and
its transliterated equivalent, it's conceivable that two addresses referring to
the same place may not match even a single character.

As a motivating example, consider the following two equivalent ways to write a
particular Manhattan street address with varying conventions and degrees
of verbosity:

* 30 W 26th St Fl #7
* 30 West Twenty-sixth Street Floor Number 7

Obviously '30 W 26th St Fl #7 != '30 West Twenty-sixth Street Floor Number 7'
in a string comparison sense, but a human can grok that these two addresses
refer to the same physical location.

libpostal aims to create normalized geographic strings, parsed into components,
such that we can more effectively reason about how well two addresses
actually match and make automated server-side decisions about dupes.

So it's not a geocoder?
-----------------------

If the above sounds a lot like geocoding, that's because it is in a way,
only in the OpenVenues case, we have to geocode without a UI or a user
to select the correct address in an autocomplete dropdown. Given a database
of source addresses such as OpenAddresses or OpenStreetMap (or all of the above),
libpostal can be used to implement things like address deduping and server-side
batch geocoding in settings like MapReduce or stream processing.

Now, instead of trying to bake address-specific conventions into traditional
document search engines like Elasticsearch using giant synonyms files, scripting,
custom analyzers, tokenizers, and the like, geocoding can look like this:

1. Run the addresses in your database through libpostal's expand\_address
2. Store the normalized string(s) in your favorite search engine, DB,
   hashtable, etc.
3. Run your user queries or fresh imports through libpostal and search
   the existing database using those strings

In this way, libpostal can perform fuzzy address matching in constant time
relative to the size of the data set.

Why C?
------

libpostal is written in C for three reasons (in order of importance):

1. **Portability/ubiquity**: libpostal targets higher-level languages that
   people actually use day-to-day: Python, Go, Ruby, NodeJS, etc. The beauty of C
   is that just about any programming language can bind to it and C compilers are
   everywhere, so pick your favorite, write a binding, and you can use libpostal
   directly in your application without having to stand up a separate server. We
   support Mac/Linux (Windows is not a priority but happy to accept patches), have
   a standard autotools build and an endianness-agnostic file format for the data
   files. The Python bindings, are maintained as part of this repo since they're
   needed to construct the training data.
2. **Memory-efficiency**: libpostal is designed to run in a MapReduce setting
   where we may be limited to < 1GB of RAM per process depending on the machine
   configuration. As much as possible libpostal uses contiguous arrays, tries
   (built on contiguous arrays), bloom filters and compressed sparse matrices to
   keep memory usage low. It's possible to use libpostal on a mobile device with
   models trained on a single country or a handful of countries.
3. **Performance**: this is last on the list for a reason. Most of the
   optimizations in libpostal are for memory usage rather than performance.
   libpostal is quite fast given the amount of work it does. It can process
   10-30k addresses / second in a single thread/process on the platforms we've
   tested (that means processing every address in OSM planet in a little over
   an hour). Check out the simple benchmark program to test on your environment
   and various types of input. In the MapReduce setting, per-core performance
   isn't as important because everything's being done in parallel, but there are
   some streaming ingestion applications at Mapzen where this needs to
   run in-process.

C conventions
-------------

libpostal is written in modern, legible, C99 and uses the following conventions:

* Roughly object-oriented, as much as allowed by C
* Almost no pointer-based data structures, arrays all the way down
* Uses dynamic character arrays (inspired by [sds](https://github.com/antirez/sds)) for safer string handling
* Confines almost all mallocs to *name*\_new and all frees to *name*\_destroy
* Efficient existing implementations for simple things like hashtables
* Generic containers (via [klib](https://github.com/attractivechaos/klib)) whenever possible
* Data structures take advantage of sparsity as much as possible
* Efficient double-array trie implementation for most string dictionaries
* Cross-platform as much as possible, particularly for \*nix

Preprocessing (Python)
----------------------

The [geodata](https://github.com/openvenues/libpostal/tree/master/scripts/geodata) Python package in the libpostal repo contains the pipeline for preprocessing the various geo
data sets and building training data for the C models to use.
This package shouldn't be needed for most users, but for those interested in generating new types of addresses or improving libpostal's training data, this is where to look.

Address parser accuracy
-----------------------

On held-out test data (meaning labeled parses that the model has *not* seen
before), the address parser achieves 99.45% full parse accuracy.

For some tasks like named entity recognition it's preferable to use something
like an F1 score or variants, mostly because there's a class bias problem (most
words are non-entities, and a system that simply predicted non-entity for
every token would actually do fairly well in terms of accuracy). That is not
the case for address parsing. Every token has a label and there are millions
of examples of each class in the training data, so accuracy is preferable as it's
a clean, simple and intuitive measure of performance.

Here we use full parse accuracy, meaning we only give the parser one "point" in
the numerator if it gets every single token in the address correct. That should
be a better measure than simply looking at whether each token was correct.

Improving the address parser
----------------------------

Though the current parser works quite well for most standard addresses, there
is still room for improvement, particularly in making sure the training data
we use is as close as possible to addresses in the wild. There are two primary
ways the address parser can be improved even further (in order of difficulty):

1. Contribute addresses to OSM. Anything with an addr:housenumber tag will be
   incorporated automatically into the parser next time it's trained.
2. If the address parser isn't working well for a particular country, language
   or style of address, chances are that some name variations or places being
   missed/mislabeled during training data creation. Sometimes the fix is to
   update the formats at: <https://github.com/OpenCageData/address-formatting>,
   and in many other cases there are relatively simple tweaks we can make
   when creating the training data that will ensure the model is trained to
   handle your use case without you having to do any manual data entry.
   If you see a pattern of obviously bad address parses, the best thing to
   do is post an issue to Github.

Contributing
------------

Bug reports, issues and pull requests are welcome. Please read the [contributing guide](/openvenues/libpostal/blob/master/CONTRIBUTING.md) before submitting your issue, bug report, or pull request.

Submit issues at: <https://github.com/openvenues/libpostal/issues>.

Shoutouts
---------

Special thanks to @BenK10 for the initial Windows build and @AeroXuk for integrating it seamlessly into the project and setting up an Appveyor build.

License
-------

The software is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).
