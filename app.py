from flask import Flask, request, jsonify, render_template_string, make_response, send_file
import hashlib
import hmac
import json
import time
import secrets
import base64
from datetime import datetime
import re
import io

app = Flask(__name__)
app.config['SECRET_KEY'] = 'whistlepodu_mumbaiindians_2008_rivalry'

# Global storage
user_sessions = {}

# Home page with story
@app.route('/')
def home():
    return render_template_string('''<!DOCTYPE html>
<html>
<head>
    <title>Wankhede | Chepauk - The Uncanny Tale</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Courier New', monospace;
            background: linear-gradient(to right, #004C93 50%, #FDB913 50%);
            color: white;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .stadium {
            max-width: 900px;
            background: rgba(0, 0, 0, 0.85);
            padding: 50px;
            border-radius: 20px;
            box-shadow: 0 0 100px rgba(255, 255, 255, 0.3);
        }
        h1 {
            text-align: center;
            font-size: 3em;
            margin-bottom: 30px;
            background: linear-gradient(90deg, #004C93, #FDB913);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: glow 2s ease-in-out infinite;
        }
        @keyframes glow {
            0%, 100% { filter: brightness(1); }
            50% { filter: brightness(1.5); }
        }
        .story {
            line-height: 1.8;
            font-size: 1.1em;
            margin: 20px 0;
        }
        .memory {
            background: rgba(255, 255, 255, 0.1);
            padding: 20px;
            margin: 20px 0;
            border-left: 5px solid #FDB913;
            font-style: italic;
        }
        .meme {
            text-align: center;
            font-size: 2em;
            margin: 30px 0;
            animation: bounce 1s infinite;
        }
        @keyframes bounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }
        .hint {
            font-size: 0.7em;
            color: #888;
            margin-top: 30px;
            text-align: center;
        }
        button {
            width: 100%;
            padding: 20px;
            background: linear-gradient(90deg, #004C93, #FDB913);
            border: none;
            border-radius: 10px;
            color: white;
            font-size: 1.2em;
            font-weight: bold;
            cursor: pointer;
            margin-top: 30px;
        }
        button:hover {
            transform: scale(1.05);
            box-shadow: 0 10px 30px rgba(253, 185, 19, 0.5);
        }
        .secret {
            color: rgba(255, 255, 255, 0.02);
            font-size: 8px;
        }
    </style>
</head>
<body>
    <div class="stadium">
        <h1>🏏 The Uncanny Rivalry 🏏</h1>
        
        <div class="story">
            <p>In the year <strong>two thousand and eight</strong>, when the IPL was born, two teams emerged from the shadows...</p>
            <br>
            <p>One wore the colors of the <strong>midnight ocean</strong> 🌊</p>
            <p>The other donned the shades of the <strong>rising sun</strong> ☀️</p>
            <br>
            <p>Their captains? Two legends who shared the number on their backs...</p>
            <p>One who kept wickets behind the stumps 🧤</p>
            <p>Another who opened the innings with power 💥</p>
        </div>

        <div class="meme">
            <p>😎 "THALA FOR A REASON" 😎</p>
            <p style="font-size: 0.5em; margin-top: 10px;">vs</p>
            <p>🔥 "ROHIT KE SHOT" 🔥</p>
        </div>

        <div class="story">
            <p>They say the rivalry isn't about wins or losses...</p>
            <p>It's about <strong>moments</strong> frozen in time ⏰</p>
            <p>About <strong>captains</strong> who never aged 👨‍✈️</p>
            <p>About <strong>numbers</strong> that tell stories 🔢</p>
            <br>
            <p style="color: #FDB913;">But to understand this tale, you must first find where it begins...</p>
            <p style="color: #004C93;">The path is hidden, but the clues are everywhere.</p>
        </div>

        <div class="hint">
            <p>💡 "When two captains share a jersey number, their paths intertwine..."</p>
            <p>💡 "The dates remember what we forget..."</p>
            <p>💡 "Sometimes you need to look at the source of the river..."</p>
        </div>

        <button onclick="alert('This button does nothing! 😜 The real path requires... investigation.')">
            🚀 START THE JOURNEY
        </button>

        <div class="secret">
            April 9 2010 was special. Format matters.YYYYMMD
            When numbers meet dates, paths reveal themselves.
        </div>

        <p style="text-align: center; margin-top: 40px; font-size: 0.8em; color: #666;">
            "In cricket, timing is everything. In CTF, so is observation."
        </p>
    </div>

    <script>
        // Developers love to hide things in console
        console.log('%c🏏 THE RIVALRY BEGINS 🏏', 'color: #FDB913; font-size: 20px; font-weight: bold;');
        console.log('%cIf you are reading this, you are on the right track!', 'color: #004C93;');
        console.log('%cMemory Fragment #1:', 'color: white; font-weight: bold;');
        console.log('%cCSK captain jersey: 7', 'color: #FDB913;');
        console.log('%cMI captain jersey: 45', 'color: #004C93;');
        console.log('%cPath structure hint: /memories/{date_format}', 'color: #888;');
        console.log('%cBut which date? And what format? 🤔', 'color: #888;');
        console.log(' ');
        console.log('%cMeme of the day:', 'color: white;');
        console.log('%c"404 - Trophy Not Found" - Delhi fans', 'color: red; font-style: italic;');
    </script>
</body>
</html>''')

# Stage 1: First memory endpoint
@app.route('/memories/<date_code>')
def first_memory(date_code):
    if date_code != '20100409':
        return jsonify({
            'error': 'Memory not found',
            'message': 'This date does not exist in the rivalry chronicles',
            
            'format': 'Use YYYYMMDD format',
            'meme': '🤔 "Ye kaunsi match hai bhai?" - Confused cricket fan'
        }), 404
    
    # Create session
    session_id = secrets.token_urlsafe(32)
    user_sessions[session_id] = {
        'stage': 1,
        'unlocked': ['first_memory'],
        'timestamp': time.time()
    }
    
    # Return response with hidden data in headers and JSON
    response = make_response(jsonify({
        'success': True,
        'memory_unlocked': 'IPL 2010 Final',
        'date': 'April 9, 2010',
        'venue': 'DY Patil Stadium, Navi Mumbai',
        'match': 'Mumbai Indians vs Chennai Super Kings',
        'result': 'CSK won by 22 runs',
        'dhoni_score': '22 runs (off 15 balls) ⚡',
        'sachin_score': '37 runs (off 31 balls)',
        'mom': 'Suresh Raina (57* off 35 balls)',
        'session_token': session_id,
        'message': 'First memory unlocked! But this is just the beginning...',
        'verified': False,
        'meme': '💛 "Whistle Podu!" - CSK fans in 2010',
        'next_hint': 'Sometimes memories whisper not through what you see, but through what travels unseen between you and the past.🕵️'
    }))
    
    # Hidden clue in response headers
    response.headers['X-Memory-Fragment'] = 'pollard_2013_revenge'
    response.headers['X-Verified-Status'] = 'false'
    response.headers['X-Secret-Clue'] = 'Change false to true and resend the request'
    
    return response

# Stage 2: Verified memory (when user changes verified=false to true)

# Stage 2: Verified memory (when user changes verified=false to true)
@app.route('/memories/20100409/verified')
def verified_memory():
    verified_param = request.args.get('verified', 'false').lower()
    session_token = request.args.get('session')
    
    if not session_token or session_token not in user_sessions:
        return jsonify({
            'error': 'Invalid session'
        }), 401
    
    if verified_param != 'true':
        return jsonify({
            'error': 'Verification failed',
            'hint': 'Sometimes memories whisper not through what you see, but through what travels unseen between you and the past.',
            'meme': '❌ "Not verified, bro"'
        }), 403
    
    # Update session
    user_sessions[session_token]['stage'] = 2
    user_sessions[session_token]['unlocked'].append('verified_memory')
    
    response = make_response(jsonify({
        'success': True,
        'status': 'Verification complete!',
        'message': 'You have proven yourself worthy to continue...',
        'flashback': 'But 2010 was just the beginning. Three years later, Mumbai got their revenge...',
        'revenge_date': 'May 26, 2013',
        'next_challenge': 'The path forward requires solving a puzzle.',
        'instruction': 'Once you solve the puzzle, you will unlock the stadium entrance.',
        'meme': '🧩 "Puzzle solve karo pehle" - Your friendly neighborhood CTF'
    }))
    
    response.headers['X-Next-Stage'] = 'stadium-puzzle'
    
    return response

# NEW Stage 2.5: Stadium Puzzle Page (Scrambled Word Challenge)
# FIXED Stage 2.5: Stadium Puzzle Page (Scrambled Word Challenge)
@app.route('/stadium-puzzle')
def stadium_puzzle():
    session_token = request.args.get('session')
    
    if not session_token or session_token not in user_sessions:
        return render_template_string('''<!DOCTYPE html>
<html><head><title>Access Denied</title></head>
<body style="background: #000; color: #ff0000; text-align: center; padding-top: 100px; font-family: monospace;">
<h1>🚫 ACCESS DENIED 🚫</h1>
<p>Session required!</p>
</body></html>'''), 403
    
    if user_sessions[session_token]['stage'] < 2:
        return render_template_string('''<!DOCTYPE html>
<html><head><title>Access Denied</title></head>
<body style="background: #000; color: #ff0000; text-align: center; padding-top: 100px; font-family: monospace;">
<h1>🚫 ACCESS DENIED 🚫</h1>
<p>Complete previous stages first!</p>
</body></html>'''), 403
    
    return render_template_string('''<!DOCTYPE html>
<html>
<head>
    <title>Stadium Puzzle - Unlock the Entrance</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Courier New', monospace;
            background: linear-gradient(135deg, #004C93, #1E3A8A);
            color: white;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }
        .container {
            max-width: 700px;
            background: rgba(0, 0, 0, 0.9);
            padding: 50px;
            border-radius: 20px;
            box-shadow: 0 0 100px rgba(0, 76, 147, 0.5);
        }
        h1 {
            text-align: center;
            font-size: 2.5em;
            margin-bottom: 30px;
            color: #FDB913;
        }
        .puzzle-display {
            text-align: center;
            font-size: 4em;
            margin: 30px 0;
            animation: bounce 2s infinite;
        }
        @keyframes bounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-15px); }
        }
        .message {
            text-align: center;
            line-height: 1.8;
            font-size: 1.1em;
            margin: 20px 0;
        }
        .input-section {
            margin: 40px 0;
            padding: 30px;
            background: rgba(253, 185, 19, 0.1);
            border: 2px solid #FDB913;
            border-radius: 15px;
        }
        input[type="text"] {
            width: 100%;
            padding: 20px;
            margin: 15px 0;
            background: rgba(255, 255, 255, 0.1);
            border: 2px solid #004C93;
            border-radius: 10px;
            color: white;
            font-size: 1.1em;
            font-family: 'Courier New', monospace;
            text-align: center;
        }
        button {
            width: 100%;
            padding: 20px;
            margin-top: 15px;
            background: linear-gradient(90deg, #004C93, #FDB913);
            border: none;
            border-radius: 10px;
            color: white;
            font-size: 1.2em;
            font-weight: bold;
            cursor: pointer;
        }
        button:hover {
            transform: scale(1.05);
            box-shadow: 0 10px 30px rgba(253, 185, 19, 0.5);
        }
        #result {
            margin-top: 20px;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            display: none;
        }
        .success {
            background: rgba(0, 255, 0, 0.2);
            border: 2px solid #00ff00;
        }
        .error {
            background: rgba(255, 0, 0, 0.2);
            border: 2px solid #ff0000;
        }
        .riddle-box {
            background: rgba(0, 76, 147, 0.2);
            padding: 20px;
            margin: 20px 0;
            border-radius: 10px;
            border-left: 5px solid #4A9EFF;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🏟️ The Gateway Challenge 🏟️</h1>
        
        <div class="puzzle-display">
            🏟️🔐🏟️
        </div>
        
        <div class="message">
            <p><strong>The Path Forward Awaits...</strong></p>
            <p style="margin-top: 15px;">
                To unlock the gates of Wankhede Stadium, you must solve a hidden puzzle.
            </p>
        </div>
    
        
        <div class="input-section">
            <h3 style="text-align: center; color: #FDB913; margin-bottom: 20px;">
                Enter the Gateway Code
            </h3>
            <input type="text" id="pass" placeholder="????????" autocomplete="off">
            <button onclick="verifyAnswer()">🚀 UNLOCK</button>
        </div>
        
        <div id="result"></div>
        
    </div>
    
    <script>
        function verifyAnswer() {
            var checkpass = document.getElementById("pass").value;
            var resultDiv = document.getElementById('result');
            
            if (typeof verify === 'function') {
                verify();
            } else {
                resultDiv.className = 'error';
                resultDiv.innerHTML = '❌ Verification failed!';
                resultDiv.style.display = 'block';
            }
        }
        
        document.getElementById('pass').addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                verifyAnswer();
            }
        });
        
        function verify() {
            var checkpass = document.getElementById("pass").value;
            var resultDiv = document.getElementById('result');
            
            // Encrypted gateway codes
            var g1 = [119,97,110,107,104,101,100,101];
            var g2 = [99,104,101,112,97,117,107];
            
            var decode = function(arr) {
                return arr.map(function(x) { return String.fromCharCode(x); }).join('');
            };
            
            var components = checkpass.split('_');
            
            if (components.length !== 2) {
                resultDiv.className = 'error';
                resultDiv.innerHTML = '❌ Invalid format!';
                resultDiv.style.display = 'block';
                return;
            }
            
            var p1 = decode(g1);
            var p2 = decode(g2);
            
            if (components[0].toLowerCase() === p1 && components[1].toLowerCase() === p2) {
                resultDiv.className = 'success';
                resultDiv.innerHTML = '<h3>✅ Gateway Unlocked!</h3><p style="margin-top: 10px;">Redirecting...</p>';
                resultDiv.style.display = 'block';
                
                var nextPath = '/' + decode([115,116,97,100,105,117,109]) + '/' + p1;
                
                setTimeout(function() {
                    window.location.href = nextPath + '?session={{ session }}';
                }, 1500);
                return;
            } else {
                resultDiv.className = 'error';
                resultDiv.innerHTML = '❌ Access Denied!';
                resultDiv.style.display = 'block';
            }
        }
    </script>
</body>
</html>'''.replace('{{ session }}', session_token))
@app.route('/stadium/<word>')
def stadium_entrance(word):
    session_token = request.args.get('session')
    
    if not session_token or session_token not in user_sessions:
        return jsonify({'error': 'Session required'}), 401
    
    if user_sessions[session_token]['stage'] < 2:
        return jsonify({
            'error': 'Complete previous stages first',
            'meme': '⏭️ "Seedha final? Pehle qualifier khelo!"'
        }), 403
    
    if word.lower() != 'wankhede':
        return jsonify({
            'error': 'Wrong path',
            'meme': '❌ "Wrong entry gate, sir!"'
        }), 404
    
    # Update session
    user_sessions[session_token]['stage'] = 3
    user_sessions[session_token]['unlocked'].append('stadium_victory')
    
    # Return HTML page with upload functionality
    return render_template_string('''<!DOCTYPE html>
<html>
<head>
    <title>Wankhede Stadium - Trophy Room</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Courier New', monospace;
            background: linear-gradient(135deg, #004C93, #1E3A8A);
            color: white;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }
        .container {
            max-width: 800px;
            background: rgba(0, 0, 0, 0.9);
            padding: 50px;
            border-radius: 20px;
            box-shadow: 0 0 100px rgba(0, 76, 147, 0.5);
        }
        h1 {
            text-align: center;
            font-size: 2.5em;
            margin-bottom: 30px;
            color: #FDB913;
        }
        .trophy-display {
            text-align: center;
            font-size: 5em;
            margin: 30px 0;
            animation: spin 4s linear infinite;
        }
        @keyframes spin {
            0% { transform: rotateY(0deg); }
            100% { transform: rotateY(360deg); }
        }
        .message {
            text-align: center;
            line-height: 1.8;
            font-size: 1.1em;
            margin: 20px 0;
        }
        .upload-section {
            margin: 40px 0;
            padding: 30px;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 15px;
            border: 2px dashed #FDB913;
        }
        .upload-box {
            margin: 20px 0;
        }
        label {
            display: block;
            margin-bottom: 10px;
            color: #FDB913;
            font-weight: bold;
        }
        input[type="file"] {
            width: 100%;
            padding: 15px;
            background: rgba(255, 255, 255, 0.1);
            border: 2px solid #004C93;
            border-radius: 10px;
            color: white;
            cursor: pointer;
        }
        button {
            width: 100%;
            padding: 20px;
            margin-top: 20px;
            background: linear-gradient(90deg, #004C93, #FDB913);
            border: none;
            border-radius: 10px;
            color: white;
            font-size: 1.2em;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s;
        }
        button:hover {
            transform: scale(1.05);
            box-shadow: 0 10px 30px rgba(253, 185, 19, 0.5);
        }
        .hint-box {
            margin: 30px 0;
            padding: 20px;
            background: rgba(253, 185, 19, 0.1);
            border-left: 5px solid #FDB913;
            border-radius: 10px;
        }
        #result {
            margin-top: 20px;
            padding: 20px;
            border-radius: 10px;
            display: none;
        }
        .success {
            background: rgba(0, 255, 0, 0.2);
            border: 2px solid #00ff00;
        }
        .error {
            background: rgba(255, 0, 0, 0.2);
            border: 2px solid #ff0000;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🏟️ Wankhede Stadium - Trophy Room 🏟️</h1>
        
        <div class="trophy-display">
            🏆💙🏆
        </div>
        
        <div class="message">
            <p><strong>Welcome to the Trophy Room!</strong></p>
            <p>You have reached Mumbai Indians' sacred ground - Wankhede Stadium.</p>
            <br>
            <p>But to access the vault where the 2013 trophy is kept, you need TWO special documents...</p>
            <p>The pavilion accepts scorecards, not souvenirs — keep your submission in the official format.</p>
        </div>
        
        <div style="text-align: center; margin: 30px 0;">
            <p style="margin-top: 15px;">
                <a href="/download/pollard_2013.exe?session={{ session }}" 
                   style="color: #FDB913; text-decoration: none; font-weight: bold;">
                   📥 pollard_2013.exe
                </a>
            </p>
            <p style="margin-top: 10px;">
                <a href="/download/rohit_captain.exe?session={{ session }}" 
                   style="color: #4A9EFF; text-decoration: none; font-weight: bold;">
                   📥rohit_captain.exe
                </a>
            </p>
        </div>
        
        <div class="upload-section">
            <h3 style="text-align: center; color: #FDB913; margin-bottom: 20px;">
                📤 Upload Files
            </h3>
            
            <form id="uploadForm" enctype="multipart/form-data">
                <div class="upload-box">
                    <label for="file1">🏏 Pollard 2013 Trophy Document:</label>
                    <input type="file" id="file1" name="file1" accept=".pdf" required>
                </div>
                
                <div class="upload-box">
                    <label for="file2">👨‍✈️ Rohit Captain Document:</label>
                    <input type="file" id="file2" name="file2" accept=".pdf" required>
                </div>
                
                <button type="submit">🚀 UNLOCK TROPHY VAULT</button>
            </form>
        </div>
        
        <div id="result"></div>
        
        <p style="text-align: center; margin-top: 40px; color: #666; font-size: 0.9em;">
            "In 2013, Pollard hit 60 off 32 balls. That's the kind of power we need here! 💪"
        </p>
    </div>
    
    <script>
        document.getElementById('uploadForm').addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const formData = new FormData();
            formData.append('file1', document.getElementById('file1').files[0]);
            formData.append('file2', document.getElementById('file2').files[0]);
            formData.append('session', '{{ session }}');
            
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '<p style="text-align: center;">⏳ Validating documents...</p>';
            resultDiv.style.display = 'block';
            resultDiv.className = '';
            
            try {
                const response = await fetch('/upload-trophies', {
                    method: 'POST',
                    body: formData
                });
                
                const data = await response.json();
                
                if (data.success) {
                    resultDiv.className = 'success';
                    resultDiv.innerHTML = `
                        <h3 style="text-align: center;">✅ ${data.message}</h3>
                        <p style="text-align: center; margin-top: 15px;">${data.flashback}</p>
                        <p style="text-align: center; margin-top: 15px; font-size: 1.1em; color: #FDB913;">
                            <strong>Next Path:</strong> ${data.next_path}
                        </p>
                        <p style="text-align: center; margin-top: 10px; color: #4A9EFF;">
                            ${data.hint}
                        </p>
                    `;
                } else {
                    resultDiv.className = 'error';
                    resultDiv.innerHTML = `
                        <h3 style="text-align: center;">❌ ${data.error}</h3>
                        <p style="text-align: center; margin-top: 10px;">${data.hint || ''}</p>
                    `;
                }
            } catch (error) {
                resultDiv.className = 'error';
                resultDiv.innerHTML = `
                    <h3 style="text-align: center;">❌ Upload failed</h3>
                    <p style="text-align: center; margin-top: 10px;">${error.message}</p>
                `;
            }
        });
        
        
    </script>
</body>
</html>'''.replace('{{ session }}', session_token))

# Download fake .exe files (actually PDFs)
@app.route('/download/<filename>')
def download_file(filename):
    session_token = request.args.get('session')
    
    if not session_token or session_token not in user_sessions:
        return jsonify({'error': 'Session required'}), 401
    
    if filename == 'pollard_2013.exe':
        pdf_content = b'''%PDF-1.4
1 0 obj
<<
/Type /Catalog
/Pages 2 0 R
>>
endobj
2 0 obj
<<
/Type /Pages
/Kids [3 0 R]
/Count 1
>>
endobj
3 0 obj
<<
/Type /Page
/Parent 2 0 R
/MediaBox [0 0 612 792]
/Contents 4 0 R
/Resources <<
/Font <<
/F1 <<
/Type /Font
/Subtype /Type1
/BaseFont /Helvetica-Bold
>>
>>
>>
>>
endobj
4 0 obj
<<
/Length 250
>>
stream
BT
/F1 24 Tf
50 750 Td
(IPL 2013 FINAL - TROPHY DOCUMENT) Tj
0 -40 Td
/F1 14 Tf
(Date: May 26, 2013) Tj
0 -25 Td
(Venue: Eden Gardens, Kolkata) Tj
0 -25 Td
(Match: MI vs CSK - Final) Tj
0 -25 Td
(Result: MI won by 23 runs) Tj
0 -30 Td
(Man of the Match: Kieron Pollard - 60 off 32 balls) Tj
0 -30 Td
/F1 12 Tf
(Secret Code Part 1: BLUE_ARMY) Tj
ET
endstream
endobj
xref
0 5
0000000000 65535 f
0000000009 00000 n
0000000058 00000 n
0000000115 00000 n
0000000314 00000 n
trailer
<<
/Size 5
/Root 1 0 R
>>
startxref
615
%%EOF'''
        
        return send_file(
            io.BytesIO(pdf_content),
            mimetype='application/octet-stream',
            as_attachment=True,
            download_name='pollard_2013.exe'
        )
    
    elif filename == 'rohit_captain.exe':
        pdf_content = b'''%PDF-1.4
1 0 obj
<<
/Type /Catalog
/Pages 2 0 R
>>
endobj
2 0 obj
<<
/Type /Pages
/Kids [3 0 R]
/Count 1
>>
endobj
3 0 obj
<<
/Type /Page
/Parent 2 0 R
/MediaBox [0 0 612 792]
/Contents 4 0 R
/Resources <<
/Font <<
/F1 <<
/Type /Font
/Subtype /Type1
/BaseFont /Helvetica-Bold
>>
>>
>>
>>
endobj
4 0 obj
<<
/Length 240
>>
stream
BT
/F1 24 Tf
50 750 Td
(ROHIT SHARMA - CAPTAINCY RECORDS) Tj
0 -40 Td
/F1 14 Tf
(Became MI Captain: 2013) Tj
0 -25 Td
(IPL Titles as Captain: 5) Tj
0 -25 Td
(Jersey Number: 45) Tj
0 -25 Td
(Playing Style: Aggressive opener) Tj
0 -30 Td
(Most famous shot: Pull shot over midwicket) Tj
0 -30 Td
/F1 12 Tf
(Secret Code Part 2: CHAMPIONS_32) Tj
ET
endstream
endobj
xref
0 5
0000000000 65535 f
0000000009 00000 n
0000000058 00000 n
0000000115 00000 n
0000000314 00000 n
trailer
<<
/Size 5
/Root 1 0 R
>>
startxref
605
%%EOF'''
        
        return send_file(
            io.BytesIO(pdf_content),
            mimetype='application/octet-stream',
            as_attachment=True,
            download_name='rohit_captain.exe'
        )
    
    return jsonify({'error': 'File not found'}), 404

# Upload and verify PDFs
@app.route('/upload-trophies', methods=['POST'])
def upload_trophies():
    session_token = request.form.get('session')
    
    if not session_token or session_token not in user_sessions:
        return jsonify({'error': 'Invalid session'}), 401
    
    if user_sessions[session_token]['stage'] < 3:
        return jsonify({'error': 'Complete previous stages first'}), 403
    
    file1 = request.files.get('file1')
    file2 = request.files.get('file2')
    
    if not file1 or not file2:
        return jsonify({
            'success': False,
            'error': 'Both files required'
        }), 400
    
    # Check if files are PDFs
    content1 = file1.read()
    content2 = file2.read()
    
    if not (content1.startswith(b'%PDF') and content2.startswith(b'%PDF')):
        return jsonify({
            'success': False,
            'error': 'Invalid file format'
        }), 400
    
    # Verify content contains expected strings
    if b'BLUE_ARMY' not in content1 and b'BLUE_ARMY' not in content2:
        return jsonify({
            'success': False,
            'error': 'Incorrect documents',
            'hint': 'Make sure you downloaded the correct files'
        }), 400
    
    # Update session
    user_sessions[session_token]['stage'] = 4
    user_sessions[session_token]['unlocked'].append('trophy_vault')
    
    return jsonify({
        'success': True,
        'message': 'Documents verified! Trophy vault unlocking...',
        'flashback': 'May 26, 2013 - The night Mumbai won their first trophy under Rohit!',
        'next_path': '/birthday-bash?session=' + session_token,
        'hint': 'Time to celebrate! Head to the birthday bash 🎂',
        'meme': '🎉 "Paltan, this is for you!" - Rohit 2013'
    })

# Stage 4: Birthday bash challenge (MD5 collision like PicoCTF)
@app.route('/birthday-bash')
def birthday_bash():
    session_token = request.args.get('session')
    
    if not session_token or session_token not in user_sessions:
        return render_template_string('''<!DOCTYPE html>
<html><head><title>Access Denied</title></head>
<body style="background: #000; color: #ff0000; text-align: center; padding-top: 100px; font-family: monospace;">
<h1>🚫 ACCESS DENIED 🚫</h1>
<p>Session required!</p>
</body></html>'''), 403
    
    if user_sessions[session_token]['stage'] < 4:
        return render_template_string('''<!DOCTYPE html>
<html><head><title>Access Denied</title></head>
<body style="background: #000; color: #ff0000; text-align: center; padding-top: 100px; font-family: monospace;">
<h1>🚫 ACCESS DENIED 🚫</h1>
<p>Complete previous stages first!</p>
</body></html>'''), 403
    
    return render_template_string('''<!DOCTYPE html>
<html>
<head>
    <title>MI Birthday Bash - May 26</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Courier New', monospace;
            background: linear-gradient(135deg, #1a1a2e, #16213e, #0f3460);
            color: white;
            min-height: 100vh;
            padding: 20px;
        }
        .container {
            max-width: 900px;
            margin: 50px auto;
            background: rgba(0, 0, 0, 0.85);
            padding: 50px;
            border-radius: 20px;
            box-shadow: 0 0 100px rgba(0, 76, 147, 0.4);
        }
        h1 {
            text-align: center;
            font-size: 2.8em;
            margin-bottom: 20px;
            background: linear-gradient(90deg, #004C93, #FDB913);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .cake {
            text-align: center;
            font-size: 6em;
            margin: 30px 0;
            animation: bounce 2s infinite;
        }
        @keyframes bounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-20px); }
        }
        .story {
            line-height: 1.8;
            font-size: 1.1em;
            margin: 20px 0;
            text-align: center;
        }
        .challenge-box {
            background: rgba(253, 185, 19, 0.1);
            padding: 30px;
            margin: 30px 0;
            border-radius: 15px;
            border: 2px solid #FDB913;
        }
        .login-form {
            margin: 30px 0;
        }
        input[type="text"], input[type="password"] {
            width: 100%;
            padding: 15px;
            margin: 10px 0;
            background: rgba(255, 255, 255, 0.1);
            border: 2px solid #004C93;
            border-radius: 10px;
            color: white;
            font-size: 1.1em;
            font-family: 'Courier New', monospace;
        }
        button {
            width: 100%;
            padding: 20px;
            margin-top: 15px;
            background: linear-gradient(90deg, #004C93, #FDB913);
            border: none;
            border-radius: 10px;
            color: white;
            font-size: 1.2em;
            font-weight: bold;
            cursor: pointer;
        }
        button:hover {
            transform: scale(1.05);
            box-shadow: 0 10px 30px rgba(253, 185, 19, 0.5);
        }
        .hint {
            text-align: center;
            margin-top: 20px;
            color: #888;
            font-size: 0.9em;
        }
        #result {
            margin-top: 20px;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            display: none;
        }
        .success {
            background: rgba(0, 255, 0, 0.2);
            border: 2px solid #00ff00;
        }
        .error {
            background: rgba(255, 0, 0, 0.2);
            border: 2px solid #ff0000;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🎂 MI Birthday Bash - May 26 🎂</h1>
        
        <div class="cake">
            🎂🎉🎊
        </div>
        
        <div class="story">
            <p><strong>May 26th - A Special Day for Mumbai Indians!</strong></p>
            <p style="margin-top: 15px;">In 2013 and 2015, both IPL finals were won on this date!</p>
            <p>It's like Mumbai's lucky birthday! 🎂</p>
        </div>
        
        <div class="challenge-box">
            <h3 style="text-align: center; color: #FDB913; margin-bottom: 20px;">
                🔐 The Birthday Party Login
            </h3>
            <p style="text-align: center; margin-bottom: 20px;">
                To enter the birthday celebration, you need valid credentials.<br>
                But finding them requires some investigation... 🕵️
            </p>
            <p style="text-align: center; color: #4A9EFF; margin-bottom: 20px;">
                💡 Hint: Every team has one player who never comes to bat, yet somehow the runs still increase.
            </p>
            
            <div class="login-form">
                <input type="text" id="username" placeholder="Username" autocomplete="off">
                <input type="password" id="password" placeholder="Password" autocomplete="off">
                <button onclick="checkCredentials()">🚀 ENTER PARTY</button>
            </div>
        </div>
    
        
        <div id="result"></div>
    </div>
    
    <script src="/static/verify.js?v={{ session }}"></script>
    
    <script>
        function checkCredentials() {
            const username = document.getElementById('username').value.trim();
            const password = document.getElementById('password').value.trim();
            const resultDiv = document.getElementById('result');
            
            if (!username || !password) {
                resultDiv.className = 'error';
                resultDiv.innerHTML = '❌ Please enter both username and password!';
                resultDiv.style.display = 'block';
                return;
            }
            
            // Check if verifyLogin function exists
            if (typeof verifyLogin !== 'function') {
                resultDiv.className = 'error';
                resultDiv.innerHTML = '❌ Verification script not loaded! Try refreshing the page.';
                resultDiv.style.display = 'block';
                return;
            }
            
            // Call the verification function from verify.js
            try {
                const result = verifyLogin(username, password);
                
                if (result && result.success) {
                    resultDiv.className = 'success';
                    resultDiv.innerHTML = `
                        <h3>🎉 ${result.message}</h3>
                        <p style="margin-top: 15px;">${result.next_hint}</p>
                        <p style="margin-top: 15px; color: #FDB913;">
                            Redirecting to next stage...
                        </p>
                    `;
                    resultDiv.style.display = 'block';
                    
                    // Update session
                    fetch('/update-stage', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                            'X-Session-Token': '{{ session }}'
                        },
                        body: JSON.stringify({ stage: 5 })
                    }).then(() => {
                        // Redirect after updating stage
                        setTimeout(() => {
                            window.location.href = result.next_path;
                        }, 2000);
                    });
                } else {
                    resultDiv.className = 'error';
                    resultDiv.innerHTML = `❌ ${result ? result.message : 'Authentication failed'}`;
                    resultDiv.style.display = 'block';
                }
            } catch (error) {
                resultDiv.className = 'error';
                resultDiv.innerHTML = '❌ Error during verification: ' + error.message;
                resultDiv.style.display = 'block';
            }
        }
        
        document.getElementById('password').addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                checkCredentials();
            }
        });
    </script>
</body>
</html>'''.replace('{{ session }}', session_token))

@app.route('/static/verify.js')
def verify_js():
    session_token = request.args.get('v', '')
    
    js_code = f'''// Birthday Bash Verification System
// MI vs CSK - Champions Authentication

function verifyLogin(username, password) {{
    var m = [
        [101,98,117,118,103,95,52,53],  
        [117,118,103,122,110,97,95,50,48,49,51]  
    ];
    

    var def = function(str) {{
        return str.replace(/[a-zA-Z]/g, function(c) {{
            var code = c.charCodeAt(0);
            if (code >= 65 && code <= 90) {{
                return String.fromCharCode(((code - 65 + 13) % 26) + 65);
            }} else if (code >= 97 && code <= 122) {{
                return String.fromCharCode(((code - 97 + 13) % 26) + 97);
            }}
            return c;
        }});
    }};
    
    // Decode arrays to strings
    var encoded1 = m[0].map(c => String.fromCharCode(c)).join('');
    var encoded2 = m[1].map(c => String.fromCharCode(c)).join('');
    
    // Apply ROT13 to get actual credentials
    var key1 = def(encoded1); 
    var key2 = def(encoded2); 
    
    if (username === key1 && password === key2) {{
        var n = [47,99,104,97,109,112,105,111,110,115,45,108,101,97,103,117,101,63,115,101,115,115,105,111,110,61];
        var nextUrl = n.map(c => String.fromCharCode(c)).join('') + '{session_token}';
        
        return {{
            success: true,
            message: 'Welcome to the Birthday Party! 🎉',
            next_hint: 'You have proven yourself worthy. The final challenge awaits...',
            next_path: nextUrl
        }};
    }} else {{
        return {{
            success: false,
            message: 'Invalid credentials - Username or password incorrect'
        }};
    }}
}}
'''
    
    response = make_response(js_code)
    response.headers['Content-Type'] = 'application/javascript'
    return response

@app.route('/update-stage', methods=['POST'])
def update_stage():
    session_token = request.headers.get('X-Session-Token')
    
    if not session_token or session_token not in user_sessions:
        return jsonify({'error': 'Invalid session'}), 401
    
    data = request.json
    new_stage = data.get('stage', 0)
    
    if new_stage > user_sessions[session_token]['stage']:
        user_sessions[session_token]['stage'] = new_stage
        user_sessions[session_token]['unlocked'].append(f'stage_{new_stage}')
    
    return jsonify({'success': True})

# Stage 5: Champions League (Burp Suite challenge with base64)
@app.route('/champions-league')
def champions_league():
    session_token = request.args.get('session')
    
    if not session_token or session_token not in user_sessions:
        return render_template_string('''<!DOCTYPE html>
<html><head><title>Access Denied</title></head>
<body style="background: #000; color: #ff0000; text-align: center; padding-top: 100px; font-family: monospace;">
<h1>🚫 ACCESS DENIED 🚫</h1>
<p>Session required!</p>
</body></html>'''), 403
    
    if user_sessions[session_token]['stage'] < 5:
        return render_template_string('''<!DOCTYPE html>
<html><head><title>Access Denied</title></head>
<body style="background: #000; color: #ff0000; text-align: center; padding-top: 100px; font-family: monospace;">
<h1>🚫 ACCESS DENIED 🚫</h1>
<p>Complete the birthday bash first!</p>
</body></html>'''), 403
    
    return render_template_string('''<!DOCTYPE html>
<html>
<head>
    <title>Champions League - Final Authentication</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Courier New', monospace;
            background: linear-gradient(135deg, #004C93, #FDB913);
            color: white;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }
        .container {
            max-width: 800px;
            background: rgba(0, 0, 0, 0.9);
            padding: 50px;
            border-radius: 20px;
            box-shadow: 0 0 150px rgba(253, 185, 19, 0.5);
        }
        h1 {
            text-align: center;
            font-size: 2.5em;
            margin-bottom: 30px;
            color: #FDB913;
        }
        .trophy {
            text-align: center;
            font-size: 5em;
            margin: 20px 0;
            animation: rotate 4s linear infinite;
        }
        @keyframes rotate {
            0% { transform: rotateY(0deg); }
            100% { transform: rotateY(360deg); }
        }
        .message {
            text-align: center;
            line-height: 1.8;
            font-size: 1.1em;
            margin: 20px 0;
        }
        .auth-box {
            margin: 30px 0;
            padding: 30px;
            background: rgba(0, 76, 147, 0.2);
            border-radius: 15px;
            border: 2px solid #004C93;
        }
        input {
            width: 100%;
            padding: 15px;
            margin: 10px 0;
            background: rgba(255, 255, 255, 0.1);
            border: 2px solid #FDB913;
            border-radius: 10px;
            color: white;
            font-size: 1.1em;
            font-family: 'Courier New', monospace;
        }
        button {
            width: 100%;
            padding: 20px;
            margin-top: 15px;
            background: linear-gradient(90deg, #004C93, #FDB913);
            border: none;
            border-radius: 10px;
            color: white;
            font-size: 1.2em;
            font-weight: bold;
            cursor: pointer;
        }
        button:hover {
            transform: scale(1.05);
        }
        .hint-box {
            margin: 20px 0;
            padding: 20px;
            background: rgba(253, 185, 19, 0.1);
            border-left: 5px solid #FDB913;
            border-radius: 10px;
        }
        #result {
            margin-top: 20px;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            display: none;
        }
        .success {
            background: rgba(0, 255, 0, 0.2);
            border: 2px solid #00ff00;
        }
        .error {
            background: rgba(255, 0, 0, 0.2);
            border: 2px solid #ff0000;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🏆 Champions League 🏆</h1>
        
        <div class="trophy">
            🏆💙🏆
        </div>
        
        <div class="message">
            <p><strong>Welcome to the Final Authentication!</strong></p>
            <p style="margin-top: 15px;">
                You've made it this far. Now for the ultimate test...
            </p>
            <p style="margin-top: 15px; color: #FDB913;">
                MI has won 5 IPL trophies. CSK has won 5 IPL trophies.<br>
                Together, they are CHAMPIONS! 👑
            </p>
        </div>
        
        <div class="hint-box">
            <p><strong>🔐 Final Authentication Required</strong></p>
            <p style="margin-top: 10px;">
                To access the trophy vault, you need to authenticate with special credentials.
            </p>
        </div>
        
        <div class="auth-box">
            <h3 style="text-align: center; color: #FDB913; margin-bottom: 20px;">
                Enter Your Details
            </h3>
            <input type="text" id="username" placeholder="Username" autocomplete="off">
            <input type="password" id="password" placeholder="Password" autocomplete="off">
            <button onclick="authenticate()">🚀 AUTHENTICATE</button>
        </div>
        
        <div id="result"></div>
        
    </div>
    
    <script>
        function authenticate() {
            const username = document.getElementById('username').value.trim();
            const password = document.getElementById('password').value.trim();
            const resultDiv = document.getElementById('result');
            
            if (!username || !password) {
                resultDiv.className = 'error';
                resultDiv.innerHTML = '❌ Please enter both username and password!';
                resultDiv.style.display = 'block';
                return;
            }
            
            resultDiv.innerHTML = '<p>🔄 Authenticating...</p>';
            resultDiv.style.display = 'block';
            resultDiv.className = '';
            
            // Send authentication request
            fetch('/verify-champion', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-Session-Token': '{{ session }}'
                },
                body: JSON.stringify({
                    username: username,
                    password: password
                })
            })
            .then(response => {
                return response.json();
            })
            .then(data => {
                if (data.success) {
                    resultDiv.className = 'success';
                    resultDiv.innerHTML = `
                        <h3>✅ ${data.message}</h3>
                        <p style="margin-top: 15px;">${data.hint}</p>
                    `;
                } else {
                    resultDiv.className = 'error';
                    resultDiv.innerHTML = `
                        <h3>❌ ${data.error}</h3>
                        <p style="margin-top: 10px;">${data.hint}</p>
                    `;
                }
            })
            .catch(error => {
                resultDiv.className = 'error';
                resultDiv.innerHTML = '❌ Error: ' + error.message;
            });
        }
        
        document.getElementById('password').addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                authenticate();
            }
        });
        
    </script>
</body>
</html>'''.replace('{{ session }}', session_token))

# Verify champion with base64 encoded redirects
@app.route('/verify-champion', methods=['POST'])
def verify_champion():
    session_token = request.headers.get('X-Session-Token')
    
    if not session_token or session_token not in user_sessions:
        return jsonify({'error': 'Invalid session'}), 401
    
    if user_sessions[session_token]['stage'] < 5:
        return jsonify({'error': 'Complete previous stages'}), 403
    
    data = request.json
    username = data.get('username', '')
    password = data.get('password', '')
    
    # Encode credentials in base64
    username_b64 = base64.b64encode(username.encode()).decode()
    password_b64 = base64.b64encode(password.encode()).decode()
    
    # Create response with base64 in headers (for Burp Suite)
    response = make_response(jsonify({
        'success': False,
        'error': 'Authentication in progress...',
        'hint': 'Send your appeal through MI’s twelfth man; he’ll pause the play and let you read the umpire’s pocket notes.'
    }))
    
    # Add base64 credentials in headers
    response.headers['X-Username-B64'] = username_b64
    response.headers['X-Password-B64'] = password_b64
    response.headers['X-Next-Endpoint'] = '/final-vault'
    
    return response

# Final vault endpoint
@app.route('/final-vault', methods=['GET', 'POST'])
def final_vault():
    session_token = request.args.get('session') or request.headers.get('X-Session-Token')
    
    if not session_token or session_token not in user_sessions:
        return jsonify({'error': 'Session required'}), 401
    
    if user_sessions[session_token]['stage'] < 5:
        return jsonify({'error': 'Complete previous stages'}), 403
    
    if request.method == 'GET':
        # Add Part 2 in response header
        response = make_response(render_template_string('''<!DOCTYPE html>
<html>
<head>
    <title>Final Vault - The Secret Code</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Courier New', monospace;
            background: linear-gradient(135deg, #1a1a2e, #16213e, #0f3460, #004C93);
            color: white;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }
        .container {
            max-width: 900px;
            background: rgba(0, 0, 0, 0.92);
            padding: 60px;
            border-radius: 25px;
            box-shadow: 0 0 150px rgba(253, 185, 19, 0.6);
        }
        h1 {
            text-align: center;
            font-size: 3em;
            margin-bottom: 30px;
            background: linear-gradient(90deg, #004C93, #FDB913, #004C93);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: glow 3s ease-in-out infinite;
        }
        @keyframes glow {
            0%, 100% { filter: brightness(1); }
            50% { filter: brightness(2); }
        }
        .vault-display {
            text-align: center;
            font-size: 6em;
            margin: 30px 0;
            animation: pulse 2s infinite;
        }
        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.1); }
        }
        .message {
            text-align: center;
            line-height: 2;
            font-size: 1.15em;
            margin: 25px 0;
        }
        .code-box {
            margin: 40px 0;
            padding: 30px;
            background: rgba(253, 185, 19, 0.1);
            border: 3px solid #FDB913;
            border-radius: 15px;
        }
        input[type="text"] {
            width: 100%;
            padding: 20px;
            margin: 15px 0;
            background: rgba(255, 255, 255, 0.1);
            border: 2px solid #004C93;
            border-radius: 10px;
            color: white;
            font-size: 1.2em;
            font-family: 'Courier New', monospace;
            text-align: center;
            letter-spacing: 3px;
        }
        button {
            width: 100%;
            padding: 25px;
            margin-top: 20px;
            background: linear-gradient(90deg, #004C93, #FDB913);
            border: none;
            border-radius: 15px;
            color: white;
            font-size: 1.3em;
            font-weight: bold;
            cursor: pointer;
            text-transform: uppercase;
            letter-spacing: 2px;
        }
        button:hover {
            transform: scale(1.05);
            box-shadow: 0 15px 40px rgba(253, 185, 19, 0.7);
        }
        .hint-section {
            margin: 30px 0;
            padding: 25px;
            background: rgba(0, 76, 147, 0.2);
            border-left: 6px solid #4A9EFF;
            border-radius: 10px;
        }
        #result {
            margin-top: 25px;
            padding: 25px;
            border-radius: 15px;
            text-align: center;
            display: none;
        }
        .success {
            background: rgba(0, 255, 0, 0.2);
            border: 3px solid #00ff00;
        }
        .error {
            background: rgba(255, 0, 0, 0.2);
            border: 3px solid #ff0000;
        }
        .secret-hint {
            color: rgba(255, 255, 255, 0.02);
            font-size: 5px;
            user-select: none;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🔐 THE FINAL VAULT 🔐</h1>
        
        <div class="vault-display">
            🏆🔒🏆
        </div>
        
        <div class="message">
            <p><strong style="color: #FDB913; font-size: 1.3em;">CONGRATULATIONS, CHAMPION!</strong></p>
            <p style="margin-top: 20px;">
                You have reached the final vault where the ultimate secret lies.<br>
                The flag is within your grasp...
            </p>
            <p style="margin-top: 20px; color: #4A9EFF;">
                But first, you must prove you're worthy by entering the<br>
                <strong style="color: #FDB913;">SECRET CODE</strong>
            </p>
        </div>
        
        <div class="hint-section">
            <p><strong style="color: #FDB913; font-size: 1.2em;">🔍 Finding the Secret Code:</strong></p>
            <p style="margin-top: 15px;">
                The secret code has TWO parts, separated by an underscore (_)
            </p>
        </div>
        
        <div class="code-box">
            <h3 style="text-align: center; color: #FDB913; margin-bottom: 20px;">
                Enter the Secret Code
            </h3>
            <input type="text" id="secret_code" placeholder="FORMAT: PART1_PART2" autocomplete="off">
            <button onclick="submitCode()">🚀 UNLOCK THE FLAG</button>
        </div>
        
        <div id="result"></div>
        
        <p style="text-align: center; margin-top: 50px; color: #666; font-size: 0.9em;">
            "In the end, it's not about MI or CSK winning... it's about cricket winning! 🏏"
        </p>
    </div>
    
    <!--  
        SECRET CODE PART 1: MI5XCHAMP2008
        This is intentionally visible in source code
    -->
    
    <script>
        function submitCode() {
            const code = document.getElementById('secret_code').value.trim();
            const resultDiv = document.getElementById('result');
            
            if (!code) {
                resultDiv.className = 'error';
                resultDiv.innerHTML = '❌ Please enter the secret code!';
                resultDiv.style.display = 'block';
                return;
            }
            
            resultDiv.innerHTML = '<p style="font-size: 1.2em;">🔄 Verifying secret code...</p>';
            resultDiv.style.display = 'block';
            resultDiv.className = '';
            
            fetch('/unlock-flag', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-Session-Token': '{{ session }}'
                },
                body: JSON.stringify({ secret_code: code })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    resultDiv.className = 'success';
                    resultDiv.innerHTML = `
                        <h2 style="font-size: 2em; margin-bottom: 20px;">🎉 CONGRATULATIONS! 🎉</h2>
                        <p style="font-size: 1.2em; margin: 15px 0;">${data.message}</p>
                        <div style="margin: 30px 0; padding: 20px; background: rgba(0,0,0,0.6); border-radius: 10px;">
                            <p style="color: #FDB913; font-size: 1.1em; margin-bottom: 10px;"><strong>YOUR FLAG:</strong></p>
                            <p style="font-size: 1.3em; color: #00ff00; word-break: break-all; font-family: monospace;">
                                ${data.flag}
                            </p>
                        </div>
                        <p style="margin-top: 20px; color: #4A9EFF; font-size: 1.1em;">
                            ${data.tribute}
                        </p>
                        <p style="margin-top: 15px; font-size: 0.95em;">
                            Time taken: ${data.stats.time_taken}<br>
                            Stages completed: ${data.stats.stages_completed}
                        </p>
                    `;
                } else {
                    resultDiv.className = 'error';
                    resultDiv.innerHTML = `
                        <h3>❌ ${data.error}</h3>
                        <p style="margin-top: 15px;">${data.hint}</p>
                    `;
                }
                resultDiv.style.display = 'block';
            })
            .catch(error => {
                resultDiv.className = 'error';
                resultDiv.innerHTML = '❌ Error: ' + error.message;
                resultDiv.style.display = 'block';
            });
        }
        
        document.getElementById('secret_code').addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                submitCode();
            }
        });
        
        
    </script>
</body>
</html>'''.replace('{{ session }}', session_token)))
    
    # Add Part 2 in response header
    response.headers['X-Code-Part2'] = 'CSK5XTROPHY2018'
    response.headers['X-Hint'] = 'Combine both parts with underscore'
    
    return response

# Final unlock endpoint
@app.route('/unlock-flag', methods=['POST'])
def unlock_flag():
    session_token = request.headers.get('X-Session-Token')
    
    if not session_token or session_token not in user_sessions:
        return jsonify({'error': 'Invalid session'}), 401
    
    if user_sessions[session_token]['stage'] < 5:
        return jsonify({'error': 'Complete previous stages'}), 403
    
    data = request.json
    secret_code = data.get('secret_code', '').strip()
    
    # Correct code: MI5XCHAMP2008_CSK5XTROPHY2018
    correct_code = 'MI5XCHAMP2008_CSK5XTROPHY2018'
    
    if secret_code != correct_code:
        # Give helpful hints based on input
        if '_' not in secret_code:
            hint = 'Secret code should have two parts separated by underscore (_)'
        elif secret_code.startswith('MI5XCHAMP2008'):
            hint = 'Part 1 is correct! Check response headers for Part 2'
        elif secret_code.endswith('CSK5XTROPHY2018'):
            hint = 'Part 2 is correct! Check page source for Part 1'
        else:
            hint = 'Both parts are incorrect. Part 1 is in page source, Part 2 is in response headers'
        
        return jsonify({
            'success': False,
            'error': 'Incorrect secret code',
            'hint': hint,
            'your_attempt': secret_code
        }), 401
    
    # SUCCESS! Generate flag
    try:
        with open('flag.txt', 'r') as f:
            flag = f.read().strip()
    except FileNotFoundError:
        flag = 'flag{M1_CSK_R1v4lry_5_F1n4ls_10_Tr0ph13s_2008_2023_Wh1stl3_P0du}'
    
    # Mark as completed
    user_sessions[session_token]['stage'] = 6
    user_sessions[session_token]['unlocked'].append('final_vault_completed')
    
    time_taken = int(time.time() - user_sessions[session_token]['timestamp'])
    minutes = time_taken // 60
    seconds = time_taken % 60
    
    return jsonify({
        'success': True,
        'message': 'You have conquered the MI vs CSK rivalry challenge!',
        'flag': flag,
        'tribute': '🏆 MI (5 trophies) and CSK (5 trophies) - The greatest rivalry in cricket! 🏆',
        'achievement': 'RIVALRY MASTER',
        'stats': {
            'stages_completed': 6,
            'memories_unlocked': len(user_sessions[session_token]['unlocked']),
            'time_taken': f'{minutes}m {seconds}s'
        },
        'final_message': '💙💛 Respect both legends, enjoy the rivalry! 💛💙'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)