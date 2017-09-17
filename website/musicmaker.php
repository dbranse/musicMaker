
<head>

<link href="https://fonts.googleapis.com/css?family=Lato" rel="stylesheet">

 
    
    <!-- import jquery-->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>
    
    <script>

        window.addEventListener('load', function() {
            console.log("WINDOW LOADED");
            click();

    
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
                if (click()){
                    $(".circle-panel").css("display", "block");
                    setTimeout(myFunction, 3000);
                    $(".text-panel").css("display", "none");
                }
            
            
            
            
            
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
    
    
</body>


