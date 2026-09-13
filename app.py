import base64
from pathlib import Path
import gradio as gr

BASE_DIR = Path(__file__).resolve().parent

with open(BASE_DIR / "nyx.png", "rb") as image_file:
    nyx_base64 = base64.b64encode(image_file.read()).decode()
nyx_image = f"data:image/png;base64,{nyx_base64}"

with open(BASE_DIR / "dusty.png", "rb") as image_file:
    dusty_base64 = base64.b64encode(image_file.read()).decode()
dusty_image = f"data:image/png;base64,{dusty_base64}"


def handle_alexa_reply(choice, points, infinity):

    samir_style = """
        background:#b56fa0;
        color:white;
        padding:10px 14px;
        border-radius:18px 18px 5px 18px;
        width:fit-content;
        max-width:75%;
        margin-left:auto;
        margin-bottom:12px;
    """

    alexa_style = """
        background:#eeeeee;
        color:#111111;
        padding:10px 14px;
        border-radius:18px 18px 18px 5px;
        width:fit-content;
        max-width:75%;
        margin-bottom:12px;
    """

    point_style = """
        text-align:center;
        margin-top:18px;
        color:#ffbfdc;
        font-weight:bold;
    """


    # ---------- I MISS YOU MORE ----------

    if choice == "i miss you more 🥺":

        points += 5

        reply_html = f"""
        <div style="{samir_style}">
            i miss you more 🥺
        </div>

        <div style="{alexa_style}">
            NOPEEE I MISS U MORE
        </div>

        <div style="{point_style}">
            ♡ +5 Boyfriend Points
        </div>
        """


    # ---------- NUFF NUFF ----------

    elif choice == "nuff nuff":

        points += 10
        infinity += 1

        reply_html = f"""
        <div style="{samir_style}">
            nuff nuff
        </div>

        <div style="{alexa_style}">
            NO NUFF NUFF
        </div>

        <div style="{alexa_style}">
            nuff nuff infinity lock 🙄
        </div>

        <div style="{point_style}">
            🔒 ♡ +10 Boyfriend Points
        </div>
        """


    # ---------- SEE YOU SOON ----------

    elif choice == "i'll see you soon baby":

        points += 5

        reply_html = f"""
        <div style="{samir_style}">
            i'll see you soon baby
        </div>

        <div style="{alexa_style}">
            NOT SOON ENOUGH 🥀
        </div>

        <div style="{point_style}">
            ♡ +5 Boyfriend Points
        </div>
        """


    # ---------- PATEL BROTHERS ----------

    elif choice == "me too but im going to Patel Brothers rn 😭":

        reply_html = f"""
        <div style="{samir_style}">
            me too but im going to Patel Brothers rn 😭
        </div>

        <div style="{alexa_style}">
            AGAIN???
        </div>
        """


    # ---------- MOM DELIVERY ----------

    elif choice == "me too im doing a delivery for my mom":

        reply_html = f"""
        <div style="{samir_style}">
            me too im doing a delivery for my mom
        </div>

        <div style="{alexa_style}">
            ohhh okay drive safe pls!!!
        </div>

        <div style="{alexa_style}">
            call me when ur done
        </div>
        """


    # ---------- CLIMBING ----------

    elif choice == "me too im climbing rn 🧗":

        reply_html = f"""
        <div style="{samir_style}">
            me too im climbing rn 🧗
        </div>

        <div style="{alexa_style}">
            WAIT
        </div>

        <div style="{alexa_style}">
            brooo i have a climbing question
        </div>
        """


    return reply_html, points, infinity

def build_alexa_conversation(reply_html=""):
    return f"""
    <div style="
        max-width:390px;
        margin:0 auto;
        min-height:520px;
        padding:20px;
        border-radius:30px;
        background:linear-gradient(
            180deg,
            #11172f,
            #3b315c
        );
        color:white;
    ">

        <div style="
            text-align:center;
            font-size:17px;
            font-weight:bold;
            margin-bottom:25px;
        ">
            Alexa ♡
        </div>

        <div style="
            background:#eeeeee;
            color:#111;
            padding:10px 14px;
            border-radius:18px 18px 18px 5px;
            width:fit-content;
            max-width:75%;
            margin-bottom:12px;
        ">
            i miss you :(
        </div>

        {reply_html}

    </div>
    """

def handle_patel_choice(choice, points):

    samir_style = """
        background:#b56fa0;
        color:white;
        padding:10px 14px;
        border-radius:18px 18px 5px 18px;
        width:fit-content;
        max-width:75%;
        margin-left:auto;
        margin-bottom:12px;
    """

    alexa_style = """
        background:#eeeeee;
        color:#111111;
        padding:10px 14px;
        border-radius:18px 18px 18px 5px;
        width:fit-content;
        max-width:75%;
        margin-bottom:12px;
    """

    point_style = """
        text-align:center;
        margin-top:18px;
        color:#ffbfdc;
        font-weight:bold;
    """

    if choice == "yes i'll get you one too":
        points += 5

        reply = f"""
        <div style="{samir_style}">
            yes i'll get you one too
        </div>

        <div style="{alexa_style}">
            AWWWWWW 🥺
        </div>

        <div style="{alexa_style}">
            see this is why i love u
        </div>

        <div style="{point_style}">
            ♡ +5 Boyfriend Points
        </div>
        """

    elif choice == "yes but it's mine":
        points -= 3

        reply = f"""
        <div style="{samir_style}">
            yes but it's mine
        </div>

        <div style="{alexa_style}">
            oh!
        </div>

        <div style="{alexa_style}">
            sleep with one eye open
        </div>

        <div style="{point_style}">
            ♡ -3 Boyfriend Points
        </div>
        """

    elif choice == "no":
        reply = f"""
        <div style="{samir_style}">
            no
        </div>

        <div style="{alexa_style}">
            then what is even the point of going AGAIN 😭
        </div>

        <div style="{alexa_style}">
            ur mom sent u on a side quest for nothing
        </div>
        """

    elif choice == "my mom is making me go 😭":
        points += 2

        reply = f"""
        <div style="{samir_style}">
            my mom is making me go 😭
        </div>

        <div style="{alexa_style}">
            LMFAOOOO I KNEW IT
        </div>

        <div style="{alexa_style}">
            professional Patel Brothers employee atp
        </div>

        <div style="{point_style}">
            ♡ +2 Boyfriend Points
        </div>
        """

    return reply, points

def handle_climbing_choice(choice, points):

    samir_style = """
        background:#b56fa0;
        color:white;
        padding:10px 14px;
        border-radius:18px 18px 5px 18px;
        width:fit-content;
        max-width:75%;
        margin-left:auto;
        margin-bottom:12px;
    """

    alexa_style = """
        background:#eeeeee;
        color:#111111;
        padding:10px 14px;
        border-radius:18px 18px 18px 5px;
        width:fit-content;
        max-width:75%;
        margin-bottom:12px;
    """

    point_style = """
        text-align:center;
        margin-top:18px;
        color:#ffbfdc;
        font-weight:bold;
    """

    if choice == "pull with your heel and keep your hips close to the wall":
        points += 5

        reply = f"""
        <div style="{samir_style}">
            pull with your heel and keep your hips close to the wall
        </div>

        <div style="{alexa_style}">
            OHHHH
        </div>

        <div style="{alexa_style}">
            wait i think ive been letting my hips come off the wall 😭
        </div>

        <div style="{alexa_style}">
            okay climbing coach
        </div>

        <div style="{point_style}">
            ♡ +5 Boyfriend Points
        </div>
        """

    elif choice == "push through your other foot while pulling with the heel":
        points += 5

        reply = f"""
        <div style="{samir_style}">
            push through your other foot while pulling with the heel
        </div>

        <div style="{alexa_style}">
            WAIT
        </div>

        <div style="{alexa_style}">
            so like push with one leg and pull with the other??
        </div>

        <div style="{alexa_style}">
            okay wait im trying that next time
        </div>

        <div style="{point_style}">
            ♡ +5 Boyfriend Points
        </div>
        """

    elif choice == "just let go of the heel hook":
        points -= 2

        reply = f"""
        <div style="{samir_style}">
            just let go of the heel hook
        </div>

        <div style="{alexa_style}">
            THEN WHY AM I HEEL HOOKING 😭
        </div>

        <div style="{alexa_style}">
            useless ass climbing coach
        </div>

        <div style="{point_style}">
            ♡ -2 Boyfriend Points
        </div>
        """

    elif choice == "skill issue":
        points -= 3

        reply = f"""
        <div style="{samir_style}">
            skill issue
        </div>

        <div style="{alexa_style}">
            fuck u 😭
        </div>

        <div style="{alexa_style}">
            im gonna flash ur project out of spite
        </div>

        <div style="{point_style}">
            ♡ -3 Boyfriend Points
        </div>
        """

    return reply, points

def handle_delivery_choice(choice, points):

    samir_style = """
        background:#b56fa0;
        color:white;
        padding:10px 14px;
        border-radius:18px 18px 5px 18px;
        width:fit-content;
        max-width:75%;
        margin-left:auto;
        margin-bottom:12px;
    """

    alexa_style = """
        background:#eeeeee;
        color:#111111;
        padding:10px 14px;
        border-radius:18px 18px 18px 5px;
        width:fit-content;
        max-width:75%;
        margin-bottom:12px;
    """

    point_style = """
        text-align:center;
        margin-top:18px;
        color:#ffbfdc;
        font-weight:bold;
    """

    if choice == "ofc baby":
        points += 5

        reply = f"""
        <div style="{samir_style}">
            ofc baby
        </div>

        <div style="{alexa_style}">
            good 🥺
        </div>

        <div style="{alexa_style}">
            i love u drive safe
        </div>

        <div style="{point_style}">
            ♡ +5 Boyfriend Points
        </div>
        """

    elif choice == "yes ma'am 🫡":
        points += 3

        reply = f"""
        <div style="{samir_style}">
            yes ma'am 🫡
        </div>

        <div style="{alexa_style}">
            LMFAOOO
        </div>

        <div style="{alexa_style}">
            good answer jittleyang
        </div>

        <div style="{point_style}">
            ♡ +3 Boyfriend Points
        </div>
        """

    elif choice == "i'll try to remember":
        points -= 3

        reply = f"""
        <div style="{samir_style}">
            i'll try to remember
        </div>

        <div style="{alexa_style}">
            TRY???
        </div>

        <div style="{alexa_style}">
            oh okay!
        </div>

        <div style="{point_style}">
            ♡ -3 Boyfriend Points
        </div>
        """

    elif choice == "no":
        points -= 10

        reply = f"""
        <div style="{samir_style}">
            no
        </div>

        <div style="{alexa_style}">
            oh!
        </div>

        <div style="{alexa_style}">
            interesting!
        </div>

        <div style="{point_style}">
            ♡ -10 Boyfriend Points
        </div>
        """

    return reply, points

def handle_missing_you_choice(choice, points):

    samir_style = """
        background:#b56fa0;
        color:white;
        padding:10px 14px;
        border-radius:18px 18px 5px 18px;
        width:fit-content;
        max-width:75%;
        margin-left:auto;
        margin-bottom:12px;
    """

    alexa_style = """
        background:#eeeeee;
        color:#111111;
        padding:10px 14px;
        border-radius:18px 18px 18px 5px;
        width:fit-content;
        max-width:75%;
        margin-bottom:12px;
    """

    point_style = """
        text-align:center;
        margin-top:18px;
        color:#ffbfdc;
        font-weight:bold;
    """

    if choice == "why are you annoyed at ME 😭":
        points += 2

        reply = f"""
        <div style="{samir_style}">
            why are you annoyed at ME 😭
        </div>

        <div style="{alexa_style}">
            BECAUSE
        </div>

        <div style="{alexa_style}">
            ur over there
        </div>

        <div style="{alexa_style}">
            and im over here
        </div>

        <div style="{alexa_style}">
            so obviously this is ur fault
        </div>

        <div style="{point_style}">
            ♡ +2 Boyfriend Points
        </div>
        """

    elif choice == "i know baby :( i miss you too":
        points += 5

        reply = f"""
        <div style="{samir_style}">
            i know baby :( i miss you too
        </div>

        <div style="{alexa_style}">
            okayyy 🥺
        </div>

        <div style="{alexa_style}">
            i still miss u tho
        </div>

        <div style="{point_style}">
            ♡ +5 Boyfriend Points
        </div>
        """

    elif choice == "don't be sad, i'll be back with you soon":
        points += 5

        reply = f"""
        <div style="{samir_style}">
            don't be sad, i'll be back with you soon
        </div>

        <div style="{alexa_style}">
            not soon enough 🥀
        </div>

        <div style="{alexa_style}">
            but okay
        </div>

        <div style="{point_style}">
            ♡ +5 Boyfriend Points
        </div>
        """

    elif choice == "come here 🫂":
        points += 4

        reply = f"""
        <div style="{samir_style}">
            come here 🫂
        </div>

        <div style="{alexa_style}">
            I WOULD IF I COULD 😭
        </div>

        <div style="{alexa_style}">
            rude
        </div>

        <div style="{point_style}">
            ♡ +4 Boyfriend Points
        </div>
        """

    elif choice == "what do you want me to do about it 💀":
        points -= 10

        reply = f"""
        <div style="{samir_style}">
            what do you want me to do about it 💀
        </div>

        <div style="{alexa_style}">
            oh!
        </div>

        <div style="{alexa_style}">
            okay!
        </div>

        <div style="{alexa_style}">
            interesting response!
        </div>

        <div style="{point_style}">
            ♡ -10 Boyfriend Points
        </div>
        """

    return reply, points

def handle_final_alexa_choice(choice, points, infinity):

    samir_style = """
        background:#b56fa0;
        color:white;
        padding:10px 14px;
        border-radius:18px 18px 5px 18px;
        width:fit-content;
        max-width:75%;
        margin-left:auto;
        margin-bottom:12px;
    """

    alexa_style = """
        background:#eeeeee;
        color:#111111;
        padding:10px 14px;
        border-radius:18px 18px 18px 5px;
        width:fit-content;
        max-width:75%;
        margin-bottom:12px;
    """

    point_style = """
        text-align:center;
        margin-top:18px;
        color:#ffbfdc;
        font-weight:bold;
    """

    if choice == "call you tonight":
        points += 5

        reply = f"""
        <div style="{samir_style}">
            call you tonight
        </div>

        <div style="{alexa_style}">
            good 🥺
        </div>

        <div style="{point_style}">
            ♡ +5 Boyfriend Points
        </div>
        """

    elif choice == "come back to San Diego as soon as i can":
        points += 7

        reply = f"""
        <div style="{samir_style}">
            come back to San Diego as soon as i can
        </div>

        <div style="{alexa_style}">
            GOOD
        </div>

        <div style="{alexa_style}">
            hurry up pls 😭
        </div>

        <div style="{point_style}">
            ♡ +7 Boyfriend Points
        </div>
        """

    elif choice == "give you a million kisses when i see you":
        points += 7

        reply = f"""
        <div style="{samir_style}">
            give you a million kisses when i see you
        </div>

        <div style="{alexa_style}">
            okay fineeee 🥺
        </div>

        <div style="{point_style}">
            ♡ +7 Boyfriend Points
        </div>
        """

    elif choice == "nuff nuff infinity lock":
        points += 10
        infinity += 1

        reply = f"""
        <div style="{samir_style}">
            nuff nuff infinity lock
        </div>

        <div style="{alexa_style}">
            BITCH THATS CHEATING
        </div>

        <div style="{alexa_style}">
            but okay 🥺
        </div>

        <div style="{point_style}">
            🔒 ♡ +10 Boyfriend Points
        </div>
        """

    elif choice == "all of the above":
        points += 15

        reply = f"""
        <div style="{samir_style}">
            all of the above
        </div>

        <div style="{alexa_style}">
            ...
        </div>

        <div style="{alexa_style}">
            okay fine i love u 🙄
        </div>

        <div style="{alexa_style}">
            come home soon pls
        </div>

        <div style="{point_style}">
            ♡ +15 Boyfriend Points
        </div>
        """

    ending = f"""
        {reply}

        <div style="{alexa_style}">
            okay go do what u were doing
        </div>

        <div style="{alexa_style}">
            text me later
        </div>

        <div style="{alexa_style}">
            and come back to me soon okay?
        </div>

        <div style="{samir_style}">
            always ♡
        </div>

        <div style="{alexa_style}">
            good
        </div>

        <div style="{alexa_style}">
            i'll be waiting :)
        </div>

        <div style="
            text-align:center;
            color:#ffbfdc;
            margin-top:25px;
            font-size:18px;
        ">
            ♡
        </div>
    """

    return ending, points, infinity

def get_alexa_choices(stage):
    if stage == "opening":
        return [
            "i miss you more 🥺",
            "nuff nuff",
            "i'll see you soon baby",
            "me too but im going to Patel Brothers rn 😭",
            "me too im doing a delivery for my mom",
            "me too im climbing rn 🧗"
        ]

    elif stage == "patel":
        return [
            "yes i'll get you one too",
            "yes but it's mine",
            "no",
            "my mom is making me go 😭"
        ]

    elif stage == "delivery":
        return [
            "ofc baby",
            "yes ma'am 🫡",
            "i'll try to remember",
            "no"
        ]

    elif stage == "climbing":
        return [
            "pull with your heel and keep your hips close to the wall",
            "push through your other foot while pulling with the heel",
            "just let go of the heel hook",
            "skill issue"
        ]

    elif stage == "missing":
        return [
            "why are you annoyed at ME 😭",
            "i know baby :( i miss you too",
            "don't be sad, i'll be back with you soon",
            "come here 🫂",
            "what do you want me to do about it 💀"
        ]

    elif stage == "final":
        return [
            "call you tonight",
            "come back to San Diego as soon as i can",
            "give you a million kisses when i see you",
            "nuff nuff infinity lock",
            "all of the above"
        ]

    return []

def process_full_alexa_conversation(
    choice,
    stage,
    conversation_history,
    points,
    infinity
):

    # ---------- OPENING ----------
    if stage == "opening":

        reply, points, infinity = handle_alexa_reply(
            choice,
            points,
            infinity
        )

        conversation_history += reply

        if choice == "me too but im going to Patel Brothers rn 😭":

            conversation_history += """
            <div style="
                background:#eeeeee;
                color:#111;
                padding:10px 14px;
                border-radius:18px 18px 18px 5px;
                width:fit-content;
                max-width:75%;
                margin-bottom:12px;
            ">
                are u getting a mango lassi tho
            </div>
            """

            stage = "patel"

        elif choice == "me too im doing a delivery for my mom":

            stage = "delivery"

        elif choice == "me too im climbing rn 🧗":

            conversation_history += """
            <div style="
                background:#eeeeee;
                color:#111;
                padding:10px 14px;
                border-radius:18px 18px 18px 5px;
                width:fit-content;
                max-width:75%;
                margin-bottom:12px;
            ">
                im still struggling with heel hooks
            </div>

            <div style="
                background:#eeeeee;
                color:#111;
                padding:10px 14px;
                border-radius:18px 18px 18px 5px;
                width:fit-content;
                max-width:75%;
                margin-bottom:12px;
            ">
                like how am i supposed to reach for the next hold while im heel hooking 😭
            </div>
            """

            stage = "climbing"

        else:
            stage = "missing"


    # ---------- PATEL BROTHERS ----------
    elif stage == "patel":

        reply, points = handle_patel_choice(
            choice,
            points
        )

        conversation_history += reply

        stage = "missing"


    # ---------- MOM DELIVERY ----------
    elif stage == "delivery":

        reply, points = handle_delivery_choice(
            choice,
            points
        )

        conversation_history += reply

        stage = "missing"


    # ---------- CLIMBING ----------
    elif stage == "climbing":

        reply, points = handle_climbing_choice(
            choice,
            points
        )

        conversation_history += reply

        stage = "missing"


    # ---------- MISSING YOU ----------
    elif stage == "missing":

        reply, points = handle_missing_you_choice(
            choice,
            points
        )

        conversation_history += reply

        stage = "final"


    # ---------- FINAL ----------
    elif stage == "final":

        reply, points, infinity = handle_final_alexa_choice(
            choice,
            points,
            infinity
        )

        conversation_history += reply

        stage = "complete"


    return (
        stage,
        conversation_history,
        points,
        infinity
    )

def handle_unknown_choice(choice, points):

    samir_style = """
        background:#b56fa0;
        color:white;
        padding:10px 14px;
        border-radius:18px 18px 5px 18px;
        width:fit-content;
        max-width:75%;
        margin-left:auto;
        margin-bottom:12px;
    """

    girl_style = """
        background:#eeeeee;
        color:#111111;
        padding:10px 14px;
        border-radius:18px 18px 18px 5px;
        width:fit-content;
        max-width:75%;
        margin-bottom:12px;
    """

    alexa_style = """
        background:#f7d6e7;
        color:#111111;
        padding:10px 14px;
        border-radius:18px 18px 18px 5px;
        width:fit-content;
        max-width:75%;
        margin-bottom:12px;
    """

    point_style = """
        text-align:center;
        margin-top:18px;
        color:#ffbfdc;
        font-weight:bold;
    """


    # ---------------------------------
    # 1. REPLY SOMETHING MEAN
    # ---------------------------------

    if choice == "reply something mean":

        points -= 50

        reply = f"""
        <div style="{samir_style}">
            *replies something mean*
        </div>

        <div style="{alexa_style}">
            why did u reply at all 🤨
        </div>

        <div style="{point_style}">
            ♡ -50 Boyfriend Points
        </div>

        <div style="
            text-align:center;
            margin-top:25px;
            padding:18px;
            background:#491c30;
            color:white;
            border-radius:18px;
            font-weight:bold;
            font-size:20px;
        ">
            GAME OVER
            <br>
            <span style="font-size:13px;">
                Reason: unnecessary engagement 💀
            </span>
        </div>
        """

        game_over = True


    # ---------------------------------
    # 2. FLIRT BACK
    # ---------------------------------

    elif choice == "flirt back":

        points -= 999999

        reply = f"""
        <div style="{samir_style}">
            *flirts back*
        </div>

        <div style="{girl_style}">
            :)
        </div>

        <div style="
            text-align:center;
            color:#ffbfdc;
            font-weight:bold;
            margin-top:18px;
        ">
            ♡ -999999 Boyfriend Points
        </div>

        <div style="
            text-align:center;
            margin-top:25px;
            padding:18px;
            background:#491c30;
            color:white;
            border-radius:18px;
            font-weight:bold;
            font-size:20px;
        ">
            GAME OVER
            <br>
            <span style="font-size:13px;">
                Dusty: i fucking knew it
            </span>
        </div>
        """

        game_over = True


    # ---------------------------------
    # 3. BLOCK + SEND TO ALEXA
    # ---------------------------------

    elif choice == "block her and immediately send everything to Alexa":

        points += 100

        reply = f"""
        <div style="{samir_style}">
            *blocks her*
        </div>

        <div style="{samir_style}">
            *immediately sends Alexa the screenshots*
        </div>

        <div style="{alexa_style}">
            LMFAOOOOOO
        </div>

        <div style="{alexa_style}">
            good answer 😭
        </div>

        <div style="{point_style}">
            ♡ +100 Boyfriend Points
        </div>

        <div style="
            text-align:center;
            margin-top:18px;
            color:#ffd2e6;
            font-weight:bold;
        ">
            🏆 GOOD FUCKING ANSWER
        </div>
        """

        game_over = False


    # ---------------------------------
    # 4. LEAVE ON READ
    # ---------------------------------

    elif choice == "leave her on read":

        points -= 25

        reply = f"""
        <div style="{samir_style}">
            *leaves her on read*
        </div>

        <div style="{alexa_style}">
            okay but why is she still not blocked 😭
        </div>

        <div style="{point_style}">
            ♡ -25 Boyfriend Points
        </div>

        <div style="
            text-align:center;
            margin-top:25px;
            padding:18px;
            background:#491c30;
            color:white;
            border-radius:18px;
            font-weight:bold;
            font-size:20px;
        ">
            GAME OVER
            <br>
            <span style="font-size:13px;">
                Reason: incomplete girlfriend protocol
            </span>
        </div>
        """

        game_over = True


    return reply, points, game_over

def reset_infinity_lock():
    return (
        "opening",   # Alexa stage
        "",          # conversation history
        0,           # boyfriend points
        0            # infinity points
    )

def build_unknown_result(choice, points):

    # Run the actual Unknown Girl game logic
    reply_html, points, game_over = handle_unknown_choice(
        choice,
        points
    )


    # =====================================================
    # FLIRT BACK = NUCLEAR RED DEATH SCREEN 💀
    # =====================================================

    if choice == "flirt back":

        screen_html = f"""
        <div style="
            max-width:390px;
            margin:0 auto;
            padding:20px;
            min-height:520px;

            border-radius:28px;

            background:
                radial-gradient(
                    circle,
                    #8f152d 0%,
                    #5c0d20 45%,
                    #22040c 100%
                );

            color:white;

            box-shadow:
                0 0 40px rgba(255,0,50,.55);

            animation:
                deathShake .12s linear 5;
        ">

            <div style="
                text-align:center;
                font-weight:bold;
                margin-bottom:20px;
                color:#ffccd5;
            ">
                Unknown
            </div>


            <div style="
                background:#eeeeee;
                color:#111;
                padding:10px 14px;
                border-radius:18px 18px 18px 5px;
                width:fit-content;
                max-width:75%;
                margin-bottom:12px;
            ">
                heyyy :)
            </div>


            <div style="
                background:#eeeeee;
                color:#111;
                padding:10px 14px;
                border-radius:18px 18px 18px 5px;
                width:fit-content;
                max-width:75%;
                margin-bottom:12px;
            ">
                you're cute, are you single?
            </div>


            {reply_html}


            <div style="
                text-align:center;
                margin-top:25px;
                padding:18px;

                background:rgba(30,0,5,.70);

                border:3px solid #ff5b76;
                border-radius:8px;

                color:white;

                font-size:28px;
                font-weight:900;
                letter-spacing:3px;

                text-shadow:
                    3px 3px 0 #3b000c;
            ">
                GAME OVER
            </div>


            <div style="
                text-align:center;
                margin-top:18px;
                color:#ffccd5;
                font-size:13px;
            ">
                You have failed the easiest test imaginable.
            </div>

        </div>
        """


    # =====================================================
    # EVERYTHING ELSE
    # =====================================================

    else:

        screen_html = f"""
        <div style="
            max-width:390px;
            margin:0 auto;
            padding:20px;
            min-height:520px;

            border-radius:28px;

            background:
                linear-gradient(
                    180deg,
                    #151a36,
                    #3b315c
                );

            color:white;
        ">

            <div style="
                text-align:center;
                font-weight:bold;
                margin-bottom:20px;
                color:white;
            ">
                Unknown
            </div>


            <div style="
                background:#eeeeee;
                color:#111;
                padding:10px 14px;
                border-radius:18px 18px 18px 5px;
                width:fit-content;
                max-width:75%;
                margin-bottom:12px;
            ">
                heyyy :)
            </div>


            <div style="
                background:#eeeeee;
                color:#111;
                padding:10px 14px;
                border-radius:18px 18px 18px 5px;
                width:fit-content;
                max-width:75%;
                margin-bottom:12px;
            ">
                you're cute, are you single?
            </div>


            {reply_html}

        </div>
        """


    return (
        screen_html,
        points,
        game_over
    )

def handle_linkedin_choice(choice, points):

    samir_style = """
        background:#b56fa0;
        color:white;
        padding:10px 14px;
        border-radius:18px 18px 5px 18px;
        width:fit-content;
        max-width:75%;
        margin-left:auto;
        margin-bottom:12px;
    """

    linkedin_style = """
        background:#eeeeee;
        color:#111111;
        padding:10px 14px;
        border-radius:18px 18px 18px 5px;
        width:fit-content;
        max-width:75%;
        margin-bottom:12px;
    """

    point_style = """
        text-align:center;
        margin-top:18px;
        color:#ffbfdc;
        font-weight:bold;
    """


    # =====================================================
    # EASY APPLY
    # =====================================================

    if choice == "Easy Apply":

        points += 5

        reply = f"""
        <div style="{samir_style}">
            Easy Apply
        </div>

        <div style="{linkedin_style}">
            Submitting application...
        </div>

        <div style="{linkedin_style}">
            Checking qualifications...
        </div>

        <div style="{linkedin_style}">
            ✓ Loves Alexa<br>
            ✓ Certified Jittleyang<br>
            ✓ Cat tolerance<br>
            ✓ Engineering<br>
            ✗ Current location
        </div>

        <div style="{linkedin_style}">
            <strong>APPLICATION INCOMPLETE</strong><br>
            Applicant currently resides too fucking far away 😭<br>
            Required work location: San Diego, CA
        </div>

        <div style="{point_style}">
            ♡ +5 Boyfriend Points
        </div>
        """

        next_stage = "complete"
        game_over = False


    # =====================================================
    # SAVE JOB
    # =====================================================

    elif choice == "Save Job":

        reply = f"""
        <div style="{samir_style}">
            Save Job
        </div>

        <div style="{linkedin_style}">
            Job saved.
        </div>

        <div style="{linkedin_style}">
            ...
        </div>

        <div style="{linkedin_style}">
            Alexa would like to know why the fuck you're saving it instead of applying 😭
        </div>
        """

        next_stage = "save"
        game_over = False


    # =====================================================
    # MESSAGE HIRING MANAGER
    # =====================================================

    elif choice == "Message Hiring Manager":

        reply = f"""
        <div style="{samir_style}">
            Message Hiring Manager
        </div>

        <div style="{linkedin_style}">
            Opening message to Hiring Manager Alexa...
        </div>
        """

        next_stage = "message"
        game_over = False


    # =====================================================
    # NOT INTERESTED
    # =====================================================

    elif choice == "Not Interested":

        reply = f"""
        <div style="{samir_style}">
            Not Interested
        </div>

        <div style="{linkedin_style}">
            Are you sure you're not interested in:
        </div>

        <div style="{linkedin_style}">
            <strong>Alexa's Husband?</strong>
        </div>
        """

        next_stage = "confirm_not_interested"
        game_over = False


    return reply, points, next_stage, game_over

def handle_linkedin_subchoice(stage, choice, points):

    samir_style = """
        background:#b56fa0;
        color:white;
        padding:10px 14px;
        border-radius:18px 18px 5px 18px;
        width:fit-content;
        max-width:75%;
        margin-left:auto;
        margin-bottom:12px;
    """

    linkedin_style = """
        background:#eeeeee;
        color:#111111;
        padding:10px 14px;
        border-radius:18px 18px 18px 5px;
        width:fit-content;
        max-width:75%;
        margin-bottom:12px;
    """

    point_style = """
        text-align:center;
        margin-top:18px;
        color:#ffbfdc;
        font-weight:bold;
    """


    # =====================================================
    # SAVE JOB FOLLOW-UP
    # =====================================================

    if stage == "save":

        if choice == "Apply now":

            points += 3

            reply = f"""
            <div style="{samir_style}">
                Apply now
            </div>

            <div style="{linkedin_style}">
                Good recovery.
            </div>

            <div style="{linkedin_style}">
                Application submitted.
            </div>

            <div style="{point_style}">
                ♡ +3 Boyfriend Points
            </div>
            """

        elif choice == "Keep browsing":

            points -= 5

            reply = f"""
            <div style="{samir_style}">
                Keep browsing
            </div>

            <div style="{linkedin_style}">
                Interesting.
            </div>

            <div style="{linkedin_style}">
                Alexa has noted your lack of urgency.
            </div>

            <div style="{point_style}">
                ♡ -5 Boyfriend Points
            </div>
            """

        return reply, points, "complete", False


    # =====================================================
    # MESSAGE HIRING MANAGER
    # =====================================================

    elif stage == "message":

        if choice == "I believe my experience makes me an excellent candidate.":

            points += 5

            reply = f"""
            <div style="{samir_style}">
                I believe my experience makes me an excellent candidate.
            </div>

            <div style="{linkedin_style}">
                Alexa: ur hired
            </div>

            <div style="{point_style}">
                ♡ +5 Boyfriend Points
            </div>
            """

        elif choice == "I'd like to discuss the position over dinner.":

            points += 7

            reply = f"""
            <div style="{samir_style}">
                I'd like to discuss the position over dinner.
            </div>

            <div style="{linkedin_style}">
                Alexa: okayyyy smooth 😭
            </div>

            <div style="{point_style}">
                ♡ +7 Boyfriend Points
            </div>
            """

        elif choice == "Can I get a referral?":

            points += 2

            reply = f"""
            <div style="{samir_style}">
                Can I get a referral?
            </div>

            <div style="{linkedin_style}">
                Alexa: bro im literally the hiring manager 😭
            </div>

            <div style="{point_style}">
                ♡ +2 Boyfriend Points
            </div>
            """

        elif choice == "nuff nuff":

            points += 10

            reply = f"""
            <div style="{samir_style}">
                nuff nuff
            </div>

            <div style="{linkedin_style}">
                Alexa: approved immediately.
            </div>

            <div style="{point_style}">
                ♡ +10 Boyfriend Points
            </div>
            """

        return reply, points, "complete", False

    # =====================================================
    # NOT INTERESTED CONFIRMATION
    # =====================================================

    elif stage == "confirm_not_interested":

        # ---------------------------------------------
        # YES = ABSOLUTELY FUCKING NOT 💀
        # ---------------------------------------------

        if choice == "yes":

            points -= 999999

            reply = f"""
            <div style="
                background:
                    radial-gradient(
                        circle,
                        #8f152d 0%,
                        #5c0d20 45%,
                        #22040c 100%
                    );

                color:white;

                padding:22px;
                border-radius:24px;

                box-shadow:
                    0 0 40px rgba(255,0,50,.55);

                animation:
                    deathShake .12s linear 5;
            ">

                <div style="{samir_style}">
                    yes
                </div>


                <div style="
                    background:rgba(30,0,5,.65);
                    color:white;

                    padding:10px 14px;

                    border-radius:18px 18px 18px 5px;

                    width:fit-content;
                    max-width:75%;

                    margin-bottom:12px;
                ">
                    ...
                </div>


                <div style="
                    background:rgba(30,0,5,.65);
                    color:white;

                    padding:10px 14px;

                    border-radius:18px 18px 18px 5px;

                    width:fit-content;
                    max-width:75%;

                    margin-bottom:12px;
                ">
                    Bold choice, Futuluhtoogan.
                </div>


                <div style="
                    text-align:center;

                    margin-top:20px;

                    color:#ffccd5;

                    font-weight:bold;
                ">
                    ♡ -999999 Boyfriend Points
                </div>


                <div style="
                    text-align:center;

                    margin-top:25px;

                    padding:18px;

                    background:rgba(30,0,5,.75);

                    border:3px solid #ff5b76;
                    border-radius:8px;

                    color:white;

                    font-size:28px;
                    font-weight:900;

                    letter-spacing:3px;

                    text-shadow:
                        3px 3px 0 #3b000c;
                ">
                    GAME OVER
                </div>


                <div style="
                    text-align:center;

                    margin-top:18px;

                    color:#ffccd5;

                    font-size:13px;
                ">
                    Reason: rejecting the only job that matters 💀
                </div>

            </div>
            """

            return (
                reply,
                points,
                "complete",
                True
            )


        # ---------------------------------------------
        # WAIT NO = RECOVERY 😭
        # ---------------------------------------------

        elif choice == "WAIT NO":

            points -= 2

            reply = f"""
            <div style="{samir_style}">
                WAIT NO
            </div>

            <div style="{linkedin_style}">
                GOOD RECOVERY 😭
            </div>

            <div style="{linkedin_style}">
                Application status restored.
            </div>

            <div style="{point_style}">
                ♡ -2 Boyfriend Points
            </div>
            """

            return (
                reply,
                points,
                "complete",
                False
            )

def build_linkedin_screen(history_html=""):

    return f"""
    <div style="
        max-width:390px;
        margin:0 auto;
        padding:20px;
        min-height:520px;

        border-radius:28px;

        background:
            linear-gradient(
                180deg,
                #0f1c2e,
                #23354d
            );

        color:white;
    ">

        <div style="
            text-align:center;
            font-weight:bold;
            margin-bottom:20px;
            color:white;
        ">
            LinkedIn
        </div>


        <div style="
            background:#ffffff;
            color:#111;
            padding:14px;
            border-radius:16px;
            width:100%;
            box-sizing:border-box;
            margin-bottom:14px;
        ">

            <div style="
                font-size:18px;
                font-weight:bold;
                color:#111;
                margin-bottom:4px;
            ">
                Alexa's Husband
            </div>

            <div style="
                font-size:13px;
                color:#444;
                margin-bottom:10px;
            ">
                Flores Household · San Diego, CA · On-site
            </div>


            <div style="
                font-size:13px;
                color:#333;
                line-height:1.5;
            ">
                <strong>Employment type:</strong> Permanent
                <br>
                <strong>Experience level:</strong> Futuluhtoogan
                <br>
                <strong>Possible Applicants:</strong> 1
                <br>
                <strong>Hiring manager:</strong> Alexa Flores
            </div>


            <hr style="
                border:none;
                border-top:1px solid #ddd;
                margin:14px 0;
            ">


            <div style="
                font-size:14px;
                font-weight:bold;
                color:#111;
                margin-bottom:5px;
            ">
                About the job
            </div>

            <div style="
                font-size:13px;
                color:#333;
                line-height:1.45;
            ">
                The Flores Household is seeking one qualified Jittleyang
                to fill a permanent position in San Diego, California.
            </div>


            <div style="
                font-size:14px;
                font-weight:bold;
                color:#111;
                margin-top:14px;
                margin-bottom:5px;
            ">
                Preferred qualifications
            </div>

            <div style="
                font-size:13px;
                color:#333;
                line-height:1.5;
            ">
                • Must love Alexa
                <br>
                • Must tolerate Nyxie
                <br>
                • Must survive Dusty's attitude
                <br>
                • Climbing experience is a plus
                <br>
                • Must answer "what's Lotus?" under pressure
                <br>
                • Must return to San Diego
            </div>


            <div style="
                font-size:14px;
                font-weight:bold;
                color:#111;
                margin-top:14px;
                margin-bottom:5px;
            ">
                Compensation
            </div>

            <div style="
                font-size:13px;
                color:#333;
                line-height:1.5;
            ">
                • Unlimited kisses
                <br>
                • Forehead kisses
                <br>
                • Alexa
                <br>
                • Nyxie
                <br>
                • Dusty
            </div>

        </div>


        {history_html}

    </div>
    """

def get_linkedin_choices(stage):

    if stage == "main":
        return [
            "Easy Apply",
            "Save Job",
            "Message Hiring Manager",
            "Not Interested"
        ]

    elif stage == "save":
        return [
            "Apply now",
            "Keep browsing"
        ]

    elif stage == "message":
        return [
            "I believe my experience makes me an excellent candidate.",
            "I'd like to discuss the position over dinner.",
            "Can I get a referral?",
            "nuff nuff"
        ]

    elif stage == "confirm_not_interested":
        return [
            "yes",
            "WAIT NO"
        ]

    return []

def build_calendar_screen():

    return """
    <div style="
        max-width:390px;
        margin:0 auto;
        padding:20px;
        min-height:520px;

        border-radius:28px;

        background:
            linear-gradient(
                180deg,
                #171a38,
                #41345f
            );

        color:white;
    ">

        <div style="
          text-align:center;
          font-weight:bold;
          font-size:18px;
          margin-bottom:20px;
          color:white;
        ">
            📅 Calendar
        </div>


        <div style="
            background:rgba(255,255,255,.92);
            color:#111;
            border-radius:18px;
            padding:16px;
        ">

            <div style="
                font-weight:bold;
                font-size:15px;
                margin-bottom:14px;
            ">
                TODAY
            </div>


            <div style="line-height:1.9; font-size:13px;">

                <strong>9:00 AM</strong>
                &nbsp; — &nbsp; Miss Alexa

                <br>

                <strong>10:00 AM</strong>
                &nbsp; — &nbsp; Engineering shit

                <br>

                <strong>12:00 PM</strong>
                &nbsp; — &nbsp; Think about Alexa

                <br>

                <strong>2:00 PM</strong>
                &nbsp; — &nbsp; Patel Brothers 🛒

                <br>

                <strong>4:00 PM</strong>
                &nbsp; — &nbsp; Delivery for Mom

                <br>

                <strong>6:00 PM</strong>
                &nbsp; — &nbsp; Climbing 🧗

                <br>

                <strong>9:00 PM</strong>
                &nbsp; — &nbsp; CALL YOUR GIRLFRIEND ‼️

                <br>

                <strong>11:00 PM</strong>
                &nbsp; — &nbsp; Nuff nuff

            </div>


            <hr style="
                border:none;
                border-top:1px solid #ddd;
                margin:16px 0;
            ">


            <div style="
                background:#f8ddeb;
                color:#481d38;

                padding:12px;

                border-radius:14px;

                font-size:13px;
                line-height:1.5;
            ">

                <strong>♡ Love Alexa</strong>

                <br>

                All day

                <br>

                Repeats: Forever

            </div>

        </div>

    </div>
    """

def handle_calendar_check(points):

    points += 2

    result_html = """
    <div style="
        max-width:390px;
        margin:0 auto;
        padding:20px;
        min-height:520px;

        border-radius:28px;

        background:
            linear-gradient(
                180deg,
                #171a38,
                #41345f
            );

        color:white;
    ">

        <div style="
            text-align:center;
            font-weight:bold;
            font-size:18px;
            margin-bottom:20px;
        ">
            📅 Calendar
        </div>


        <div style="
            background:rgba(255,255,255,.92);
            color:#111;
            border-radius:18px;
            padding:16px;
        ">

            <div style="
                font-weight:bold;
                font-size:15px;
                margin-bottom:14px;
            ">
                TODAY
            </div>


            <div style="line-height:1.9; font-size:13px;">

                <strong>9:00 AM</strong>
                &nbsp; — &nbsp; Miss Alexa

                <br>

                <strong>10:00 AM</strong>
                &nbsp; — &nbsp; Engineering shit

                <br>

                <strong>12:00 PM</strong>
                &nbsp; — &nbsp; Think about Alexa

                <br>

                <strong>2:00 PM</strong>
                &nbsp; — &nbsp; Patel Brothers 🛒

                <br>

                <strong>4:00 PM</strong>
                &nbsp; — &nbsp; Delivery for Mom

                <br>

                <strong>6:00 PM</strong>
                &nbsp; — &nbsp; Climbing 🧗

                <br>

                <strong>9:00 PM</strong>
                &nbsp; — &nbsp; CALL YOUR GIRLFRIEND ‼️

                <br>

                <strong>11:00 PM</strong>
                &nbsp; — &nbsp; Nuff nuff

            </div>


            <hr style="
                border:none;
                border-top:1px solid #ddd;
                margin:16px 0;
            ">


            <div style="
                background:#f8ddeb;
                color:#481d38;

                padding:12px;

                border-radius:14px;

                font-size:13px;
                line-height:1.5;
            ">

                <strong>♡ Love Alexa</strong>

                <br>

                All day

                <br>

                Repeats: Forever

            </div>

        </div>


        <div style="
            text-align:center;
            margin-top:18px;
            color:#ffbfdc;
            font-weight:bold;
        ">
            ✓ Schedule checked
        </div>


        <div style="
            text-align:center;
            margin-top:8px;
            color:#ffbfdc;
            font-weight:bold;
        ">
            ♡ +2 Boyfriend Points
        </div>

    </div>
    """

    return (
        result_html,
        points
    )

def handle_reminder_choice(choice, nyxie_trust, dusty_trust):

    result_style = """
        background:#eeeeee;
        color:#111;
        padding:10px 14px;
        border-radius:18px;
        margin-bottom:12px;
    """

    reward_style = """
        text-align:center;
        margin-top:16px;
        color:#ffbfdc;
        font-weight:bold;
    """

    if choice == "Text Alexa":

        result = f"""
        <div style="{result_style}">
            ✓ Text Alexa
            <br>
            Good. She misses you 😭
        </div>
        """


    elif choice == "Call Alexa":

        result = f"""
        <div style="{result_style}">
            ✓ Call Alexa
            <br>
            Even better. Go talk to your girlfriend 😭
        </div>
        """


    elif choice == "Give Nyxie treats":

        nyxie_trust += 5

        result = f"""
        <div style="{result_style}">
            ✓ Give Nyxie treats
            <br>
            Nyxie approves.
        </div>

        <div style="{reward_style}">
            🐈 +5 Nyxie Trust
        </div>
        """


    elif choice == "Scoop Nyxie's litter box":

        nyxie_trust += 5

        result = f"""
        <div style="{result_style}">
            ✓ Scoop Nyxie's litter box
            <br>
            Nyxie: finally.
        </div>

        <div style="{reward_style}">
            🐈 +5 Nyxie Trust
        </div>
        """


    elif choice == "Give Dusty treats":

        dusty_trust += 5

        result = f"""
        <div style="{result_style}">
            ✓ Give Dusty treats
            <br>
            Dusty: acceptable.
        </div>

        <div style="{reward_style}">
            🤍 +5 Dusty Trust
        </div>
        """


    elif choice == "Go back to San Diego":

        result = f"""
        <div style="{result_style}">
            ✓ Go back to San Diego
            <br>
            This reminder cannot be completed here.
            <br>
            Open Maps when you're ready ♡
        </div>
        """


    return result, nyxie_trust, dusty_trust

def build_reminders_screen(result_html=""):

    return f"""
    <div style="
        max-width:390px;
        margin:0 auto;
        padding:20px;
        min-height:520px;

        border-radius:28px;

        background:
            linear-gradient(
                180deg,
                #171a38,
                #41345f
            );

        color:white;
    ">

        <div style="
            text-align:center;
            font-weight:bold;
            font-size:18px;
            margin-bottom:20px;
            color:white;
        ">
            ⏰ Reminders
        </div>


        <div style="
            background:rgba(255,255,255,.92);
            color:#111;

            border-radius:18px;

            padding:16px;

            margin-bottom:14px;
        ">

            <div style="
                font-weight:bold;
                font-size:15px;
                margin-bottom:12px;
                color:#111;
            ">
                TO DO
            </div>


            <div style="
                font-size:13px;
                line-height:1.9;
                color:#111;
            ">

                ☐ Text Alexa
                <br>

                ☐ Call Alexa
                <br>

                ☐ Give Nyxie treats
                <br>

                ☐ Scoop Nyxie's litter box
                <br>

                ☐ Give Dusty treats
                <br>

                ☐ Go back to San Diego

            </div>

        </div>


        {result_html}

    </div>
    """

def get_reminder_choices():

    return [
        "Text Alexa",
        "Call Alexa",
        "Give Nyxie treats",
        "Scoop Nyxie's litter box",
        "Give Dusty treats",
        "Go back to San Diego"
    ]

def build_maps_screen(route_choice=None, route_result_html=""):

    icon_map = {
        "🚗 Drive": "🚗",
        "🚀 Aerospace Engineer": "🚀",
        "🧗 Climb": "🧗",
        "🏃 Run": "🏃",
        "✈️ Fly": "✈️"
    }

    travel_icon = icon_map.get(route_choice, "♡")

    animation_html = ""

    if route_choice is not None:

        animation_html = f"""
        <div class="maps-animation-box">

            <div class="maps-route-line"></div>

            <div class="maps-start-pin">
                📍
                <div class="maps-location-label">
                    Samir
                </div>
            </div>

            <div class="maps-travel-icon">
                {travel_icon}
            </div>

            <div class="maps-end-pin">
                ♡
                <div class="maps-location-label">
                    Alexa
                </div>
            </div>

        </div>


        <div class="maps-distance-box">

            <div class="maps-distance-title">
                Distance to Alexa
            </div>

            <div class="maps-progress-track">

                <div class="maps-progress-fill"></div>

                <div class="maps-progress-heart">
                    ♡
                </div>

            </div>

            <div class="maps-distance-text">
                getting closer...
            </div>

        </div>
        """


    return f"""
    <div class="maps-main-screen">

        <div class="maps-title">
            🗺️ Maps
        </div>


        <div class="maps-location-card">

            <div class="maps-location-heading">
                📍 Current Location
            </div>

            <div class="maps-location-value">
                Samir
            </div>

            <div class="maps-location-sub">
                too fucking far away
            </div>

        </div>


        <div class="maps-destination-arrow">
            ↓
        </div>


        <div class="maps-location-card destination-card">

            <div class="maps-location-heading">
                ♡ Destination
            </div>

            <div class="maps-location-value">
                Alexa
            </div>

            <div class="maps-location-sub">
                Home · San Diego, CA
            </div>

        </div>


        <div class="maps-calculating">
            Calculating routes
            <span>.</span>
            <span>.</span>
            <span>.</span>
        </div>


        <div class="maps-route-found">
            Route found ♡
        </div>


        {route_result_html}

        {animation_html}

    </div>
    """

    maps_animation_css = """

/* ========================================================
   MAPS MAIN SCREEN
   ======================================================== */

.maps-main-screen {
    max-width:390px;
    min-height:520px;

    margin:0 auto;
    padding:20px;

    border-radius:28px;

    background:
        linear-gradient(
            180deg,
            #111a32,
            #25395b,
            #4a4069
        );

    color:white;
}


.maps-title {
    text-align:center;

    font-size:20px;
    font-weight:700;

    margin-bottom:20px;

    color:white;
}


/* ========================================================
   LOCATION CARDS
   ======================================================== */

.maps-location-card {
    background:rgba(255,255,255,.92);

    color:#111;

    padding:14px;

    border-radius:18px;

    box-shadow:
        0 6px 18px rgba(0,0,0,.15);
}


.maps-location-heading {
    font-size:12px;
    font-weight:700;

    color:#666;

    margin-bottom:5px;
}


.maps-location-value {
    font-size:18px;
    font-weight:700;

    color:#111;
}


.maps-location-sub {
    margin-top:3px;

    font-size:12px;

    color:#555;
}


.destination-card {
    box-shadow:
        0 0 20px rgba(255,174,215,.23);
}


.maps-destination-arrow {
    text-align:center;

    padding:8px 0;

    font-size:24px;

    color:#ffc2df;

    animation:
        mapsArrowBounce 1.2s ease-in-out infinite;
}


@keyframes mapsArrowBounce {

    0%,
    100% {
        transform:translateY(0);
    }

    50% {
        transform:translateY(5px);
    }
}


/* ========================================================
   CALCULATING DOTS
   ======================================================== */

.maps-calculating {
    text-align:center;

    margin-top:20px;

    color:#e5e8ff;

    font-size:13px;
}


.maps-calculating span {
    display:inline-block;

    animation:
        mapsDot 1.3s infinite;

    opacity:.2;
}


.maps-calculating span:nth-child(2) {
    animation-delay:.2s;
}


.maps-calculating span:nth-child(3) {
    animation-delay:.4s;
}


@keyframes mapsDot {

    0%,
    100% {
        opacity:.2;
        transform:translateY(0);
    }

    50% {
        opacity:1;
        transform:translateY(-3px);
    }
}


.maps-route-found {
    margin-top:8px;

    text-align:center;

    color:#ffc2df;

    font-weight:700;

    font-size:13px;
}


/* ========================================================
   ROUTE ANIMATION
   ======================================================== */

.maps-animation-box {
    position:relative;

    height:120px;

    margin-top:25px;

    overflow:hidden;

    border-radius:20px;

    background:
        linear-gradient(
            180deg,
            rgba(255,255,255,.08),
            rgba(255,255,255,.03)
        );
}


.maps-route-line {
    position:absolute;

    left:35px;
    right:35px;
    top:58px;

    height:3px;

    border-radius:999px;

    background:
        repeating-linear-gradient(
            90deg,
            #d996bd 0,
            #d996bd 8px,
            transparent 8px,
            transparent 15px
        );

    opacity:.7;

    animation:
        mapsRoutePulse 1.4s ease-in-out infinite;
}


@keyframes mapsRoutePulse {

    0%,
    100% {
        opacity:.35;
    }

    50% {
        opacity:1;
    }
}


/* ========================================================
   START + DESTINATION
   ======================================================== */

.maps-start-pin,
.maps-end-pin {
    position:absolute;

    top:35px;

    font-size:27px;

    z-index:3;
}


.maps-start-pin {
    left:22px;
}


.maps-end-pin {
    right:22px;

    color:#ffc0df;

    animation:
        mapsHeartBounce 1.1s ease-in-out infinite;
}


@keyframes mapsHeartBounce {

    0%,
    100% {
        transform:scale(1);
    }

    50% {
        transform:scale(1.25);
    }
}


.maps-location-label {
    position:absolute;

    top:34px;
    left:50%;

    transform:translateX(-50%);

    white-space:nowrap;

    font-size:10px;

    color:#fff;
}


/* ========================================================
   MOVING VEHICLE
   ======================================================== */

.maps-travel-icon {
    position:absolute;

    left:38px;
    top:36px;

    z-index:4;

    font-size:30px;

    animation:
        mapsTravel 5s ease-in-out infinite;
}


@keyframes mapsTravel {

    0% {
        left:38px;
        transform:translateY(0) rotate(0deg);
    }

    20% {
        transform:translateY(-6px) rotate(-3deg);
    }

    50% {
        transform:translateY(4px) rotate(2deg);
    }

    80% {
        transform:translateY(-3px) rotate(-2deg);
    }

    100% {
        left:290px;
        transform:translateY(0) rotate(0deg);
    }
}


/* ========================================================
   DISTANCE PROGRESS
   ======================================================== */

.maps-distance-box {
    margin-top:20px;
}


.maps-distance-title {
    text-align:center;

    color:white;

    font-size:12px;

    margin-bottom:9px;
}


.maps-progress-track {
    position:relative;

    height:12px;

    border-radius:999px;

    overflow:visible;

    background:rgba(255,255,255,.15);
}


.maps-progress-fill {
    position:absolute;

    left:0;
    top:0;

    height:100%;

    border-radius:999px;

    background:
        linear-gradient(
            90deg,
            #8e6eb3,
            #d98db9,
            #ffc2df
        );

    animation:
        mapsProgress 5s ease-in-out infinite;
}


@keyframes mapsProgress {

    0% {
        width:5%;
    }

    100% {
        width:100%;
    }
}


.maps-progress-heart {
    position:absolute;

    right:-5px;
    top:-10px;

    font-size:23px;

    color:#ffc2df;

    text-shadow:
        0 0 8px rgba(255,166,213,.6);
}


.maps-distance-text {
    text-align:center;

    margin-top:9px;

    font-size:11px;

    color:#d9dced;
}
"""


def get_maps_choices():
    return [
        "🚗 Drive",
        "🚀 Aerospace Engineer",
        "🧗 Climb",
        "🏃 Run",
        "✈️ Fly"
    ]

maps_finale_css = """

/* ========================================================
   FINAL MAPS SCREEN
   ======================================================== */

.maps-finale-screen {
    position:relative;

    max-width:390px;
    min-height:700px;

    margin:0 auto;
    padding:20px;

    overflow:hidden;

    border-radius:28px;

    background:
        radial-gradient(
            circle at 50% 85%,
            rgba(255,184,219,.25),
            transparent 34%
        ),
        linear-gradient(
            180deg,
            #111a32,
            #29385c,
            #60476f
        );

    color:white;
}


/* ========================================================
   START MESSAGE
   ======================================================== */

.final-route-message {
    margin-top:18px;

    text-align:center;

    color:#ffc3df !important;

    font-weight:700;

    animation:
        finalFade 1s ease forwards;
}


/* ========================================================
   ROUTE
   ======================================================== */

.final-route-animation {
    position:relative;

    height:110px;

    margin-top:20px;
}


.final-route-line {
    position:absolute;

    left:35px;
    right:35px;
    top:52px;

    height:3px;

    background:
        repeating-linear-gradient(
            90deg,
            #d991b9 0,
            #d991b9 8px,
            transparent 8px,
            transparent 15px
        );

    opacity:.65;
}


.final-start {
    position:absolute;

    left:18px;
    top:30px;

    font-size:28px;
}


.final-home {
    position:absolute;

    right:18px;
    top:30px;

    font-size:31px;

    color:#ffc1df;

    animation:
        homePulse 1s ease-in-out infinite;
}


@keyframes homePulse {

    0%,
    100% {
        transform:scale(1);
    }

    50% {
        transform:scale(1.3);
    }
}


.final-moving-icon {
    position:absolute;

    left:40px;
    top:30px;

    font-size:30px;

    z-index:5;

    animation:
        finalTravel 5.5s ease-in-out forwards;
}


@keyframes finalTravel {

    0% {
        left:40px;
    }

    20% {
        transform:translateY(-7px) rotate(-4deg);
    }

    50% {
        transform:translateY(5px) rotate(3deg);
    }

    80% {
        transform:translateY(-3px);
    }

    100% {
        left:290px;
        transform:translateY(0);
    }
}


/* ========================================================
   DISTANCE COUNTDOWN
   ======================================================== */

.final-distance {
    margin-top:5px;

    text-align:center;

    font-family:monospace;

    font-size:12px;

    min-height:110px;

    color:white !important;
}


.distance-step {
    opacity:0;

    margin-bottom:6px;

    color:white !important;

    animation:
        distanceAppear .5s forwards;
}


/* FORCE EVERYTHING INSIDE DISTANCE COUNTDOWN WHITE */

.maps-finale-screen .final-distance,
.maps-finale-screen .final-distance *,
.maps-finale-screen .distance-step,
.maps-finale-screen .distance-step * {
    color:#ffffff !important;
    -webkit-text-fill-color:#ffffff !important;
}


.d1 {
    animation-delay:.5s;
    color:white !important;
}

.d2 {
    animation-delay:1.3s;
    color:white !important;
}

.d3 {
    animation-delay:2.1s;
    color:white !important;
}

.d4 {
    animation-delay:2.9s;
    color:white !important;
}

.d5 {
    animation-delay:3.7s;
    color:white !important;
}

.d6 {
    animation-delay:4.5s;

    font-size:25px;

    color:#ffc1df !important;
    -webkit-text-fill-color:#ffc1df !important;
}


@keyframes distanceAppear {

    from {
        opacity:0;
        transform:translateY(5px);
    }

    to {
        opacity:1;
        transform:translateY(0);
    }
}


/* ========================================================
   ARRIVAL
   ======================================================== */

.arrival-card {
    opacity:0;

    margin-top:15px;

    padding:18px;

    text-align:center;

    border-radius:20px;

    background:rgba(255,255,255,.92);

    color:#111;

    box-shadow:
        0 0 30px rgba(255,181,219,.35);

    animation:
        arrivalReveal 1s ease forwards;

    animation-delay:5.5s;
}


@keyframes arrivalReveal {

    from {
        opacity:0;
        transform:scale(.9);
    }

    to {
        opacity:1;
        transform:scale(1);
    }
}


.arrival-pin {
    font-size:26px;
}


.arrival-title {
    margin-top:5px;

    font-size:21px;
    font-weight:900;

    letter-spacing:1px;

    color:#111 !important;
}


.arrival-home {
    margin-top:10px;

    color:#b34f83 !important;

    font-size:17px;
    font-weight:700;
}


.arrival-location {
    margin-top:3px;

    color:#555 !important;

    font-size:12px;
}


/* ========================================================
   FINAL ALEXA MESSAGES
   ======================================================== */

.alexa-final-message {
    opacity:0;

    width:fit-content;
    max-width:78%;

    margin-top:14px;

    padding:10px 14px;

    border-radius:18px 18px 18px 5px;

    background:#eeeeee;

    color:#111 !important;

    animation:
        finalMessage .8s ease forwards;
}


.first-final-message {
    animation-delay:6.7s;
}


.second-final-message {
    animation-delay:7.8s;
}


@keyframes finalMessage {

    from {
        opacity:0;
        transform:translateY(8px);
    }

    to {
        opacity:1;
        transform:translateY(0);
    }
}


/* ========================================================
   INFINITY LOCK ENDING
   ======================================================== */

.infinity-ending {
    opacity:0;

    margin-top:25px;

    padding:24px 15px;

    text-align:center;

    border-radius:24px;

    background:
        radial-gradient(
            circle,
            rgba(255,183,219,.24),
            rgba(20,16,40,.75)
        );

    box-shadow:
        0 0 35px rgba(255,171,214,.25);

    animation:
        infinityReveal 1.2s ease forwards;

    animation-delay:9s;
}


@keyframes infinityReveal {

    from {
        opacity:0;
        transform:scale(.85);
    }

    to {
        opacity:1;
        transform:scale(1);
    }
}


.ending-small {
    color:#f1d5e4 !important;

    font-size:13px;
}


.ending-symbol {
    margin-top:12px;

    font-size:42px;

    animation:
        infinityPulse 1.6s ease-in-out infinite;
}


@keyframes infinityPulse {

    0%,
    100% {
        transform:scale(1);
    }

    50% {
        transform:scale(1.14);
    }
}


.ending-points {
    margin-top:12px;

    color:#ffc1df !important;

    font-weight:700;
}


.ending-title {
    margin-top:22px;

    font-size:26px;
    font-weight:900;

    letter-spacing:4px;

    color:white !important;
}


.ending-thanks {
    margin-top:12px;

    font-size:13px;

    color:#e8d6e1 !important;
}


/* ========================================================
   FLOATING ENDING HEARTS
   ======================================================== */

.ending-heart {
    position:absolute;

    bottom:-30px;

    color:#ffc1df !important;

    font-size:20px;

    opacity:0;

    animation:
        endingHeartFloat 5s ease-in infinite;
}


.eh1 {
    left:10%;
    animation-delay:8.5s;
}

.eh2 {
    left:28%;
    animation-delay:9.2s;
}

.eh3 {
    left:48%;
    animation-delay:8.8s;
}

.eh4 {
    left:68%;
    animation-delay:9.5s;
}

.eh5 {
    left:86%;
    animation-delay:9s;
}


@keyframes endingHeartFloat {

    0% {
        opacity:0;
        transform:translateY(0) scale(.7);
    }

    15% {
        opacity:.9;
    }

    100% {
        opacity:0;
        transform:translateY(-500px) scale(1.2);
    }
}


@keyframes finalFade {

    from {
        opacity:0;
    }

    to {
        opacity:1;
    }
}

"""

def handle_maps_choice(choice):

    result_style = """
        background:#eeeeee;
        color:#111;
        padding:10px 14px;
        border-radius:18px;
        margin-top:18px;
        margin-bottom:12px;
        line-height:1.5;
    """

    if choice == "🚗 Drive":

        result = f"""
        <div style="{result_style}">
            🚗 <strong>Driving route selected.</strong>
            <br>
            Estimated travel time: disgusting.
            <br>
            Alexa: hurry tf up 🥀
        </div>
        """


    elif choice == "🚀 Aerospace Engineer":

        result = f"""
        <div style="{result_style}">
            🚀 <strong>Aerospace Engineer selected.</strong>
            <br>
            Okay Futuluhtoogan.
            <br>
            Figure it out bro 😭
            <br><br>
            +5 Engineering
            <br>
            +10 Confusion
        </div>
        """


    elif choice == "🧗 Climb":

        result = f"""
        <div style="{result_style}">
            🧗 <strong>Climbing route selected.</strong>
            <br>
            Route grade: V∞
            <br>
            First hold: approximately 2,000 miles away.
            <br>
            Maybe find different beta 😭
        </div>
        """


    elif choice == "🏃 Run":

        result = f"""
        <div style="{result_style}">
            🏃 <strong>Running route selected.</strong>
            <br>
            Estimated arrival: eventually.
            <br>
            Nyx and Dusty will have forgotten u by then :(
        </div>
        """


    elif choice == "✈️ Fly":

        result = f"""
        <div style="{result_style}">
            ✈️ <strong>Flight selected.</strong>
            <br>
            ...
            <br>
            wow.
            <br>
            a reasonable fucking decision 😭
            <br>
            Destination: Alexa ♡
        </div>
        """


    else:

        result = f"""
        <div style="{result_style}">
            Maps has absolutely no idea where you're trying to go 😭
        </div>
        """


    return result

maps_animation_css = """

/* ========================================================
   MAPS MAIN SCREEN
   ======================================================== */

.maps-main-screen {
    max-width:390px;
    min-height:520px;
    margin:0 auto;
    padding:20px;
    border-radius:28px;

    background:
        linear-gradient(
            180deg,
            #111a32,
            #25395b,
            #4a4069
        );

    color:white;
}

.maps-title {
    text-align:center;
    font-size:20px;
    font-weight:700;
    margin-bottom:20px;
    color:white;
}


/* ========================================================
   LOCATION CARDS
   ======================================================== */

.maps-location-card {
    background:rgba(255,255,255,.92);
    color:#111;
    padding:14px;
    border-radius:18px;

    box-shadow:
        0 6px 18px rgba(0,0,0,.15);
}

.maps-location-heading {
    font-size:12px;
    font-weight:700;
    color:#666;
    margin-bottom:5px;
}

.maps-location-value {
    font-size:18px;
    font-weight:700;
    color:#111;
}

.maps-location-sub {
    margin-top:3px;
    font-size:12px;
    color:#555;
}

.destination-card {
    box-shadow:
        0 0 20px rgba(255,174,215,.23);
}

.maps-destination-arrow {
    text-align:center;
    padding:8px 0;
    font-size:24px;
    color:#ffc2df;

    animation:
        mapsArrowBounce 1.2s ease-in-out infinite;
}

@keyframes mapsArrowBounce {
    0%,
    100% {
        transform:translateY(0);
    }

    50% {
        transform:translateY(5px);
    }
}


/* ========================================================
   CALCULATING DOTS
   ======================================================== */

.maps-calculating {
    text-align:center;
    margin-top:20px;
    color:#e5e8ff;
    font-size:13px;
}

.maps-calculating span {
    display:inline-block;
    animation:mapsDot 1.3s infinite;
    opacity:.2;
}

.maps-calculating span:nth-child(2) {
    animation-delay:.2s;
}

.maps-calculating span:nth-child(3) {
    animation-delay:.4s;
}

@keyframes mapsDot {
    0%,
    100% {
        opacity:.2;
        transform:translateY(0);
    }

    50% {
        opacity:1;
        transform:translateY(-3px);
    }
}

.maps-route-found {
    margin-top:8px;
    text-align:center;
    color:#ffc2df;
    font-weight:700;
    font-size:13px;
}


/* ========================================================
   ROUTE ANIMATION
   ======================================================== */

.maps-animation-box {
    position:relative;
    height:120px;
    margin-top:25px;
    overflow:hidden;
    border-radius:20px;

    background:
        linear-gradient(
            180deg,
            rgba(255,255,255,.08),
            rgba(255,255,255,.03)
        );
}

.maps-route-line {
    position:absolute;
    left:35px;
    right:35px;
    top:58px;
    height:3px;
    border-radius:999px;

    background:
        repeating-linear-gradient(
            90deg,
            #d996bd 0,
            #d996bd 8px,
            transparent 8px,
            transparent 15px
        );

    opacity:.7;

    animation:
        mapsRoutePulse 1.4s ease-in-out infinite;
}

@keyframes mapsRoutePulse {
    0%,
    100% {
        opacity:.35;
    }

    50% {
        opacity:1;
    }
}


/* ========================================================
   START + DESTINATION
   ======================================================== */

.maps-start-pin,
.maps-end-pin {
    position:absolute;
    top:35px;
    font-size:27px;
    z-index:3;
}

.maps-start-pin {
    left:22px;
}

.maps-end-pin {
    right:22px;
    color:#ffc0df;

    animation:
        mapsHeartBounce 1.1s ease-in-out infinite;
}

@keyframes mapsHeartBounce {
    0%,
    100% {
        transform:scale(1);
    }

    50% {
        transform:scale(1.25);
    }
}

.maps-location-label {
    position:absolute;
    top:34px;
    left:50%;
    transform:translateX(-50%);
    white-space:nowrap;
    font-size:10px;
    color:#fff;
}


/* ========================================================
   MOVING VEHICLE
   ======================================================== */

.maps-travel-icon {
    position:absolute;
    left:38px;
    top:36px;
    z-index:4;
    font-size:30px;

    animation:
        mapsTravel 5s ease-in-out infinite;
}

@keyframes mapsTravel {
    0% {
        left:38px;
        transform:translateY(0) rotate(0deg);
    }

    20% {
        transform:translateY(-6px) rotate(-3deg);
    }

    50% {
        transform:translateY(4px) rotate(2deg);
    }

    80% {
        transform:translateY(-3px) rotate(-2deg);
    }

    100% {
        left:290px;
        transform:translateY(0) rotate(0deg);
    }
}


/* ========================================================
   DISTANCE PROGRESS
   ======================================================== */

.maps-distance-box {
    margin-top:20px;
}

.maps-distance-title {
    text-align:center;
    color:white;
    font-size:12px;
    margin-bottom:9px;
}

.maps-progress-track {
    position:relative;
    height:12px;
    border-radius:999px;
    overflow:visible;
    background:rgba(255,255,255,.15);
}

.maps-progress-fill {
    position:absolute;
    left:0;
    top:0;
    height:100%;
    border-radius:999px;

    background:
        linear-gradient(
            90deg,
            #8e6eb3,
            #d98db9,
            #ffc2df
        );

    animation:
        mapsProgress 5s ease-in-out infinite;
}

@keyframes mapsProgress {
    0% {
        width:5%;
    }

    100% {
        width:100%;
    }
}

.maps-progress-heart {
    position:absolute;
    right:-5px;
    top:-10px;
    font-size:23px;
    color:#ffc2df;

    text-shadow:
        0 0 8px rgba(255,166,213,.6);
}

.maps-distance-text {
    text-align:center;
    margin-top:9px;
    font-size:11px;
    color:#d9dced;
}

"""


def build_maps_route_result(route_choice, start_choice):

    route_result = handle_maps_choice(route_choice)

    icon_map = {
        "🚗 Drive": "🚗",
        "🚀 Aerospace Engineer": "🚀",
        "🧗 Climb": "🧗",
        "🏃 Run": "🏃",
        "✈️ Fly": "✈️"
    }

    travel_icon = icon_map.get(route_choice, "♡")

    if start_choice == "Not yet":

        return f"""
        <div class="maps-main-screen">

            <div class="maps-title">
                🗺️ Maps
            </div>

            {route_result}

            <div style="
                background:#eeeeee;
                color:#111;
                padding:12px 14px;
                border-radius:18px;
                margin-top:18px;
                line-height:1.5;
            ">
                Alexa: NOT YET???
                <br>
                Alexa: bro COME HOME 😭
            </div>

        </div>
        """

    elif start_choice == "Start":

        return f"""
        <div class="maps-finale-screen">

            <div class="maps-title">
                🗺️ Maps
            </div>

            {route_result}

            <div class="final-route-message">
                Starting route to Alexa ♡
            </div>

            <div class="final-route-animation">

                <div class="final-route-line"></div>

                <div class="final-start">
                    📍
                </div>

                <div class="final-moving-icon">
                    {travel_icon}
                </div>

                <div class="final-home">
                    ♡
                </div>

            </div>

            <div class="final-distance">

                <div class="distance-step d1">
                    ██████████ &nbsp; too far
                </div>

                <div class="distance-step d2">
                    ████████░░ &nbsp; getting closer...
                </div>

                <div class="distance-step d3">
                    ██████░░░░
                </div>

                <div class="distance-step d4">
                    ████░░░░░░
                </div>

                <div class="distance-step d5">
                    ██░░░░░░░░
                </div>

                <div class="distance-step d6">
                    ♡
                </div>

            </div>

            <div class="arrival-card">

                <div class="arrival-pin">
                    📍
                </div>

                <div class="arrival-title">
                    YOU HAVE ARRIVED
                </div>

                <div class="arrival-home">
                    ♡ Home
                </div>

                <div class="arrival-location">
                    Alexa · San Diego, CA
                </div>

            </div>

            <div class="alexa-final-message first-final-message">
                told you i'd be waiting :)
            </div>

            <div class="alexa-final-message second-final-message">
                i love you
            </div>

            <div class="infinity-ending">

                <div class="ending-small">
                    nuff nuff infinity lock.
                </div>

                <div class="ending-symbol">
                    🔒 ♾️
                </div>

                <div class="ending-points">
                    ♡ +∞ Boyfriend Points
                </div>

                <div class="ending-title">
                    INFINITY LOCK
                </div>

                <div class="ending-thanks">
                    Thanks for playing, Futuluhtoogan ♡
                </div>

            </div>

            <div class="ending-heart eh1">♡</div>
            <div class="ending-heart eh2">♥</div>
            <div class="ending-heart eh3">♡</div>
            <div class="ending-heart eh4">♥</div>
            <div class="ending-heart eh5">♡</div>

        </div>
        """

    return build_maps_screen(route_choice, route_result)


# =========================================================
# INFINITY LOCK — FULL MAIN APP
# Alexa + Unknown + LinkedIn + Calendar + Reminders + Maps
# =========================================================


combined_css = """

/* ========================================================
   PHONE
   ======================================================== */

.infinity-phone {
    position: relative !important;
    overflow: hidden !important;

    max-width: 390px !important;
    min-height: 760px !important;

    margin: 25px auto !important;
    padding: 28px 18px !important;

    border: 7px solid #171717 !important;
    border-radius: 48px !important;

    background:
        radial-gradient(
            circle at 72% 12%,
            rgba(255,198,225,.30) 0%,
            rgba(171,118,202,.13) 18%,
            transparent 34%
        ),
        linear-gradient(
            180deg,
            #0e1530 0%,
            #1c2145 30%,
            #3b315c 58%,
            #7a4c72 78%,
            #b36d86 100%
        ) !important;

    box-shadow:
        0 25px 60px rgba(0,0,0,.45) !important;
}


/* ========================================================
   WALLPAPER
   ======================================================== */

#wallpaper_host {
    position: absolute !important;
    inset: 0 !important;

    width: 100% !important;
    height: 100% !important;

    margin: 0 !important;
    padding: 0 !important;

    background: transparent !important;
    border: none !important;

    pointer-events: none !important;

    overflow: hidden !important;

    z-index: 0 !important;
}

#wallpaper_host .wallpaper-layer {
    position: absolute !important;
    inset: 0 !important;

    width: 100% !important;
    height: 100% !important;
}

.infinity-phone > *:not(#wallpaper_host) {
    position: relative;
    z-index: 10;
}


/* ========================================================
   MOON
   ======================================================== */

.game-moon {
    position: absolute;

    top: 42px;
    right: 42px;

    width: 44px;
    height: 44px;

    border-radius: 50%;

    background: #ffd2a8;

    box-shadow:
        0 0 16px rgba(255,201,160,.45);

    z-index: 1;
}

.game-moon::after {
    content: "";

    position: absolute;

    width: 38px;
    height: 38px;

    left: 14px;
    top: -3px;

    border-radius: 50%;

    background: #11172f;
}


/* ========================================================
   STARS
   ======================================================== */

.game-star {
    position: absolute;

    color: #ffc1dd;

    font-size: 15px;

    opacity: .9;

    text-shadow:
        0 0 8px rgba(255,177,220,.65);

    z-index: 1;
}

.gs1 { top:70px; left:35px; }
.gs2 { top:120px; left:80px; }
.gs3 { top:155px; right:95px; }
.gs4 { top:215px; left:52px; }
.gs5 { top:255px; right:55px; }


/* ========================================================
   CITY
   ======================================================== */

.game-city-back {
    position:absolute;

    left:0;
    right:0;
    bottom:82px;

    height:180px;

    background:#161a35;

    z-index:0;

    clip-path:polygon(
        0% 50%,
        7% 50%,
        7% 25%,
        14% 25%,
        14% 58%,
        22% 58%,
        22% 18%,
        31% 18%,
        31% 45%,
        40% 45%,
        40% 28%,
        48% 28%,
        48% 62%,
        57% 62%,
        57% 20%,
        66% 20%,
        66% 48%,
        75% 48%,
        75% 12%,
        84% 12%,
        84% 38%,
        92% 38%,
        92% 24%,
        100% 24%,
        100% 100%,
        0% 100%
    );
}


.game-city-front {
    position:absolute;

    left:0;
    right:0;
    bottom:0;

    height:125px;

    background:#080d20;

    z-index:1;

    clip-path:polygon(
        0% 30%,
        12% 30%,
        12% 10%,
        24% 10%,
        24% 42%,
        37% 42%,
        37% 18%,
        50% 18%,
        50% 35%,
        65% 35%,
        65% 8%,
        78% 8%,
        78% 28%,
        90% 28%,
        90% 15%,
        100% 15%,
        100% 100%,
        0% 100%
    );
}


/* ========================================================
   WINDOWS
   ======================================================== */

.city-window {
    position:absolute;

    width:5px;
    height:8px;

    background:#f3a6c8;

    opacity:.75;

    box-shadow:
        0 0 5px rgba(243,166,200,.5);

    z-index:2;
}

.gw1 { bottom:102px; left:38px; }
.gw2 { bottom:118px; left:84px; }
.gw3 { bottom:90px; left:135px; }
.gw4 { bottom:120px; right:105px; }
.gw5 { bottom:98px; right:50px; }
.gw6 { bottom:140px; right:155px; }


/* ========================================================
   RAIN
   ======================================================== */

.game-rain {
    position:absolute;
    inset:0;

    overflow:hidden;

    z-index:2;
}

.game-drop {
    position:absolute;

    width:2px;
    height:10px;

    background:rgba(210,225,255,.55);

    animation:gameRain 2.5s linear infinite;
}

.gd1 { left:8%; animation-delay:0s; }
.gd2 { left:20%; animation-delay:.6s; }
.gd3 { left:35%; animation-delay:1.2s; }
.gd4 { left:52%; animation-delay:.3s; }
.gd5 { left:68%; animation-delay:1.5s; }
.gd6 { left:82%; animation-delay:.9s; }
.gd7 { left:93%; animation-delay:1.8s; }

@keyframes gameRain {
    0% {
        top:-20px;
        opacity:0;
    }

    15% {
        opacity:.7;
    }

    100% {
        top:780px;
        opacity:0;
    }
}


/* ========================================================
   HEARTS
   ======================================================== */

.game-heart {
    position:absolute;

    bottom:25px;

    color:#ffb6d9;

    font-size:18px;

    text-shadow:
        0 0 8px rgba(255,160,210,.7);

    animation:gameHeart 6s ease-in infinite;

    z-index:3;
}

.gh1 { left:20%; animation-delay:0s; }
.gh2 { left:48%; animation-delay:2s; }
.gh3 { left:75%; animation-delay:4s; }

@keyframes gameHeart {
    0% {
        transform:translateY(0) scale(.7);
        opacity:0;
    }

    15% {
        opacity:.8;
    }

    70% {
        opacity:.6;
    }

    100% {
        transform:translateY(-280px) scale(1.1);
        opacity:0;
    }
}


/* ========================================================
   CAT GROUND
   ======================================================== */

.game-cat-ground {
    position:absolute;

    left:22px;
    right:22px;
    bottom:22px;

    height:62px;

    border-radius:12px;

    background:
        linear-gradient(
            180deg,
            #252346,
            #14172f
        );

    box-shadow:
        inset 0 3px 0 rgba(255,255,255,.04),
        0 -5px 20px rgba(0,0,0,.18);

    z-index:2;
}


/* ========================================================
   NYX
   ======================================================== */

.game-nyx {
    position:absolute;

    bottom:40px;
    left:-150px;

    width:118px;
    height:auto;

    image-rendering:pixelated;

    z-index:4;

    animation:gameNyxWalk 18s linear infinite;
}

@keyframes gameNyxWalk {
    0% {
        left:-150px;
        transform:scaleX(1);
    }

    45% {
        left:300px;
        transform:scaleX(1);
    }

    50% {
        left:300px;
        transform:scaleX(-1);
    }

    95% {
        left:-150px;
        transform:scaleX(-1);
    }

    100% {
        left:-150px;
        transform:scaleX(1);
    }
}


/* ========================================================
   DUSTY
   ======================================================== */

.game-dusty {
    position:absolute;

    bottom:40px;
    left:-55px;

    width:118px;
    height:auto;

    image-rendering:pixelated;

    z-index:4;

    animation:gameDustyWalk 18s linear infinite;
}

@keyframes gameDustyWalk {
    0% {
        left:-55px;
        transform:scaleX(1);
    }

    45% {
        left:395px;
        transform:scaleX(1);
    }

    50% {
        left:395px;
        transform:scaleX(-1);
    }

    95% {
        left:-55px;
        transform:scaleX(-1);
    }

    100% {
        left:-55px;
        transform:scaleX(1);
    }
}


/* ========================================================
   NOTIFICATIONS
   ======================================================== */

.lock-notification,
.extra-notification {
    width:100% !important;

    min-height:0 !important;
    height:auto !important;

    margin:0 0 8px 0 !important;
    padding:9px 13px !important;

    border:none !important;
    border-radius:18px !important;

    background:rgba(245,245,250,.82) !important;

    box-shadow:
        0 4px 12px rgba(0,0,0,.12) !important;

    color:#111 !important;

    text-align:left !important;

    white-space:pre-line !important;

    display:flex !important;
    align-items:flex-start !important;
    justify-content:flex-start !important;

    font-size:13px !important;
    line-height:1.3 !important;

    opacity:1 !important;
}


.lock-notification span,
.extra-notification span {
    display:block !important;

    width:100% !important;

    margin:0 !important;
    padding:0 !important;

    color:#111 !important;

    white-space:pre-line !important;

    text-align:left !important;

    font-size:13px !important;
    line-height:1.3 !important;
}


#alexa_game_notification:hover,
#unknown_game_notification:hover,
#linkedin_game_notification:hover,
#calendar_notification:hover,
#reminders_notification:hover,
#maps_notification:hover {
    background:rgba(255,255,255,.94) !important;

    transform:scale(1.01);
}


/* Keep disabled Maps visible */

#maps_notification {
    opacity:1 !important;
    filter:none !important;
}


/* ========================================================
   SEE MORE
   ======================================================== */

#show_more_button {
    width:fit-content !important;

    margin:5px auto 9px auto !important;

    padding:7px 14px !important;

    border-radius:16px !important;

    border:none !important;

    background:rgba(20,22,45,.68) !important;

    color:white !important;

    font-size:12px !important;
    font-weight:600 !important;
}


/* ========================================================
   INNER PHONE SCREENS
   ======================================================== */

.alexa-game-screen,
.unknown-game-screen,
.linkedin-game-screen,
.calendar-game-screen,
.reminders-game-screen,
.maps-game-screen {
    max-width:390px !important;

    min-height:700px !important;

    margin:25px auto !important;
    padding:22px 18px !important;

    border:7px solid #171717 !important;
    border-radius:48px !important;

    background:
        linear-gradient(
            180deg,
            #11172f,
            #262348,
            #49375e
        ) !important;

    box-shadow:
        0 25px 60px rgba(0,0,0,.45) !important;

    overflow:hidden !important;
}


/* ========================================================
   APP BUTTONS
   ======================================================== */

#alexa_back_button,
#unknown_back_button,
#linkedin_back_button,
#calendar_back_button,
#reminders_back_button,
#maps_back_button {
    border:none !important;

    border-radius:18px !important;

    background:rgba(255,255,255,.10) !important;

    color:white !important;
}


#alexa_send_button,
#unknown_send_button,
#linkedin_send_button,
#calendar_check_button,
#reminders_check_button,
#maps_action_button {
    border:none !important;

    border-radius:18px !important;

    background:#b56fa0 !important;

    color:white !important;
}


#restart_button,
#linkedin_restart_button,
#maps_restart_button {
    border:none !important;

    border-radius:18px !important;

    background:#8d1f3f !important;

    color:white !important;

    font-weight:700 !important;
}


.points-box,
.points-box * {
    color:#ffc0dd !important;
}


/* ========================================================
   DEATH SHAKE
   ======================================================== */

@keyframes deathShake {
    0% { transform:translateX(0); }
    25% { transform:translateX(-7px); }
    50% { transform:translateX(7px); }
    75% { transform:translateX(-4px); }
    100% { transform:translateX(0); }
}

"""


# =========================================================
# WALLPAPER HTML
# =========================================================

wallpaper_html = f"""
<div class="wallpaper-layer">

    <div class="game-moon"></div>

    <div class="game-star gs1">✦</div>
    <div class="game-star gs2">♡</div>
    <div class="game-star gs3">✦</div>
    <div class="game-star gs4">♡</div>
    <div class="game-star gs5">✦</div>

    <div class="game-city-back"></div>
    <div class="game-city-front"></div>

    <div class="city-window gw1"></div>
    <div class="city-window gw2"></div>
    <div class="city-window gw3"></div>
    <div class="city-window gw4"></div>
    <div class="city-window gw5"></div>
    <div class="city-window gw6"></div>

    <div class="game-rain">
        <div class="game-drop gd1"></div>
        <div class="game-drop gd2"></div>
        <div class="game-drop gd3"></div>
        <div class="game-drop gd4"></div>
        <div class="game-drop gd5"></div>
        <div class="game-drop gd6"></div>
        <div class="game-drop gd7"></div>
    </div>

    <div class="game-heart gh1">♡</div>
    <div class="game-heart gh2">♥</div>
    <div class="game-heart gh3">♡</div>

    <div class="game-cat-ground"></div>

    <img src="{nyx_image}" class="game-nyx">
    <img src="{dusty_image}" class="game-dusty">

</div>
"""


# =========================================================
# LOCK HEADER
# =========================================================

lock_header_html = """
<div style="
    position:relative;
    z-index:20;
    text-align:center;
    color:white;
">

    <div style="
        font-size:58px;
        font-weight:300;
        line-height:1;
        color:white;
    ">
        11:47
    </div>

    <div style="
        margin-top:10px;
        margin-bottom:18px;
        font-size:18px;
        color:white;
    ">
        Saturday, September 12
    </div>

    <div style="
        margin-bottom:24px;
        font-size:15px;
        color:white;
    ">
        🌧️ Sad & Rainy Without U

        <br>

        <span style="
            font-size:13px;
            color:white;
        ">
            Chance of missing Alexa: 100%
        </span>

    </div>

</div>
"""


# =========================================================
# UNKNOWN INITIAL
# =========================================================

unknown_initial_html = """
<div style="
    max-width:390px;
    margin:0 auto;
    padding:20px;
    min-height:520px;

    border-radius:28px;

    background:
        linear-gradient(
            180deg,
            #151a36,
            #3b315c
        );

    color:white;
">

    <div style="
        text-align:center;
        font-weight:bold;
        margin-bottom:20px;
        color:white;
    ">
        Unknown
    </div>

    <div style="
        background:#eeeeee;
        color:#111;

        padding:10px 14px;

        border-radius:18px 18px 18px 5px;

        width:fit-content;
        max-width:75%;

        margin-bottom:12px;
    ">
        heyyy :)
    </div>

    <div style="
        background:#eeeeee;
        color:#111;

        padding:10px 14px;

        border-radius:18px 18px 18px 5px;

        width:fit-content;
        max-width:75%;

        margin-bottom:12px;
    ">
        you're cute, are you single?
    </div>

</div>
"""


# =========================================================
# MAIN APP
# =========================================================

with gr.Blocks() as infinity_lock_app:

    # =====================================================
    # STATES
    # =====================================================

    stage_state = gr.State("opening")
    conversation_state = gr.State("")

    boyfriend_state = gr.State(0)
    infinity_state = gr.State(0)

    nyxie_trust_state = gr.State(0)
    dusty_trust_state = gr.State(0)

    unknown_opened_state = gr.State(False)

    linkedin_stage_state = gr.State("main")
    linkedin_history_state = gr.State("")
    linkedin_opened_state = gr.State(False)

    calendar_opened_state = gr.State(False)
    reminders_opened_state = gr.State(False)

    maps_stage_state = gr.State("route")
    maps_route_state = gr.State(None)
    maps_opened_state = gr.State(False)


    # =====================================================
    # LOCK SCREEN
    # =====================================================

    with gr.Column(
        visible=True,
        elem_classes="infinity-phone"
    ) as lock_screen:

        gr.HTML(
            wallpaper_html,
            elem_id="wallpaper_host"
        )

        gr.HTML(
            lock_header_html
        )


        alexa_notification = gr.Button(
            "💬 Alexa · now\ni miss you :(",
            elem_id="alexa_game_notification",
            elem_classes="lock-notification"
        )


        unknown_notification = gr.Button(
            "💌 Unknown · 1m\nheyyy :)",
            elem_id="unknown_game_notification",
            elem_classes="lock-notification"
        )


        linkedin_notification = gr.Button(
            "💼 LinkedIn · 4m\nNew position recommended for you\n📍 San Diego, CA",
            elem_id="linkedin_game_notification",
            elem_classes="lock-notification"
        )


        show_more_button = gr.Button(
            "↓ See 3 More Notifications",
            elem_id="show_more_button"
        )


        with gr.Column(
            visible=False
        ) as extra_notifications:

            calendar_notification = gr.Button(
                "📅 Calendar · 8m\nGo see your girlfriend — OVERDUE",
                elem_id="calendar_notification",
                elem_classes="extra-notification"
            )


            reminders_notification = gr.Button(
                "⏰ Reminders · 11m\nCALL ALEXA ‼️",
                elem_id="reminders_notification",
                elem_classes="extra-notification"
            )


            # Starts locked
            maps_notification = gr.Button(
                "🗺️ Maps\nRoute unavailable",
                elem_id="maps_notification",
                elem_classes="extra-notification",
                interactive=False
            )


    # =====================================================
    # ALEXA SCREEN
    # =====================================================

    with gr.Column(
        visible=False,
        elem_classes="alexa-game-screen"
    ) as alexa_screen:

        alexa_back_button = gr.Button(
            "‹ Back",
            elem_id="alexa_back_button"
        )

        gr.Markdown(
            "### Alexa ♡"
        )

        conversation_display = gr.HTML(
            build_alexa_conversation()
        )

        choice_selector = gr.Radio(
            choices=get_alexa_choices("opening"),
            label="How do you reply?"
        )

        alexa_send_button = gr.Button(
            "Send",
            elem_id="alexa_send_button"
        )

        boyfriend_display = gr.Markdown(
            "Boyfriend Points: 0 ♡",
            elem_classes="points-box"
        )

        infinity_display = gr.Markdown(
            "Infinity Points: 0 🔒",
            elem_classes="points-box"
        )


    # =====================================================
    # UNKNOWN SCREEN
    # =====================================================

    with gr.Column(
        visible=False,
        elem_classes="unknown-game-screen"
    ) as unknown_screen:

        unknown_back_button = gr.Button(
            "‹ Back",
            elem_id="unknown_back_button"
        )

        unknown_conversation = gr.HTML(
            unknown_initial_html
        )

        unknown_choice = gr.Radio(
            choices=[
                "reply something mean",
                "flirt back",
                "block her and immediately send everything to Alexa",
                "leave her on read"
            ],
            label="What do you do?"
        )

        unknown_send_button = gr.Button(
            "Choose",
            elem_id="unknown_send_button"
        )

        unknown_points_display = gr.Markdown(
            "Boyfriend Points: 0 ♡",
            elem_classes="points-box"
        )

        restart_button = gr.Button(
            "↻ START OVER",
            elem_id="restart_button",
            visible=False
        )

        unknown_continue_button = gr.Button(
            "← Back to Phone",
            visible=False
        )


    # =====================================================
    # LINKEDIN SCREEN
    # =====================================================

    with gr.Column(
        visible=False,
        elem_classes="linkedin-game-screen"
    ) as linkedin_screen:

        linkedin_back_button = gr.Button(
            "‹ Back",
            elem_id="linkedin_back_button"
        )

        linkedin_conversation = gr.HTML(
            build_linkedin_screen()
        )

        linkedin_choice = gr.Radio(
            choices=get_linkedin_choices("main"),
            label="What do you do?"
        )

        linkedin_send_button = gr.Button(
            "Choose",
            elem_id="linkedin_send_button"
        )

        linkedin_points_display = gr.Markdown(
            "Boyfriend Points: 0 ♡",
            elem_classes="points-box"
        )

        linkedin_restart_button = gr.Button(
            "↻ START OVER",
            elem_id="linkedin_restart_button",
            visible=False
        )

        linkedin_continue_button = gr.Button(
            "← Back to Phone",
            visible=False
        )


    # =====================================================
    # CALENDAR SCREEN
    # =====================================================

    with gr.Column(
        visible=False,
        elem_classes="calendar-game-screen"
    ) as calendar_screen:

        calendar_back_button = gr.Button(
            "‹ Back",
            elem_id="calendar_back_button"
        )

        calendar_display = gr.HTML(
            build_calendar_screen()
        )

        calendar_check_button = gr.Button(
            "✓ Check Schedule",
            elem_id="calendar_check_button"
        )

        calendar_points_display = gr.Markdown(
            "Boyfriend Points: 0 ♡",
            elem_classes="points-box"
        )

        calendar_continue_button = gr.Button(
            "← Back to Phone",
            visible=False
        )


    # =====================================================
    # REMINDERS SCREEN
    # =====================================================

    with gr.Column(
        visible=False,
        elem_classes="reminders-game-screen"
    ) as reminders_screen:

        reminders_back_button = gr.Button(
            "‹ Back",
            elem_id="reminders_back_button"
        )

        reminders_display = gr.HTML(
            build_reminders_screen()
        )

        reminder_choice = gr.Radio(
            choices=get_reminder_choices(),
            label="Choose a reminder:"
        )

        reminders_check_button = gr.Button(
            "Complete Reminder",
            elem_id="reminders_check_button"
        )

        reminder_trust_display = gr.Markdown(
            """
Nyxie Trust: 0 🐈
Dusty Trust: 0 🤍
            """,
            elem_classes="points-box"
        )

        reminders_continue_button = gr.Button(
            "← Back to Phone",
            visible=False
        )


    # =====================================================
    # MAPS SCREEN
    # =====================================================

    with gr.Column(
        visible=False,
        elem_classes="maps-game-screen"
    ) as maps_screen:

        maps_back_button = gr.Button(
            "‹ Back",
            elem_id="maps_back_button"
        )

        maps_display = gr.HTML(
            build_maps_screen()
        )

        maps_choice = gr.Radio(
            choices=get_maps_choices(),
            label="How are you getting to Alexa?"
        )

        maps_action_button = gr.Button(
            "Use This Route",
            elem_id="maps_action_button",
            visible=False
        )

        maps_restart_button = gr.Button(
            "↻ PLAY AGAIN ♡",
            elem_id="maps_restart_button",
            visible=False
        )


    # =====================================================
    # SHOW EXTRA NOTIFICATIONS
    # =====================================================

    def show_extra_notifications():

        return (
            gr.update(visible=True),
            gr.update(value="↑ Show Less")
        )


    show_more_button.click(
        fn=show_extra_notifications,

        inputs=[],

        outputs=[
            extra_notifications,
            show_more_button
        ]
    )


    # =====================================================
    # SCREEN NAVIGATION
    # =====================================================

    def show_screen(which):

        return (
            gr.update(visible=(which == "lock")),
            gr.update(visible=(which == "alexa")),
            gr.update(visible=(which == "unknown")),
            gr.update(visible=(which == "linkedin")),
            gr.update(visible=(which == "calendar")),
            gr.update(visible=(which == "reminders")),
            gr.update(visible=(which == "maps"))
        )


    navigation_outputs = [
        lock_screen,
        alexa_screen,
        unknown_screen,
        linkedin_screen,
        calendar_screen,
        reminders_screen,
        maps_screen
    ]


    alexa_notification.click(
        fn=lambda: show_screen("alexa"),
        inputs=[],
        outputs=navigation_outputs
    )


    unknown_notification.click(
        fn=lambda: show_screen("unknown"),
        inputs=[],
        outputs=navigation_outputs
    )


    linkedin_notification.click(
        fn=lambda: show_screen("linkedin"),
        inputs=[],
        outputs=navigation_outputs
    )


    calendar_notification.click(
        fn=lambda: show_screen("calendar"),
        inputs=[],
        outputs=navigation_outputs
    )


    reminders_notification.click(
        fn=lambda: show_screen("reminders"),
        inputs=[],
        outputs=navigation_outputs
    )


    maps_notification.click(
        fn=lambda: show_screen("maps"),
        inputs=[],
        outputs=navigation_outputs
    )


    # =====================================================
    # MAPS UNLOCK CHECK
    # =====================================================

    def maps_is_unlocked(
        alexa_stage,
        unknown_done,
        linkedin_done,
        calendar_done,
        reminders_done
    ):

        return (
            alexa_stage == "complete"
            and unknown_done
            and linkedin_done
            and calendar_done
            and reminders_done
        )


    # =====================================================
    # RETURN TO LOCK + REFRESH MAPS
    # =====================================================

    def back_to_lock_and_refresh(
        alexa_stage,
        unknown_done,
        linkedin_done,
        calendar_done,
        reminders_done
    ):

        unlocked = maps_is_unlocked(
            alexa_stage,
            unknown_done,
            linkedin_done,
            calendar_done,
            reminders_done
        )


        if unlocked:

            maps_update = gr.update(
                value="🗺️ Maps\n♡ ROUTE READY — Alexa · Home",
                interactive=True
            )

        else:

            maps_update = gr.update(
                value="🗺️ Maps\nRoute unavailable",
                interactive=False
            )


        return (
            gr.update(visible=True),
            gr.update(visible=False),
            gr.update(visible=False),
            gr.update(visible=False),
            gr.update(visible=False),
            gr.update(visible=False),
            gr.update(visible=False),
            maps_update
        )


    back_inputs = [
        stage_state,
        unknown_opened_state,
        linkedin_opened_state,
        calendar_opened_state,
        reminders_opened_state
    ]


    back_outputs = [
        lock_screen,
        alexa_screen,
        unknown_screen,
        linkedin_screen,
        calendar_screen,
        reminders_screen,
        maps_screen,
        maps_notification
    ]


    for back_button in [
        alexa_back_button,
        unknown_back_button,
        unknown_continue_button,
        linkedin_back_button,
        linkedin_continue_button,
        calendar_back_button,
        calendar_continue_button,
        reminders_back_button,
        reminders_continue_button,
        maps_back_button
    ]:

        back_button.click(
            fn=back_to_lock_and_refresh,
            inputs=back_inputs,
            outputs=back_outputs
        )


    # =====================================================
    # ALEXA
    # =====================================================

    def advance_alexa_game(
        choice,
        stage,
        conversation_history,
        points,
        infinity
    ):

        stage, conversation_history, points, infinity = (
            process_full_alexa_conversation(
                choice,
                stage,
                conversation_history,
                points,
                infinity
            )
        )


        if stage == "missing":

            conversation_history += """
            <div style="
                background:#eeeeee;
                color:#111;
                padding:10px 14px;
                border-radius:18px;
                margin-bottom:12px;
            ">
                okay but actually
            </div>

            <div style="
                background:#eeeeee;
                color:#111;
                padding:10px 14px;
                border-radius:18px;
                margin-bottom:12px;
            ">
                i hate that ur so far away
            </div>

            <div style="
                background:#eeeeee;
                color:#111;
                padding:10px 14px;
                border-radius:18px;
                margin-bottom:12px;
            ">
                i miss u :(
            </div>

            <div style="
                background:#eeeeee;
                color:#111;
                padding:10px 14px;
                border-radius:18px;
                margin-bottom:12px;
            ">
                and now im annoyed at u
            </div>
            """


        if stage == "final":

            conversation_history += """
            <div style="
                background:#eeeeee;
                color:#111;
                padding:10px 14px;
                border-radius:18px;
                margin-bottom:12px;
            ">
                so what are u gonna do about it 🙄
            </div>
            """


        updated_conversation = build_alexa_conversation(
            conversation_history
        )


        if stage == "complete":

            choice_update = gr.update(
                choices=[],
                value=None,
                visible=False
            )

            send_update = gr.update(
                visible=False
            )

        else:

            choice_update = gr.update(
                choices=get_alexa_choices(stage),
                value=None,
                visible=True
            )

            send_update = gr.update(
                visible=True
            )


        return (
            updated_conversation,
            stage,
            conversation_history,
            points,
            infinity,
            choice_update,
            send_update,
            f"Boyfriend Points: {points} ♡",
            f"Infinity Points: {infinity} 🔒"
        )


    alexa_send_button.click(
        fn=advance_alexa_game,

        inputs=[
            choice_selector,
            stage_state,
            conversation_state,
            boyfriend_state,
            infinity_state
        ],

        outputs=[
            conversation_display,
            stage_state,
            conversation_state,
            boyfriend_state,
            infinity_state,
            choice_selector,
            alexa_send_button,
            boyfriend_display,
            infinity_display
        ]
    )


    # =====================================================
    # UNKNOWN
    # =====================================================

    def process_unknown_game(
        choice,
        points
    ):

        screen_html, points, game_over = (
            build_unknown_result(
                choice,
                points
            )
        )


        success = (
            choice
            == "block her and immediately send everything to Alexa"
        )


        if game_over:

            return (
                screen_html,
                points,
                f"Boyfriend Points: {points} ♡",

                gr.update(visible=False),
                gr.update(visible=False),

                gr.update(visible=True),
                gr.update(visible=False),

                False
            )


        return (
            screen_html,
            points,
            f"Boyfriend Points: {points} ♡",

            gr.update(visible=False),
            gr.update(visible=False),

            gr.update(visible=False),
            gr.update(visible=True),

            success
        )


    unknown_send_button.click(
        fn=process_unknown_game,

        inputs=[
            unknown_choice,
            boyfriend_state
        ],

        outputs=[
            unknown_conversation,
            boyfriend_state,
            unknown_points_display,
            unknown_choice,
            unknown_send_button,
            restart_button,
            unknown_continue_button,
            unknown_opened_state
        ]
    )


    # =====================================================
    # LINKEDIN
    # =====================================================

    def process_linkedin_game(
        choice,
        stage,
        history,
        points
    ):

        if stage == "main":

            reply, points, new_stage, game_over = (
                handle_linkedin_choice(
                    choice,
                    points
                )
            )

        else:

            reply, points, new_stage, game_over = (
                handle_linkedin_subchoice(
                    stage,
                    choice,
                    points
                )
            )


        history += reply


        updated_screen = build_linkedin_screen(
            history
        )


        if game_over:

            return (
                updated_screen,
                new_stage,
                history,
                points,

                f"Boyfriend Points: {points} ♡",

                gr.update(
                    choices=[],
                    value=None,
                    visible=False
                ),

                gr.update(visible=False),
                gr.update(visible=True),
                gr.update(visible=False),

                False
            )


        if new_stage == "complete":

            return (
                updated_screen,
                new_stage,
                history,
                points,

                f"Boyfriend Points: {points} ♡",

                gr.update(
                    choices=[],
                    value=None,
                    visible=False
                ),

                gr.update(visible=False),
                gr.update(visible=False),
                gr.update(visible=True),

                True
            )


        return (
            updated_screen,
            new_stage,
            history,
            points,

            f"Boyfriend Points: {points} ♡",

            gr.update(
                choices=get_linkedin_choices(new_stage),
                value=None,
                visible=True
            ),

            gr.update(visible=True),
            gr.update(visible=False),
            gr.update(visible=False),

            False
        )


    linkedin_send_button.click(
        fn=process_linkedin_game,

        inputs=[
            linkedin_choice,
            linkedin_stage_state,
            linkedin_history_state,
            boyfriend_state
        ],

        outputs=[
            linkedin_conversation,
            linkedin_stage_state,
            linkedin_history_state,
            boyfriend_state,
            linkedin_points_display,
            linkedin_choice,
            linkedin_send_button,
            linkedin_restart_button,
            linkedin_continue_button,
            linkedin_opened_state
        ]
    )


    # =====================================================
    # CALENDAR
    # =====================================================

    def process_calendar(points):

        result_html, points = (
            handle_calendar_check(
                points
            )
        )


        return (
            result_html,
            points,

            f"Boyfriend Points: {points} ♡",

            gr.update(visible=False),
            gr.update(visible=True),

            True,

            gr.update(
                value="📅 Calendar ✓\nSchedule checked"
            )
        )


    calendar_check_button.click(
        fn=process_calendar,

        inputs=[
            boyfriend_state
        ],

        outputs=[
            calendar_display,
            boyfriend_state,
            calendar_points_display,
            calendar_check_button,
            calendar_continue_button,
            calendar_opened_state,
            calendar_notification
        ]
    )


    # =====================================================
    # REMINDERS
    # =====================================================

    def process_reminder(
        choice,
        nyxie_trust,
        dusty_trust
    ):

        result_html, nyxie_trust, dusty_trust = (
            handle_reminder_choice(
                choice,
                nyxie_trust,
                dusty_trust
            )
        )


        updated_screen = build_reminders_screen(
            result_html
        )


        return (
            updated_screen,

            nyxie_trust,
            dusty_trust,

            f"""
Nyxie Trust: {nyxie_trust} 🐈
Dusty Trust: {dusty_trust} 🤍
            """,

            gr.update(
                choices=get_reminder_choices(),
                value=None,
                visible=True
            ),

            gr.update(
                visible=True
            ),

            gr.update(
                visible=True
            ),

            True,

            gr.update(
                value="⏰ Reminders ✓\nReminders checked"
            )
        )


    reminders_check_button.click(
        fn=process_reminder,

        inputs=[
            reminder_choice,
            nyxie_trust_state,
            dusty_trust_state
        ],

        outputs=[
            reminders_display,

            nyxie_trust_state,
            dusty_trust_state,

            reminder_trust_display,

            reminder_choice,
            reminders_check_button,
            reminders_continue_button,

            reminders_opened_state,

            reminders_notification
        ]
    )


    # =====================================================
    # MAPS
    # =====================================================

    def preview_maps_route(
        choice,
        maps_stage,
        selected_route
    ):

        # Only preview while choosing a transportation method.
        # This prevents Start / Not yet from triggering route previews.
        if maps_stage != "route":
            return (
                gr.update(),
                selected_route,
                gr.update()
            )

        if not choice:
            return (
                build_maps_screen(),
                None,
                gr.update(visible=False)
            )

        route_result = handle_maps_choice(choice)

        updated_screen = build_maps_screen(
            choice,
            route_result
        )

        return (
            updated_screen,
            choice,
            gr.update(
                value="Use This Route",
                visible=True
            )
        )


    # -----------------------------------------------------
    # PREVIEW ROUTES
    # -----------------------------------------------------

    maps_choice.change(
        fn=preview_maps_route,
        inputs=[
            maps_choice,
            maps_stage_state,
            maps_route_state
        ],
        outputs=[
            maps_display,
            maps_route_state,
            maps_action_button
        ]
    )


    # -----------------------------------------------------
    # USE ROUTE / START ROUTE
    # -----------------------------------------------------

    def maps_action(
        choice,
        maps_stage,
        selected_route
    ):

        # Commit to whichever route is currently previewed.
        if maps_stage == "route":

            if not selected_route:
                return (
                    build_maps_screen(),
                    "route",
                    selected_route,
                    gr.update(
                        choices=get_maps_choices(),
                        value=None,
                        visible=True,
                        label="How are you getting to Alexa?"
                    ),
                    gr.update(
                        value="Use This Route",
                        visible=False
                    ),
                    gr.update(visible=False),
                    False
                )

            route_result = handle_maps_choice(selected_route)

            updated_screen = build_maps_screen(
                selected_route,
                route_result
            )

            return (
                updated_screen,
                "start",
                selected_route,
                gr.update(
                    choices=["Start", "Not yet"],
                    value=None,
                    visible=True,
                    label="START ROUTE?"
                ),
                gr.update(
                    value="Confirm",
                    visible=True
                ),
                gr.update(visible=False),
                False
            )

        # Confirm Start / Not yet.
        if maps_stage == "start":

            if choice == "Not yet":
                updated_screen = build_maps_route_result(
                    selected_route,
                    "Not yet"
                )

                return (
                    updated_screen,
                    "route",
                    selected_route,
                    gr.update(
                        choices=get_maps_choices(),
                        value=selected_route,
                        visible=True,
                        label="How are you getting to Alexa?"
                    ),
                    gr.update(
                        value="Use This Route",
                        visible=True
                    ),
                    gr.update(visible=False),
                    False
                )

            if choice == "Start":
                updated_screen = build_maps_route_result(
                    selected_route,
                    "Start"
                )

                return (
                    updated_screen,
                    "complete",
                    selected_route,
                    gr.update(
                        choices=[],
                        value=None,
                        visible=False
                    ),
                    gr.update(visible=False),
                    gr.update(visible=True),
                    True
                )

            # Confirm was clicked without choosing Start / Not yet.
            return (
                build_maps_screen(
                    selected_route,
                    handle_maps_choice(selected_route)
                    if selected_route else ""
                ),
                "start",
                selected_route,
                gr.update(
                    choices=["Start", "Not yet"],
                    value=None,
                    visible=True,
                    label="START ROUTE?"
                ),
                gr.update(
                    value="Confirm",
                    visible=True
                ),
                gr.update(visible=False),
                False
            )

        # Completed ending: leave the ending visible and keep Play Again available.
        return (
            gr.update(),
            maps_stage,
            selected_route,
            gr.update(),
            gr.update(visible=False),
            gr.update(visible=True),
            True
        )


    maps_action_button.click(
        fn=maps_action,
        inputs=[
            maps_choice,
            maps_stage_state,
            maps_route_state
        ],
        outputs=[
            maps_display,
            maps_stage_state,
            maps_route_state,
            maps_choice,
            maps_action_button,
            maps_restart_button,
            maps_opened_state
        ]
    )


    # =====================================================
    # RESET EVERYTHING
    # =====================================================

    def restart_everything():

        stage, history, points, infinity = (
            reset_infinity_lock()
        )


        return (
            # ---------- SCREENS ----------
            gr.update(visible=True),
            gr.update(visible=False),
            gr.update(visible=False),
            gr.update(visible=False),
            gr.update(visible=False),
            gr.update(visible=False),
            gr.update(visible=False),

            # ---------- CORE ----------
            stage,
            history,
            points,
            infinity,

            0,
            0,

            # ---------- ALEXA ----------
            build_alexa_conversation(),

            gr.update(
                choices=get_alexa_choices("opening"),
                value=None,
                visible=True
            ),

            gr.update(
                visible=True
            ),

            "Boyfriend Points: 0 ♡",
            "Infinity Points: 0 🔒",

            # ---------- UNKNOWN ----------
            unknown_initial_html,

            gr.update(
                choices=[
                    "reply something mean",
                    "flirt back",
                    "block her and immediately send everything to Alexa",
                    "leave her on read"
                ],
                value=None,
                visible=True
            ),

            gr.update(
                visible=True
            ),

            "Boyfriend Points: 0 ♡",

            gr.update(
                visible=False
            ),

            gr.update(
                visible=False
            ),

            False,

            # ---------- LINKEDIN ----------
            "main",
            "",

            build_linkedin_screen(),

            gr.update(
                choices=get_linkedin_choices("main"),
                value=None,
                visible=True
            ),

            gr.update(
                visible=True
            ),

            "Boyfriend Points: 0 ♡",

            gr.update(
                visible=False
            ),

            gr.update(
                visible=False
            ),

            False,

            # ---------- CALENDAR ----------
            build_calendar_screen(),

            gr.update(
                visible=True
            ),

            "Boyfriend Points: 0 ♡",

            gr.update(
                visible=False
            ),

            False,

            gr.update(
                value="📅 Calendar · 8m\nGo see your girlfriend — OVERDUE"
            ),

            # ---------- REMINDERS ----------
            build_reminders_screen(),

            gr.update(
                choices=get_reminder_choices(),
                value=None,
                visible=True
            ),

            gr.update(
                visible=True
            ),

            """
Nyxie Trust: 0 🐈
Dusty Trust: 0 🤍
            """,

            gr.update(
                visible=False
            ),

            False,

            gr.update(
                value="⏰ Reminders · 11m\nCALL ALEXA ‼️"
            ),

            # ---------- MAPS ----------
            "route",
            None,
            False,

            build_maps_screen(),

            gr.update(
                choices=get_maps_choices(),
                value=None,
                visible=True,
                label="How are you getting to Alexa?"
            ),

            gr.update(
                value="Use This Route",
                visible=False
            ),

            gr.update(
                visible=False
            ),

            gr.update(
                value="🗺️ Maps\nRoute unavailable",
                interactive=False
            )
        )


    reset_outputs = [

        # ---------- SCREENS ----------
        lock_screen,
        alexa_screen,
        unknown_screen,
        linkedin_screen,
        calendar_screen,
        reminders_screen,
        maps_screen,

        # ---------- CORE ----------
        stage_state,
        conversation_state,
        boyfriend_state,
        infinity_state,

        nyxie_trust_state,
        dusty_trust_state,

        # ---------- ALEXA ----------
        conversation_display,
        choice_selector,
        alexa_send_button,
        boyfriend_display,
        infinity_display,

        # ---------- UNKNOWN ----------
        unknown_conversation,
        unknown_choice,
        unknown_send_button,
        unknown_points_display,
        restart_button,
        unknown_continue_button,
        unknown_opened_state,

        # ---------- LINKEDIN ----------
        linkedin_stage_state,
        linkedin_history_state,
        linkedin_conversation,
        linkedin_choice,
        linkedin_send_button,
        linkedin_points_display,
        linkedin_restart_button,
        linkedin_continue_button,
        linkedin_opened_state,

        # ---------- CALENDAR ----------
        calendar_display,
        calendar_check_button,
        calendar_points_display,
        calendar_continue_button,
        calendar_opened_state,
        calendar_notification,

        # ---------- REMINDERS ----------
        reminders_display,
        reminder_choice,
        reminders_check_button,
        reminder_trust_display,
        reminders_continue_button,
        reminders_opened_state,
        reminders_notification,

        # ---------- MAPS ----------
        maps_stage_state,
        maps_route_state,
        maps_opened_state,
        maps_display,
        maps_choice,
        maps_action_button,
        maps_restart_button,
        maps_notification
    ]


    restart_button.click(
        fn=restart_everything,
        inputs=[],
        outputs=reset_outputs
    )


    linkedin_restart_button.click(
        fn=restart_everything,
        inputs=[],
        outputs=reset_outputs
    )


    maps_restart_button.click(
        fn=restart_everything,
        inputs=[],
        outputs=reset_outputs
    )


# =========================================================
# LAUNCH
# maps_animation_css + maps_finale_css are your helper cells
# =========================================================

if __name__ == "__main__":
    import os
    infinity_lock_app.launch(
        server_name="0.0.0.0",
        server_port=int(os.environ.get("PORT", "10000")),
        css=combined_css + maps_animation_css + maps_finale_css
    )
