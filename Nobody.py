from flask import Flask

app = Flask(__name__)

@app.route('/')
def warning():
    return '''
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>⚠️ FUCK YOU BRO  ⚠️</title>
<style>
    body {
        background-color: black;
        color: red;
        font-family: 'Courier New', monospace;
        text-align: center;
        margin-top: 10%;
        overflow: hidden;
        animation: bgFlash 1.2s infinite alternate;
    }
    @keyframes bgFlash {
        0% { background-color: black; }
        100% { background-color: #200000; }
    }
    .alert-box {
        border: 2px solid red;
        padding: 40px;
        display: inline-block;
        animation: flicker 1.5s infinite alternate;
        box-shadow: 0 0 30px red;
    }
    @keyframes flicker {
        0% { opacity: 1; }
        50% { opacity: 0.7; }
        100% { opacity: 1; }
    }
    h1 {
        font-size: 2.2em;
        text-shadow: 0 0 15px red;
        margin-bottom: 20px;
    }
    .blink {
        animation: blink 0.7s infinite alternate;
    }
    @keyframes blink {
        from { opacity: 1; }
        to { opacity: 0.3; }
    }
    .console {
        width: 70%;
        margin: 20px auto;
        text-align: left;
        font-size: 1em;
        line-height: 1.4em;
        color: #ff5555;
        background: rgba(0,0,0,0.7);
        border: 1px solid red;
        padding: 15px;
        height: 200px;
        overflow-y: auto;
        box-shadow: 0 0 15px red;
    }
    .glitch {
        position: relative;
        color: red;
        font-weight: bold;
    }
    .glitch::before, .glitch::after {
        content: attr(data-text);
        position: absolute;
        left: 0;
        width: 100%;
        overflow: hidden;
    }
    .glitch::before {
        animation: glitchTop 1s infinite linear alternate-reverse;
        color: cyan;
        top: 0;
    }
    .glitch::after {
        animation: glitchBottom 1s infinite linear alternate-reverse;
        color: lime;
        top: 0;
    }
    @keyframes glitchTop {
        0% { clip: rect(0, 9999px, 0, 0); }
        50% { clip: rect(0, 9999px, 30px, 0); transform: translate(-5px, -5px); }
        100% { clip: rect(0, 9999px, 0, 0); }
    }
    @keyframes glitchBottom {
        0% { clip: rect(0, 9999px, 0, 0); }
        50% { clip: rect(0, 9999px, 30px, 0); transform: translate(5px, 5px); }
        100% { clip: rect(0, 9999px, 0, 0); }
    }
</style>
</head>
<body>

    <div class="alert-box">
        <h1 class="glitch" data-text="⚠️ HI BELG GUY ⚠️">⚠️ HI BELG GUY ⚠️</h1>
        <p class="blink">WE KNOW WHO YOU ARE BRO</p>
        <p class="blink">AND BACK STORY</p>
    </div>

    <div class="console" id="console"></div>

    <audio id="beep" src="https://actions.google.com/sounds/v1/alarms/beep_short.ogg"></audio>

<script>
    const consoleBox = document.getElementById('console');
    const lines = [
        "WHAT DO YOU SMELL HER LIKE ?",
        "GOOD BOY",
        "LAST YEAR STUDENT",
        "HELL YEAH,TEACH HER TO BE THE BEST",
        "GOOD LUCK",
        "MOTHER FUCKER",
        ".........",
        "FUCK YOU BRO",
    ];
    let i = 0;
    const beep = document.getElementById('beep');

    function printLine() {
        if (i < lines.length) {
            beep.play();
            consoleBox.innerHTML += lines[i] + "<br>";
            consoleBox.scrollTop = consoleBox.scrollHeight;
            i++;
            setTimeout(printLine, 1200);
        } else {
            alert("⚠️ SYSTEM BREACH DETECTED ⚠️\\nThis activity has been logged! FUCK YOU BRO!");
        }
    }
    setTimeout(printLine, 1000);
</script>

</body>
</html>
'''

if __name__ == "__main__":
    app.run(debug=True)
