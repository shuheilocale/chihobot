import discord
import cv2
import argparse
from datetime import datetime as dt

client = discord.Client()

def datestr():
    tdatetime = dt.now()
    tstr = tdatetime.strftime('%Y%m%d%H%M%S')
    return tstr

class MyClient(discord.Client):

    def __init__(self, command, camid, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.command = command
        self.camid = camid

    def __get_channel(self, channels, channel_name):
        for channel in client.get_all_channels():
            if channel.name == channel_name:
                return channel
        return None

    async def on_ready(self):
            print('Logged in as')
            print(self.user.name)
            print(self.user.id)
            print('------')

    async def on_message(self, message):
        if message.author == self.user:
            return

        filepath = 'capt/{}.jpg'.format(datestr())
        if(message.content == self.command):
            cap = cv2.VideoCapture(self.camid)
            ret, frame = cap.read()
            frame = cv2.resize(frame, (frame.shape[1], frame.shape[0]))
            cv2.imrtite(filepath, frame)

            cap.release()

            await message.channel.send(file=discord.File(filepath))


parser = argparse.ArgumentParser()
parser.add_argument('--token', '-t', type=str)
parser.add_argument('--command', '-c', type=str, default='/capture')
parser.add_argument('--camid', '-i', type=int, default=0)
args = parser.parse_args()

client = MyClient(args.command, args.camid)
client.run(args.token)
