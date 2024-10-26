### twitter_get_replies_tool:
Fetch replies for a specific tweet on Twitter.

This tool allows you to retrieve recent replies to a given tweet. It can fetch up to 100 of the most recent replies.

Usage:
- Provide the "tweet_id" of the tweet you want to get replies for.
- Optionally, set "store_replies" to true if you want to save the replies locally.

**Example usage:**
~~~json
{
    "thoughts": [
        "I need to fetch replies for a specific tweet...",
        "I'll use the twitter_get_replies_tool...",
    ],
    "tool_name": "twitter_get_replies_tool",
    "tool_args": {
        "tweet_id": "1234567890",
        "store_replies": false
    }
}
~~~

**Example usage with storing replies:**
~~~json
{
    "thoughts": [
        "I need to fetch and store replies for a specific tweet...",
        "I'll use the twitter_get_replies_tool with store_replies option...",
    ],
    "tool_name": "twitter_get_replies_tool",
    "tool_args": {
        "tweet_id": "1234567890",
        "store_replies": true
    }
}
~~~

The tool will return a message indicating the number of replies retrieved. If store_replies is set to true, it will also provide the file path where the replies are stored.

If there is an error you should return an error message exactly as it is.
