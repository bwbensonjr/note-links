---
id: 128
url: https://pocketbase.io/
title: PocketBase - Open Source backend in 1 file
domain: pocketbase.io
source_date: '2025-11-28'
tags:
- database
- javascript
- github-repo
summary: PocketBase is an open-source backend solution that runs as a single file,
  offering a complete database system with built-in authentication, file storage,
  admin dashboard, and real-time capabilities. It comes ready to use out of the box
  and provides SDKs for multiple languages including JavaScript and Dart, making it
  easy to integrate with various frontend frameworks. The platform supports standard
  database operations like querying, filtering, creating, and subscribing to real-time
  record changes.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# PocketBase - Open Source backend in 1 file

Open Source backend in 1 file Realtime database Authentication File storage Admin dashboard Live demo Read the documentation Ready to use out of the box JavaScript Dart // JavaScript SDK import PocketBase from 'pocketbase' ; const pb = new PocketBase ( 'http://127.0.0.1:8090' ) ; ... // list and search for 'example' collection records const list = await pb . collection ( 'example' ) . getList ( 1 , 100 , { filter : 'title != "" && created > "2022-08-01"' , sort : '-created,title' , } ) ; // or fetch a single 'example' collection record const record = await pb . collection ( 'example' ) . getOne ( 'RECORD_ID' ) ; // delete a single 'example' collection record await pb . collection ( 'example' ) . delete ( 'RECORD_ID' ) ; // create a new 'example' collection record const newRecord = await pb . collection ( 'example' ) . create ( { title : 'Lorem ipsum dolor sit amet' , } ) ; // subscribe to changes in any record from the 'example' collection pb . collection ( 'example' ) . subscribe ( '*' , function ( e ) { console . log ( e . record ) ; } ) ; // stop listening for changes in the 'example' collection pb . collection ( 'example' ) . unsubscribe ( ) ; Integrate nicely with your favorite frontend stack
