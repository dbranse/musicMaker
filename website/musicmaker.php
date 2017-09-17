
<head>

<link href="https://fonts.googleapis.com/css?family=Lato" rel="stylesheet">

 
    
    <!-- import jquery-->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>
    
    <script>
        window.addEventListener('load', function() {
            console.log("WINDOW LOADED");
            var intervalId = setInterval(function() {
                click(intervalId);
            });
        }, 1000);
        
        
        function gotSound() { //asking if the server got the sound
            $.get("http://localhost:5555", function(data,status){
                return (status=="success");
            });
        }
        
        function click(intervalId){
            $.post("http://localhost:5555/click", function(data,status){
                if (data['isClicked']) {
                    
                    clearInterval(intervalId);
                    //$(".circle-panel").css("display", "block");///
                    initialRecordings();
                };
                return (data['isClicked']);
            });
        }
        
        function startRec(name){ //bass snare hihat clap
            $.post("http://localhost:5555/sound/" + name);
        }
    
        function initialRecordings(){
            setTimeout(function() {bass();}, 1500);
        }

        function bass() {
            //Remove Information Panels
            $(".circle-panel").css("display", "none");
            $(".text-panel").css("display", "none");

            //Set Up Text/Counter
            var counter = 6;
            var text1 = "Say 'Buh' deeply and quickly in ";
            var text2 = " seconds.";
            $("#timeText").text(text1 + counter + text2);
            $("#timeText").css("display", "block");
            
            //Tell to startRecording
            startRec("bass");

            //Count Down
            var id = setInterval(function() {
                $("#timeText").text(text1 + counter + text2);
                counter--;
                if(counter < 0) {
                    clearInterval(id);
                }
            }, 1000);

            setTimeout(function() {snare();}, 10000);
        }

        function snare() {
            //$(".circle-panel").css("display", "none");
            //Set Up Text/Counter
            var counter = 6;
            var text1 = "Say 'Psh' loudly and quickly in ";
            var text2 = " seconds.";
            $("#timeText").text(text1 + counter + text2);

            //Tell to startRecording
            startRec("snare");

            //Count Down
            var id = setInterval(function() {
                $("#timeText").text(text1 + counter + text2);
                counter--;
                if(counter < 0) {
                    clearInterval(id);
                }
            }, 1000);

            setTimeout(function() {hihat();}, 10000);
        }

        function hihat() {
            //$(".circle-panel").css("display", "none");
            //Set Up Text/Counter
            var counter = 6;
            var text1 = "Say 'Tss' loudly and quickly in ";
            var text2 = " seconds.";
            $("#timeText").text(text1 + counter + text2);
            
            //Tell to startRecording
            startRec("hihat");

            //Count Down
            var id = setInterval(function() {
                $("#timeText").text(text1 + counter + text2);
                counter--;
                if(counter < 0) {
                    clearInterval(id);
                }
            }, 1000);

            setTimeout(function() {clap();}, 10000);
        }
        
        function clap() {
            //$(".circle-panel").css("display", "none");
            //Set Up Text/Counter
            var counter = 6;
            var text1 = "Clap your hands once in ";
            var text2 = " seconds.";
            $("#timeText").text(text1 + counter + text2);
            
            //Tell to startRecording
            startRec("clap");

            //Count Down
            var id = setInterval(function() {
                $("#timeText").text(text1 + counter + text2);
                counter--;
                if(counter < 0) {
                    clearInterval(id);
                }
            }, 1000);
            
            setTimeout(function() {sing();}, 10000);
        }        
    
        
        function sing() {
            //$(".circle-panel").css("display", "none");
            //Set Up Text/Counter
            var counter = 6;
            var text1 = "Quickly sing any note in ";
            var text2 = " seconds.";
            $("#timeText").text(text1 + counter + text2);
            
            //Tell to startRecording
            startRec("sing");

            //Count Down
            var id = setInterval(function() {
                $("#timeText").text(text1 + counter + text2);
                counter--;
                if(counter < 0) {
                    clearInterval(id);
                }
            }, 1000);
        }
        
        
    </script>
    <!-- fonts-->
<link href='https://fonts.googleapis.com/css?family=Arvo|Bree+Serif|Varela+Round|Signika:400,600,300' rel='stylesheet' type='text/css'>
<link href='https://fonts.googleapis.com/css?family=Montserrat' rel='stylesheet' type='text/css'>
<link rel="stylesheet" type="text/css" href="MyFontsWebfontsKit.css">

<!-- glyphicons-->
<link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
       <!-- site-wide CSS-->
<link rel="stylesheet" type="text/css" href="musicmaker.css">
    </head>



<body>

    <div class="title-top">
        Welcome to <span class="text-panel-green">BeatRoot.</span> A semi-automated beat generation tool with a human touch.
</div>
    
    
    <div class="text-panel">
    To begin, stay within 1 foot of the laptop and press the go button<span class="text-panel-green"></span> .
        <span class="glyphicon glyphicon-hand-right"></span>
        
        
    </div>
    
    
    <div class="circle-panel">
        <img src="http://varungadh.com/hackmit.png" href="">
    </div>
    
    <div id="timeText"></div>
    <!-- <div id="timeText" class="buh">Buh!</div>
    
    <div id="timeText" class="snare">Psh!</div>
    
    <div id="timeText" class="hi">Tss!</div>
    
    <div id="timeText" class="clap">Clap!</div> -->
    
    
</body>


