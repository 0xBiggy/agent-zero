### twitter_post_tool:
Post a tweet to Twitter.

Usage:
- Use the "tweet_content" argument to specify the text of the tweet.
- Optionally, use the "media" argument to include an image with the tweet.
- This tool requires proper Twitter API credentials to be set in the environment variables.
- Do not use in combination with other tools except for thoughts. 
- Wait for response before using other tools. 
- Propose the tweet to the user before executing the tool.

**Example usage for posting a tweet:**
~~~json
{
    "thoughts": [
        "I need to post a tweet...",
        "I'll use the twitter_post_tool...",
    ],
    "tool_name": "twitter_post_tool",
    "tool_args": {
        "tweet_content": "Hello, world! This is a test tweet."
    }
}
~~~

**Example usage for posting a tweet with media:**
~~~json
{
    "thoughts": [
        "I need to post a tweet with an image...",
        "I'll use the twitter_post_tool with media...",
    ],
    "tool_name": "twitter_post_tool",
    "tool_args": {
        "tweet_content": "Check out this cool image!",
        "media": "/path/to/image.jpg"
    }
}
~~~

Remember to handle the response appropriately. The tool will return a message indicating whether the tweet was posted successfully or if an error occurred.
