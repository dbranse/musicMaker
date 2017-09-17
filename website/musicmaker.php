
<head>

<link href="https://fonts.googleapis.com/css?family=Lato" rel="stylesheet">

 
    
    <!-- import jquery-->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>
    
    <script>

        window.addEventListener('load', function() {
            console.log("WINDOW LOADED");
            click();
        })
        
        function gotSound() { //asking if the server got the sound
            $.get("http://localhost:5555", function(data,status){
                return (status=="success");
            })
        }
        
        function click(){
            $.post("http://localhost:5555/click", function(data,status){
                return (data['isClicked']);
            })
        }
        
        function startRec(name){ //bass snare hihat clap
            $.post("http://localhost:5555/sound/" + name, function(data,status){
                return (data['isClicked']);
            })
        }
    
        function main(){
            isClicked = false;
            setInterval(function {
                if (click() && !isClicked) {
                    isClicked = true;
                    $(".circle-panel").css("display", "block");
                    setTimeout(function() {}, 3000);
                    $(".text-panel").css("display", "none");
                    isClicked = false;
                };
            }, 1000);
                }
                
            
            setTimeout(function() {}, 3000);
            $(".circle-panel").css("display", "none");
            //bass
            $(".buh").css("display", "block");
            startRec("bass");
            var downloadButton = document.getElementById("download");
            var counter = 3;
            var newElement = document.createElement("p");
            newElement.innerHTML = "Say 'Buh' deeply and quickly in 3 seconds.";
            var id;

            downloadButton.parentNode.replaceChild(newElement, downloadButton);

            id = setInterval(function() {
                counter--;
            if(counter < 0) {
                newElement.parentNode.replaceChild(downloadButton, newElement);
                clearInterval(id);
            } else {
                newElement.innerHTML = "Say 'Buh' deeply and quickly in " + counter.toString() + " seconds.";
            }
                }, 1000);
            $(".circle-panel").css("display", "block");
            
            setTimeout(function() {}, 3000);
            $(".buh").css("display", "none");
            $(".circle-panel").css("display", "none");
            $(".snare").css("display", "block");
        
            //snare
            startRec("snare");
            var downloadButton = document.getElementById("download");
            var counter = 3;
            var newElement = document.createElement("p");
            newElement.innerHTML = "Say 'Psh' loudly and quickly in 3 seconds.";
            var id;

            downloadButton.parentNode.replaceChild(newElement, downloadButton);

            id = setInterval(function() {
                counter--;
            if(counter < 0) {
                newElement.parentNode.replaceChild(downloadButton, newElement);
                clearInterval(id);
            } else {
                newElement.innerHTML = "Say 'Psh' loudly and quickly in " + counter.toString() + " seconds.";
            }
                }, 1000);
            $(".circle-panel").css("display", "block");
            
            setTimeout(function() {}, 3000);
            $(".snare").css("display", "none");
            $(".circle-panel").css("display", "none");
            $(".hi").css("display", "block");
            
            //hihat
            startRec("hihat");
            var downloadButton = document.getElementById("download");
            var counter = 3;
            var newElement = document.createElement("p");
            newElement.innerHTML = "Say 'Tss' loudly and quickly in 3 seconds.";
            var id;

            downloadButton.parentNode.replaceChild(newElement, downloadButton);

            id = setInterval(function() {
                counter--;
            if(counter < 0) {
                newElement.parentNode.replaceChild(downloadButton, newElement);
                clearInterval(id);
            } else {
                newElement.innerHTML = "Say 'Tss' loudly and quickly in " + counter.toString() + " seconds.";
            }
                }, 1000);
            $(".circle-panel").css("display", "block");
            
            setTimeout(function() {}, 3000);
            $(".hi").css("display", "none");
            $(".circle-panel").css("display", "none");
            $(".clap").css("display", "block");
            
            //hihat
            startRec("clap");
            var downloadButton = document.getElementById("download");
            var counter = 3;
            var newElement = document.createElement("p");
            newElement.innerHTML = "Clap your hands once in 3 seconds.";
            var id;

            downloadButton.parentNode.replaceChild(newElement, downloadButton);

            id = setInterval(function() {
                counter--;
            if(counter < 0) {
                newElement.parentNode.replaceChild(downloadButton, newElement);
                clearInterval(id);
            } else {
                newElement.innerHTML = "Clap your hands once in " + counter.toString() + " seconds.";
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
        Welcome to <span class="text-panel-green">the Thing.</span>
</div>
    
    
    <div class="text-panel">
    To begin, hold the controller 3 inches (7.5 cm) from your face and press the go button<span class="text-panel-green"></span>.
        <span class="glyphicon glyphicon-hand-right"></span>
        
        
    </div>
    
    
    <div class="circle-panel">
        <img src="http://varungadh.com/hackmit.png" href="">
    </div>
    
    <div id="download" class="buh">Buh!</div>
    
    <div id="download" class="snare">Psh!</div>
    
    <div id="download" class="hi">Tss!</div>
    
    <div id="download" class="clap">Clap!</div>
    
    
</body>


