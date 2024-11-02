---
layout: post
title:  "Generating release notes from git commit messages using basic shell commands (git/grep)"
author: laith
date: "2022-01-01"
categories: [blabbing , cheatsheet ]
tags: [ git, guide ]
---

# Not Mine, I copied it from somewhere and I would like to find wherer it was to link to it, Its super useful #

We’re going to use simple commands instead of using one of the many tools available… And keep in mind that there are many options available even when using git commands, the ones listed here are just some of the options you have…

1. Assumptions
Let’s assume you have agreed in your project to prefix git commit messages with one or more of certain prefixes (not necessarily for all changes/commits):

Annotation	Description	Example git commit
```
[INTERNAL]	used for internal stuff	git commit -m “[INTERNAL] my internal change”
[FIX]	contains a bugfix	git commit -m “[FIX] my fix change”
[FEATURE]	contains a new feature	git commit -m “[FEATURE] my new feature”
[DOC]	contains documentation	git commit -m “[DOC] my documentation change”
``` 

Based on the annotations above, it’s quite easy to generate a simple list that contains for example all features, or all features and bug fixes etc. In more advanced scenarios you could also generate files of a certain format, i.e. you could generate json files containing the features – maybe to display these features inside the help menu of your web application 😉 For simplicity we’ll just create a simple list. When we talk about release notes we might want to list only features added since the last release; something we also want to generate from the commit messages.

What a coincidence that OpenUI5 uses such annotations 🙂

 

2. Clone a git repo that uses annotations in commit messages
For this demo I use the publicly available OpenUI5 JavaScript library. I’m aware that they use annotations for their commit messages. Just clone the repo and change into the created folder:

git clone https://github.com/SAP/openui5.git
cd openui5
 

3. Showing commit logs
Using git log in your CLI allows you to see commit messages:
```
git log
```

 

4. Formatting the commit logs to “one-liners”
Cool, but there’s too much distractive information. Let’s improve this:
```
git log --pretty=oneline
```

5. Custom formatting of commit logs
Ok, looks better. We could even format the output in a way that we it to be:
```
git log --pretty=format:"%h - %an, %ar : %s"
```

6. Getting commits since a given date
The problem with the last command is that it returns pretty much everything. Let’s only get the items from the last 2 weeks:
```
git log --pretty=format:"%h - %an, %ar : %s" --since=2.weeks
```

 
```
git log --pretty=format:"%h - %an, %ar : %s" | wc -l
git log --pretty=format:"%h - %an, %ar : %s" --since=2.weeks | wc -l
```



Well, that shows we have 38.720 commits, while 350 of them where made in the last 2 weeks.

Hint: if you only want the count you might prefer using git rev-list:
```
git rev-list master --count
```

7. Showing commits since a given tag/version until now
Next, let’s change the output format a little. Additionally, we want only to see the commits made since version (=tag) 1.44.16 until now:

 
```
git log --pretty="%h - %s (%an)" 1.44.16..HEAD
```



The total amount of commits since 1.44.16 is 17.519! What version do your customers use again? Maybe you can convince them with a few numbers to upgrade 😉 Lots of changes, lots of feature, lots of bugfixes…

Just to mention it: if you only want the count you could use –pretty=oneline:
```
git log --pretty=oneline 1.44.16..HEAD | wc -l
```

8. Listing only [FEATURE] commits
Now we want to get only the features:
```
git log --pretty="%h - %s (%an)" 1.44.16..HEAD | grep -i -E "^.{13}(\[INTERNAL\]|\[FEATURE\]|\[FIX\]|\[DOC\])*\[feature\]"
```

Note the that the regex of grep ignores the case and finds even [FEATURE] in case there are multiple annotations available. Well, it works so far, but we’re not satisfied…

 

9. Improving the output format for a nicer regex
We don’t actually wanna see the commit hash in the output, and leaving it out makes the regex look better:
```
git log --pretty=format:"%s" 1.44.16..HEAD | grep -i -E "^(\[INTERNAL\]|\[FEATURE\]|\[FIX\]|\[DOC\])*\[FEATURE\]"
```

10. Listing [FEATURE] commits since a given tag without using a hard coded tag
Let’s say the latest tag/version is 1.56.0, then we could get the features since that version as follows:
```
git log 1.56.0..HEAD --pretty=format:"%s" | grep -i -E "^(\[INTERNAL\]|\[FEATURE\]|\[FIX\]|\[DOC\])*\[FEATURE\]"
```

Now if the latest version is 1.56.1 then we would have to change the code to get the same result because the version is hard coded in our little command/script. Instead, we could achieve a robust script using git describe:
```
git describe --tags --abbrev=0
```

So with the command from above we can simply get the latest tag. Now we can take this command an execute it in our git log command by simply replacing the hard coded tag as follows:
```
git log $(git describe --tags --abbrev=0)..HEAD --pretty=format:"%s" | grep -i -E "^(\[INTERNAL\]|\[FEATURE\]|\[FIX\]|\[DOC\])*\[FEATURE\]"
```

 

11. Using only the git command with its included grep feature
The git log command has a few options that implement grep. Using this we can get rid of the “non-git” grep and the pipe we used above; so it all happens inside git log:
```
git log $(git describe --tags --abbrev=0)..HEAD --pretty=format:"%s" -i -E --grep="^(\[INTERNAL\]|\[FEATURE\]|\[FIX\]|\[DOC\])*\[FEATURE\]"
```

 

12. Writing the results into a file
Too simple to talk about it:
```
git log $(git describe --tags --abbrev=0)..HEAD --pretty=format:"%s" -i -E --grep="^(\[INTERNAL\]|\[FEATURE\]|\[FIX\]|\[DOC\])*\[FEATURE\]" > myfile.txt
```

 

Conclusion
You’ve seen how easy it is to create simple release notes from your git commit messages. For simplicity I’ve avoided to also add merge commits to the regex. By the way: haven’t you seen the UI5 release notes? Now make a guess how they are generated 😉

Based on the commands you could also better keep track of what happens in your favorite git repo, i.e. to leak what you’ve found before certain announcements are made on a conference 😉 Leaks? Well, here is one leak:
