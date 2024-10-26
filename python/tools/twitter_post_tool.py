import os
import json
import requests
from datetime import datetime
from python.helpers.tool import Tool, Response
from python.helpers.errors import handle_error
from dotenv import load_dotenv

# Add this import statement
import requests_oauthlib

try:
    from requests_oauthlib import OAuth1Session
except ImportError:
    print("Error: The 'requests_oauthlib' module is not installed. Please install it using 'pip install requests_oauthlib'")
    OAuth1Session = None

class TwitterPostTool(Tool):
    def __init__(self, agent, name, args, message):
        super().__init__(agent, name=name, args=args, message=message)
        if OAuth1Session is None:
            raise ImportError("The 'requests_oauthlib' module is required for this tool. Please install it using 'pip install requests_oauthlib'")
        self.oauth = self.create_oauth_session()

    def create_oauth_session(self):
        # Load environment variables
        load_dotenv('.env')

        # Retrieve credentials
        api_key = os.getenv('API_KEY')
        api_secret_key = os.getenv('API_SECRET_KEY')
        access_token = os.getenv('ACCESS_TOKEN')
        access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

        if not all([api_key, api_secret_key, access_token, access_token_secret]):
            raise ValueError("One or more Twitter API credentials are missing. Please check your .env file.")

        return OAuth1Session(
            api_key,
            client_secret=api_secret_key,
            resource_owner_key=access_token,
            resource_owner_secret=access_token_secret
        )

    async def execute(self, tweet_content='', media=None, get_replies=False, tweet_id=None, store_replies=False, **kwargs):
        if get_replies:
            if not tweet_id:
                return Response(message="Error: Tweet ID is required to get replies.", break_loop=False)
            return await self.get_replies(tweet_id, store_replies)
        
        if not tweet_content:
            return Response(message="Error: No tweet content provided.", break_loop=False)

        try:
            media_id = None
            if media:
                media_id = self.upload_media(media)

            url = 'https://api.twitter.com/2/tweets'
            payload = {'text': tweet_content}
            if media_id:
                payload['media'] = {'media_ids': [media_id]}
            response = self.oauth.post(url, json=payload)
            response.raise_for_status()
            result = f'Tweet posted successfully! Response: {response.json()}'
            return Response(message=result, break_loop=False)
        except requests.exceptions.HTTPError as e:
            error_message = f'HTTP error occurred: {e}\nResponse: {e.response.text}'
            handle_error(e)
            return Response(message=error_message, break_loop=False)
        except Exception as e:
            error_message = f'An error occurred: {str(e)}'
            handle_error(e)
            return Response(message=error_message, break_loop=False)

    def upload_media(self, media):
        url = 'https://upload.twitter.com/1.1/media/upload.json'
        with open(media, 'rb') as file:
            files = {'media': file}
            response = self.oauth.post(url, files=files)
            response.raise_for_status()
            return response.json()['media_id_string']

    async def get_replies(self, tweet_id, store_replies):
        try:
            url = f'https://api.twitter.com/2/tweets/search/recent'
            params = {
                'query': f'conversation_id:{tweet_id}',
                'max_results': 100,
                'tweet.fields': 'author_id,created_at,text'
            }
            response = self.oauth.get(url, params=params)
            response.raise_for_status()
            replies = response.json().get('data', [])
            result = f'Retrieved {len(replies)} replies for tweet {tweet_id}'
            
            if store_replies:
                filepath = self.store_replies(tweet_id, replies)
                result += f"\nReplies stored at: {filepath}"
            
            return Response(message=result, data=replies, break_loop=False)
        except requests.exceptions.HTTPError as e:
            error_message = f'HTTP error occurred while fetching replies: {e}\nResponse: {e.response.text}'
            handle_error(e)
            return Response(message=error_message, break_loop=False)
        except Exception as e:
            error_message = f'An error occurred while fetching replies: {str(e)}'
            handle_error(e)
            return Response(message=error_message, break_loop=False)

    def store_replies(self, tweet_id, replies):
        storage_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'twitter_replies')
        os.makedirs(storage_dir, exist_ok=True)
        filename = f"{tweet_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        filepath = os.path.join(storage_dir, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(replies, f, ensure_ascii=False, indent=2)
        
        return filepath

    async def before_execution(self, **kwargs):
        self.log = self.agent.context.log.log(
            type="info",
            heading=f"{self.agent.agent_name}: Using tool '{self.name}'",
            content="",
            kvps=self.args,
        )

    async def after_execution(self, response, **kwargs):
        msg_response = self.agent.read_prompt(
            "fw.tool_response.md", tool_name=self.name, tool_response=response.message
        )
        await self.agent.append_message(msg_response, human=True)
