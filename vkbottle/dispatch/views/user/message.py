from abc import ABC
from typing import Optional

from vkbottle_types.events import UserEventType

from vkbottle.dispatch.return_manager.user import UserMessageReturnHandler
from vkbottle.dispatch.views.abc.message import ABCMessageView
from vkbottle.tools.dev.mini_types.user import MessageMin, message_min


class ABCUserMessageView(ABCMessageView, ABC):
    def __init__(self):
        super().__init__()
        self.handler_return_manager = UserMessageReturnHandler()

    @staticmethod
    def get_event_type(event):
        return event[0]

    @staticmethod
    async def get_message(event, ctx_api):
        return await message_min(event[1], ctx_api)

    async def process_event(self, event: list) -> bool:
        return UserEventType(self.get_event_type(event)) == UserEventType.NEW_MESSAGE


class UserMessageView(ABCUserMessageView):
    def get_state_key(self, message: MessageMin) -> Optional[int]:
        return getattr(message, self.state_source_key, None)