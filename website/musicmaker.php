
<head>

<link href="https://fonts.googleapis.com/css?family=Lato" rel="stylesheet">

 
    
    <!-- import jquery-->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>
    
    <script>

        window.addEventListener('load', function() {click();
        }, false);
    
        function gotSound() { //asking if the server got the sound
            $.get("localhost:5555", function(data,status){
                return (status=="success")
            })
        }
        
        function click(){
            $.get("localhost:5555", function(data,status)){
                return (status=="success");
            }
        }
    
        function main(){
                if (click()){
                    
                    setTimeout(myFunction, 3000);
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
    
    
    <div class=".circle-panel">
        <img src="http://varungadh.com/hackmit.png" href="" style="display: block;
    margin: auto; margin-top: -270px; opacity: .9;
    width: 40%;">
    </div>
    
    
</body>


