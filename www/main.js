$(document).ready(function () {
    $('.text').textillate({
        loop: true,
        sync: true,
        in:{
            effect: "bounceIn",
        },
        out:{
            effect: "bounceOut",
        },
    })

    //siri configuration
    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 800,
        height: 200,
        style: "ios9",
        amplitude: "1",
        speed: "0.30",
        autostart: true
      });

    //siri message animation
    //   $('.siri-message').textillate({
    //     loop: true,
    //     sync: true,
    //     in:{
    //         effect: "fadeInUp",
    //         sync: true,
    //     },
    //     out:{
    //         effect: "fadeOutUp",
    //         sync: true,
    //     },
    // })


    $('.siri-message').textillate({
        loop: false,               // Disable looping
        autoStart: true,           // Start immediately
        minDisplayTime: 5000,      // Hold the text for 5 seconds
        in: {
            effect: "fadeInUp",    // Use fade-in effect
            delayScale: 1.5,       // Delay between letters
            delay: 50,             // Delay between each character
            sync: true,            // Animate all letters together
            shuffle: false,        // Don't shuffle letters
        },
        out: {
            effect: '',            // No fade-out effect (hold the text)
            sync: true,
        }
    });

    // Micbtn click event
    $("#MicBtn").click(function () { 
        eel.PlayAssistantSound()
        $("#Oval").attr("hidden", true);
        $("#SiriWave").attr("hidden", false);
        eel.allCommands()()
        
    });

    // win+J autostart
    function doc_keyUp(e) {
        

        if (e.key === 'C' && e.metaKey) {
            eel.PlayAssistantSound()
            $("#Oval").attr("hidden", true);
            $("#SiriWave").attr("hidden", false);
            eel.allCommands()()
        }
    }
    document.addEventListener('keyup', doc_keyUp, false);

    //created shortcut key to access the Chanakya Assistant
    //created shortcut key to access the Chanakya Assistant
    // function doc_keyUp(e) {
    //     // this would test for whichever key is 40 (down arrow) and the ctrl key at the same time

    //     if (e.key === 'C' || e.key === 'J' && e.metaKey) {
    //         eel.PlayAssistantSound()
    //         $("#Oval").attr("hidden", true);
    //         $("#SiriWave").attr("hidden", false);
    //         showSiriWaveAndStop();
    //         eel.allCommands()()
    //     }
    // }
    // document.addEventListener('keyup', doc_keyUp, false);



    // to play assisatnt 
    function PlayAssistant(message) {

        if (message != "") {

            $("#Oval").attr("hidden", true);
            $("#SiriWave").attr("hidden", false);
            eel.allCommands(message);
            $("#chatbox").val("")
            $("#MicBtn").attr('hidden', false);
            $("#SendBtn").attr('hidden', true);

        }

    }
    // toogle fucntion to hide and display mic and send button 
    function ShowHideButton(message) {
        if (message.length == 0) {
            $("#MicBtn").attr('hidden', false);
            $("#SendBtn").attr('hidden', true);
        }
        else {
            $("#MicBtn").attr('hidden', true);
            $("#SendBtn").attr('hidden', false);
        }
    }

    // key up event handler on text box
    $("#chatbox").keyup(function () {

        let message = $("#chatbox").val();
        ShowHideButton(message)
    
    });
    
    // send button event handler
    $("#SendBtn").click(function () {
    
        let message = $("#chatbox").val()
        PlayAssistant(message)
    
    });
    

    // enter press event handler on chat box
    $("#chatbox").keypress(function (e) {
        key = e.which;
        if (key == 13) {
            let message = $("#chatbox").val()
            PlayAssistant(message)
        }
    });





    // Toggle Theme Function
    $(document).ready(function () {
        // Button click handlers for navigation
        $('#theme1Btn').click(function () {
            window.location.href = 'index2.html';
        });
    
        $('#theme2Btn').click(function () {
            window.location.href = 'index1.html';
        });
        $('#theme3Btn').click(function () {
            window.location.href = 'logintry.html';
        });
    
        $('#theme4Btn').click(function () {
            window.location.href = 'hometry.html';
        });
    });
            
});