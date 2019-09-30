# VKBottle Commercial Recommendations

Welcome to VKBottle! VKBottle is a useful client with useful facilities for working with VK. Be confident about it after using this test version. But we have an another version which contains more advantages for you:

* Better Structure

* :call_me_hand:Callback API

* Full VK Api with specified objects
  
  * :man_technologist:Full Can-Be-Sended objects for advanced usage
    
    ```
    @bot.on.message.lower('plastify <material:usage>', validators=(validators.SafeMessage)}:
    async def handler(ans: Message, material):
        poll = Poll('Material {} is cool?'.format(material)).add(('yes', 'noh'))
        await ans('Wow it\'s a poll!', poll, Photo(owner=1, id=327778612))
    ```

* :couple_with_heart_woman_man:Validators for arguments in messages and also messages
  
  * For arguments
    
    ```
    class CustomValidators(RegexValidators):
        async def some_user(self, text):
            matched = re.match(r'\[id([\d]+)\|', text)
            if matched:
                return int(matched.group(1))
            return
    
    @bot.on.message('id <uid:some_user>')
    async def handler(ans: Message, uid):
        await ans(uid)
    ```
  
  * For messages
    
    ```
    @bot.on.message.startswith('my opinion: <opinion>', validators=(validators.SafeMessage))
    ```

* HTTP Executor (self)