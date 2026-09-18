---
title: "L8 Principal's Agentic Engineering Workflow"
source: "https://www.youtube.com/watch?v=iQyg-KypKAA&t=1s"
author:
  - "[[Kun Chen]]"
published: 2026-06-20
created: 2026-08-03
description: "Find everything from me here: https://linktr.ee/kunchenguidTools I mentioned:- WezTerm https://wezterm.org/index.html- tmux https://github.com/tmux/tmux/wiki- Neovim https://neovim.io/- npx skil"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=iQyg-KypKAA)

Find everything from me here: https://linktr.ee/kunchenguid  
  
Tools I mentioned:  
\- WezTerm https://wezterm.org/index.html  
\- tmux https://github.com/tmux/tmux/wiki  
\- Neovim https://neovim.io/  
\- npx skills CLI https://github.com/vercel-labs/skills  
\- OpenSuperWhisper https://github.com/starmel/OpenSuperWhisper  
\- AXI https://axi.md/  
\- lavish https://github.com/kunchenguid/lavish-axi  
\- no-mistakes https://github.com/kunchenguid/no-mistakes  
\- gnhf https://github.com/kunchenguid/gnhf  
\- treehouse https://github.com/kunchenguid/treehouse  
\- firstmate https://github.com/kunchenguid/firstmate  
  
\--------  
  
Chapters:  
00:00 How to watch this video  
02:10 Why I work in the terminal  
03:49 WezTerm and my lua config  
05:09 What is tmux  
07:18 Neovim as editor  
09:21 Agent harnesses  
11:24 My global memory file  
14:50 Project level memory file  
16:12 Using skills  
18:40 How skills may hurt your agent  
20:27 Voice input  
22:12 The importance of agent ergonomics  
24:25 Planning with interactive artifacts  
28:29 Validating code changes  
33:12 Long running tasks  
36:20 Parallel worktrees and agents  
40:23 First mate  
44:26 The captain's mindset

## Transcript

### How to watch this video

**0:00** · Hi everyone.

**0:01** · Welcome to this video and this will be a full walkthrough of my agent engineering workflow.

**0:06** · My name is Kun.

**0:07** · I was previously an late principal engineer, worked at meta, Microsoft, and assassin on many large scale systems like the Bing search engine, windows, and Facebook games.

**0:18** · In the recent couple of years, I have been building frontier coding agents at Atlassian and helped many engineering teams figure out how to use them effectively.

**0:27** · and I have been building heavily with agents myself and shipping 40 to 50 almost every day, sometimes more.

**0:34** · And these are all well tested and shipped production.

**0:37** · not those Minecraft demos.

**0:38** · You see people wipe code on social media.

**0:40** · I have shaped my workflow to be both highly productive and enjoyable.

**0:45** · Many people recently asked me what it looks like, be honest, I did debate a lot with myself whether I should make this video a paid course because it does have that level of value, but ultimately I decided to just share it here with everyone because I want to stay focused on building products as my main business.

**1:03** · you can see this is a bit of a long video, because I'm going to walk through many fundamental concepts of agent engineering that's not only show you how I do it, but also the why and how things really work under the hood.

**1:15** · These are not gimmicks that look cool but can't actually be used for real work.

**1:19** · These are all real workflows that professionals like myself use to get real work done.

**1:25** · By the end of this video, I want you to feel like a captain that can sail a large ship with a crew of agents working for you, and do so in a stress free and satisfying way.

**1:36** · Largely speaking, we will be walking through these chapters.

**1:39** · We'll start with assembling our ship, where I will introduce the core setup.

**1:45** · We will then talk through how we recruit and ramp up our crewmates with the right usage of memory and skills.

**1:52** · I will then demonstrate how we work with a single crewmate effectively.

**1:57** · Then we'll upgrade to working with multiple crewmates all at the same time.

**2:01** · And lastly, we will recruit a first mate that manages a lot of the overhead for us so we can stay focused on the big picture.

**2:09** · As a captain, the very first level is to gather our gears and build our ship.

### Why I work in the terminal

**2:14** · Now, as we get into my workflow, something that's going to be really hard to miss is that I do almost everything in my terminal.

**2:22** · I know there are a lot of people who will tell you that the graphical user interface is better.

**2:27** · It allows richer interactions and better visuals, but I think by the end of this video, I might just be able to convince you that terminal is not quite that yet.

**2:37** · I use the terminal mostly for two very real reasons.

**2:41** · One is to allow my hands to almost never have to leave the keyboard.

**2:45** · This is actually a much bigger deal than most people think, because when your hands stay on the keyboard, you stay in the flow.

**2:52** · But if you have to move your hand to the mouse every couple of seconds, it breaks the flow and forces your brain to contact switch.

**3:01** · I know there are some guy apps that also have great key points that allow you to do most things with the keyboard as well, but that's just not the primary interaction paradigm for guy apps, And it's hard to build the discipline of hands on keyboard when every once in a while you still have to use the mouse terminal apps.

**3:19** · On the other hand, are all designed for the keyboard, so there is no reason for your hands to move anywhere else.

**3:25** · The other very important factor that drives me to use the terminal is that I can keep the exact same workflow everywhere, even on my phone.

**3:33** · but if you really don't like the terminal, that's okay too.

**3:37** · I designed this video to be more about the fundamental concepts behind agent engineering rather than the mechanics.

**3:43** · So most of the things that I talk about should be applicable to GUI based workflows as well. Now.

### WezTerm and my lua config

**3:50** · Since we are looking at a terminal here, let me share what it is I'm using this beautiful, clean and elegant terminal emulator you are looking at here is called Western.

**4:01** · Western is a highly performance terminal emulator built by a guy named West.

**4:06** · It's got 26 k GitHub stars and has existed for many years.

**4:10** · I like it mostly for two reasons.

**4:13** · One is that it's truly cross-platform.

**4:15** · It's pretty much the only terminal emulator I can find that can work on windows exactly the same way it works on Mac and Linux.

**4:23** · Right now I mostly only work on Mac, but it was a big lifesaver when I was working for Microsoft and was forced to use windows for work.

**4:32** · The other reason is that it's highly customizable.

**4:34** · You can write Lua scripts to configure pretty much everything. Here.

**4:38** · Let me show you my config in my dot files.

**4:41** · It's all in this file called Western dot lua.

**4:44** · It's a lower script.

**4:45** · So it's not just static values.

**4:47** · You can actually set conditions and write various kind of logic to make your config very dynamic and flexible.

**4:54** · If I change some settings here, let's say I change the color scheme to chalk.

**5:00** · You will see that it does a hot reload instantly, which is super handy.

**5:04** · But I still like my rose pine moon, so let's come back to it.

**5:07** · I can't use anything else.

### What is tmux

**5:09** · Inside of West term, I run something called tmux.

**5:13** · It's short for terminal multiplexer.

**5:16** · If you haven't come across this yet, it's probably easiest to just show you what this does.

**5:20** · so I'm typing this command here to start a session.

**5:24** · Now I'm inside of t max.

**5:26** · You can see not much is different except for that.

**5:29** · There is a bar at the top showing some information, and I still get a shell where I can type commands, But now I can split my terminal into multiple panes, as many of them as I like.

**5:41** · This is super useful because I can spin up an agent in one pain and spin up an editor in another, and still have a pain to myself so I can just run commands.

**5:52** · I can also spin up multiple tabs and they are also called windows in.

**5:57** · This is very useful for running multiple agent sessions in parallel.

**6:01** · The other cool thing is that tmux sessions are persistent in the server.

**6:06** · So if I use a keyboard shortcut here to detach from tmux, you can see I'm back in the normal shell without the status bar at the top.

**6:14** · But if I type the same command to launch tmux again, I get back to the exact same state I was in So I can continue my work here.

**6:24** · What's even more useful is that I can connect to this same session from another device, like my laptop or my phone.

**6:30** · that's a real game changer.

**6:32** · That's very hard to replicate without this terminal centric workflow.

**6:36** · If you just install tmux by default, it doesn't have the same experience while showing here, like the tab bar and the metadata.

**6:44** · You will probably need to do a bit of configuration and customize it.

**6:48** · Let me show you my team config.

**6:52** · Here it is.

**6:53** · Most of these settings are key points that I have been using for many years, and built into my muscle memory.

**7:00** · Some of these are for styling and various kind of behaviors.

**7:03** · There are many YouTube videos that go into more details about tmux configuration.

**7:08** · So I'm not going to go down the rabbit hole here. For now.

**7:11** · You just need to know that you are likely want to spend some time configuring your t mux for it.

**7:17** · Look good and work well for This text editor here is Nuvem.

### Neovim as editor

**7:21** · It's basically the modern version of vim.

**7:23** · It's my favorite text editor.

**7:25** · If you are not familiar with vim yet, it's an editor whose main purpose is to keep your hands on the keyboard.

**7:31** · So if you watch my keystrokes here, I can move the cursor up and down, left and right with keys.

**7:38** · I can also scroll up or scroll down.

**7:42** · If I have to make edits, I can go into insert mode and start to type anything I like.

**7:48** · There are a ton of keyboard shortcuts for doing everything you need.

**7:51** · For example, let's say I want to delete the current line.

**7:54** · I can just type dd and it's gone.

**7:56** · I can undo it by typing you.

**7:59** · And if you look at the left hand side I have relative line numbers.

**8:03** · This line number 238 is the current line number.

**8:07** · And the line above shows one, which means it's one line above the current line and the lines below as well.

**8:14** · So let's say I want to jump to the line that says set environment.

**8:19** · That's 11 lines above the current line.

**8:21** · So I can just type 11 k.

**8:23** · And I'm here.

**8:24** · So once you have enough muscle memory, you can just navigate around much more quickly than using a mouse.

**8:31** · I also have a bunch of plugins that help me get around in as well.

**8:35** · And I have key points for all of them.

**8:38** · Like space S allows me to search or grep for the code base, so I can just type rows and it will find all the occurrences of rows in the current code base.

**8:48** · I can type space F to find files by their names, like if I type flake I'll get to the flake file immediately.

**8:56** · Working with them has a learning curve for sure.

**8:59** · But once you get used to it, it just feels really, really good.

**9:03** · Whenever I'm in, I'm just flying like a bird and it's awesome okay?

**9:07** · I have to stop here before this turns into a vim tutorial.

**9:10** · You can find a lot of great YouTube videos that will help you get started on them and become a master.

**9:16** · Maybe one last tip for me is just how to exit.

**9:20** · Here you go.

### Agent harnesses

**9:21** · All right.

**9:22** · Our ship is ready to sail, but we have no crewmates yet.

**9:25** · Where? The captain.

**9:27** · We can't do everything by ourselves.

**9:28** · We need to bring in agents as our crewmates.

**9:31** · I use four different agent harnesses regularly.

**9:34** · There is cloud, which is cloud code, which is basically the only practical choice if you are using the subscription from anthropic.

**9:42** · Generally speaking, though, it's a pretty good harness.

**9:45** · I think it has the most sensible default experience out of the box.

**9:49** · It's also got a pretty rich feature set.

**9:51** · The downside is that sometimes it's a little bit buggy, and it's not as customizable as some of the other options.

**9:58** · The next one I use a lot is Codex COI.

**10:02** · It's written in rust, and you can feel it's a little bit smoother than cloud code when you use it.

**10:07** · It's also open source, so if you run into some problems, You can often just have Codex inspect its own source code and figure out a workaround by itself.

**10:17** · It's a bit lacking in terms of bells and whistles, and it's also not very customizable.

**10:22** · And then there is the Pi coding agent.

**10:25** · And this whole philosophy is to be minimal and highly extensible.

**10:29** · It's great if you don't want any bloat and you'd like to tinker around and kind of make it your own.

**10:35** · and lastly, there is open code.

**10:38** · I like it a lot.

**10:40** · It's got a battery smooth t UI, And it's got good integration with pretty much every model you can find.

**10:46** · It's also got a more complete out of the box feature set than Pi.

**10:50** · So if you want to use an agent harness that is model agnostic and one that you can just grab from the shelf and just go.

**10:57** · Open code is a pretty good choice.

**10:59** · For the rest of this video though.

**11:01** · I'm going to use cloud code because I know many people are already familiar with it, but I have been very strict about making my workflow agent agnostic because the landscape is changing very, very fast.

**11:12** · who knows which model or agents will be the best performing one next month?

**11:16** · Right.

**11:16** · So everything I show here in the video is agent agnostic and should be applicable regardless of which model or harness you use.

### My global memory file

**11:25** · The problem with this crewmates is that they are fresh recruits, and they have no idea how we run our ship or how we like to work.

**11:32** · We need a proper onboarding process to ramp them up.

**11:35** · We will do this mostly through two ways memory files and skills.

**11:40** · There are few types of memory files, global memory files, and project level memory files.

**11:45** · The global memory file for cloud code is at this location, and every other agent uses the other standard location here.

**11:56** · So what I do is that I use this command Which made MD a symbolic link to MD.

**12:04** · So they both exist, but under the hood they point to the same file.

**12:08** · Here's the content of my actual global memory file. You can see it's pretty minimal.

**12:14** · There is only 27 lines.

**12:16** · Because everything in this file gets loaded into the system prompt of every single agent session across all our projects.

**12:23** · If we have too much content in this file, it will silently use a lot of our tokens.

**12:29** · I mostly write down my personal preferences here, like never use em.

**12:34** · Somehow AI models are trained to use em by default instead of a plain dash.

**12:39** · So now whenever I see em, I just feel like it's robotic.

**12:43** · And I don't like that when I need the agent to write something for me.

**12:46** · Like PR descriptions.

**12:48** · Oh, and this is a good one.

**12:49** · When making technical decisions, don't give too much weight to development cost.

**12:54** · Here is something interesting that you may not know. Let me show you.

**12:58** · If we ask a frontier model to estimate the development cost of a project, let's say I want to build a 3D first person shooting game that I can play locally with AI enemies.

**13:12** · How long do you think that will take?

**13:16** · Let's see what cloud will say.

**13:18** · Okay, here it is.

**13:19** · See, the estimate is in days and weeks and months.

**13:23** · But if we ask the agents to actually build it now, I can guarantee it will come back with a playable version in just a few minutes.

**13:31** · Because I have done this so many times.

**13:33** · This mismatch is happening because the models were trained from human data, and that is what a typical human developer would give as the estimate.

**13:43** · AI doesn't seem to know it can code much faster than humans yet.

**13:47** · When AI is making technical decisions, it's implicitly assuming the development cost for some of the options are much higher than they actually are.

**13:56** · This biases the model to choose cheap solutions that are often low quality, not scalable, or hard to maintain.

**14:04** · So I have this rule here to correct that bias.

**14:09** · I also said when doing bug fixes always starts with reproducing the bug in an end to end setting as closely aligned with how an end user would experience it as possible.

**14:21** · AI models today by default like to write unit tests, which are often not sufficient and not really covering the product behaviors we want to guard.

**14:30** · I found that leaning into end to end testing is a lot more reliable.

**14:34** · Besides these preferences, I also have some interesting stuff opinions, which is super useful.

**14:41** · That's a slightly different topic though, so I won't go into too much detail here, but I do have a blog post explaining how that works, which I'll link here in case you're interested.

**14:49** · Besides the global memory file, each project can also have a project level memory file.

### Project level memory file

**14:54** · Let me show you one example here by going into this project called High Bit.

**14:59** · This is an AI Twitter app I have been working on.

**15:01** · The project level memory file is typically stored as cloud or agents, depending on which agent you use.

**15:09** · I do the same thing here with a symbolic link.

**15:11** · So the same file is shared for both cloud and other agents.

**15:15** · This one we are looking at here is a little bit verbose.

**15:18** · I would say I will probably clean this up after this, but let me show you on a high level what I put into this file.

**15:24** · It has some context on what this project is, how the repo is laid out, some terminology, how some of the most important components work, and how to do end to end testing, and some conventions at the bottom.

**15:40** · This file is a lot more verbose than the global memory file, because this is basically the collective learning of all the agent sessions in this project.

**15:49** · The way I built this file is not by writing everything by hand, but rather that every time I saw the agent doing something wrong, I would correct it and ask it to remember to not make the same mistake again by storing the learning into this memory file.

**16:03** · So over time, our crewmates working on this project get smarter and more experienced.

**16:08** · You don't need any fancy memory system to do that.

**16:10** · This markdown file is all it takes over time.

### Using skills

**16:13** · It does tend to get more and more bloated though.

**16:16** · One way I reduce the size of this file is by moving some conditional information that is not always needed into a skill.

**16:24** · For example, the end to end testing instruction here is only needed if the agent is making changes, right?

**16:31** · So if I just ask the agent a question, this whole section is totally useless and would be wasting tokens.

**16:38** · The way to improve efficiency here is by converting this kind of conditionally useful information from the memory file into skills.

**16:47** · I typically just ask the agent to do this.

**16:49** · Here, let me do it alive.

**16:52** · I will say let's extract the end to end testing instructions junctions in our agents and file into a project level skill.

**17:07** · Cloud already knew how to do this, what skills mean and how to create them, but other agent harnesses may not understand how to do that out of the box.

**17:17** · To teach your agent how to create skills, you can install a skill called Skill Creator which which was written by anthropic.

**17:26** · You can do that by running this command.

**17:28** · This NPC's skills thing is a call from Vercel that is very handy.

**17:34** · It's basically my main tool for installing and managing skills.

**17:38** · It supports pretty much any agent.

**17:41** · Once this skill is installed, your agent will be able to follow the rules and create new skills for you moving forward.

**17:48** · cloud has done its work.

**17:49** · Let's look at what cloud created for us.

**17:53** · It basically removed a large chunk of the content from our agents MD file and move that into this this skill file.

**18:05** · This is a good thing about skills is that it's designed for progressive disclosure, which means when your agent starts, it only loads this tiny description field from your skills into the system prompt to know what these skills do, and only when it actually decides that it needs to use a certain skill.

**18:23** · It will then reads the rest of this file.

**18:25** · This allows you to store a lot of the knowledge about how to do various kinds of things without blowing up your system.

**18:32** · Prompt and memory file with a ton of contents that uses your tokens for every single request, whether the request actually needs those skills or not.

### How skills may hurt your agent

**18:40** · One thing I do want you to know about skills is that you should generally avoid installing random skills from the internet.

**18:47** · Even the ones that have a lot of GitHub stars.

**18:50** · First of all, these skills can instruct your agents to run pretty much anything on your machine.

**18:56** · This is a very risky thing to do, because the agent can lick your API keys or even credentials to your bank account to untrusted third parties without you knowing.

**19:06** · even if we put aside the security problem, some of the skills actually degrade your agents performance.

**19:12** · Look at this repo here called Android Skills, which has 177,000 GitHub stars.

**19:20** · That's like massive.

**19:21** · So it must be really good, right?

**19:23** · I actually evaluated a skill in this repo with Program Bench, which tests the agent's ability to build programs end to end.

**19:32** · And the result shows that by using this skill, the agent will use 5% more tokens while making the results worse.

**19:40** · And if you look closely, this skill is not even written by André Karpathy himself.

**19:47** · I'm not here to criticize the author of this repo, though.

**19:50** · I'm mainly saying that being popular is not the same as actually being good.

**19:55** · A lot of the skills being widely shared today have not been rigorously evaluated, and are typically just some random guy who found something that worked for themselves and and somehow got it to go viral.

**20:08** · Their GitHub stars only tell you how popular they are and not whether they are actually helpful.

**20:14** · So as a general rule of thumb, I recommend that you do not install any skill from the internet that claims to magically make your agent perform better, but hasn't published anything rigorous that proves its claim.

### Voice input

**20:27** · All right.

**20:28** · Now that we have memory files and skills to help ramp up crewmates, it's finally time to actually start working with the crewmates and set sail.

**20:36** · The first thing about working with the crewmate is how you talk to them.

**20:40** · I have pretty much completely moved to voice input now, So.

**20:44** · Instead of typing, I will just say, explain this repo in a concise way and give me a recap of what the recent press have been working on.

**20:53** · This is just so easy.

**20:54** · There is an actual paper from Stanford that seriously compared the efficiency.

**20:59** · And basically talking is three times faster than typing.

**21:04** · So this is a very big boost in productivity.

**21:07** · I also want to show you something interesting here.

**21:09** · If we go to the references of this paper look who's here.

**21:15** · It's our guy Dario.

**21:17** · What is the CEO of anthropic doing here?

**21:20** · Apparently if we follow this link Dario was doing some speech recognition stuff back in 2016.

**21:28** · Now we're using speech recognition technology to talk to cloud which is also created by Dario.

**21:33** · What a small world.

**21:35** · The voice input.

**21:36** · We just did was actually transcribed locally using this app called Open Super Whisper.

**21:43** · It's completely free and open source, which is what I think this type of software should be.

**21:47** · It runs the whisper model locally on your machine and do the transcription.

**21:51** · And the quality is like really, really good.

**21:54** · So this is how I do most of my prompts.

**21:56** · Now, the only case where I fall back to typing is when I need to give the agent a URL or a file path, or something like that.

**22:05** · Trust me, you don't want to speak a URL out loud, whether it's by yourself or with other humans around.

### The importance of agent ergonomics

**22:13** · If we come back to this prompt and let the agent run, you will see that because we asked the agent to look at recent polls, it will need to call GitHub to fetch the data.

**22:24** · This is an important thing to pay attention to, because agents rely on external tools like GitHub to do its tasks.

**22:31** · The design of these external tools can greatly affect your agents performance.

**22:35** · Take GitHub as an example.

**22:37** · Many people use the GitHub MCP server for accessing GitHub.

**22:41** · However, I ran this benchmark here that measured various kinds of ways to access GitHub For the exact same tasks using GitHub, MCP server will cost you to spend three times more on token cost, and more than double the latency compared to using the CLI.

**23:00** · If you are using the GitHub MCP, you are pretty much wasting both time and money for no clear benefits.

**23:06** · Now you can see there's this thing called axi, which has the lowest cost but highest success rate.

**23:12** · So what is it? Let me show you.

**23:16** · Axi is a set of design standards I authored after discovering the huge upside we can have by designing our tools to treat agents as a first class citizen and optimize for agent ergonomics.

**23:30** · I created ten principles for how to make a tool highly efficient for agents.

**23:35** · For example, using token efficient output format can save about 40% tokens compared to using JSON.

**23:42** · And then I built a few axes with Besides the GitHub axis I showed earlier, I also built Chrome dev tools actually, and benchmarked it against other various browser tools.

**23:54** · And Here you can see the agents taking less turns and using less tokens to get the same tasks done with the ax.

**24:02** · The main point here is when you give tools to your agents, do some research on their efficiency because they can greatly affect how much mileage you get out of your agents.

**24:12** · If you want to use the axes I mentioned earlier, you can just go to this site called axis and find them in this catalog.

**24:20** · You can just go to the repo and find instructions for how to start using them.

### Planning with interactive artifacts

**24:25** · Speaking of this catalog, there is something called lavish axi here.

**24:30** · This is a very important tool in my setup.

**24:33** · I pretty much rely on this tool for planning any kind of complex work.

**24:37** · Let's do a real feature live and I'll show you how it works.

**24:40** · Let me first launch high bit to show you what I'm trying to work on here.

**24:45** · Hybrid is an AI Twitter I'm building for kids.

**24:48** · I'll just create a test profile here.

**24:53** · You can see here at the top I have these two buttons, what I can do and my progress.

**24:59** · They are showing very similar content right now which is a problem.

**25:03** · So and also the UI is not very exciting or fun.

**25:08** · So let me go back and talk to cloud.

**25:14** · I'll still use voice input here.

**25:16** · I'll just say I'd like to consolidate the what I can do and my progress buttons, because their functionality is very similar and I'd like to revamp the experience there to be something more fun and exciting, like in an achievement system.

**25:33** · Come up with some options and let's discuss.

**25:36** · Don't use lavish.

**25:39** · Okay, the reason I said don't use lavish is that I wanted to show you what's the default workflow today.

**25:45** · Looks like for many people.

**25:47** · And then I'm going to show you the difference lavish makes.

**25:50** · Because I already have leverage skills installed.

**25:53** · My cloud will automatically use lavish for this type of question, which is why I had to tell it not to do that right now.

**26:00** · Okay, cloud is doing this work.

**26:02** · Now. Cloud has come back with a response.

**26:05** · Sometimes it will use its plan mode, or sometimes I will ask you to write down the plan in the markdown file, but it's more or less the same.

**26:13** · It's a wall of text I now have to read through.

**26:15** · It's not very easy to understand what what each option is actually going to look like, and if I'm not happy with some parts of it, I can't very easily tell cloud which parts I'm talking about.

**26:28** · I can select a piece of text in the plan and say, this is wrong.

**26:32** · Now let's try the exact same prompt with lavish.

**26:35** · Here it goes again.

**26:36** · I actually don't have to say use lavish because the agent already has the lavish skill that tells the agent for this type of planning it should establish, for demo purpose, I just wanted to be explicit.

**26:48** · Cloud would roughly do the same things to figure out the options, except at the end it would not print out that wall of text.

**26:56** · Again, it will launch the browser and show me this page. Now look at this.

**27:01** · This is the lavish editor.

**27:03** · The reason I named it lavish is that it's richer than a rich editor.

**27:07** · I almost named it filthy rich editor, but that's just not the best sounding name.

**27:12** · Lavish editor basically instructed the agent to create an HTML artifact to visualize what we need to discuss.

**27:19** · It always uses the same design system as the current project being worked on, so this is consistent with how the app actually looks.

**27:28** · This makes it very easy to reveal concepts and prototypes.

**27:32** · See the option is laid out here.

**27:33** · This is so much easier to understand than the huge wall of text we were looking at in the terminal, right?

**27:40** · I can also annotate and make comments on specific parts of the artifacts to give feedback to the agent.

**27:47** · This is something that's really hard to do with the wall of text, or a markdown file And at the bottom, there are things for me to decide on, and I can just click on these options to make the decisions.

**28:00** · I just sent this feedback back to the agents inside of lavish without even having to go back to the terminal.

**28:06** · Honestly, I can never go back to reading text in the terminal anymore.

**28:10** · This is just way too much more efficient.

**28:12** · Now the agent has made updates to the and I feel happy about this, so I'll just tell the agent to start building.

**28:19** · Start building and we'll end the session.

**28:23** · We can then go back to the terminal now and see.

**28:27** · The agent will start to work on the implementation, because we already clarified all the requirements in the planning phase.

### Validating code changes

**28:33** · I typically don't need to interfere at all during this implementation phase.

**28:37** · I only come back to this when the agent has done.

**28:39** · And when the agent says it's done, that's actually when things get really tricky.

**28:45** · This is where a lot of people will spin up their editor and start reviewing the diff.

**28:51** · The problem is, AI writes code so fast, and if every piece of code requires your review, then you are creating a big bottleneck on yourself because you can only review so many every day.

**29:03** · Your velocity will be hard capped by it.

**29:06** · And even more importantly, reviewing diff is just not fun.

**29:11** · No one says I became an engineer because I love reviewing diffs all day.

**29:15** · My advice here is that in order to really scale ourselves with AI, we have to think of ourselves more as an engineering manager or engineering director.

**29:26** · Your directors most likely don't review any place yet.

**29:30** · They can influence the quality of their team's software by creating good culture and processes, and rely on the team to carry them out.

**29:38** · That's what we should do with AI.

**29:40** · What I do here, when the agent says the work is done, is not to start reviewing the dips or start manually testing the changes.

**29:48** · That's too much overhead.

**29:49** · On myself, I sense the change into a pipeline I built called No Mistakes.

**29:57** · No mistakes is also free and open source.

**30:00** · It orchestrates your agent to execute a series of steps that takes this first pass code all the way through to a clean PR.

**30:07** · It would first create a branch if one doesn't exist yet, and then create a commit and then take it through a pipeline in an isolated work tree, so nothing during the validation would affect your current repo.

**30:19** · It would first understand your real intent behind the change by analyzing your agent session, then rebase the change on top of the latest main branch on remote origin and resolve merge conflicts up front, then starts an adversarial review in its own fresh context window.

**30:36** · This is where most problems get caught, and obvious problems will get self corrected, but ambiguous ones that have product implications will be escalated to us humans for a decision after review.

**30:49** · It also tries to test the change end to end against the original intent, and this step will actually record evidence that proves the change is working that we can.

**30:58** · Then later on look at to gain more confidence.

**31:02** · It will then do a documentation pass of updating all relevant documentation to reflect the latest change.

**31:08** · And also finally, make sure there is no linting problems before pushing the branch to remote and raise a PR.

**31:15** · The no mistakes pipeline will also keep babysitting the PR until it's merged, because during the PR phase, we can still have merge conflicts that come in, or CI pipeline failures that are very annoying as well, with no mistakes doing the babysitting.

**31:30** · We don't have to waste our own time at all.

**31:32** · Another way to trigger no mistakes is as a skill.

**31:36** · I can just type no mistakes in the agent and it will do the same pipeline as This may seem very slow, but in practice I never stare at this screen.

**31:46** · I would go spin up other tasks.

**31:47** · I come back only when no mistake says all checks passed that's when I go to the PR and apply my judgment.

**31:54** · Here's the PR from the change we just did.

**31:57** · We can see here it summarized the original intent.

**32:00** · What's changed, how it's tested, and what happened during the normal stakes pipeline.

**32:06** · We can click to see the evidence from its testing to know whether it's really done what we asked for, depending on what the change is, the evidence could be a screenshot like this a video demo, a log file, or something else.

**32:22** · It's designed to give you the most direct way to see the change working as you intended.

**32:26** · We can also see that the pipeline discovers some problems and fix them before raising the PR.

**32:32** · This is a good time to audit whether these changes are actually what we need.

**32:36** · If anything doesn't look right, we can go back to the agent and ask for more changes before merging this PR.

**32:42** · This risk assessment here is also very useful.

**32:45** · I basically look at this to decide how much time I should spend on reviewing this change in more detail.

**32:51** · For low risk changes, I don't really look at the diff at all Because I have validated time and time again for low risk changes.

**32:58** · Any problem I could catch is very likely already caught by the pipeline only more risky changes are worth my This is how I scale up the volume of code changes I do every day through a large crew of agents, without losing control on quality.

### Long running tasks

**33:12** · One thing we are starting to see now is that the place where I spend time is towards the beginning and the end of the task.

**33:20** · At the beginning I would spend time in lavish to plan the requirements more clearly.

**33:25** · At the end I would come in and hold a bar on quality.

**33:29** · All these parts in the middle is done by AI, which frees me up to spin up other tasks.

**33:35** · This is a core aspect of how I work, and you can see the more time I can free up in the middle, the more work I can go do in parallel.

**33:43** · So an interesting question now is how do we get the agents to work for longer and longer in the middle?

**33:50** · That depends on us giving them more and more complex tasks that take longer to complete.

**33:55** · But more complex tasks are often not as easy for our agents to complete autonomously.

**34:02** · An extreme version of this is when I go to bed, I sleep for 7 to 8 hours every night.

**34:07** · How do I keep the agents busy for eight hours?

**34:10** · This is where I say good night.

**34:13** · Have fun.

**34:13** · It's another free and open source tool I built specifically for long running tasks.

**34:18** · It's becoming quite popular.

**34:20** · It's that simple to use.

**34:22** · Just give it an objective and it will keep going until it meets some stop condition you defined.

**34:27** · Let me show you a real example that I often do.

**34:30** · This is again in the hybrid repo I will run.

**34:33** · Good night.

**34:33** · Have fun and give a prompt.

**34:36** · Pretend you are a seven year old kid and use the high bit app end to end.

**34:41** · Don't mind the profile creation step which is designed for parents in the rest of the app.

**34:46** · Try to do different things and find the first usability problem that will confuse you as a kid, or stop you from knowing how to proceed.

**34:54** · If you find a problem, stop and fix it, then rinse and repeat.

**35:00** · Here he goes.

**35:01** · Good night. Have fun.

**35:02** · Is now running in the loop.

**35:03** · To execute on what I just asked for.

**35:06** · I can monitor token usage here or how many iterations have been done.

**35:10** · The iterations will be showing up as the moons in this row, and I can see how many commits have been made as well.

**35:16** · Or I can just go to bed knowing the agents won't stop until there is no more problem to be found.

**35:21** · When I wake up, I can reveal a list of commits made on this new branch and decide which ones I want.

**35:28** · I typically use goodnight.

**35:29** · Have fun for improving on some verifiable objectives or objectives, where I trust the agent to have the reasonable judgment over, like the one we just did.

**35:39** · Verifiable objectives are more like reducing page load time, improving end to end test coverage or like Android hypothesis auto research.

**35:48** · Keep experimenting different hypotheses to improve on the metric.

**35:52** · These are all well suited for a long running loop.

**35:55** · To tackle the recently introduced slash goal command in Codex and Cloud code can also do something similar, good night.

**36:03** · Have fun still gives me a better experience.

**36:05** · Because I can set a token cap or iteration cap or stop condition more precisely, whereas in Cloud Code and Codex, if I set a goal before I go to bed, I might wake up realizing my weekly quota is all Good night.

### Parallel worktrees and agents

**36:20** · Have fun.

**36:21** · Solved a very important problem, which is to keep the agents running for a long time.

**36:26** · So when the agents are running, I'm freed up to do more things.

**36:30** · This is when we level up and start working with multiple crewmates in parallel.

**36:34** · So let's spin up another tab in teams and get more work started.

**36:39** · Now here's the problem.

**36:40** · In this directory I already have.

**36:42** · Good night.

**36:43** · Have fun running.

**36:44** · So if I spin up another agent working in the same directory, they will step on each other's toes and cause conflicts.

**36:51** · The default solution here is git work tree.

**36:54** · For those of you who aren't familiar with it, a guitar work tree is basically creating a clone of your report directory.

**37:00** · I can create one by typing git work tree add and give a path here.

**37:07** · Now we have to think about a name.

**37:09** · This is when you waste five minutes and eventually give up and just say hi.

**37:13** · Bit two.

**37:15** · Now we have a work tree and we can navigate to it.

**37:18** · So let's go find it.

**37:20** · It's in high bit two.

**37:21** · This is a separate directory on the file system.

**37:24** · So we can have an agent doing anything here.

**37:26** · And it won't conflict with good night to have fun, which is running in the original report directory.

**37:31** · The problem with work trees is that we now have something to maintain in our head.

**37:36** · I need to remember.

**37:38** · Oh, I have hybrid two here.

**37:40** · Next time I come into this hybrid two directory I would wonder what was I doing in this work tree last time?

**37:47** · Is there still an agent running or is it All of that has to exist in my head, and there is no way I'm going to remember all that.

**37:54** · So this work tree basically becomes a debt.

**37:57** · To get rid of it.

**37:58** · I need to run this remove command.

**38:02** · Remove.

**38:05** · This is just a lot of overhead.

**38:07** · My solution to that is another tool I built called Treehouse.

**38:11** · It's very simple.

**38:12** · I just come into this repo and I run Treehouse.

**38:16** · It would drop me into a fresh work tree where I can start doing whatever I want.

**38:21** · I can keep spinning up more and more of this work trees by running Treehouse again.

**38:27** · And if I want, I can see a list of all the work trees by typing Treehouse status.

**38:34** · So I can see which ones are being used versus not.

**38:37** · When I'm done, I can just close this tab and Treehouse knows that I'm done, so it will free up that work tree for future use.

**38:45** · Next time I ask for work tree, it will try to reuse one of the idol work trees instead of creating a brand new So let's start some real work.

**38:54** · I have a bunch of user feedback from my son's last round of playtesting, so let me use this first worksheet we created and launch cloud, and I will say, I remember it's hard for the kid to realize they can press and hold the voice input button to talk.

**39:10** · By default they just click it and then they will see a popover.

**39:13** · Maybe in the popover, we add a label that tells them they can also press and hold and I'll enter.

**39:21** · Then I'll spin up a new tab Treehouse Cloud, and this time I will say the Image attachment dropdown menu should have an action that takes a screenshot of the current app and use that as the attachment.

**39:37** · All right, one more tab.

**39:39** · Treehouse cloud.

**39:44** · Our agent status bar right above the chat input is not always showing bot activity.

**39:49** · Look into what happened there and make sure when any bots are in progress, it always displays something that reflects the latest activity.

**39:59** · Boom!

**40:00** · We now have three sessions running in parallel.

**40:02** · Now I can keep going because none of these sessions will need my attention anytime soon, especially if I tell them to run.

**40:09** · No mistakes after implementation.

**40:11** · I know whether they need me by looking at the top status bar, and I can switch between the tabs using keyboard shortcuts like this.

**40:19** · That's very important for managing a lot of parallel sessions efficiently.

### First mate

**40:23** · That said, after doing this for a while, you will discover that juggling between all these sessions, it's quite exhausting.

**40:31** · The constant context switch and having to remind yourself what each session was even doing just doesn't feel like an ideal end game experience.

**40:39** · So I kept pushing the boundary on this and I discovered that I needed a first mate, someone I can talk to as a captain that will carry out all my directions and manage all the crewmates for me so I can focus on the big picture like where should we go next?

**40:56** · not playing whack a mole with this increasingly high number of crewmates, this is how I level up and truly become a captain.

**41:04** · My First mate is another free and open source project and it's very new.

**41:08** · The way to use it is by just cloning it.

**41:14** · And then I can run an agent in this repository.

**41:19** · Now I just talk to it and ask it to work on any projects I like.

**41:24** · Let's say I'd like to work on lavish access, GitHub, Axi and Chrome dev tools.

**41:29** · Actually They are all GitHub projects I own.

**41:32** · first mate is starting up and the first time we run it it will do some setup and ask for some preferences, but it's also just talking to it, which is pretty easy.

**41:41** · you might wonder why is the transcription so good?

**41:44** · Because it's recognizing this project names.

**41:47** · Let me show you.

**41:49** · Open Silver Whisper actually supports this customization through a system prompt.

**41:56** · So what we can do here is in this model menu in the transcription menu there is an initial prompt.

**42:03** · And we can put in some common vocabulary that we use into this system prompt.

**42:08** · this prompt is what makes the transcription really good.

**42:10** · First mate here is asking how strict I want to be with the code changes in this repos, and I want to select full gates to PR.

**42:19** · This is basically going to be using no mistakes as the pipeline to validate its change and first task.

**42:26** · Yeah, I'll describe it. Right now.

**42:29** · A real thing I want to do is for all three projects, I'd like to add an update command on the CLI that will update their version to the latest on npm.

**42:41** · And let's see what First Mate does.

**42:43** · It realizes that this is not one task, but three parallel tasks, and it's now spinning up these tabs in timox, just like we be the scenes.

**42:53** · It would also call tree House to create work trees, and then run an agent in that work tree to get the work done, and then it will run.

**43:00** · No mistakes to validate the change and get the PR ready for us to review.

**43:04** · Now you can see it's first made that it's doing the juggling.

**43:08** · I don't need to worry about any of this now.

**43:10** · I can just keep giving it more work.

**43:13** · Hey first mate, let's also look at the most recent three open issues in lavish axillary and let's discuss which ones are actionable.

**43:23** · Boom!

**43:24** · First mate now is pulling the open issues from the repo while waiting for the three background agents working in parallel.

**43:31** · All right, first mate said number 87 is cleanest.

**43:35** · It's very actionable.

**43:36** · And let me just see.

**43:38** · What is this?

**43:39** · Don't toggle in annotation mode.

**43:42** · Okay.

**43:44** · That's the clear bug.

**43:46** · All right, first mate, let's address number 87.

**43:52** · Look, now first mate is struggling a lot of tasks for me that I otherwise would have to manage by myself.

**43:59** · Watching it context switch is actually an oddly satisfying experience, because I know that's what I would have to do otherwise.

**44:06** · First mate is basically all my tools coming together as one cohesive workflow, and I have been really happy with it.

**44:13** · It's been a pretty significant improvement to my overall experience working with agents.

**44:18** · I highly recommend trying it out if you are still directly talking to every single agent session one by one, it will be a pretty massive upgrade.

### The captain's mindset

**44:26** · Something you start to notice after having a first mate.

**44:28** · Is that because first mate took care of so many things for you, you start to run out of ideas for what to ask you to do.

**44:36** · This is a good thing because it indicates the bottleneck is shifting, but it also means you, as the captain, needs to keep up.

**44:44** · This requires a mindset shift of focusing more of your energy on understanding what matters by talking to your users, understanding the competitive landscape, and crafting a good treasure map that can lead your crew to a good direction.

**45:00** · Once you started doing that, congratulations!

**45:03** · You have successfully transitioned from a sailor into a great captain.

**45:07** · All right.

**45:08** · We have gone from not having a ship to being a captain that has a first mate and a big crew that sailed together.

**45:15** · This is a pretty good time to wrap up this video.

**45:18** · All my tools can be found on my GitHub and will be linked in the description below.

**45:23** · They are all free and open source.

**45:25** · I built them because I just want to see more people learning how to do a genetic engineering effectively and doing it in an enjoyable way, and that's what I hope you can get out of this video.

**45:36** · I will continue to share more of my workflow and things I find useful on my channel, so don't forget to subscribe if you don't want to miss anything.

**45:43** · Thank you for watching and see you next time!