---
id: 109
url: https://aelerinya.substack.com/p/the-10-principles-of-slack-maximalism
title: The 10 Principles of Slack Maximalism - by Lucie Philippon
domain: aelerinya.substack.com
source_date: '2025-12-07'
tags:
- cli-tool
- tutorial
- devops
summary: This article outlines "Slack Maximalism," a operational management approach
  that uses Slack as the central hub for all communication, task management, and workflow
  coordination. The methodology is particularly effective for live, reactive operations
  like event management or customer service, and includes 10 principles such as creating
  atomic channels with single purposes, using channels as work queues, automating
  incoming work, and replacing direct messages with channels to maintain team visibility.
  The author presents Inkhaven, a residential program, as a case study demonstrating
  how these principles streamline coordination across residents, staff, and external
  partners.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# The 10 Principles of Slack Maximalism - by Lucie Philippon

The 10 Principles of Slack Maximalism
=====================================

### As applied at Inkhaven

[![Lucie Philippon's avatar](https://substackcdn.com/image/fetch/$s_!GcHB!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fda01904b-e911-47dc-823b-033e36112b96_1280x1280.png)](https://substack.com/@aelerinya)

[Lucie Philippon](https://substack.com/@aelerinya)

Nov 07, 2025

9

2

1

Share

*EDIT: Think of this as an anthropological study of one idiosyncratic way in which a small and intense organization handles operations. An extreme data point in the space of possible communication practices.*

Recently, I’ve been introduced to a new way to manage an organization’s operations: Slack Maximalism.

Coming from a background of using Notion or Google Doc for everything, I now believe that Slack Maximalism is **the best way I know to run live operations** (i.e. work that is acting on the world in real time and is primarily reactive, like events, or customer service). As the name implies, it involves using Slack a lot.

In this post, I’ll describe the principles of Slack Maximalism I’ve discovered, and for each one, show examples of how they’re used to run [Inkhaven](https://www.inkhaven.blog/).

Principle 1: The Atomic Channel
-------------------------------

Each channel should have one purpose. It should always be obvious which channel is the right channel for a specific message. Each topic which is regularly discussed should have a channel. Channels should be created liberally as soon as they are needed.

Each message which does not find its channel is a message at risk of never being sent. Creating new channels signals that a type of message is welcome, and allows pent-up information to finally be shared.

**Examples from Inkhaven:**

* `#inkhaven-activities`: for announcing, gauging interest, discussing and cancelling program activities
* `#inkhaven-chatter`: general fallback for communication between residents, the fast pace of one-off coordination and requests. Messages get lost or ignored, but creativity flourishes
* `#inkhaven-walks`: For coordinating going on walks around the campus. Created on day three when multiple people realized they wanted to go on walks with other residents, and could not find each other in the rapid stream of chatter; or just did not imagine that others were interested.

Principle 2: To Each their Channel
----------------------------------

Each person using the Slack workspace should have their own channel, where all the people who have a stake in their work/participation going well should be added. This channel is the ultimate fallback for anything this person has to say.

**Examples from Inkhaven:**

* Each resident has their own channel, in which they talk to their coach, ask questions of the team, request improvements to their room or writing setup or just generally throw anything they want someone to look at.
* Each member of the staff has their own channel, in which they give updates on their work status, ask questions of other teammates, notify of their unavailability, share their uncertainties and thoughts on the program.

Also, each natural group of people should have a Slack channel, for discussions related to this group.

**Examples from Inkhaven:**

* A channel for the whole Inkhaven team
* A channel for each coach and their coachees
* A channel for all the contributing writers

Principle 3: Use Channels as Work Queues
----------------------------------------

Message channels act naturally as a queue. When you open a channel, you start at the last message you read, and read new messages in their chronological order.

Most operation work is processed as part of a queue, be they bug reports to resolve, client requests to complete or automated alerts to check. By making each message in a channel one work item, you can use a Slack channel as a work queue. You don’t need a to-do list or kanban (though Slack includes those too).

In this setup, each top level message is an individual work item, and discussion happens in threads on each item.

**Examples from Inkhaven:**

* The residents requests channel, where residents’ logistical requests are logged, discussed and tracked.

Principle 4: Pipe Incoming Work to Slack
----------------------------------------

Many types of work will originate from systems outside Slack. Set up automations to pipe the new work items to a Slack channel, so you keep Slack as the only place to check for new work. Make sure that those messages include all the information necessary to start acting on them (e.g. request type, urgency, link to further information).

**Examples from Inkhaven:**

* When residents use the form to request feedback from a contributing writer, the writer receives a message in Slack to notify them of the request. They don’t have to check another app or website for new requests.

Principle 5: Use Explicit Statuses for Long Work Items
------------------------------------------------------

Sometimes, a message cannot be acted upon right at the moment when the reader sees it. In those cases, set explicit statuses on items by assigning reactions to them. (e.g. At EAG conferences, we use ✅ for done, 👀 for “I’ve seen it”, 🏃 for owning the item’s resolution)

By using an explicit status system, the risk of dropping an item is reduced, and work can be processed at a different time than the moment the message is read.

**Examples from Inkhaven:**

* In the residents requests channel, we mark completed requests with ✅ and regularly go over the history of the channel to check if we missed any.

Principle 6: Use Channels and Automations to Build Workflows
------------------------------------------------------------

Once incoming work is piped directly to channels, which are set up as work queues, you can start building complex workflows out of multiple channels. Automations will save you time when moving work through the workflow steps.

A simple example is the residents requests. They usually originate in the resident’s individual channel. There, I discuss with the resident what exactly they need, and once this is clear, I forward the message to the requests channel, a consolidated work queue for all requests.

A more complex example is the Inkhaven Newsletter: Inkhaven residents are expected to publish a blog post each day. Once those are published, coaches review each post and curate one interesting post each day, which are transmitted to Vaniver for final curation and inclusion in the Inkhaven Spotlight newsletter.

This workflow is set up as follows:

1. Each day at 6pm and 10:30pm, residents receive an automatic reminder to publish and submit their work using our Daily Publication Form. The message is an incoming actionable work item (see principle 4).
2. On form submission, an automation is triggered, which sends a message to the spotlight channel of the resident’s coach (principle 4).
3. Coaches go through the posts, write their thoughts about it in thread, mark them as read by reacting with ✅, and select one for curation by reacting with 👑 (principle 3 and 5).
4. Vaniver, our newsletter author, goes through the coaches’ channels, picks the posts marked with 👑, does his final selection, and includes them in the newsletter.

Principle 7: Replace DMs with Channels
--------------------------------------

A message in a channel is nearly always better than a direct message, as they allow the rest of the team to know about the discussion, provide any context they have, and possibly even resolve it directly.

If a direct message is about a topic where a channel exists, use the channel. If not, create the channel, or ping the person in your personal channel.

(Maybe I should call it Slack *Channel* Maximalism?)

Principle 8: Onboard Your External Stakeholders to Slack
--------------------------------------------------------

As any organization, you need to interact with people outside your organization. When those communications happen outside of Slack, it leads to work items being dropped, lack of visibility for the rest of the team, and cognitive load from having to track multiple platforms.

Thankfully, most organizations use Slack, so you can use Slack Connect to create shared channels between the two organizations, and have all your discussions there.

If an external stakeholder is not part of another Slack workspace, invite them as a single or multi-channel guest to your Slack.

**Examples from Inkhaven:**

* A Slack channel to coordinate between the Inkhaven Team and the Lighthaven team
* A Slack channel with Leah, our barista from Gratified
* A Slack channel with our chef, to share headcounts, status updates, and feedback on the meals

Principle 9: Use LLMs to Index Information
------------------------------------------

Slack channels are only a temporary storage of information. As nobody looks at pins, you need another way to store important information for future browsing. Thankfully, LLMs can now automate the process of looking at your unstructured message data and transforming it into structured and searchable data.

**Example: The Inkhaven Calendar**

The activities channel is great at putting a low bar to creating new events, but it’s terrible to find which events are happening today, or in which building is the Gwern office hours. To fix this, I use [Claude Code with Slack MCP](https://aelerinya.substack.com/p/how-i-used-claude-code-for-ops-today?r=1piuxp) to keep up to date a Google Calendar with all the events dates, details and locations, and create a daily announcement of the events happening today.

Principle 10: Embrace the Flood of Channels
-------------------------------------------

You followed the 9 Principles of Slack Maximalism dutifully. Now, your Slack workspace has 150 channels, and you feel lost and overwhelmed. Was it a good idea after all? Yes it was. Channel profusion can be managed.

* **Categorize Channels.** Before Slack Maximalism you had one channel for your team. Now you have one for your team, one for each member, and one for each project. Store them all in a [Section](https://slack.com/help/articles/360043207674-Organize-your-sidebar-with-custom-sections).
* **Only show unread channels:** Change the section setting to only show channels with unread messages. Most channels won’t be used every day and that’s fine, don’t display them.
* **Navigate with Ctrl+K:** Once your channels are hidden, you can’t just go to the sidebar and click on them to send a message. But since you followed principle 1 and have one channel for each natural unit of work (topic, person, team), you can just press Ctrl+K, start typing the name of the team/person/topic, and get to the appropriate channel.
* **Mute Channels:** If you’re in a channel just for transparency, as per principle 7, but you’re overwhelmed by the number of messages, just mute the channel. If someone needs you to look at something there, they will ping you.

Conclusion
----------

Slack Maximalism is not for everyone. If you’re working on the [Maker’s Schedule](https://paulgraham.com/makersschedule.html), you should probably keep using Notion. But if you’re doing high intensity operations, consider moving everything to Slack.

*For more inspiration on Slack Maximalism, read the [Adventures of the Lightcone Team](https://www.lightconeinfrastructure.com/adventures-of-lightcone.html). (It’s Awesome)*

9

2

1

Share
