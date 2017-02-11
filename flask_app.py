
from flask import Flask, request
import chatbot_db
import requests, json, logging

# For Curious Minds Page
PAGE_ACCESS_TOKEN = "EAACtFXjtZCncBAI6RHruaeenxfGK8vFT34ZBbAoBrQHDOCvjX5efLKvoOvZBnPGVlWCNWW9bVmxmUmfYoqQe3wm62OtwnHMREBSmYKR6xYj2gCri8np3j7A4gxQ3M1fZB3AoL962HnStSxWtzf6fZA8jsctmfLmzK81HM6vLueAZDZD"
VERIFICATION_STRING = "verification"

logging.basicConfig(filename='chatbot.log',level=logging.DEBUG)

app = Flask(__name__)

############################################
@app.route('/', methods=['GET'])
def verify():
    # This endpoint is used to complete the verification phase of the chatbot
    # application, or if the call is not from Facebook - return an 'Hello World'.

    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        # This is a verification message.
        if not request.args.get("hub.verify_token") == VERIFICATION_STRING:
            return "Verification token mismatch", 403

        # We return the content of the challenge string, and 200 code.
        return request.args["hub.challenge"], 200

    # This is not a verification msg -> send a string.
    return "Hello world", 200

############################################
@app.route('/', methods=['POST'])
def webhook():
    # endpoint for processing incoming messaging events

    data = request.get_json()
    logging.info(data)

    if data["object"] == "page":
        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:

                sender_id = messaging_event["sender"]["id"]       #User ID
                #recipient_id = messaging_event["recipient"]["id"] #Page ID

                #We detected a facebook message. Now deal with specific types of messages.

                if messaging_event.get("message"):  # someone sent us a message
                    message_text = messaging_event["message"]["text"]

                    if messaging_event['message'].get('quick_reply'):
                        if message_text == "Tech":
                            send_episode_list(sender_id, chatbot_db.tech_episodes, chatbot_db.all_episodes_url)
                        elif message_text == "Sciences":
                            send_episode_list(sender_id, chatbot_db.science_episodes, chatbot_db.all_episodes_url)
                        elif message_text == "Life Sciences":
                            send_episode_list(sender_id, chatbot_db.life_episodes, chatbot_db.all_episodes_url)
                        elif message_text == "Humanities":
                            send_episode_list(sender_id, chatbot_db.humanities_episodes, chatbot_db.all_episodes_url)

                        send_back_to_top_btn(sender_id)

                    elif message_text == "Go Back To Top":
                        send_restart_msg(sender_id)

                    elif message_text.lower() == "restart" or message_text.lower() == 'hi' or message_text.lower() == 'hi.':
                        send_restart_msg(sender_id)
                    elif message_text.lower() == "topics":
                        send_topics_msg(sender_id)
                    elif message_text.lower() == "recomended":
                        send_episode_list(sender_id, chatbot_db.recomended_episodes, chatbot_db.all_episodes_url)
                    elif message_text.lower() == "latest":
                        send_episode_msg(sender_id, chatbot_db.latest)
                    else:
                        send_message(sender_id, "Sorry, right now I can only respond to: restart, topics, latest and recomended.")

                if messaging_event.get("postback"):
                    payload   = messaging_event["postback"]["payload"]

                    if payload == "restart":
                        send_restart_msg(sender_id)
                    elif payload == "Topics":
                        send_topics_msg(sender_id)
                    elif payload == "Latest":
                        send_episode_msg(sender_id, chatbot_db.latest)
                        send_back_to_top_btn(sender_id)
                    elif payload == "Recomended":
                        send_episode_list(sender_id, chatbot_db.recomended_episodes, chatbot_db.all_episodes_url)
                        send_back_to_top_btn(sender_id)
                    elif "Ep_Req" in payload:
                        episode_id = payload.split(' ')[1]

                        for ep in chatbot_db.all_episodes:
                            if ep.id == episode_id:
                                send_episode_msg(sender_id, ep)
                                send_back_to_top_btn(sender_id)

                    elif "Ep_Description_Req" in payload:
                        episode_id = payload.split(' ')[1]
                        for ep in chatbot_db.all_episodes:
                            if ep.id == episode_id:
                                send_message(sender_id, ep.description)
                                send_back_to_top_btn(sender_id)

    return "ok", 200 #Always send an 200 OK response

def send_restart_msg(sender_id):
    # This message is the starting point of interaction with the user.
    # We first send a text message, then buttons.

    logging.info("Sending a Start Message to {sender_id}".format(sender_id=sender_id))

    params = {
        "access_token": PAGE_ACCESS_TOKEN
    }
    headers = {
        "Content-Type": "application/json"
    }
    data = json.dumps({
        "recipient": {
            "id": sender_id
        },
        "message":{
            "attachment":{
                "type":"template",
                "payload":{
                    "template_type":"button",
                    "text": chatbot_db.START_TEXT,
                    "buttons":[
                        {
                            "type":"postback",
                            "title":"Topics",
                            "payload":"Topics"
                        },{
                            "type":"postback",
                            "title":"Latest",
                            "payload":"Latest"
                        },{
                            "type":"postback",
                            "title":"Recomended",
                            "payload":"Recomended"
                        }
                    ]
                }
            }
        }
    })

    r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)
    if r.status_code != 200:
        logging.info(r.status_code)
        logging.info(r.text)

def send_topics_msg(sender_id):
    # Sending topics buttons to the user
    logging.info("Sending a Topics Message to {sender_id}".format(sender_id=sender_id))

    params = {
        "access_token": PAGE_ACCESS_TOKEN
    }
    headers = {
        "Content-Type": "application/json"
    }
    data = json.dumps({
        "recipient": {
            "id": sender_id
        },
        "message":{
            "text":"Select a topic.",
            "quick_replies":[
                {
                "content_type":"text",
                "title":"Tech",
                "payload":"Topic_Tech",
                },{
                "content_type":"text",
                "title":"Sciences",
                "payload":"Topic_Sciences",
                },{
                "content_type":"text",
                "title":"Life Sciences",
                "payload":"Topic_Life",
                },{
                "content_type":"text",
                "title":"Humanities",
                "payload":"Topic_Humanities",
                },{
                "content_type":"text",
                "title":"Back To Top",
                "payload":"restart",
                }
                ]
                }
            })

    r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)
    if r.status_code != 200:
        logging.info(r.status_code)
        logging.info(r.text)

def send_episode_msg(sender_id, episode_info):

    logging.info("sending episode {name} template to {sender_id}".format(name = episode_info.name, sender_id=sender_id))

    params = {
        "access_token": PAGE_ACCESS_TOKEN
    }
    headers = {
        "Content-Type": "application/json"
    }
    data = json.dumps({
        "recipient": {
            "id": sender_id
        },
        "message": {
            "attachment": {
                "type":"template",
                "payload":{
                    "template_type":"generic",
                    "elements":[
                        {
                            "title": episode_info.name,
                            "image_url" : episode_info.image_url,
                            "default_action": {
                                "type": "web_url",
                                "url": episode_info.ep_url
                            },
                            "buttons" : [
                                {
                                    "type": "postback",
                                    "payload" : "Ep_Description_Req" + " " + episode_info.id,
                                    "title": "Episode Description"
                                },{
                                    "type": "web_url",
                                    "url" : episode_info.mp3_url,
                                    "title": "Listen"
                                },{
                                    "type": "web_url",
                                    "url" : episode_info.transcript_url,
                                    "title": "Read Full Transcript"
                                }
                            ]
                        }
                        ]
                    }
                }
                }
            }
        )
    r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)
    if r.status_code != 200:
        logging.info(r.status_code)
        logging.info(r.text)

def send_episode_list(sender_id, episode_list, view_more_url):

    logging.info("sending episode list template to {sender_id}".format(sender_id=sender_id))

    params = {
        "access_token": PAGE_ACCESS_TOKEN
    }
    headers = {
        "Content-Type": "application/json"
    }
    data = json.dumps({
        "recipient": {
            "id": sender_id
        },
        "message": {
            "attachment": {
                "type":"template",
                "payload":{
                    "template_type":"list",
                    "top_element_style": "compact",
                    "elements":[
                        {
                        "title": episode_list[0].name,
                        "image_url": episode_list[0].image_url,
                        "subtitle": episode_list[0].topic,
                        "buttons": [
                            {
                                "title": "More",
                                "type": "postback",
                                "payload" : "Ep_Req" + " " +episode_list[0].id
                            }
                            ]
                        },{
                        "title": episode_list[1].name,
                        "image_url": episode_list[1].image_url,
                        "subtitle": episode_list[1].topic,
                        "buttons": [
                            {
                                "title": "More",
                                "type": "postback",
                                "payload" : "Ep_Req" + " " +episode_list[1].id
                            }
                            ]
                        },{
                        "title": episode_list[2].name,
                        "image_url": episode_list[2].image_url,
                        "subtitle": episode_list[2].topic,
                        "buttons": [
                            {
                                "title": "More",
                                "type": "postback",
                                "payload" : "Ep_Req" + " " +episode_list[2].id
                            }
                            ]
                        },{
                        "title": episode_list[3].name,
                        "image_url": episode_list[3].image_url,
                        "subtitle": episode_list[3].topic,
                        "buttons": [
                            {
                                "title": "More",
                                "type": "postback",
                                "payload" : "Ep_Req" + " " +episode_list[3].id
                            }
                            ]
                        }],
                        "buttons": [
                            {
                            "title": "View More",
                            "type": "web_url",
                            "url": view_more_url
                            }
                        ]
                    }
                }
                }
            }
        )
    r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)
    if r.status_code != 200:
        logging.info(r.status_code)
        logging.info(r.text)

def send_back_to_top_btn(sender_id):
    logging.info("sending Back To Top Button to {sender_id}".format(sender_id=sender_id))

    params = {
        "access_token": PAGE_ACCESS_TOKEN
    }
    headers = {
        "Content-Type": "application/json"
    }
    data = json.dumps({
        "recipient": {
            "id": sender_id
        },
        "message":{
            "text":"Click above, or - ",
            "quick_replies":[
                {
                "content_type":"text",
                "title":"Go Back To Top",
                "payload":"restart",
                }
                ]
                }
    })

    r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)
    if r.status_code != 200:
        logging.info(r.status_code)
        logging.info(r.text)

def send_message(sender_id, message_text):

    logging.info("sending message to {recipient}: {text}".format(recipient=sender_id, text=message_text))

    #Building a Request according to the Send API
    params = {
        "access_token": PAGE_ACCESS_TOKEN
    }
    headers = {
        "Content-Type": "application/json"
    }
    data = json.dumps({
        "recipient": {
            "id": sender_id
        },
        "message": {
            "text": message_text
        }
    })
    r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)
    if r.status_code != 200:
        logging.info(r.status_code)
        logging.info(r.text)
