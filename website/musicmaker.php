
<head>

<link href="https://fonts.googleapis.com/css?family=Lato" rel="stylesheet">

    <!-- site-wide CSS-->
<link rel="stylesheet" type="text/css" href="musicmaker.css">
    
    <!-- import jquery-->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>
    
    <script>

        window.addEventListener('load', function() {
        // Incrementally call getTweets every 5 seconds
            console.log("WINDOW LOADED");
            click();
        }, false);
    
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
    
        function main(){
                
                
            
            
            
            
        }
    
    
    </script>
    
    
    
    </head>

<!-- fonts-->
<link href='https://fonts.googleapis.com/css?family=Arvo|Bree+Serif|Varela+Round|Signika:400,600,300' rel='stylesheet' type='text/css'>
<link href='https://fonts.googleapis.com/css?family=Montserrat' rel='stylesheet' type='text/css'>
<link rel="stylesheet" type="text/css" href="MyFontsWebfontsKit.css">

<!-- glyphicons-->
<link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">

<body>

    <div class="title-top">
        Welcome to <span class="text-panel-green">the Thing.</span>
</div>
    
    
    <div class="text-panel">
    To begin, hold the controller 3 inches (7.5 cm) from your face and press the go button<span class="text-panel-green"></span>.
        <span class="glyphicon glyphicon-hand-right"></span>
    </div>
    
    
    
    
    
    
</body>


