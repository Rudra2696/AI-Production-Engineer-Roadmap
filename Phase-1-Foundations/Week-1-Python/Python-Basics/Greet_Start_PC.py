# This program only select and and read that text according to local time.

morning_greetings = [
    "Good morning. Hope you have a focused and productive day ahead.",
    "Good morning. Let’s start the day with clarity and purpose.",
    "Good morning. Time to get things moving.",
    "Good morning. Wishing you a calm and successful start.",
    "Good morning. Make today count.",
    "Good morning. One step at a time—begin well.",
    "Good morning. Stay sharp and stay consistent.",
    "Good morning. New day, clean slate.",
    "Good morning. Let’s build something meaningful today.",
    "Good morning. Start strong and stay steady."
]

afternoon_greetings = [
    "Good afternoon. Hope your day is going well.",
    "Good afternoon. Keep the momentum going.",
    "Good afternoon. Stay focused and push through.",
    "Good afternoon. Halfway through—stay on track.",
    "Good afternoon. Keep things moving forward.",
    "Good afternoon. A steady pace wins the day.",
    "Good afternoon. Stay clear, stay sharp.",
    "Good afternoon. Progress over perfection.",
    "Good afternoon. You’re doing fine—keep going.",
    "Good afternoon. Stay disciplined and finish strong."
]

evening_greetings = [
    "Good evening. You’ve done well today—finish strong.",
    "Good evening. Time to wrap things up with focus.",
    "Good evening. Reflect, adjust, and move forward.",
    "Good evening. Close the day with purpose.",
    "Good evening. A little more effort goes a long way.",
    "Good evening. Stay calm and complete what matters.",
    "Good evening. Strong endings matter.",
    "Good evening. Review the day and learn from it.",
    "Good evening. Keep it steady till the end.",
    "Good evening. Finish clean and rest easy later."
]

night_greetings = [
    "Good night. Don’t forget to rest when you’re done.",
    "Good night. Slow down and take care of yourself.",
    "Good night. It’s okay to pause and reset.",
    "Good night. Rest is part of progress.",
    "Good night. You’ve earned some quiet time.",
    "Good night. Wrap up and recharge.",
    "Good night. Tomorrow can wait.",
    "Good night. Take it easy and recover well.",
    "Good night. Step away when needed.",
    "Good night. Rest now, resume stronger later."
]

import random
import time
import win32com.client

hour = int(time.strftime("%H"))
speaker = win32com.client.Dispatch("SAPI.SpVoice")

if 5 <= hour < 12:
    message = random.choice(morning_greetings)
elif 12 <= hour < 17:
    message = random.choice(afternoon_greetings)
elif 17 <= hour < 21:
    message = random.choice(evening_greetings)
else:
    message = random.choice(night_greetings)

speaker.Speak(message)