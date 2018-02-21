
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests


class TelBotClass():
    """Documentation for TelBotClass"""
    def __init__(self, token):
        self._token = token
        self._url = "https://api.telegram.org/bot" + self._token

    def getUpdates(self, **kwargs):
        """Get new incoming messages from bot"""
        self._offset = kwargs.get('offset', None)
        self._timeout = kwargs.get('timeout', None)
        self._limit = kwargs.get('limit', None)

        data = {
        'offset': self._offset,
        'limit': self._limit,
        'timeout': self._timeout
        }

        response = requests.post(self._url + '/getUpdates', data=data)
        if (response.status_code != 200
            or not response.json()['ok']):
            return None
        else:
            return response.json()['result']

    def setWebhook(self, url, **kwargs):
        """Documentation for setWebhook method"""
        data={
        'url': url,
        'max_connections': kwargs.get('max_connections', 40),
        'allowed_updates': kwargs.get('allowed_updates', None)
        }
        if 'certificate' in list(kwargs.keys()):
            cert = {
            'certificate': open(kwargs['certificate'], 'rb')
            }
        else:
            cert = None
        requests.post(self._url + '/setWebhook', data=data, files=cert)
        if requests.status_code == 200:
            return True
        else:
            return False

    def deleteWebhook(self):
        """Try to delete Webhook. If success returns True, else returns False"""
        try:
            response = requests.get(self._url + '/deleteWebhook')
        except:
            return False
        else:
            if (response.status_code == 200 and response.json()['ok']
                and response.json()['result']):
                return True
            else:
                return False

    def getWebhookInfo(self):
        """Get information about webhook"""
        response = requests.get(self._url + '/getWebhookInfo')
        if response.status_code != 200:
            return None
        else:
            return response.json()['result']

    def sendMessage(self, chat_id, text, **kwargs):
        """ Sending a message from the bot to the specified chat """
        param = {
        'chat_id': chat_id,
        'text': text,
        'parse_mode': kwargs.get('parse_mode', None),
        'disable_web_page_preview': kwargs.get('disable_web_page_preview',
                                               None),
        'disable_notification': kwargs.get('disable_notification', False),
        'reply_to_message_id': kwargs.get('reply_to_message_id', None),
        'reply_markup': kwargs.get('reply_markup', None)
        }

        response = requests.post(self._url
                                       + '/sendMessage', data=param)
        return response.json()['result']

    def forwardMessage(self, chat_id,from_chat_id,
                       message_id, disable_notification=True):
        data = {
        'chat_id': chat_id,
        'from_chat_id': from_chat_id,
        'message_id': message_id,
        'disable_notification': disable_notification
        }
        response = requests.post(self._url + '/forwardMessage',
                                 data=data)
        if response.status_code != 200:
            return None
        else:
            return response.json()['result']

    def sendPhoto(self, chat_id, photo, **kwargs):
        data = {
        'chat_id': chat_id,
        'caption': kwargs.get('caption', None),
        'disable_notification': kwargs.get('disable_notification', False),
        'reply_to_message_id': kwargs.get('reply_to_message_id', None),
        'reply_markup': kwargs.get('reply_markup', None)
        }
        files = {
        'photo': open(photo, 'rb')
        }
        response = requests.post(self._url + '/sendPhoto',
                                 data=data, files=files)
        if response.status_code != 200:
            return None
        else:
            return response.json()['result']

    def sendAudio(self, chat_id, audio, **kwargs):
        data = {
        'chat_id': chat_id,
        'caption': kwargs.get('caption', None),
        'duration': kwargs.get('duration', None),
        'performer': kwargs.get('performer', None),
        'title': kwargs.get('title', None),
        'disable_notification': kwargs.get('disable_notification', False),
        'reply_to_message_id': kwargs.get('reply_to_message_id', None),
        'reply_markup': kwargs.get('reply_markup', None)
        }
        files = {
        'audio': open(audio, 'rb')
        }
        response = requests.post(self._url + '/sendPhoto',
                                 data=data, files=files)
        if response.status_code != 200:
            return None
        else:
            return response.json()['result']

    def sendDocument(self, chat_id, document, **kwargs):
        data = {
        'chat_id': chat_id,
        'caption': kwargs.get('caption', None),
        'disable_notification': kwargs.get('disable_notification', False),
        'reply_to_message_id': kwargs.get('reply_to_message_id', None),
        'reply_markup': kwargs.get('reply_markup', None)
        }
        files={
        'document': open(document, 'rb')
        }
        response = requests.post(self._url + '/sendDocument',
                                 data=data, files=files)
        if response.status_code != 200:
            return None
        else:
            return response.json()['result']

    def sendVideo(self,chat_id, video, **kwargs):
        data = {
        'chat_id': chat_id,
        'duration': kwargs.get('duration', None),
        'caption': kwargs.get('caption', None),
        'width': kwargs.get('width', None),
        'height': kwargs.get('height', None),
        'disable_notification': kwargs.get('disable_notification', False),
        'reply_to_message_id': kwargs.get('reply_to_message_id', None),
        'reply_markup': kwargs.get('reply_markup', None)
        }
        files= {
        'video': open(video, 'rb')
        }
        response = requests.post(self._url + '/sendPhoto',
                                 data=data, files=files)
        if response.status_code != 200:
            return None
        else:
            return response.json()['result']

    def sendVoice(self, chat_id, voice, **kwargs):
        data = {
        'chat_id': chat_id,
        'caption': kwargs.get('caption', None),
        'duration': kwargs.get('duration', None),
        'disable_notification': kwargs.get('disable_notification', False),
        'reply_to_message_id': kwargs.get('reply_to_message_id', None),
        'reply_markup': kwargs.get('reply_markup', None)
        }
        files={
        'voice': open(voice, 'rb')
        }
        response = requests.post(self._url + '/sendPhoto',
                                 data=data, files=files)
        if response.status_code != 200:
            return None
        else:
            return response.json()['result']

    def sendVideoNote(self, chat_id, vnote, **kwargs):
        data = {
        'chat_id': chat_id,
        'duration': kwargs.get('duration', 10),
        'length': kwargs.get('length', None),
        'disable_notification': kwargs.get('disable_notification', False),
        'reply_to_message_id': kwargs.get('reply_to_message_id', None),
        'reply_markup': kwargs.get('reply_markup', None)
        }
        files = {
        'video_note': open(vnote, 'rb')
        }
        response = requests.post(self._url + '/sendPhoto',
                                 data=data, files=files)
        if response.status_code != 200:
            return None
        else:
            return response.json()['result']

    def sendMediaGroup(self, chat_id, media,
                       reply_to_message_id=None, **kwargs):
        data = {
        'chat_id': chat_id,
        'disable_notification': kwargs.get('disable_notification', False),
        'reply_to_message_id': reply_to_message_id,
        }

    def sendLocation(self, chat_id, latitude, longtitude, **kwargs):
        data = {
        'chat_id': chat_id,
        'latitude': latitude,
        'longtitude': longtitude,
        'live_period': kwargs.get('live_period', 86400),
        'disable_notification': kwargs.get('disable_notification', False),
        'reply_to_message_id': kwargs.get('reply_to_message_id', None),
        'reply_markup': kwargs.get('reply_markup', None)
        }
        response = requests.post(self._url + '/sendLocation', data=data)
        if response.status_code != 200:
            return None
        else:
            return response.json()['result']

    def editMessageLiveLocation(self, chat_id, latitude, longtitude, **kwargs):
        pass

    def stopMessageLiveLocation(self, chat_id, **kwargs):
        pass

    def sendVenue(self, chat_id, latitude, longtitude, title, address, **kwargs):
        pass

    def sendContact(self, chat_id, phone_num, first_name, **kwargs):
        pass

    def sendChatAction(self, chat_id, action):
        """
        Type of action to broadcast. Choose one, depending on what the user is
        about to receive: typing for text messages, upload_photo for photos,
        record_video or upload_video for videos, record_audio or upload_audio
        for audio files, upload_document for general files, find_location for
        location data, record_video_note or upload_video_note for video notes.
        """
        data = {
        'chat_id': chat_id,
        'action': action
        }
        response = requests.post(self._url + '/sendChatAction', data=data)
        if response.status_code != 200:
            return False
        else:
            return True

    def getUserProfilePhotos(self, user_id, **kwargs):
        pass

    def kickChatMember(self, chat_id, user_id, until_date=None):
        data= {
        'chat_id': chat_id,
        'user_id': user_id,
        'until_date': until_date
        }
        requests.post(self._url + '/kickChatMember', data=data)
        if response.status_code != 200:
            return False
        else:
            return True

    def unbanChatMember(self, chat_id, user_id):
        data = {
        'chat_id': chat_id,
        'user_id': user_id
        }
        requests.post(self._url + '/unbanChatMember', data=data)
        if response.status_code != 200:
            return False
        else:
            return True

    def restrictChatMember(self, chat_id, user_id, **kwargs):
        data = {
        'chat_id': chat_id,
        'user_id': user_id,
        'until_date': kwargs.get('until_date', None),
        'can_send_messages': kwargs.get('can_send_messages', False),
        'can_send_media_messages': kwargs.get('can_send_media_messages', False),
        'can_send_other_messages': kwargs.get('can_send_other_messages', False),
        'can_add_web_page_previews': kwargs.get('can_add_web_page_previews',
                                                False)
        }
        requests.post(self._url + '/restrictChatMember', data=data)
        if response.status_code != 200:
            return False
        else:
            return True

    def promoteChatMember(self, chat_id, user_id, **kwargs):
        data = {
        'chat_id': chat_id,
        'user_id': user_id,
        'can_change_info': kwargs.get('can_change_info', True),
        'can_post_messages': kwargs.get('can_post_messages', True),
        'can_edit_messages': kwargs.get('can_edit_messages', True),
        'can_delete_messages': kwargs.get('can_delete_messages', True),
        'can_invite_users': kwargs.get('can_invite_users', True),
        'can_restrict_members': kwargs.get('can_restrict_members', True),
        'can_pin_messages': kwargs.get('can_pin_messages', True),
        'can_promote_members': kwargs.get('can_promote_members', True)
        }
        requests.post(self._url + '/promoteChatMember', data=data)
        if response.status_code != 200:
            return False
        else:
            return True

    def exportChatInviteLink(self, chat_id):
        response = requests.post(self._url + '/exportChatInviteLink',
                                 data={'chat_id': chat_id})
        if response.status_code != 200:
            return None
        else:
            return response.json()['result']

    def setChatPhoto(self, chat_id, chat_photo):
        data = {
        'chat_id': chat_id
        }
        files = {
        'photo': open(chat_photo, 'rb')
        }
        response = requests.post(self._url + '/setChatPhoto',
                                 data=data, files=files)
        if response.status_code != 200:
            return False
        else:
            return True

    def deleteChatPhoto(self, chat_id):
        data = {
        'chat_id': chat_id
        }
        requests.post(self._url + '/deleteChatPhoto', data=data)
        if response.status_code != 200:
            return False
        else:
            return True

    def setChatTitle(self, chat_id, title):
        data = {
        'chat_id': chat_id,
        'title': title
        }
        requests.post(self._url + '/setChatTitle', data=data)
        if response.status_code != 200:
            return False
        else:
            return True

    def setChatDescription(self, chat_id, description):
        data = {
        'chat_id': chat_id,
        'description': str(description)
        }
        requests.post(self._url + '/setChatDescription', data=data)
        if response.status_code != 200:
            return False
        else:
            return True

    def pinChatMessage(self, chat_id, message_id,
                       disable_notification=False):
        data = {
        'chat_id':chat_id,
        'message_id': message_id,
        'disable_notification': disable_notification
        }
        requests.post(self._url + '/pinChatMessage', data=data)
        if response.status_code != 200:
            return False
        else:
            return True

    def unpinChatMessage(self, chat_id):
        data = {
        'chat_id': chat_id
        }
        requests.post(self._url + '/unpinChatMessage', data=data)
        if response.status_code != 200:
            return False
        else:
            return True

    def leaveChat(self, chat_id):
        data = {
        'chat_id': chat_id
        }
        requests.post(self._url + '/leaveChat', data=data)
        if response.status_code != 200:
            return False
        else:
            return True

    def getChat(self, chat_id):
        data = {
        'chat_id': chat_id
        }
        response = requests.post(self._url + '/getChat', data=data)
        if response.status_code != 200:
            return None
        else:
            return response.json()['result']

    def getChatAdministrators(self, chat_id):
        response = requests.post(self._url + '/getChatAdministrators',
                                 data={'chat_id': chat_id})
        if response.status_code != 200:
            return None
        else:
            return response.json()['result']

    def getChatMembersCount(self, chat_id):
        response = requests.post(self._url + '/getChatMembersCount',
                                 data={'chat_id': chat_id})
        if response.status_code != 200:
            return None
        else:
            return response.json()["result"]

    def getChatMember(self, chat_id, member_id):
        data = {
        'chat_id': chat_id,
        'member_id': int(member_id)
        }
        response = requests.post(self._url + '/getChatMember',data=data)
        if response.status_code != 200:
            return None
        else:
            response.json()['result']

    def setChatStickerSet(self, chat_id, sticker_set_name):
        data = {
        'chat_id': chat_id,
        'sticker_set_name': sticker_set_name
        }
        if self.getChat(chat_id):
            chat = self.getChat(chat_id)
            if ('can_set_sticker_set' in list(chat.keys()) and
                chat['can_set_sticker_set'] == True):
                requests.post(self._url + '/setChatStickerSet', data=data)
                if response.status_code != 200:
                    return False
                else:
                    return True
            else:
                return False
        else:
            return False

    def deleteChatStickerSet(self, chat_id):
        if self.getChat(chat_id):
            chat = self.getChat(chat_id)
            if ('can_set_sticker_set' in list(chat.keys()) and
                chat['can_set_sticker_set'] == True):
                requests.post(self._url + '/deleteChatStickerSet',
                              data={'chat_id': chat_id})
                if response.status_code != 200:
                    return False
                else:
                    return True
            else:
                return False
        else:
            return False

    def answerCallbackQuery(self, callback_query_id, **kwargs):
        pass

    def answerInlineQuery(inline_query_id, results, **kwargs):
        pass

    def editMessageText(self, text, **kwargs):
        pass

    def editMessageCaption(self, **kwargs):
        pass

    def editMessageReplyMarkup(self, **kwargs):
        pass

    def deleteMessage(self, chat_id, message_id):
        requests.post(self._url + '/deleteMessage',
                      data = {'chat_id': chat_id,'message_id': message_id})
        if response.status_code != 200:
            return False
        else:
            return True
