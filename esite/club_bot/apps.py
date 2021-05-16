# -*- coding: utf-8 -*-
import os
import io
import logging
import json
import hashlib
import uuid

from django.conf import settings
from django.apps import AppConfig
from django.core.files import File
from django.contrib.auth import get_user_model

from telethon import TelegramClient, events, functions
from .file_handler import progress
import os
import time
import datetime
import asyncio
import threading

from pydub import AudioSegment
from pydub.silence import split_on_silence
import speech_recognition as sr
from asgiref.sync import sync_to_async


recognizer = sr.Recognizer()


def load_chunks(audio_in):
    audio_chunks = split_on_silence(audio_in, min_silence_len=1800, silence_thresh=-17)

    if audio_chunks:
        return audio_chunks
    else:
        return [
            audio_in,
        ]


@sync_to_async
def transcribe_audio(audio_in):
    for audio_chunk in load_chunks(audio_in):
        audio_chunk.export("temp", format="wav")

        with sr.AudioFile("temp") as source:
            audio = recognizer.listen(source)

            try:
                transcript = recognizer.recognize_google(
                    audio, language="de-AT", show_all=True
                )
                return transcript
            except Exception as ex:
                print("Error occured")
                print(ex)


@sync_to_async
def _audio_to_ow(
    chat_id,
    chat_title,
    track_audio_file,
    chat_description=None,
    tags=None,
    attendees=None,
    transcript=None,
):
    from django.contrib.auth.models import Group
    from esite.track.models import Track, ProjectAudioChannel
    

    pac, created = ProjectAudioChannel.objects.update_or_create(
        channel_id=chat_id,
        defaults={"title": chat_title, "description": chat_description},
    )

    track = Track.objects.create(
        pac=pac,
        title=track_audio_file.name,
        description=track_audio_file.description,
        audio_file=File(track_audio_file),
        audio_channel=track_audio_file.channel,
        audio_format=track_audio_file.format,
        audio_codec=track_audio_file.codec,
        audio_bitrate=track_audio_file.bitrate,
        tags=json.dumps([{"type": "tag", "value": tag} for tag in tags]),
        attendees=json.dumps(
            [{"type": "attendee", "value": attendee} for attendee in attendees]
        ),
        transcript=transcript,
    )

    if created:
        # pac has been created
        slavename = f"slave-{uuid.uuid4()}"
        password = get_user_model().objects.make_random_password()

        member = get_user_model().objects.create(username=slavename, is_active=True)
        member.set_password(hashlib.sha256(str.encode(password)).hexdigest())

        member.groups.add(Group.objects.get(name="ohrwurm-supervisor"))
        member.groups.add(Group.objects.get(name="ohrwurm-member"))

        member.pacs.add(pac)
        member.save()

        return f"Thx for joining Ohrwurm\nSlavename: {slavename}\nPassword: {password}"


class ClubBotConfig(AppConfig):
    name = "esite.club_bot"

    def ready(self):
        """Start the client."""
        print("waveaterbot started...")
        waveater_thread = threading.Thread(
            name="waveater-main-thread", target=ClubBot.main
        )
        waveater_thread.daemon = False  # -> dies after main thread is closed
        waveater_thread.start()


class ClubBot:
    def main():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        client = TelegramClient(
            "client", settings.TELEGRAM_API_ID, settings.TELEGRAM_API_HASH, loop=loop
        ).start(bot_token=settings.TELEGRAM_BOT_TOKEN)

        @client.on(events.NewMessage(pattern="/start"))
        @client.on(events.NewMessage(pattern="/help"))
        async def start(event):
            """Send a message when the command /start is issued."""
            await event.respond(
                "Hi, I'm an audio slave! :3\nI would love to convert every wav you got into a telegram voice message. (>.<)"
            )
            raise events.StopPropagation

        @client.on(events.NewMessage(pattern="/motivation"))
        async def start(event):
            """Send a message when the command /start is issued."""
            await event.respond(
                "OMG! Senpai, *o* let me convewt some wav into telegwam voice message, ~Nyaaaa"
            )
            raise events.StopPropagation

        @client.on(events.NewMessage)
        async def echo(event):
            try:
                """Check input file for audio mime type"""
                if event.message.file and event.message.file.mime_type in [
                    "audio/mpeg3",
                    "audio/x-mpeg3",
                    "audio/x-wav",
                ]:
                    """Echo the user message."""
                    msg = await event.respond("Processing...")

                    start = time.time()
                    await msg.edit("**Downloading start...**")
                    audio_in = io.BytesIO()
                    audio_in = await client.download_media(
                        event.message,
                        audio_in,
                        progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                            progress(d, t, msg, start)
                        ),
                    )

                    # > Identify the specific audio format
                    if event.message.file.mime_type == "audio/x-wav":
                        """Create autosegment from wav"""
                        audio_seg = AudioSegment.from_wav(audio_in)

                    elif (
                        event.message.file.mime_type == "audio/x-mpeg3" or "audio/mpeg3"
                    ):
                        """Create autosegment from mp3"""
                        #! Bug: Decoding failed. ffmpeg returned error code: 1
                        audio_seg = AudioSegment.from_mp3(audio_in)

                    # > Export audiosegment as ogg
                    audio_out = io.BytesIO()
                    """Configure export settings"""
                    audio_out.name = f"{event.message.file.name.split('.')[0]}_{event.message.media.document.date.strftime('%m-%d_%H-%M')}.ogg"
                    audio_out.description = event.message.text
                    audio_out.channel = "2"
                    audio_out.format = "ogg"
                    audio_out.codec = "opus"
                    audio_out.bitrate = "128k"

                    """Convert audio to desired format."""
                    audio_out = audio_seg.export(
                        audio_out,
                        bitrate=audio_out.bitrate,
                        format=audio_out.format,
                        codec=audio_out.codec,
                        parameters=[
                            "-strict",
                            "-2",
                            "-ac",
                            audio_out.channel,
                            "-vol",
                            "150",
                        ],
                        tags={
                            "ARTIST": "waveater",
                            "GENRE": "Meeting/Trashtalk",
                            "ALBUM": "waveater",
                            "TITLE": f"{event.message.file.name.split('.')[0]}_{event.message.media.document.date.strftime('%m-%d_%H-%M')}",
                            "DATE": f"{event.message.media.document.date.strftime('%Y/%m/%d_%H:%M:%S')}",
                            "COMMENT": f"A wav file converted to telegram voice message.",
                            "CONTACT": "@waveater",
                        },
                    )

                    """Return converted file."""
                    result = await client.send_file(
                        event.chat_id,
                        audio_out,
                        voice_note=True,
                        caption=f"{event.message.message}\n\n`track: '{event.message.file.name.split('.')[0]}_{event.message.media.document.date.strftime('%m-%d_%H-%M')}',\nchannel: '{audio_out.channel}',\nformat: '{audio_out.format}',\ncodec: '{audio_out.codec}',\nbitrate: '{audio_out.bitrate}'`",
                        reply_to=event.message,
                    )

                    await msg.delete()

                    # > Get a more detailed chat message
                    try:
                        chat = await event.get_chat()
                        chat_detail = await client(
                            functions.messages.GetFullChatRequest(chat_id=chat.id)
                        )
                        chat_description = chat_detail.full_chat.about
                    except:
                        chat_description = None

                    # > Excract track information
                    attendees = [
                        {"name": e.split(" ")[0]}
                        for e in event.message.text.split("@")[1:]
                    ]
                    tags = [
                        {
                            "name": e.split(":")[0],
                            "significance": e.split(":")[1].split(" ")[0:],
                        }
                        for e in event.message.text.split("!")[1:]
                    ]

                    if hasattr(event._chat, "title"):
                        chat_title = event._chat.title
                    elif hasattr(event._chat, "username"):
                        chat_title = f"User: {event._chat.username}"

                    owmsg = await _audio_to_ow(
                        chat_id=event._chat.id,
                        chat_title=chat_title,
                        chat_description=chat_description,
                        track_audio_file=audio_out,
                        tags=tags,
                        attendees=attendees,
                        transcript=await transcribe_audio(audio_seg),
                    )

                    if owmsg:
                        await client.send_message(event._chat.id, owmsg)

            except Exception as e:
                print(e)
                await msg.edit(
                    f"Shit happens! Something has gone wrong.\n\n**Error:** {e}"
                )

        with client:
            client.run_until_disconnected()


# SPDX-License-Identifier: (EUPL-1.2)
# Copyright © 2020 miraculix-org Florian Kleber
