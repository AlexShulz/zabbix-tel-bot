""" Telegram Message Types.

There are all classes that emplements Telegram messages and other objects.
"""
import json


class JsonEnc:
    """
    Doc for class
    """
    def enjson(self):
        raise NotImplementedError


class JsonDec:
    """
    """
    @classmethod
    def dejson(cls, jtype):
        raise NotImplementedError

    @staticmethod
    def check_json(jtype):
        if isinstance(jtype, dict):
            return jtype
        elif isinstance(jtype, str):
            return json.loads(jtype)
        else:
            raise ValueError('jtype is not json dict or string type.')


class WebHookInfo(JsonDec):
    """
    Doc for WebHookInfo class
    """
    @classmethod
    def dejson(cls, jtype):
        obj = cls.check_json(jtype)
        url = obj.get('url')
        has_custom_certificate = obj['has_custom_certificate']
        pending_update_count = obj['pending_update_count']
        last_error_date = obj.get('last_error_date')
        last_error_message = obj.get('last_error_message')
        max_connections = obj.get('max_connections')
        allowed_updates = obj.get('allowed_updates')
        return cls(url, has_custom_certificate, pending_update_count,
                   last_error_date, last_error_message, max_connections,
                   allowed_updates)

    def __init__(self, url, has_custom_certificate=False,
                 pending_update_count=None,
                 last_error_date=None, last_error_message=None,
                 max_connections=None, allowed_updates=[]):
        self.url = url
        self.has_custom_certificate = has_custom_certificate
        self.pending_update_count = pending_update_count
        self.last_error_date = last_error_date
        self.last_error_message = last_error_message
        self.max_connections = max_connections
        self.allowed_updates = allowed_updates


class Update(JsonDec):
    """
    Doc string for Update class
    """
    @classmethod
    def dejson(cls, jtype):
        obj = cls.check_json(jtype)
        update_id = obj['update_id']
        if 'message' in obj:
            message = Message.dejson(obj['message'])
        else:
            message = None
        if 'edited_message' in obj:
            edited_message = Message.dejson(obj['edited_message'])
        else:
            edited_message = None
        if 'chanel_post' in obj:
            chanel_post = Message.dejson(obj['chanel_post'])
        else:
            chanel_post = None
        if 'edited_chanel_post' in obj:
            edited_chanel_post = Message.dejson(obj['edited_chanel_post'])
        else:
            edited_chanel_post = None
        if 'inline_query' in obj:
            inline_query = InlineQuery.dejson(obj['inline_query'])
        else:
            inline_query = None
        if 'chosen_inline_result' in obj:
            chosen_inline_result = ChosenInlineResult.dejson(
                                       obj['chosen_inline_result'])
        else:
            chosen_inline_result = None
        if 'callback_query' in obj:
            callback_query = CallbackQuery.dejson(obj['callback_query'])
        else:
            callback_query = None
        if 'shipping_query' in obj:
            shipping_query = ShippingQuery.dejson(obj['shipping_query'])
        else:
            shipping_query = None
        if 'pre_checkout_query' in obj:
            pre_checkout_query = PreCheckoutQuery.dejson(
                                     obj['pre_checkout_query'])
        else:
            pre_checkout_query = None
        return cls(update_id, message, edited_message, chanel_post,
                   edited_chanel_post, inline_query, chosen_inline_result,
                   callback_query, shipping_query, pre_checkout_query)

    def __init__(self, update_id, message, edited_message, chanel_post,
                 edited_chanel_post, inline_query, chosen_inline_result,
                 callback_query, shipping_query, pre_checkout_query):
        self.update_id = update_id
        self.message = message
        self.edited_message = edited_message
        self.chanel_post = chanel_post
        self.edited_chanel_post = edited_chanel_post
        self.inline_query = inline_query
        self.chosen_inline_result = chosen_inline_result
        self.callback_query = callback_query
        self.shipping_query = shipping_query
        self.pre_checkout_query = pre_checkout_query


class Message(JsonDec):
    """
    Doc string for Message class
    """
    @classmethod
    def dejson(cls, jtype):
        obj = cls.check_json(jtype)
        message_id = obj['message_id']
        if 'from' in obj:
            from_user = User.dejson(obj['from'])
        else:
            from_user = None
        date = obj['date']
        chat = Chat.dejson(obj['chat'])
        options = {}
        if 'forward_from' in obj:
            options['forward_from'] = User.dejson(obj['forward_from'])
        if 'forward_from_chat' in obj:
            options['forward_from_chat'] = Chat.dejson(
                                               obj['forward_from_chat'])
        options['forward_from_message_id'] = obj.get('forward_from_message_id')
        options['forward_signature'] = obj.get('forward_signature')
        options['forward_date'] = obj.get('forward_date')
        if 'reply_to_message' in obj:
            options['reply_to_message'] = Message.dejson(
                                              obj['reply_to_message'])
        options['edit_date'] = obj.get('edit_date')
        options['media_group_id'] = obj.get('media_group_id')
        options['author_signature'] = obj.get('author_signature')
        options['text'] = obj.get('text')
        if 'entities' in obj:
            options['entities'] = []
            for e in obj.get('entities'):
                options['entities'].append(MessageEntity.dejson(e))
        if 'caption_entities' in obj:
            options['caption_entities'] = []
            for ce in obj.get('caption_entities'):
                options['caption_entities'].append(MessageEntity.dejson(ce))
        if 'audio' in obj:
            options['audio'] = Audio.dejson(obj['audio'])
        if 'document' in obj:
            options['document'] = Document.dejson(obj['document'])
        if 'game' in obj:
            options['game'] = Game.dejson(obj['game'])
        if 'photo' in obj:
            options['photo'] = Photo.dejson(obj['photo'])
        if 'sticker' in obj:
            options['sticker'] = Stiker.dejson(obj['stiker'])
        if 'video' in obj:
            options['video'] = Video.dejson(obj['video'])
        if 'voice' in obj:
            options['voice'] = Voice.dejson(obj['voice'])
        if 'video_note' in obj:
            options['video_note'] = VideoNote.dejson(obj['video_note'])
        options['caption'] = obj.get('caption')
        if 'contact' in obj:
            options['contact'] = Contact.dejson(obj['contact'])
        if 'location' in obj:
            options['location'] = Location.dejson(obj['location'])
        if 'venue' in obj:
            options['venue'] = Venue.dejson(obj['venue'])
        if 'new_chat_members' in obj:
            options['new_chat_members'] = []
            for nm in obj.get('new_chat_members'):
                options['new_chat_members'].append(User.dejson(nm))
        if 'left_chat_member' in obj:
            options['left_chat_member'] = User.dejson(obj['left_chat_member'])
        options['new_chat_title'] = obj.get('new_chat_title')
        if 'new_chat_photo' in obj:
            options['new_chat_photo'] = []
            for photo in obj.get('new_chat_photo'):
                options['new_chat_photo'].append(PhotoSize.dejson(photo))
        options['delete_chat_photo'] = obj.get('delete_chat_photo')
        options['group_chat_created'] = obj.get('group_chat_created')
        options['supergroup_chat_created'] = obj.get('supergroup_chat_created')
        options['channel_chat_created'] = obj.get('channel_chat_created')
        options['migrate_to_chat_id'] = obj.get('migrate_to_chat_id')
        options['migrate_from_chat_id'] = obj.get('migrate_from_chat_id')
        if 'pinned_message' in obj:
            options['pinned_message'] = Message.dejson(obj['pinned_message'])
        if 'invoice' in obj:
            options['invoice'] = Invoice.dejson(obj['invoice'])
        if 'successful_payment' in obj:
            options['successful_payment'] = SuccessfulPayment.dejson(
                                                obj['successful_payment'])
        options['connected_website'] = obj.get('connected_website')
        return cls(message_id, from_user, date, chat, options)

    def __init__(self, message_id, from_user, date, chat, options):
        self.message_id = message_id
        self.from_user = from_user
        self.date = date
        self.chat = chat

        for key in options:
            setattr(self, key, options[key])


class MessageEntity(JsonDec):
    """
    Doc string for MessageEnity class
    """
    @classmethod
    def dejson(cls, jtype):
        obj = cls.check_json(jtype)
        ent_type = obj['type']
        offset = obj['offset']
        length = obj['length']
        url = obj.get('url')
        user = None
        if 'user' in obj:
            user = User.dejson(obj['user'])
        return cls(ent_type, offset, length, url, user)

    def __init__(self, etype, offset, length, url=None, user=None):
        self.type = etype
        self.offset = offset
        self.length = length
        self.url = url
        self.user = user


class User(JsonDec):
    """
    Doc string for User class
    """
    @classmethod
    def dejson(cls, jtype):
        obj = cls.check_json(jtype)
        uid = obj['id']
        is_bot = obj['is_bot']
        first_name = obj['first_name']
        last_name = obj['last_name']
        username = obj['username']
        language_code = obj['language_code']
        return cls(uid, is_bot, first_name, last_name, username, language_code)

    def __init__(self, uid, is_bot, fname, lname=None, username=None,
                 lang_code=None):
        self.id = uid
        self.is_bot = is_bot
        self.first_name = fname
        self.last_name = lname
        self.username = username
        self.language_code = lang_code


class Chat(JsonDec):
    """
    Doc string for Chat class
    """
    @classmethod
    def dejson(cls, jtype):
        obj = cls.check_json(jtype)
        id = obj['id']
        type = obj['type']
        title = obj.get('title')
        username = obj.get('username')
        first_name = obj.get('first_name')
        last_name = obj.get('last_name')
        all_members_are_administrators = obj.get('all_members_are_administrators')
        photo = None
        if 'photo' in obj:
            photo = ChatPhoto.dejson(obj['photo'])
        description = obj.get('description')
        invite_link = obj.get('invite_link')
        pinned_message = None
        if 'pinned_message' in obj:
            pinned_message = Message.dejson(obj['pinned_message'])
        sticker_set_name = obj.get('sticker_set_name')
        can_set_sticker_set = obj.get('can_set_sticker_set')
        return cls(id, type, title, username, first_name, last_name,
                   all_members_are_administrators, photo, description,
                   invite_link, pinned_message, sticker_set_name,
                   can_set_sticker_set)

    def __init__(self, id, type, title=None, username=None, first_name=None,
                 last_name=None, all_members_are_administrators=None,
                 photo=None, description=None, invite_link=None,
                 pinned_message=None, sticker_set_name=None,
                 can_set_sticker_set=None):
        self.id = id
        self.type = type
        self.title = title
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.all_members_are_administrators = all_members_are_administrators
        self.photo = photo
        self.description = description
        self. invite_link = invite_link
        self.pinned_message = pinned_message
        self.sticker_set_name = sticker_set_name
        self.can_set_sticker_set = can_set_sticker_set


class PhotoSize(JsonDec):
    """
    Doc for PhotoSize
    """
    @classmethod
    def dejson(cls, jtype):
        obj = clt.check_json(jtype)
        file_id = obj['file_id']
        width = obj['width']
        height = obj['height']
        file_size = obj.get('file_size')
        return cls(file_id, width, height, file_size)

    def __init__(self, file_id, width, height, file_size=None):
        self.file_id = file_id
        self.width = width
        self.height = height
        self.file_size = file_size


class Audio(JsonDec):
    """
    Doc for Audio
    """
    @classmethod
    def dejson(cls, jtype):
        obj = cls.check_json(jtype)
        file_id = obj['file_id']
        duration = obj['duration']
        performer = obj.get('performer')
        title = obj.get('title')
        mime_type = obj.get('mime_type')
        file_size = obj.get('file_size')
        return cls(file_id, duration, performer, title, mime_type, file_size)

    def __init__(self, file_id, duration, performer=None, title=None,
                 mime_type=None, file_size=None):
        self.file_id = file_id
        self.duration = duration
        self.performer = performer
        self.title = title
        self.mime_type = mime_type
        self.file_size = file_size


class Document(JsonDec):
    """
    Doc for Document class
    """
    @classmethod
    def dejson(cls, jtype):
        obj = cls.check_json(jtype)
        file_id = obj['file_id']
        thumb = None
        if 'thumb' in obj:
            thumb = PhotoSize.dejson(obj['thumb'])
        file_name = obj.get('file_name')
        mime_type = obj.get('file_name')
        file_size = obj.get('file_size')
        return cls(file_id, thumb, file_name, mime_type, file_size)

    def __init__(self, file_id, thumb=None, file_name=None, mime_type=None,
                 file_size=None):
        self.file_id = file_id
        self.thumb = thumb
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size


class Video(JsonDec):
    """
    Doc for Video class
    """
    @classmethod
    def dejson(cls, jtype):
        obj = cls.check_json(jtype)
        file_id = obj['file_id']
        width = obj['width']
        height = obj['height']
        duration = obj['duration']
        thumb = None
        if 'thumb' in obj:
            thumb = PhotoSize.dejson(obj['thumb'])
        mime_type = obj.get('mime_type')
        file_size = obj.get('file_size')
        return cls(file_id, width, height, duration, thumb, mime_type,
                   file_size)

    def __init__(self, file_id, width, height, duration, thumb=None,
                 mime_type=None, file_size=None):
        self.file_id = file_id
        self.width = width
        self.height = height
        self.duration = duration
        self.thumb = thumb
        self.mime_type = mime_type
        self.file_size = file_size


class Voice(JsonDec):
    """
    Doc for Voice class
    """
    @classmethod
    def dejson(cls, jtype):
        obj = cls.check_json(jtype)
        file_id = obj['file_id']
        duration = obj['duration']
        mime_type = obj.get('mime_type')
        file_size = obj.get('file_size')

        return cls(file_id, duration, mime_type, file_size)

    def __init__(self, file_id, duration, mime_type=None, file_size=None):
        self.file_id = file_id
        self.duration = duration
        self.mime_type = mime_type
        self.file_size = file_size


class VideoNote(JsonDec):
    """
    Doc for VideoNote class
    """
    @classmethod
    def dejson(cls, jtype):
        obj = cls.check_json(jtype)
        file_id = obj['file_id']
        length = obj['length']
        duration = obj['duration']
        thumb = None
        if 'thumb' in obj:
            thumb = PhotoSize.dejson(obj['thumb'])
        file_size = obj.get('file_size')
        return cls(file_id, length, duration, thumb, file_size)

    def __init__(self, file_id, length, duration, thumb=None, file_size=None):
        self.file_id = file_id
        self.length = length
        self.duration = duration
        self.thumb = thumb
        self.file_size = file_size


class Contact(JsonDec):
    """
    Doc for Contact class
    """
    @classmethod
    def dejson(cls, jtype):
        obj = cls.check_json(jtype)
        phone_number = obj['phone_number']
        first_name = obj['first_name']
        last_name = obj.get('last_name')
        user_id = obj.get('user_id')
        return cls(phone_number, first_name, last_name, user_id)

    def __init__(self, phone_number, first_name, last_name=None, user_id=None):
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id


class Location(JsonDec):
    """
    Location
    """
    @classmethod
    def dejson(cls, jtype):
        obj = cls.check_json(jtype)
        longtitude = obj['longtitude']
        latitude = obj['latitude']
        return cls(longtitude, latitude)

    def __init__(self, longtitude, latitude):
        self.longtitude = longtitude
        self.latitude = latitude


class UserProfilePhotos(JsonDec):
    """
    """
    @classmethod
    def dejson(cls, jtype):
        obj = cls.check_json(jtype)
        total_count = obj['total_count']
        photos = [[PhotoSize.dejson(i) for i in j] for j in obj['photos']]
        return cls(total_count, Photos)

    def __init__(self, total_count, photos):
        self.total_count = total_count
        self.photos = photoss


class File(JsonDec):
    """
    """
    @classmethod
    def dejson(cls, jtype):
        obj = cls.check_json(jtype)
        file_id = obj['file_id']
        file_size = obj['file_size']
        file_path = obj['file_path']
        return cls(file_id, file_size, file_path)

    def __init__(self, file_id, file_size, file_path):
        self.file_id = file_id
        self.file_size = file_size
        self.file_path = file_path


class ReplyKeyboardMarkup(JsonEnc):
    """
    Doc for class
    """
    def __init__(self, resize_keyboard=False, one_time_keyboard=False,
                 selective=False, row_width=3):
        self.resize_keyboard = resize_keyboard
        self.one_time_keyboard = one_time_keyboard
        self.selective = selective
        self.row_width = row_width
        self.keyboard = []

    def add_button(self, *args):
        row = []
        for btn in args:
            if isinstance(btn, KeyboardButton):
                row.append(btn.to_dict())
            else:
                raise TypeError('The button in args must be a KeyboardButton instance.')
            if (len(row) % self.row_width == 0):
                self.keyboard.append(row)
                row = []
        if len(row) > 0:
            self.keyboard.append(row)

    def enjson(self):
        jdict = {'keyboard': self.keyboard}
        if self.resize_keyboard:
            jdict['resize_keyboard'] = self.resize_keyboard
        if self.one_time_keyboard:
            jdict['one_time_keyboard'] = self.one_time_keyboard
        if self.selective:
            jdict['selective'] = self.selective
        return json.dumps(jdict)


class KeyboardButton(JsonEnc):
    """
    DOc for KeyboardButton class
    """
    def __init__(self, text, request_contact=False, request_location=False):
        self.text = text
        self.request_contact = request_contact
        self.request_location = request_location

    def enjson(self):
        return json.dumps(self.__dict__)

    def to_dict(self):
        return self.__dict__


class ReplyKeyboardRemove(JsonEnc):
    """
    Doc for ReplyKeyboardRemove class
    """
    def __init__(self, remove_keyboard=True, selective=False):
        self.remove_keyboard = remove_keyboard
        self.selective = selective

    def enjson(self):
        return json.dumps(self.__dict__)


class InlineKeyboardMarkup(JsonEnc):
    """
    Doc for InlineKeyboardMarkup class
    """
    def __init__(self, row_width=3):
        self.keyboard = list()
        self.row_width = row_width

    def add_button(self, *args):
        row = []
        for btn in args:
            if isinstance(btn, InlineKeyboardButton):
                row.append(btn.to_dict())
            else:
                raise TypeError('The button in args must be a InlineKeyboardButton instance.')
            if (len(row) % self.row_width == 0):
                self.keyboard.append(row)
                row = []
        if len(row) > 0:
            self.keyboard.append(row)

    def enjson(self):
        jdict = {'inline_keyboard': self.keyboard}
        return json.dumps(jdict)


class InlineKeyboardButton(JsonEnc):
    """
    """
    def __init__(self, text, url=None, callback_data=None,
                 switch_inline_query=None,
                 switch_inline_query_current_chat=None,
                 callback_game=None, pay=None):
        self.text = text
        self.url = url
        self.callback_data = callback_data
        self.switch_inline_query = switch_inline_query
        self.switch_inline_query_current_chat = switch_inline_query_current_chat
        self.callback_game = callback_game
        self.pay = pay

    def enjson(self):
        return json.loads(self.__dict__)

    def to_dict(self):
        return self.__dict__


class CallbackQuery(JsonDec):
    """
    """
    @classmethod
    def dejson(cls, jtype):
        obj = cls.check_json(jtype)
        qid = obj['id']
        from_user = User.dejson(obj['from'])
        if 'message' in obj:
            message = Message.dejson(obj['message'])
        else:
            message = None
        inline_message_id = obj.get('inline_message_id')
        chat_instance = obj['chat_instance']
        data = obj.get('data')
        game_short_name = obj.get('game_short_name')

        return cls(qid, from_user, chat_instance, message, inline_message_id,
                   data, game_short_name)

    def __init__(self, qid, from_user, chat_instance, message=None,
                 inline_message_id=None, data=None, game_short_name=None):
        self.id = qid
        self.user_from = user_from
        self.chat_instance = chat_instance
        self.message = message
        self.inline_message_id = inline_message_id
        self.data = data
        self.game_short_name = game_short_name


class ForceReply(JsonEnc):
    """
    """
    def __init__(self, selective=False):
        self.selective = selective

    def enjson(self):
        jdict['force_reply'] = True
        jdict['selective'] = self.selective
        return json.loads(jdict)


class ChatPhoto(JsonDec):
    """
    """
    @classmethod
    def dejson(cls, jtype):
        obj = cls.check_json(jtype)
        small_file_id = obj['small_file_id']
        big_file_id = obj['big_file_id']
        return cls(small_file_id, big_file_id)

    def __init__(self, small_file_id, big_file_id):
        self.small_file_id = small_file_id
        self.big_file_id = big_file_id


class ChatMember(JsonDec):
    """
    Doc for ChatMember class
    """
    @classmethod
    def dejson(cls, jtype):
        obj = cls.check_json(jtype)
        user = User.dejson(obj['user'])
        status = obj['status']
        until_date = obj.get('until_date')
        can_be_edited = obj.get('can_be_edited')
        can_change_info = obj.get('can_change_info')
        can_post_messages = obj.get('can_post_messages')
        can_edit_messages = obj.get('can_edit_messages')
        can_delete_messages = obj.get('can_delete_messages')
        can_invite_users = obj.get('can_invite_users')
        can_restrict_members = obj.get('can_restrict_members')
        can_pin_messages = obj.get('can_pin_messages')
        can_promote_members = obj.get('can_promote_members')
        can_send_messages = obj.get('can_send_messages')
        can_send_media_messages = obj.get('can_send_media_messages')
        can_send_other_messages = obj.get('can_send_other_messages')
        can_add_web_page_previews = obj.get('can_add_web_page_previews')

        return cls(user, status, until_date, can_be_edited, can_change_info,
                   can_post_messages, can_edit_messages, can_delete_messages,
                   can_invite_users, can_restrict_members, can_pin_messages,
                   can_promote_members, can_send_messages,
                   can_send_media_messages, can_send_other_messages,
                   can_add_web_page_previews)

    def __init__(self, user, status, until_date=None, can_be_edited=False,
                 can_change_info=False, can_post_messages=False,
                 can_edit_messages=False, can_delete_messages=False,
                 can_invite_users=False, can_restrict_members=False,
                 can_pin_messages=False, can_promote_members=False,
                 can_send_messages=False, can_send_media_messages=False,
                 can_send_other_messages=False,
                 can_add_web_page_previews=False):
        self.user = user
        self.status = status
        self.until_date = until_date
        self.can_be_edited = can_be_edited
        self.can_change_info = can_change_info
        self.can_post_messages = can_post_messages
        self.can_edit_messages = can_edit_messages
        self.can_delete_messages = can_delete_messages
        self.can_invite_users = can_invite_users
        self.can_restrict_members = can_restrict_members
        self.can_pin_messages = can_pin_messages
        self.can_promote_members = can_promote_members
        self.can_send_messages = can_send_messages
        self.can_send_media_messages = can_send_media_messages
        self.can_send_other_messages = can_send_other_messages
        self.can_add_web_page_previews = can_add_web_page_previews


class ResponseParameters(JsonDec):
    """
    Doc for ResponseParameters class
    """
    @classmethod
    def dejson(cls, jtype):
        obj = cls.check_json(jtype)
        migrate_to_chat_id = obj.get('migrate_to_chat_id')
        retry_after = obj.get('retry_after')
        return cls(migrate_to_chat_id, retry_after)

    def __init__(self, migrate_to_chat_id=None, retry_after=None):
        self.migrate_to_chat_id = migrate_to_chat_id
        self.retry_after = retry_after


class InputMediaPhoto(JsonEnc):
    """
    """
    def __init__(self, media, caption=None, parse_mode=None):
        self.type = 'photo'
        self.media = media
        self.caption = caption
        self.parse_mode = parse_mode

    def enjson(self):
        return json.loads(self.__dict__)


class InputMediaVideo(JsonEnc):
    """
    """
    def __init__(self, media, caption=None, parse_mode=None, width=None,
                 height=None, duration=None, supports_streaming=None):
        self.type = 'video'
        self.media = media
        self.caption = caption
        self.parse_mode = parse_mode
        self.width = width
        self.height = height
        self.duration = duration
        self.supports_streaming = supports_streaming

    def enjson(self):
        return json.loads(self.__dict__)


# Inline types
class InlineQuery(JsonDec):
    """
    """
    @classmethod
    def dejson(cls, jtype):
        obj = cls.check_json(jtype)
        qid = obj['id']
        user = User.dejson(obj['user'])
        location = None
        if 'location' in obj:
            location = Location.dejson(obj['location'])
        query = obj['query']
        offset = obj['offset']
        return cls(qid, user, query, offset, location)

    def __init__(self, qid, user, query, offset, location=None):
        self.id = qid
        self.from_user = user
        self.location = location
        self.query = query
        self.offset = offset


class ChosenInlineResult(JsonDec):
    """
    """
    def __init__(self):
        pass


class ShippingQuery(JsonDec):
    def __init__(self):
        pass


class PreCheckoutQuery(JsonDec):
    def __init__(self):
        pass
