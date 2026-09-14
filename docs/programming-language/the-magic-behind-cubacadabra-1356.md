---
id: 1356
url: https://andrewarrow.dev/2026/moon/2/day/19/the-magic-behind-cubacadabra/
title: The Magic Behind cubacadabra
domain: andrewarrow.dev
source_date: '2026-09-12'
tags:
- rust
- web-dev
- tutorial
summary: The article describes how cubacadabra, a multi-platform application, uses
  a shared Rust core to eliminate code duplication across iOS, Android, and web versions.
  Rather than rebuilding features three times in different languages, the project
  keeps platform-specific native controls minimal while moving portable application
  logic, validation, and business rules into reusable Rust crates exposed through
  language bindings. This approach allows product decisions and complex behaviors—like
  handling username saves with concurrent edits or managing multiplayer session state—to
  be implemented once and maintained consistently across all platforms.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# The Magic Behind cubacadabra

01 / Make some code disappear
-----------------------------

Before abracadabra was something you said over a top hat, it was something you wore around your neck. In the ancient Roman [Liber Medicinalis](https://artsandculture.google.com/asset/quintus-serenus-liber-medicinalis/fAGBmLhWW99n0g), attributed to Quintus Serenus Sammonicus, the prescription was to write the word repeatedly, removing a letter each time, and wear the result as a charm against fever. An unusually literal approach to making a problem smaller.

If you've shipped iOS, Android, and web versions of something, you know the usual routine. Build the feature in Swift. Build it again in Kotlin. Build it again in JavaScript. Each version gets its own validation, requests, loading state, and error handling. They talk to the same backend, so we call them three clients of one product. We still wrote much of the product three times.

Then the feature changes. iOS learns how to recover from a failed save. Android gets the fix a week later. The browser handles the same error differently. Nobody set out to design three behaviors. They just accumulated while everyone was doing normal development.

I want cubacadabra's clients to become thin shells around Rust. Keep the minimum Swift, Kotlin, and JavaScript needed for native controls, device services, and browser integration. Move the portable application logic into shared Rust crates. That includes the boring account screens as well as the game engine. DRY, don't repeat yourself, should apply to the decisions the application makes.

A username field can still be a SwiftUI text field, a Compose text field, or an HTML input. Each forwards edits to Rust and displays the resulting state. Rust decides whether Save is enabled, which request to make, and what its response means. Changing the rule changes one implementation. The three screens can keep looking like they belong on their platforms.

There are good precedents. [Litter](https://github.com/0xSero/litter) has native iOS and Android interfaces over a Rust core that owns session state, streaming, and reconnect behavior, exposed through UniFFI bindings. [Mozilla's shared Rust components](https://firefox-source-docs.mozilla.org/rust-components/developing-rust-components/index.html) grew out of maintaining separate sync implementations for Firefox's desktop and mobile apps. The reason will sound familiar: duplicated logic was hard to maintain, and differences between implementations caused bugs.

02 / Is all this worth a save button?
-------------------------------------

I worked through this in a [long architecture discussion](https://chatgpt.com/share/6aa2eb74-0490-83e8-aba5-57d9ad42b994) and the [iOS development notes](https://github.com/cubacadabra/ios_app/tree/main/docs). A senior mobile developer could reasonably ask why a username field needs Rust, a C ABI, JNI, and WASM. Separate native implementations are easier to debug in their own IDEs. Bindings add build work and lifetime bugs. For a small app with a few forms, duplication could be cheaper.

For cubacadabra, I'm convinced the shared core is worth it. Rust already runs the engine and desktop Studio, and the browser already runs it through WASM. As the platform grows, joining a game will involve content compatibility, parental permissions, subscription access, blocked players, and recovery when a connection dies halfway through. I want to work out those interactions once. I don't want every new rule to become a coordination problem between three implementations.

The investment is starting to pay off. One [iOS integration commit](https://github.com/cubacadabra/ios_app/commit/bbde24eb3edb07cb2f580dc2bd17e8ef15cc32d3) added 106 lines and removed 269, simplifying the username screens and their bridge. The first web integration grew because it needed the infrastructure. Future features should reuse that machinery. The test is whether their complicated behavior lives in one place and their host adapters stay small.

03 / The save button has opinions
---------------------------------

One implementation doesn't mean one enormous crate. [cubacadabra-client](https://github.com/cubacadabra/rust/commit/205e3c81b3f5eb69786eb17f3f228ef6cbda6efd) owns the engine-facing multiplayer session. [cubacadabra-app](https://github.com/cubacadabra/rust/commit/1221dcd28f6526e086e7721a97c8f22dc735e5b0) owns portable behavior outside gameplay. The engine owns simulation and rendering. A username save belongs in the app crate, where all three consumer clients can use it.

Suppose you save "Dragon\_7," keep typing, then sign out before the response arrives. The old response could overwrite your newer draft or update whoever signed in next. That is exactly the sort of rule I want fixed once.

The host dispatches `UsernameChanged` and `SaveUsername`. Rust validates the draft and emits an HTTP effect with an ID, account ID, method, path, and body. The host supplies credentials, performs the request, and returns its raw status and body. Rust accepts or rejects the response before any screen updates the profile. The HTTP executor stays native; the meaning of the request stays shared.

Replacing the session invalidates pending work. Effect IDs aren't reused within the model, so a late response can't complete a new account's operation. Editing during a save preserves the newer draft. Those decisions now have one implementation and one set of shared contract cases.

> I want to work out those interactions once.

Avatar saves, catalog pagination, and optimistic block/unblock now follow the same pattern. Reporting remains host-owned. On the phones, an `AppViewModel` lives beside the `GameViewModel`, so restarting a game doesn't cancel an account save. The [runtime contract](https://github.com/cubacadabra/rust/blob/main/docs/app-runtime.md) documents that boundary and its tests. Device integration still needs checking; the product rules can be exercised independently of a screen.

04 / Who owns that pointer?
---------------------------

Our bindings differ from Litter's: cubacadabra currently uses a small C interface on mobile and wasm-bindgen in the browser. The app crate needs Serde and serde\_json, with no renderer or async HTTP runtime. That keeps shared application behavior usable without starting a game.

The [native app ABI](https://github.com/cubacadabra/rust/blob/main/include/cubacadabra_app.h) is seven functions: create, destroy, dispatch JSON, get snapshot JSON, poll effect JSON, and read the output pointer and length. Handles are single-threaded. Output belongs to Rust and must be copied before the next mutation. Swift copies it into `Data`; Android has a small JNI byte-array adapter. Both check the snapshot protocol version. An incompatible binding fails instead of quietly reviving a second set of account rules.

![Cubacadabra running on an iPhone 17 with a player in a bright game world](assets/iphone.jpg)


iPhone / native clientThe host supplies the device surface; the shared runtime supplies the world, controls, and player state.

There is serialization and copying here. For account edits and catalog pages, I like being able to read the contract. Studio calls the game client through ordinary Rust methods and enums. The native game client exposes a borrowed engine pointer for existing input and rendering APIs; destroying the client invalidates it. Rust's ownership rules still need an honest description when the next caller is C.

The browser has another easy mistake waiting for you. `WebClient` and `WebRenderer` come from the same generated WASM module, so an engine handle refers to the same linear memory on both sides. Two modules compiled from the same source wouldn't make their pointers interchangeable. The app runtime is a separate WASM module, which lets an account page edit a username without loading the renderer. It has no engine pointer to share.

05 / Two people touched the same thing
--------------------------------------

The client extraction removed a different kind of repetition. Each host had been translating socket messages, maintaining remote players, routing world changes, and draining the Luau network outbox. In the browser's ["crate 2nd" commit](https://github.com/cubacadabra/web/commit/60c11f85d198080a59ee491f7ea95ffd3f2f0b82), 244 lines came out and 74 went in. That's one host's diff, including its adapters. The useful part is having one session implementation to fix.

![Cubacadabra Studio test workspace showing one active player session and three session preview panels](assets/testing.jpg)


Studio / test workspaceA multiplayer surface makes the gap between “one client works” and “the session behaves” impossible to ignore.

Hosts pass socket text to `ClientSession::receive_text` and poll actions before and after stepping the engine. Rust emits `SetWorld` and `SendText`. The host still owns authentication, reconnect backoff, and movement-send throttling. A launch can keep the engine's logical world as "arena" while routing the socket to "arena:7." Rust also tracks remote identities and generations, filters ignored accounts, and submits a versioned roster when it changes.

Now put two friends at the same relay checkpoint. Both read sequence 7. Both try to advance the round. The JavaScript backend uses a Cloudflare Durable Object for a world instance, and its retained-state API accepts a compare-and-set with the sequence the client observed. One update advances the sequence. The other gets the current state back with a conflict flag.

![Sally standing at a colorful canyon checkpoint in cubacadabra's platforming game](assets/jump.jpg)


Signal Run / checkpointThe shared session keeps the world moving even when two players reach the same state at once.

The shared Luau SDK keeps pending intents, rebases them on that response, and retries. In Signal Run, the reducer returns nil if somebody else already captured that node. The duplicate intent can disappear. Retained channels also go to new arrivals, and server-derived `ageMs` lets a short timer resume without believing whatever time a phone thinks it is.

This is enough to coordinate cooperative state. It doesn't establish that a player earned a score. Clients still propose the payload, and the backend doesn't understand the game's reducer. The [network contract](https://github.com/cubacadabra/rust/blob/main/docs/network-runtime.md) is explicit about that limit. Competitive games will need server-side rule validation. Ordering two claims correctly doesn't make either claim true.

06 / The part that draws the dragon
-----------------------------------

Rendering goes through wgpu: Metal on iOS, configured Vulkan/GLES backends for Android, and WebGPU/WebGL paths for the browser. That shares a lot of renderer code. Surface lifetimes, input, audio playback, and the operating system interrupting you still belong to each host. An Android surface disappearing is a fairly effective reminder that the engine isn't the whole application.

![Sally avatar standing in a bright cubacadabra game world with another player in the distance](assets/sally.jpg)


A shared renderer / live clientThe same character-facing runtime can show up in a browser, on a phone, or inside a desktop tool.

The character renderer uses an indexed mesh catalog and batches instances by mesh and material. It chooses among three LODs using projected height, with nominal boundaries at 180 and 70 pixels. The instance layout is 128 bytes. A fixed 15-joint hierarchy drives the characters. These are concrete constraints you can find in the code and reason about before adding another decorative thing to somebody's head.

![Cubacadabra running on an iPad Air with a player standing in the Signal Run level](assets/ipad.jpg)


iPad / native hostThe renderer is shared; the device still gives the game its own surface, controls, and interruptions.

There are some wonderfully specific solutions in there. The person's hoodie sleeve bends around the elbow in the vertex shader, carrying axis-angle data in spare lanes of the normal rows. Other garments use rigid attachments. Hair has bounded spring motion while its cap stays attached to the head. This is the sort of work hidden inside the apparently simple request to make somebody wave without their clothes coming apart.

The [character budget](https://github.com/cubacadabra/rust/blob/main/docs/character_runtime.md) includes 50 renderer-only characters and 32 MiB of mesh/instance buffers. Those are limits in the implementation, not a claim that every phone sustains a particular frame rate. The network roster has its own smaller bound. I'd want physical-device frame times before turning either number into a performance promise.

07 / The hat has 248 triangles
------------------------------

Which brings us back to the top hat. There's a Blender export in the morph work log with one node named `Cylinder` and 248 triangles. The validator rejected it. A perfectly understandable hat, missing the three distinct LOD nodes required by the sidecar. That's a much more useful early result than a green checkmark meaning only that we managed to open a file.

![Cubacadabra Studio morph inspector showing a top hat GLB with 248 triangles and missing LOD mappings](assets/early.jpg)


Studio / morph previewThe validator can make an incomplete asset legible before it ever reaches a device.

The existing character system has bodies and outfits encoded in Rust enums, and the renderer prepares their combinations. That gets a prototype moving. It becomes awkward when adding a hat means changing engine code, or when independent hairstyles and garments multiply the combinations. I want an artist's second hat to be a content change.

The new `cubacadabra-morphs` crate owns IDs, catalog schemas, loadouts, and compatibility decisions. Its resolver checks supported bases, rig compatibility, common fit profiles, occupied slots, conflicts, and required capabilities such as `mesh.rigid.v1`. It produces deterministic diagnostics. Studio can use it without initializing a GPU. Runtime adoption is still early; the existing appearance and rendering paths haven't all moved over.

The [Studio authoring crate](https://github.com/cubacadabra/studio/tree/main/crates/morph_authoring) handles the source boundary. A GLB export has a readable `.morph.json` sidecar declaring the asset, geometry path, named near/mid/far nodes, triangle counts, and a rigid attachment to a semantic joint such as "head." Attachment transforms get checked, including a normalized quaternion. The declared counts must satisfy `near >= mid >= far > 0`. Copying one node name into all three slots fails validation.

The GLB inspector checks the `glTF` magic, version 2, declared file length, and chunk bounds. It reads JSON nodes, meshes, and accessor counts, then compares derived triangle counts against the sidecar. It understands triangles, strips, and fans for that calculation. The library rejects sources over 64 MiB and sidecars over 256 KiB. Diagnostics identify a code and field path, so an artist has something more useful than "import failed."

You can run `morph_validate` against a sidecar and GLB today. It still stops before decoding vertex buffers or compiling a runtime pack. Studio's Morphs tab has a searchable catalog and inspector; import, reimport, and the complete rendered authoring loop are unfinished. A metadata check doesn't prove the mesh will draw correctly.

The [planned path](https://github.com/cubacadabra/rust/blob/main/docs/morph_plan.md) is Blender export, Studio validation and compilation, then a bounded `.morphpack` consumed by the shared renderer. Import machinery stays in Studio. Phones receive runtime assets. New geometry using an existing capability should be data; a new deformation or material behavior can require engine work. The milestone I'm interested in is adding that second hat without opening a Rust source file.

08 / Leave room for the game
----------------------------

The same idea applies to the games themselves. A source project has `manifest.json`, `src/main.luau`, and assets. The Python tools expand explicit includes and assemble a portable package. Studio can also assemble a raw project in memory and run it without writing generated files back into the source directory.

![Cubacadabra Studio world workspace showing a forest scene with a player and tree asset selected](assets/studio.jpg)


Studio / world workspaceThe authoring surface is where a project becomes a place: a scene, a material, a landmark, and a clue.


![Sally exploring the grassy Stormline Outpost game world beside a campfire and beacon](assets/grass.jpg)


Stormline Outpost / in playOnce the runtime owns the plumbing, the game can spend its energy on weather, resources, and weird little stories.

Native builds execute Luau through mlua with vendored Luau; WASM uses the pure-Rust luaur-rt runtime. They expose the same game API, though two runtime implementations still deserve parity checks. Game HUDs can also live in Luau, with Rust doing safe-area layout, hit testing, and the wgpu overlay. Account screens remain in the native shells.

Read [Signal Run's reducer](https://github.com/cubacadabra/second-game/blob/main/src/relay.luau), or the [Stormline Outpost example](https://github.com/cubacadabra/examples/tree/main/survival-101) with its beacon fuel and radio supplies. Those rules belong to the game. I want someone to change the storm, make the relay ridiculous, or put a hat on the dragon without coordinating three client patches and a backend release.

As cubacadabra grows, I want the complexity to accumulate in shared code we can understand and test together. A new platform should need a shell, not another implementation of everything we've learned about running the product. That's why I'm continuing to move logic into Rust. The old charm removed letters until almost nothing remained. I'd be happy to get down to the Swift, Kotlin, and JavaScript that actually need to be different.
