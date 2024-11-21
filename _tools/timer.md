---
title: Tools
layout: blank
icon: fas fa-info-circle
order: 3
visible: false
---

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Timed Activity</title>
    <style>
      body {
        transition: background-color 0.5s ease;
        text-align: center;
        font-family: Arial, sans-serif;
        padding: 20px;
      }
      h1,
      h2,
      h3 {
        margin: 20px 0;
      }
      #time {
        font-size: 24px;
        margin-top: 10px;
      }
      #next,
      #time-left {
        font-size: 18px;
        margin-top: 5px;
      }
      #buttons {
        margin-top: 20px;
      }
      button {
        padding: 10px 20px;
        font-size: 16px;
        margin: 5px;
        cursor: pointer;
        border: none;
        border-radius: 5px;
      }
      button#skip {
        background-color: #f39c12;
        color: white;
      }
      button#delay {
        background-color: #3498db;
        color: white;
      }
      button#restart {
        background-color: #e74c3c;
        color: white;
      }
    </style>
  </head>
  <body>
    <h1 id="activity">Welcome!</h1>
    <h2 id="time">00:00</h2>
    <h3 id="next">Coming next: Teach Back Introductions and Overview</h3>
    <h3 id="time-left">Time left: 5:00</h3>
    <div id="buttons">
      <button id="skip" onclick="skipSection()">Skip to Next Section</button>
      <button id="delay" onclick="delaySection()">Delay 1 Minute</button>
      <button id="restart" onclick="restartTimer()">Restart</button>
    </div>
    <script>
      let currentSectionIndex = 0;
      let startTime = Date.now();
      const sections = [
        {
          activity: 'Teach Back Introductions and Overview',
          duration: 5,
          color: 'lightblue',
          next: 'Instructor Do: Question and Answering',
        },
        {
          activity: 'Instructor Do: Question and Answering',
          duration: 10,
          color: 'orange',
          next: 'Break/Midway Feedback',
        },
        { activity: 'Break/Midway Feedback', duration: 5, color: 'bagie', next: 'Tokenization Activity Review' },
        {
          activity: 'Tokenization Activity Review',
          duration: 10,
          color: 'lightgreen',
          next: 'Final Feedback, Wrap-up, and Next Steps',
        },
        { activity: 'Final Feedback, Wrap-up, and Next Steps', duration: 5, color: 'yellow', next: 'End of Session' },
      ];

      function setBackgroundColor() {
        let elapsedMilliseconds = Date.now() - startTime;
        let elapsedMinutes = Math.floor(elapsedMilliseconds / 60000);
        let elapsedSeconds = Math.floor((elapsedMilliseconds % 60000) / 1000);
        let totalElapsedMinutes = elapsedMinutes + elapsedSeconds / 60;
        let timeInCurrentSection = totalElapsedMinutes;
        let timeLeft = sections[currentSectionIndex].duration - timeInCurrentSection;

        if (timeLeft <= 0 && currentSectionIndex < sections.length - 1) {
          currentSectionIndex++;
          startTime = Date.now();
          timeLeft = sections[currentSectionIndex].duration;
        }

        document.body.style.backgroundColor = sections[currentSectionIndex].color;
        document.getElementById('activity').textContent = sections[currentSectionIndex].activity;
        document.getElementById('next').textContent = 'Coming next: ' + sections[currentSectionIndex].next;
        document.getElementById('time').textContent =
          (elapsedMinutes < 10 ? '0' : '') + elapsedMinutes + ':' + (elapsedSeconds < 10 ? '0' : '') + elapsedSeconds;
        document.getElementById('time-left').textContent =
          'Time left: ' +
          Math.floor(timeLeft) +
          ':' +
          (Math.floor((timeLeft % 1) * 60) < 10 ? '0' : '') +
          Math.floor((timeLeft % 1) * 60);
      }

      function startTimer() {
        setInterval(setBackgroundColor, 1000);
      }

      function skipSection() {
        if (currentSectionIndex < sections.length - 1) {
          currentSectionIndex++;
          startTime = Date.now();
          setBackgroundColor();
        }
      }

      function delaySection() {
        startTime += 5 * 12000; // delay switch by 1 minutes
      }

      function restartTimer() {
        currentSectionIndex = 0;
        startTime = Date.now();
        setBackgroundColor();
      }

      window.onload = startTimer;
    </script>
  </body>
