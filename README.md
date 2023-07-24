# YouTube comment downloader
The script allows you to download just under 1 million youtube comments per day.

To connect you will need an`API_KEY`, you can get it from the official website of [Google Developer Console](https://console.developers.google.com/project).

It is also important that you do NOT need a username for the`CHANNEL_ID`variable. You need a unique identifier. This can be found in a few different ways, here is [one of them](https://mixedanalytics.com/blog/find-a-youtube-channel-id/).

**!!!** The script does not download comments that were left in response to other comments. However, you can download them too. You need to modify the code, everything is in the official documentation. 

I also made a little converter from `.json` to `.xlsx`, because sometimes you get non-standard characters in comments that Excel doesn't want to accept and dies. Nevertheless, even my converter doesn't work properly, but it will show you exactly where you have a non-standard character and you can edit it by hand. This is a non-standard situation, so I didn't bother much with the implementation. 